"""ARIN Public Policy and Members Meetings: agenda tables with per-item links.

www.arin.net/participate/meetings/ARIN<n> serves one table per day — Agenda
Item | Speaker | Presentation | Webcast. Policy rows link their draft page,
presentations are PDFs and the webcast column carries a timestamped YouTube
link per agenda item. Plain HTML, no bot blocking. No extraction services or
YouTube searches at fetch time.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, scan_end_date, OK, NOT_PUBLISHED

_SKIP = re.compile(r"^(?:break|lunch|registration|welcome coffee|adjourn)", re.I)


class ArinFetcher(Fetcher):
    name = "arin"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="agenda not published yet")
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
        for table in soup.select("table.table"):
            caption = table.find("caption")
            if not caption or "meeting" not in caption.get_text(" ", strip=True).lower():
                continue
            lines.append(f"## {caption.get_text(' ', strip=True)}")
            for row in table.select("tbody tr"):
                cells = row.find_all("td")
                if len(cells) < 2:
                    continue
                item, speaker = cells[0], cells[1]
                title = item.get_text(" ", strip=True)
                if not title or _SKIP.match(title) or title in seen:
                    continue
                seen.add(title)
                lines.append(f"### {title}")
                if speaker.get_text(" ", strip=True):
                    lines.append(f"Speakers: {speaker.get_text(' ', strip=True)}")
                links: list[str] = []
                page = item.find("a", href=True)
                if page:
                    links.append(f"page: {urljoin(url, page['href'])}")
                for cell in cells[2:]:
                    for a in cell.find_all("a", href=True):
                        href = urljoin(url, a["href"])
                        if href.lower().endswith(".pdf"):
                            links.append(f"slides: {href}")
                        elif "youtube.com" in href or "youtu.be" in href:
                            links.append(f"video: {href}")
                if links:
                    lines.append(" | ".join(links))
                lines.append("No abstract; agenda item, speaker and materials only.")
                lines.append("")
        return "\n".join(lines), len(seen)
