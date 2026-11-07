"""@Scale event agendas: talks, speakers, abstracts, articles and recordings.

The four current series share one WordPress layout. Each agenda accordion
carries its exact title, speakers with affiliations and, where published, an
abstract. Watch buttons lead to an @Scale video page whose embedded player
identifies the YouTube recording. Networking and Product may publish those
buttons after the event; the links step also searches @Scale's own channel.

The page's form CSS mentions captcha, so status codes rather than body markers
detect blocks. The hero, not the article cards below the agenda, supplies the
event date for discovery.
"""

from __future__ import annotations

import re
from collections import Counter
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, scan_end_date, OK, NOT_PUBLISHED

_SKIP = re.compile(
    r"^(?:attendee registration|registration|breakfast\b|lunch\b|break$|"
    r"event welcome|closing\b|(?:networking )?happy hour\b|transition back\b|special mentions|"
    r"lightning talks introduction)", re.I
)
_YOUTUBE_EMBED = re.compile(r"youtube(?:-nocookie)?\.com/embed/([A-Za-z0-9_-]{11})")


def _text(element) -> str:
    return re.sub(r"\s+", " ", element.get_text(" ", strip=True)).strip() if element else ""


class AtScaleFetcher(Fetcher):
    name = "atscale"

    @staticmethod
    def _get(url: str):
        resp = http_get(url)
        resp.encoding = "utf-8"
        return resp

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = self._get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="event page not published yet")
            if resp.status_code != 200:
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"), resp.url)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} program items")

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            resp = self._get(url)
            if resp.status_code == 404:
                return ProbeResult(False, "404 (no such edition yet)", source_url=url)
            if resp.status_code != 200:
                return ProbeResult(False, f"unexpected status {resp.status_code}", source_url=url)
            soup = BeautifulSoup(resp.text, "html.parser")
            hero = soup.select_one(".hero__section, .hero__content")
            end = scan_end_date(_text(hero), years) if hero else None
            return ProbeResult(True, "200; event hero" + ("; date found" if end else ""),
                               end_date=end, source_url=resp.url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)

    def _recording(self, url: str) -> str:
        """Resolve an agenda's Watch button to its embedded YouTube upload.

        If the intermediate page is temporarily unavailable, its own URL is
        still a valid recording page and safer than dropping the known link.
        """
        try:
            resp = self._get(url)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                for frame in soup.find_all("iframe", src=True):
                    if match := _YOUTUBE_EMBED.search(frame["src"]):
                        return f"https://www.youtube.com/watch?v={match.group(1)}"
        except Exception:
            pass
        return url

    def _parse(self, soup: BeautifulSoup, source_url: str) -> tuple[str, int]:
        tab_names = {
            tab.get("data-tab"): _text(tab.select_one(".event-agenda__agenda-tab-title"))
            for tab in soup.select(".event-agenda__agenda-tab[data-tab]")
        }
        items = soup.select(".event-agenda__section .event-agenda__accordion")
        id_counts = Counter(item.get("id", "") for item in items)
        groups: dict[str, list[str]] = {}
        count = 0

        for item in items:
            title = _text(item.select_one(".event-agenda__accordion-header-title"))
            if not title or _SKIP.match(title):
                continue
            count += 1

            # A few track items currently reuse id="agenda-item-0". Such an
            # anchor cannot identify one talk, so leave page: off those items.
            item_id = item.get("id", "")
            links = []
            if item_id and id_counts[item_id] == 1:
                links.append(f"page: {source_url}#{item_id}")

            speakers = []
            for speaker in item.select(".event-agenda__accordion-body-center-speaker"):
                name_el = speaker.select_one(".event-agenda__accordion-body-center-speaker-name")
                company_el = speaker.select_one(".event-agenda__accordion-body-center-speaker-company")
                name = re.sub(r"\s+", " ", "".join(
                    name_el.find_all(string=True, recursive=False) if name_el else []
                )).strip().rstrip(",")
                company = _text(company_el)
                if name:
                    speakers.append(f"{name} ({company})" if company else name)

            block = [f"### {title}"]
            if speakers:
                block.append("Speakers: " + ", ".join(speakers))

            abstract = []
            text_el = item.select_one(".event-agenda__accordion-body-center-text")
            paragraphs = text_el.find_all("p", recursive=False) if text_el else []
            for paragraph in paragraphs:
                value = _text(paragraph)
                if re.match(r"^Authors\s*:", value, re.I):
                    block.append(re.sub(r"^Authors\s*:", "Authors:", value, flags=re.I))
                elif value:
                    abstract.append(value)

            for a in item.select(".event-agenda__accordion-body-left a[href]"):
                if "watch" in _text(a).lower() or "post_type=video" in a["href"]:
                    links.append("video: " + self._recording(urljoin(source_url, a["href"])))
            for a in item.select(".event-agenda__accordion-body-center-resources a[href]"):
                links.append("materials: " + urljoin(source_url, a["href"]))
            if links:
                block.append(" | ".join(links))
            block.extend(abstract or ["No abstract published; title, speakers and materials only."])
            block.append("")

            tabs = item.find_parents(class_="event-agenda__agenda-tab-content")
            labels = [tab_names[tab.get("id")] for tab in tabs if tab.get("id") in tab_names]
            heading = " — ".join(reversed(labels)) or "Program"
            groups.setdefault(heading, []).extend(block)

        lines = []
        for heading, block in groups.items():
            lines.append(f"## {heading}")
            lines.extend(block)
        return "\n".join(lines), count
