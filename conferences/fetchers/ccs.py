"""ACM CCS's published schedule: sessions, exact paper titles and authors.

The conference site (www.sigsac.org/ccs/CCS<yy>/program/schedule.html) is plain
server-rendered HTML with one <article> per session and one <li> per paper.
Abstracts and papers live behind the ACM DL, so items carry title, authors and
session context only — the digest writer marks picks "from title and authors".
No bot blocking observed. No extraction services or YouTube searches at fetch
time.
"""

from __future__ import annotations

import re

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_ID = re.compile(r"\s*\([AB]#[0-9A-F]+\)\s*")
_SKIP_META = re.compile(r"registration|welcome|break|lunch|reception|poster session|opening|closing|coffee", re.I)


class CcsFetcher(Fetcher):
    name = "ccs"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="schedule not published yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"), url)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count,
                           detail=f"parsed {count} papers; titles and authors only")

    def _parse(self, soup: BeautifulSoup, url: str) -> tuple[str, int]:
        lines: list[str] = []
        count = 0
        for session in soup.select("article.schedule-session"):
            session_id = session.select_one(".schedule-session-id")
            title = session.find("h5")
            room = session.select_one(".schedule-room")
            if not (session_id and title and room) or _SKIP_META.search(title.get_text(" ")):
                continue
            heading = f"{session_id.get_text(' ', strip=True)} — {title.get_text(' ', strip=True)}"
            lines.append(f"## {heading} · {room.get_text(' ', strip=True)}")
            for paper in session.select("li.schedule-paper"):
                paper_title = paper.select_one(".schedule-paper-title")
                authors = paper.select_one(".schedule-authors")
                if not paper_title or not authors:
                    continue
                name = _ID.sub("", paper_title.get_text(" ", strip=True)).strip()
                if not name:
                    continue
                count += 1
                lines.append(f"### {name}")
                lines.append(f"Authors: {authors.get_text(' ', strip=True)}")
                lines.append("No public abstract; title, authors and session only.")
                lines.append("")
        return "\n".join(lines), count
