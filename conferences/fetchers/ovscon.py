"""OVS+OVNcon: one static program page with anchored abstracts and materials.

2024 uses h3 + p abstracts, 2025 h3 + pre, and 2026 div.talk cards.
The schedule's #tN anchors join each talk to its abstract and material links;
opening/closing remarks, breaks and sponsors are not program items. No bot
blocking observed. Discovery reads dates from the introductory paragraph,
not CFP deadlines elsewhere on the page.
"""

from __future__ import annotations

import re
from typing import Iterable, Optional
from urllib.parse import quote, urljoin, urlparse

from bs4 import BeautifulSoup

from .base import (
    Fetcher, FetchResult, ProbeResult, http_get, looks_blocked,
    scan_end_date, OK, NOT_PUBLISHED,
)

_TALK = re.compile(r"^t\d+$")
_SPEAKER = re.compile(r"^Speaker(?:\(s\)|s)?:\s*", re.I)
_RANGE = re.compile(r"\b([A-Za-z]+)\s+\d{1,2}\s*(?:[-–&]|and)\s*(\d{1,2}),?\s+(\d{4})\b")


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _row_links(row, base_url: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for a in row.select("a[href]"):
        url = quote(urljoin(base_url, a["href"]), safe=":/?#[]@!$&'*+,;=%~")
        parsed = urlparse(url)
        host = (parsed.hostname or "").removeprefix("www.")
        if host in ("youtu.be", "youtube.com"):
            found.setdefault("video", url)
        elif parsed.path.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
            if url not in found.values():
                found.setdefault("slides" if "slides" not in found else "slides2", url)
    return found


def talk_links(soup: BeautifulSoup, url: str) -> dict[str, str]:
    """Refresh only the schedule row for this anchor, never the whole program."""
    fragment = urlparse(url).fragment
    if not _TALK.fullmatch(fragment):
        return {}
    for a in soup.select("table td a[href]"):
        if a["href"] == f"#{fragment}":
            return _row_links(a.find_parent("tr"), url)
    return {}


class OvsconFetcher(Fetcher):
    name = "ovscon"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if looks_blocked(resp):
                return self.manual(entry, f"blocked ({resp.status_code} / challenge)")
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, detail="program not posted yet", source_url=url)
            if resp.status_code != 200:
                return self.manual(entry, f"unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse(resp.text, url)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(
            status=OK if count else NOT_PUBLISHED,
            program_text=text,
            source_url=url,
            item_count=count,
            detail=f"parsed {count} talks" if count else "no anchored talks with abstracts found yet",
        )

    def _parse(self, html: str, url: str) -> tuple[str, int]:
        soup = BeautifulSoup(html, "html.parser")
        main = soup.find("main") or soup
        lines: list[str] = []
        seen: set[str] = set()
        for a in main.select("table td a[href]"):
            fragment = a["href"].removeprefix("#")
            if not a["href"].startswith("#") or not _TALK.fullmatch(fragment) or fragment in seen:
                continue
            detail = main.find(id=fragment)
            title = _clean(a.get_text(" "))
            if detail is None or not title:
                continue
            speakers = ""
            paragraphs: list[str] = []
            if detail.name == "div" and "talk" in detail.get("class", []):
                speaker = detail.select_one(".speakers")
                speakers = _clean(speaker.get_text(" ")) if speaker else ""
                abstract = detail.select_one(".abstract")
                if abstract:
                    paragraphs.append(_clean(abstract.get_text(" ")))
            elif detail.name == "h3":
                for node in detail.find_next_siblings():
                    text = _clean(node.get_text(" "))
                    if node.name == "h2" or (node.name == "h3" and not _SPEAKER.match(text)):
                        break
                    if _SPEAKER.match(text):
                        speakers = _SPEAKER.sub("", text)
                    elif node.name in ("p", "pre", "ul", "ol") and text:
                        paragraphs.append(text)
            if not any(paragraphs):
                continue  # A schedule/placeholder alone is not a digestible talk.
            seen.add(fragment)
            links = {"page": urljoin(url, f"#{fragment}"), **_row_links(a.find_parent("tr"), url)}
            lines.append(f"### {title}")
            if speakers:
                lines.append(f"Speakers: {_SPEAKER.sub('', speakers)}")
            lines.append(" | ".join(f"{'slides' if k == 'slides2' else k}: {v}" for k, v in links.items()))
            lines.extend(paragraphs)
            lines.append("")
        return "\n".join(lines), len(seen)

    def probe(self, entry: dict, years: Optional[Iterable[int]] = None) -> ProbeResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return ProbeResult(False, "404 (no such edition yet)", source_url=url)
            if looks_blocked(resp) or resp.status_code != 200:
                return ProbeResult(False, f"blocked or unexpected status {resp.status_code}", source_url=url)
            resp.encoding = "utf-8"
            soup = BeautifulSoup(resp.text, "html.parser")
            heading = soup.select_one("main h1")
            intro = heading.find_next("p") if heading else None
            text = _clean(intro.get_text(" ")) if intro else ""
            # November 20&21, 2024 / November 19 - 20, 2025 -> last day.
            text = _RANGE.sub(r"\1 \2, \3", text)
            end = scan_end_date(text, years)
            return ProbeResult(True, "200; dates read from introduction" if end else "200; dates not found",
                               end_date=end, source_url=url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
