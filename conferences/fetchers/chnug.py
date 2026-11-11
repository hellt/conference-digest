"""Swiss Network User Group (CHNUG) meetup programs, slides and recordings.

chnug.ch/chnugNNN is a static Jekyll page. The agenda is one top-level list
item per slot: time, exact title, a parenthesised speaker/affiliation line,
and nested Slides/Recording links. Administrative slots are dropped. CHNUG
publishes no abstracts or per-talk pages, so the shared agenda is deliberately
not emitted as a `page:` link. The page title states the exact meetup date as
"12th of March 2026"; probe() normalises that wording for the shared scanner.
No bot blocking or extraction services.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, looks_blocked, scan_end_date, OK, NOT_PUBLISHED

_TIME = re.compile(r"^\s*\d{1,2}:\d{2}\s*[-–—]\s*\d{1,2}:\d{2}\s*:?\s*")
_SPEAKERS = re.compile(r"\s*\(Speakers?:\s*(.+?)\)\s*$")
_SKIP = re.compile(
    r"^(?:arrival|welcome(?:\s+and\s+intro(?:duction)?)?|closing\b|outro\b|"
    r"technical\s+break|further\s+education|networking\b|registration\b)", re.I
)
_ORDINAL_OF = re.compile(r"\b(\d{1,2})(?:st|nd|rd|th)\s+of\s+", re.I)


def _speaker_list(raw: str) -> str:
    """Turn "Jane Doe + John Roe @Example" into affiliations for both names."""
    affiliation = ""
    match = re.search(r"\s+@([^@]+)$", raw)
    if match:
        affiliation = match.group(1).strip()
        raw = raw[:match.start()]
    names = [name.strip() for name in re.split(r"\s+\+\s+|\s*,\s*", raw) if name.strip()]
    return ", ".join(f"{name} ({affiliation})" if affiliation else name for name in names)


class ChnugFetcher(Fetcher):
    name = "chnug"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="meetup page not up yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"), url)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count,
                           detail=f"parsed {count} talks; no abstracts published")

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return ProbeResult(False, "404 (no such edition yet)", source_url=url)
            if resp.status_code != 200 or looks_blocked(resp):
                return ProbeResult(False, f"blocked or unexpected status {resp.status_code}", source_url=url)
            resp.encoding = "utf-8"
            soup = BeautifulSoup(resp.text, "html.parser")
            heading = next((h.get_text(" ", strip=True) for h in soup.select("h1")
                            if h.get_text(" ", strip=True).startswith("CHNUG #")), "")
            end = scan_end_date(_ORDINAL_OF.sub(r"\1 ", heading), years)
            return ProbeResult(True, "meetup page" + ("; dates scanned" if end else ""),
                               end_date=end, source_url=url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)

    def _parse(self, soup: BeautifulSoup, url: str) -> tuple[str, int]:
        lines: list[str] = []
        count = 0
        for agenda in soup.select("h2"):
            if not agenda.get_text(" ", strip=True).lower().startswith("agenda"):
                continue
            slots = agenda.find_next_sibling("ul")
            if slots is None:
                continue
            lines.append(f"## {agenda.get_text(' ', strip=True)}")
            for slot in slots.find_all("li", recursive=False):
                text = " ".join("".join(slot.find_all(string=True, recursive=False)).split())
                match = _SPEAKERS.search(text)
                if not match:
                    continue
                title = _TIME.sub("", text[:match.start()]).strip()
                if not title or _SKIP.match(title):
                    continue
                speakers = _speaker_list(match.group(1).strip())
                links: list[str] = []
                for a in slot.select("ul a[href]"):
                    href = urljoin(url, a["href"])
                    label = a.get_text(" ", strip=True).lower()
                    path = urlparse(href).path.lower()
                    if label == "slides" and path.endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
                        links.append(f"slides: {href}")
                    elif label == "recording" and (urlparse(href).hostname or "").removeprefix("www.") in (
                            "youtube.com", "youtu.be"):
                        links.append(f"video: {href}")
                count += 1
                lines.extend([f"### {title}", f"Speakers: {speakers}"])
                if links:
                    # PDF decks come before recordings even if the source lists
                    # Recording first; the writer can enrich from the deck.
                    links.sort(key=lambda link: not link.startswith("slides:"))
                    lines.append(" | ".join(links))
                lines.extend(["No abstract published; title, speakers and materials only.", ""])
        return "\n".join(lines), count
