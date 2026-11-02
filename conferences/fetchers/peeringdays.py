"""Peering Days per-year sites: talks with speakers, slides and some abstracts.

Each edition has its own site (<year>.peeringdays.eu). The programme page is
static HTML: day <h2> headings and one row per slot — time, bold title, a
speaker line ("(Speaker: IXP - Name [Download])") and, sometimes, an abstract
paragraph. The Download links are the decks. Exact dates are on the page, so
the default probe reads them. No bot blocking.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_SKIP = re.compile(r"^(?:registration|welcome coffee|opening|closing|lunch|coffee|break|welcome evening|dinner|networking)", re.I)
_SPEAKER = re.compile(r"\(Speaker:\s*(.+)\)", re.S)


class PeeringDaysFetcher(Fetcher):
    name = "peeringdays"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="programme not published yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"), url)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} programme items")

    def _parse(self, soup: BeautifulSoup, url: str) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        count = 0
        for day in soup.select("h2"):
            heading = day.get_text(" ", strip=True)
            if not re.search(r"(mon|tues|wednes|thurs|fri|satur|sun)day", heading, re.I):
                continue
            lines.append(f"## {heading}")
            container = day.find_next("div", class_="row")
            # walk the rows that belong to this day, until the next day heading
            for row in soup.select("div.row[id^='20']"):
                if not row.find_previous("h2") or row.find_previous("h2").get_text(" ", strip=True) != heading:
                    continue
                title_el = row.select_one("strong")
                if not title_el:
                    continue
                title = title_el.get_text(" ", strip=True)
                if not title or _SKIP.match(title) or title in seen:
                    continue
                seen.add(title)
                count += 1
                lines.append(f"### {title}")
                speaker_block = None
                description = ""
                content = row.find_all("div", recursive=False)[-1]
                for div in content.find_all("div", recursive=False):
                    if "mt-2" in (div.get("class") or []):
                        continue  # the title cell
                    text = div.get_text(" ", strip=True)
                    if not text:
                        continue
                    match = _SPEAKER.search(text)
                    if match:
                        speaker_block = div
                    else:
                        description = description or text
                links: list[str] = []
                for a in (speaker_block or row).select("a[href]"):
                    href = urljoin(url, a["href"])
                    if href.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
                        links.append(f"slides: {href}")
                if speaker_block:
                    speaker = _SPEAKER.search(speaker_block.get_text(" ", strip=True)).group(1)
                    speaker = re.sub(r"\s*Download\s*$", "", speaker).strip(" -–")
                    if speaker:
                        lines.append(f"Speakers: {speaker}")
                if links:
                    lines.append(" | ".join(links))
                lines.append(description if description else
                             "No abstract published; title, speakers and materials only.")
                lines.append("")
        return "\n".join(lines), count
