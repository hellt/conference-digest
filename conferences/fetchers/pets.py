"""PETS accepted-papers list: exact titles and authors, grouped by PoPETs issue.

petsymposium.org/<year>/paperlist.php is a static page: one "Issue" heading per
PoPETs issue and one <li> per paper — the title, optional artifact links and
an italic author line. Papers and abstracts live in the PoPETs journal (not
fetched); the digest writer marks picks "from title and authors". No bot
blocking.
"""

from __future__ import annotations

import re

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED


class PetsFetcher(Fetcher):
    name = "pets"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="paper list not published yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"))
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} papers; titles and authors only")

    def _parse(self, soup: BeautifulSoup) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        count = 0
        for issue in soup.select("h3.side-headings"):
            papers = issue.find_next("ul")
            if papers is None:
                continue
            lines.append(f"## {issue.get_text(' ', strip=True)}")
            for li in papers.find_all("li", recursive=False):
                authors = li.find("span")
                if authors:
                    authors = authors.extract()
                for a in li.find_all("a"):
                    a.extract()  # artifact badges, not part of the title
                title = li.get_text(" ", strip=True)
                title = re.sub(r"Artifact:.*$", "", title).strip(" ,")
                if not title or title in seen:
                    continue
                seen.add(title)
                count += 1
                lines.append(f"### {title}")
                if authors:
                    names = authors.get_text(" ", strip=True)
                    names = re.sub(r",?\s+and\s+", ", ", names).strip(" ,")
                    lines.append(f"Authors: {names}")
                lines.append("No public abstract; title, authors and issue only.")
                lines.append("")
        return "\n".join(lines), count
