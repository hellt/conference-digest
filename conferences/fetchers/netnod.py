"""Netnod's Tech Meeting agenda: Drupal paragraphs with talks and speakers.

www.netnod.se/netnod-tech-meeting-<year> renders the agenda as
paragraph--type--nn-agenda blocks: a date label and one session per
field-collection item — time, title, speaker(s) with company, and a links
cell with the presentation files under /sites/default/files/
NetnodMeetingPresentations/. Registration/meals are skipped. The page states
the meeting date; no year appears in the date label, so the series template
carries the year in the URL and the probe relies on the page text.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_SKIP = re.compile(r"^(?:registration|breakfast|break|lunch|coffee|closing|welcome)", re.I)


class NetnodFetcher(Fetcher):
    name = "netnod"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url, timeout=120)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="meeting page not up yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"), url)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} agenda items")

    def _parse(self, soup: BeautifulSoup, url: str) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        count = 0
        for agenda in soup.select("div.paragraph--type--nn-agenda"):
            date_label = agenda.select_one(".field--name-field-block-date")
            heading = f"Netnod Tech Meeting — {date_label.get_text(' ', strip=True)}" if date_label else "Agenda"
            lines.append(f"## {heading}")
            for session in agenda.select("div.field-collection-item--name-field-event-session"):
                title_el = session.select_one(".field--name-field-block-title")
                if not title_el:
                    continue
                title = title_el.get_text(" ", strip=True)
                if not title or _SKIP.match(title) or title in seen:
                    continue
                seen.add(title)
                count += 1
                lines.append(f"### {title}")
                speakers = []
                for a in session.select(".session-speakers a"):
                    name = a.select_one(".speaker-name")
                    company = a.select_one(".speaker-company")
                    if name:
                        speakers.append(f"{name.get_text(' ', strip=True)}"
                                        + (f" - {company.get_text(' ', strip=True)}" if company else ""))
                if speakers:
                    lines.append("Speakers: " + ", ".join(speakers))
                links = []
                for a in session.select("div.grid-item.links a[href]"):
                    href = urljoin(url, a["href"])
                    if href.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
                        links.append(f"slides: {href}")
                    elif "youtube.com" in href or "youtu.be" in href:
                        links.append(f"video: {href}")
                if links:
                    lines.append(" | ".join(links))
                lines.append("No abstract published; title, speakers and materials only.")
                lines.append("")
        return "\n".join(lines), count
