"""NZNOG's accepted-talks pages: speaker-headed blocks with abstracts.

nznog.org keeps one site per conference under /conferences/nznog-<year>/.
talks.html lists the accepted talks in the order received: an h3 speaker
heading, a bold line, abstract paragraphs and an italic speaker bio. The
page links no slides, and recordings are whole-day streams on NZNOG's
YouTube channel rather than per-talk uploads, so the links step finds none
of the latter — that stays honest rather than guessed.

The layout changed between editions: 2026 puts the plain speaker name in
the h3 and the talk title in the bold line; 2025 packed "Speaker - Title"
into the h3 (sometimes with two speakers before the dash) and made the
bold line the affiliation. Both are read by splitting the h3 on its first
" - ": a title may itself contain dashes, so only the first split counts.

The conference landing page one level up (/conferences/nznog-<year>.html)
states the meeting dates as "Monday 23 March" table rows, with the year only
in its heading, so probe() parses them and takes the year from the key.
"""

from __future__ import annotations

import re
from datetime import date

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_MONTHS = ("january february march april may june july august september october november december"
           ).split()
_ROW = re.compile(r"\b(?:Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)day\s+(\d{1,2})\s+([A-Z][a-z]+)\b")


class NznogFetcher(Fetcher):
    name = "nznog"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url, timeout=120)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="no talks page yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"))
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} talks")

    def _parse(self, soup: BeautifulSoup) -> tuple[str, int]:
        content = soup.find("div", class_="post-content") or soup
        lines: list[str] = []
        count = 0
        title = affiliation = ""
        speakers: list[str] = []
        abstract: list[str] = []

        def flush() -> None:
            nonlocal count
            if title:
                count += 1
                lines.append(f"### {title}")
                if speakers:
                    named = ", ".join(speakers) + (f" ({affiliation})" if affiliation else "")
                    lines.append(f"Speakers: {named}")
                lines.extend(abstract)
                lines.append("")

        for el in content.find_all(recursive=False):
            if el.name == "h3":
                flush()
                title, affiliation, speakers, abstract = "", "", [], []
                head = el.get_text(" ", strip=True)
                m = re.search(r"\s+-\s+", head)
                if m:                                   # 2025: "Speaker(s) - Title"
                    speakers = [s.strip() for s in head[:m.start()].split(",") if s.strip()]
                    title = head[m.end():].strip()
                else:                                   # 2026: the h3 is the speaker alone
                    speakers = [head] if head else []
            elif el.name == "p" and el.find("strong"):
                if title:                                # 2025: the bold line is the affiliation
                    affiliation = el.get_text(" ", strip=True)
                else:                                    # 2026: the bold line is the title
                    title = el.get_text(" ", strip=True)
            elif el.name in ("p", "ul") and title:
                if el.find("em"):                        # speaker bio, not program content
                    continue
                para = el.get_text(" ", strip=True)
                if para:
                    abstract.append(para)
        flush()
        if count:
            lines.insert(0, "## Accepted talks")
        return "\n".join(lines), count

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
        except Exception as e:
            return ProbeResult(False, f"request error: {e}", source_url=url)
        if resp.status_code == 404:
            return ProbeResult(False, "404 (no such edition yet)", source_url=url)
        if resp.status_code != 200 or looks_blocked(resp):
            return ProbeResult(False, f"blocked ({resp.status_code})", source_url=url)
        year = next(iter(years), None) if years else None
        if year is None:
            m = re.search(r"nznog-(\d{4})", entry["key"])
            year = int(m.group(1)) if m else None
        end = self._end_date(url, year) if year else None
        return ProbeResult(True, f"200; dates {'read off the landing page' if end else 'not found'}",
                           end_date=end, source_url=url)

    def _end_date(self, url: str, year: int) -> date | None:
        """The last day stated by the conference landing page (its dates carry no year)."""
        landing = re.sub(r"/nznog-\d+/talks\.html$", f"/nznog-{year}.html", url)
        if landing == url:
            return None
        try:
            resp = http_get(landing)
            if resp.status_code != 200:
                return None
            resp.encoding = "utf-8"
        except Exception:
            return None
        found = [date(year, _MONTHS.index(m.lower()) + 1, int(d))
                 for d, m in _ROW.findall(resp.text) if m.lower() in _MONTHS]
        return max(found) if found else None
