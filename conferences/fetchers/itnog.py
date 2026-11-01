"""ITNOG meeting pages: program tables with titles, speakers and slide files.

www.itnog.it/itnog<n> is a static page whose tables list every slot — Start |
End | Title | Speakers | Slides (or Title | Sponsor for vendor workshops on
day 1). The slide cells link PDFs under files/. Titles are Italian; the digest
presents them as-is. No bot blocking.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_SKIP = re.compile(r"^(?:welcome|code of conduct|light lunch|aperitif|social dinner|lunch|break)", re.I)


class ItnogFetcher(Fetcher):
    name = "itnog"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="meeting page not up yet")
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
        count = 0
        for table in soup.select("table"):
            headers = [th.get_text(" ", strip=True).lower() for th in table.select("th")]
            if "title" not in headers:
                continue
            for row in table.select("tbody tr"):
                cells = row.find_all("td")
                if len(cells) < 3:
                    continue
                title_cell = cells[2]
                title = title_cell.get_text(" ", strip=True)
                if not title or _SKIP.match(title) or title in seen:
                    continue
                seen.add(title)
                count += 1
                lines.append(f"### {title}")
                speakers = cells[3].get_text(" ", strip=True) if len(cells) > 3 else ""
                if speakers:
                    lines.append(f"Speakers: {speakers}")
                links = []
                for a in title_cell.find_all("a", href=True) + (cells[4].find_all("a", href=True) if len(cells) > 4 else []):
                    href = urljoin(url, a["href"])
                    if href.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
                        links.append(f"slides: {href}")
                if links:
                    lines.append(" | ".join(links))
                lines.append("No abstract published; title, speakers and materials only.")
                lines.append("")
        if lines:
            lines.insert(0, "## ITNOG program")
        return "\n".join(lines), count
