"""ACM IMC's program page: papers with authors, abstracts and DOI links.

conferences.sigcomm.org/imc/<year>/program/ is server-rendered HTML. Each paper
row pairs the title link (an #anchor into the same page) with a hidden abstract
panel and a doi.org Paper button. Sessions group the papers; the fetcher emits
one item per paper. No bot blocking observed (the SIGCOMM site already works
for the sigcomm fetcher). No extraction services or YouTube searches at fetch
time.
"""

from __future__ import annotations

import re

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_SESSION = re.compile(r"^Session\s+\d+\s*:\s*(.+?)\s*(?:\(Session Chair:.*)?$", re.S)
_OVERHEAD = re.compile(r"keynote|opening|welcome|break|lunch|reception|poster|awards|business", re.I)


class ImcFetcher(Fetcher):
    name = "imc"

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
                           source_url=url, item_count=count, detail=f"parsed {count} papers")

    def _parse(self, soup: BeautifulSoup, url: str) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        for heading in soup.select("li.panel-subheading-session"):
            match = _SESSION.match(heading.get_text(" ", strip=True))
            if not match or _OVERHEAD.search(match.group(1)):
                continue
            lines.append(f"## {match.group(1).strip()}")
            for item in heading.find_next_siblings("ul"):
                if "list-group-session" not in (item.get("class") or []):
                    break
                for row in item.select("li.list-group-item"):
                    title_link = row.select_one("div.paper-body strong a[href]")
                    if not title_link:
                        continue
                    title = title_link.get_text(" ", strip=True)
                    anchor = title_link.get("href", "")
                    if not title or anchor in seen:
                        continue
                    seen.add(anchor)
                    links = [f"page: {url}{anchor if anchor.startswith('#') else ''}"]
                    doi = row.select_one('a[href^="https://doi.org/"]')
                    if doi:
                        links.append(f"pdf: {doi['href']}")
                    lines.append(f"### {title}")
                    speakers = row.select_one("div.paper-body > div > i")
                    if speakers:
                        names = re.sub(r"\s+", " ", speakers.parent.get_text(" ", strip=True)).strip(" ,")
                        if names:
                            lines.append(f"Authors: {names}")
                    if len(links) > 1:
                        lines.append(" | ".join(links))
                    abstract = row.select_one("div.collapse")
                    if abstract and abstract.get_text(" ", strip=True).startswith("Abstract:"):
                        lines.append(abstract.get_text(" ", strip=True)[len("Abstract:"):].strip())
                    else:
                        lines.append("No abstract in the program; title and authors only.")
                    lines.append("")
        return "\n".join(lines), len(seen)
