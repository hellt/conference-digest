"""CPH^Automate schedules, talk abstracts and slides.

cph-automate.network is a static Hextra site. Each year's /schedule/ page
lists its talk rows with exact titles, speakers and links to individual talk
pages. Those pages carry the full abstract and any PDF/PPTX deck. The 2026
recordings live in an IDA playlist rather than on the individual talk pages,
so only per-talk materials actually published by the source are emitted.

Discovery reads the edition overview, which states the full event date. No
bot blocking or extraction services.
"""

from __future__ import annotations

from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, looks_blocked, scan_end_date, OK, NOT_PUBLISHED

_SLIDES = (".pdf", ".pptx", ".ppt", ".odp", ".key")


class CphAutomateFetcher(Fetcher):
    name = "cphautomate"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="schedule not published yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            talks = self._schedule(BeautifulSoup(resp.text, "html.parser"), url)

            lines = ["## Program", ""]
            for title, speakers, page in talks:
                detail = http_get(page)
                if detail.status_code != 200 or looks_blocked(detail):
                    raise RuntimeError(f"talk page returned {detail.status_code}: {page}")
                detail.encoding = "utf-8"
                soup = BeautifulSoup(detail.text, "html.parser")
                abstract = soup.select_one(".cph-talk-detail-abstract")
                body = abstract.get_text(" ", strip=True) if abstract else ""

                links = [f"page: {page}"]
                for a in soup.select(".cph-talk-detail a[href]"):
                    href = urljoin(page, a["href"])
                    if urlparse(href).path.lower().endswith(_SLIDES):
                        link = f"slides: {href}"
                        if link not in links:
                            links.append(link)

                lines.append(f"### {title}")
                if speakers:
                    lines.append(f"Speakers: {speakers}")
                lines.append(" | ".join(links))
                lines.append(body or "No abstract published; title and speakers only.")
                lines.append("")
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")

        return FetchResult(status=OK if talks else NOT_PUBLISHED, program_text="\n".join(lines),
                           source_url=url, item_count=len(talks), detail=f"parsed {len(talks)} talks")

    def _schedule(self, soup: BeautifulSoup, url: str) -> list[tuple[str, str, str]]:
        talks = []
        seen = set()
        for row in soup.select(".cph-tt-talk"):
            link = row.select_one(".cph-tt-title a[href]")
            if link is None:
                continue
            title = link.get_text(" ", strip=True)
            page = urljoin(url, link["href"])
            if not title or page in seen:
                continue
            seen.add(page)
            speakers = ", ".join(a.get_text(" ", strip=True) for a in row.select(".cph-tt-speaker a"))
            talks.append((title, speakers, page))
        return talks

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        overview = url.replace("/schedule/", "/")
        try:
            resp = http_get(overview)
            if resp.status_code == 404:
                return ProbeResult(False, "404 (no such edition yet)", source_url=overview)
            if resp.status_code != 200 or looks_blocked(resp):
                return ProbeResult(False, f"blocked or unexpected status {resp.status_code}", source_url=overview)
            resp.encoding = "utf-8"
            end = scan_end_date(resp.text, years)
            return ProbeResult(True, "edition overview" + ("; dates scanned" if end else ""),
                               end_date=end, location="Copenhagen", source_url=overview)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=overview)
