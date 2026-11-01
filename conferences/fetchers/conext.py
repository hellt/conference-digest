"""ACM CoNEXT's program partial: sessions, papers, abstracts and ACM DL links.

conferences.sigcomm.org/co-next/<year>/ is an Angular app, but every page is a
server-rendered partial (partials/program.html) with one block per session and
one row per paper: title, authors, a hidden Abstract panel and ACM DL + PDF
buttons. No bot blocking observed. No extraction services or YouTube searches
at fetch time.
"""

from __future__ import annotations

import re
from datetime import date

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, looks_blocked, scan_end_date, OK, NOT_PUBLISHED

_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7,
           "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12}
# "Monday, 1st, Dec 2025" — the program's day headers, which plain date
# scanning misses because of the comma between ordinal and month.
_DAY = re.compile(r"\b(?:Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)day,\s*(\d{1,2})(?:st|nd|rd|th)?,?\s+"
                  r"([A-Z][a-z]{2,8})\.?\s+(\d{4})", re.I)
_SESSION = re.compile(r"^(?:\d{1,2}:\d{2}\s*[-–]\s*\d{1,2}:\d{2}[:?]?\s*)?Session\s+\d+\s*:\s*(.+?)\s*(?:Session chair:.*)?$", re.I | re.S)
_SKIP = re.compile(r"^(?:workshops?|poster|welcome|break|breakfast|lunch|coffee|reception|closing|opening|awards?)\b", re.I)
_LABEL = re.compile(r"\s*(?:Long|Short|Poster|Award|Demo|Talk)\s*$")


def _day_dates(text: str, years) -> date | None:
    found = []
    for day, month, year in _DAY.findall(text):
        m = _MONTHS.get(month.lower()[:4]) or _MONTHS.get(month.lower()[:3])
        try:
            found.append(date(int(year), m, int(day)))
        except (ValueError, TypeError):
            continue
    found = [d for d in found if years is None or d.year in set(years)]
    return max(found) if found else None


class ConextFetcher(Fetcher):
    name = "conext"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="program partial not published yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"))
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} papers")

    def _parse(self, soup: BeautifulSoup) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        for session in soup.select("li.list-group-item.session"):
            match = _SESSION.match(session.get_text(" ", strip=True))
            if not match or _SKIP.match(match.group(1)):
                continue
            lines.append(f"## {match.group(1).strip()}")
            for row in session.find_next_sibling("ul").select("li.list-group-item"):
                title_el = row.select_one(".col-md-7 strong, .col-md-10 strong")
                if not title_el:
                    continue
                title = _LABEL.sub("", title_el.get_text(" ", strip=True)).strip()
                if not title or title in seen:
                    continue
                seen.add(title)
                authors = row.select_one(".col-md-7 > div:not([style]), .col-md-10 > div:not([style])")
                links: list[str] = []
                for a in row.select('a[href^="https://dl.acm.org/doi"]'):
                    if "/pdf/" in a["href"]:
                        links.append(f"pdf: {a['href']}")
                    else:
                        links.append(f"page: {a['href']}")
                lines.append(f"### {title}")
                if authors:
                    names = re.sub(r"\s+", " ", authors.get_text(" ", strip=True)).strip(" ,;")
                    if names:
                        lines.append(f"Authors: {names}")
                if links:
                    lines.append(" | ".join(links))
                abstract = row.select_one("div.collapse")
                if abstract:
                    body = abstract.get_text(" ", strip=True)
                    lines.append(re.sub(r"^Abstract:\s*", "", body).strip())
                else:
                    lines.append("No abstract in the program; title and authors only.")
                lines.append("")
        return "\n".join(lines), len(seen)

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return ProbeResult(False, "404 (no such edition yet)", source_url=url)
            if resp.status_code != 200 or looks_blocked(resp):
                return ProbeResult(False, f"blocked ({resp.status_code} / challenge)", source_url=url)
            resp.encoding = "utf-8"
            end = _day_dates(resp.text, years) or scan_end_date(resp.text, years)
            return ProbeResult(True, "program partial; day headers scanned" if end else "dates not found",
                               end_date=end, source_url=url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
