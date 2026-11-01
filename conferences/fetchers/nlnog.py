"""NLNOG Day's public program table: exact titles, speakers, decks and videos.

The Hugo site uses HTML meta-refresh aliases; follow only its explicit canonical
NLNOG URL. No abstracts are published in the table, and none are invented.
No bot blocking observed. No extraction services or YouTube searches at fetch time.
"""

from __future__ import annotations

import re
from collections import Counter
from urllib.parse import parse_qs, urljoin, urlparse

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, looks_blocked, scan_end_date, OK, NOT_PUBLISHED

_SKIP = re.compile(r"^(?:registration|welcome|opening|closing|coffee|lunch|food|drinks|the merciless nlnog quiz)\b", re.I)


def _video_id(url: str) -> str:
    parsed = urlparse(url)
    if parsed.hostname == "youtu.be":
        video = parsed.path.strip("/")
    elif parsed.hostname in ("www.youtube.com", "youtube.com") and parsed.path == "/watch":
        video = (parse_qs(parsed.query).get("v") or [""])[0]
    else:
        return ""
    return video if re.fullmatch(r"[A-Za-z0-9_-]{11}", video) else ""


def _program(url: str):
    for _ in range(2):
        resp = http_get(url)
        if resp.status_code == 404:
            return None, url
        if resp.status_code != 200 or looks_blocked(resp):
            raise RuntimeError(f"blocked or unexpected status {resp.status_code}")
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
        refresh = soup.find("meta", attrs={"http-equiv": re.compile("^refresh$", re.I)})
        canonical = soup.select_one('link[rel="canonical"][href]')
        if not refresh or not canonical:
            return soup, url
        target = urljoin(url, canonical["href"])
        if urlparse(target).hostname != "nlnog.net" or target == url:
            break
        url = target
    raise ValueError("unresolved NLNOG canonical redirect")


class NlnogFetcher(Fetcher):
    name = "nlnog"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            soup, source = _program(url)
            if soup is None:
                return FetchResult(status=NOT_PUBLISHED, source_url=source, detail="program not posted yet")
            text, count = self._parse(soup, source)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=source, item_count=count, detail=f"parsed {count} talks; no abstracts published")

    def _parse(self, soup: BeautifulSoup, url: str) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        # The 2026 source reuses one video for two different talks. Neither is
        # safe to attach; let verified recording search resolve them later.
        videos = Counter(v for a in soup.select("main table a[href]") if (v := _video_id(a["href"])))
        for table in soup.select("main table"):
            headers = [th.get_text(" ", strip=True).lower() for th in table.select("th")]
            if "topic" not in headers or not any(h.startswith("presenter") for h in headers):
                continue
            for row in table.select("tr"):
                cells = row.find_all("td", recursive=False)
                if len(cells) < 3:
                    continue
                title = cells[1].get_text(" ", strip=True)
                speakers = cells[2].get_text(" ", strip=True)
                if not title or not speakers or title in seen or _SKIP.match(title):
                    continue
                seen.add(title)
                links: list[str] = []
                for a in row.select("a[href]"):
                    href = urljoin(url, a["href"])
                    parsed = urlparse(href)
                    if parsed.path.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
                        links.append(f"slides: {href}")
                    elif (video := _video_id(href)) and videos[video] == 1:
                        links.append(f"video: {href}")
                lines.extend([f"### {title}", f"Speakers: {speakers}"])
                # No page: the shared table is not a talk page, and refreshing it
                # would silently attach another talk's slides or recording.
                if links:
                    lines.append(" | ".join(links))
                lines.extend(["No abstract published; title, speakers and materials only.", ""])
        return "\n".join(lines), len(seen)

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            soup, source = _program(url)
            if soup is None:
                return ProbeResult(False, "404 (no such edition yet)", source_url=source)
            intro = soup.select_one("main p")
            end = scan_end_date(intro.get_text(" ") if intro else "", years)
            return ProbeResult(True, "event introduction", end_date=end, source_url=source)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
