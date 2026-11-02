"""AusNOG's program page: day tables with titles, speakers, slides and videos.

www.ausnog.net/events/ausnog-<year>/program serves one table per conference
day — time | slide icon | video icon | title with speaker and affiliation.
The icon links are the real materials (PDF decks, YouTube recordings); breaks
are grey rows without links. Pre-conference socials are skipped. Plain HTML,
no bot blocking.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_SKIP = re.compile(r"^(?:coffee|lunch|break|registration|welcome drinks|afternoon tea|beer, gear and peer)", re.I)


class AusnogFetcher(Fetcher):
    name = "ausnog"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="program not published yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"), url)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} talks")

    def _parse(self, soup: BeautifulSoup, url: str) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        for table in soup.select("table"):
            caption = table.find("caption")
            if not caption:
                continue
            heading = caption.get_text(" ", strip=True)
            if "pre conference" in heading.lower():
                continue
            lines.append(f"## {heading}")
            for row in table.select("tbody tr"):
                cells = row.find_all("td")
                if not cells:
                    continue
                body = cells[-1]
                title_el = body.find("strong")
                if not title_el:
                    continue
                title = title_el.get_text(" ", strip=True)
                if not title or _SKIP.match(title) or title in seen:
                    continue
                seen.add(title)
                who = body.get_text(" ", strip=True)[len(title):].strip(" -–")
                lines.append(f"### {title}")
                if who:
                    lines.append(f"Speakers: {who}")
                links: list[str] = []
                for cell in cells[:-1]:
                    for a in cell.find_all("a", href=True):
                        href = urljoin(url, a["href"])
                        if href.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
                            links.append(f"slides: {href}")
                        elif "youtube.com" in href or "youtu.be" in href:
                            links.append(f"video: {href}")
                if links:
                    lines.append(" | ".join(links))
                lines.append("No abstract published; title, speakers and materials only.")
                lines.append("")
        return "\n".join(lines), len(seen)
