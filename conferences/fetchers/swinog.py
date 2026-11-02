"""SwiNOG meeting pages: talks with speakers, abstracts, slides and recordings.

www.swinog.ch/meetings/swinog<n>/ renders the program with the swinog-program
plugin: one article per talk — title, "Name · Company", abstract, and link
spans holding Slides and Video links (recordings exist since 2014). Breaks
and meals are separate row types, skipped here. The Quick facts box states the
meeting dates. No bot blocking. looks_blocked()'s body markers are not
applied: the page embeds form-validation strings that mention recaptcha —
status codes alone decide.
"""

from __future__ import annotations

import re

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, scan_end_date, OK, NOT_PUBLISHED

_SKIP = re.compile(r"^(?:welcome|closing|break|lunch|registration|coffee|social|get together)", re.I)


class SwinogFetcher(Fetcher):
    name = "swinog"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="meeting page not up yet")
            if resp.status_code != 200 or resp.status_code in (403, 429, 503):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"))
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} talks")

    def probe(self, entry: dict, years=None) -> ProbeResult:
        # Status-only, like fetch(): the page legitimately contains
        # form-validation strings that mention recaptcha.
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return ProbeResult(False, "404 (no such edition yet)", source_url=url)
            if resp.status_code != 200:
                return ProbeResult(False, f"unexpected status {resp.status_code}", source_url=url)
            resp.encoding = "utf-8"
            end = scan_end_date(resp.text, years)
            return ProbeResult(True, "200; meeting page" + ("; dates scanned" if end else ""),
                               end_date=end, source_url=url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)

    def _parse(self, soup: BeautifulSoup) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        headings: dict[str, list[str]] = {}
        count = 0
        for row in soup.select("article.swinog-program__row--talk"):
            title_el = row.select_one(".swinog-program__title")
            if not title_el:
                continue
            title = title_el.get_text(" ", strip=True)
            if not title or _SKIP.match(title) or title in seen:
                continue
            seen.add(title)
            count += 1
            heading_el = row.find_previous("h2")
            heading = re.sub(r"Talks, slides & recordings\.?", "", heading_el.get_text(" ", strip=True)).strip() \
                if heading_el else "Program"
            block = headings.setdefault(heading or "Program", [])
            block.append(f"### {title}")
            who = row.select_one(".swinog-program__who")
            if who:
                block.append(f"Speakers: {who.get_text(' ', strip=True).replace('·', '-')}")
            links: list[str] = []
            for a in row.select(".swinog-program__link a[href]"):
                text = a.get_text(" ", strip=True).lower()
                if "video" in text or "youtube" in a["href"]:
                    links.append(f"video: {a['href']}")
                else:
                    links.append(f"slides: {a['href']}")
            if links:
                block.append(" | ".join(links))
            abstract = row.select_one(".swinog-program__abstract")
            body = re.sub(r"\s+", " ", abstract.get_text(" ", strip=True)) if abstract else ""
            block.append(body if body else "No abstract published; title, speakers and materials only.")
            block.append("")
        for heading in headings:
            lines.append(f"## {heading}")
            lines += headings[heading]
        return "\n".join(lines), count
