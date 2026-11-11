"""AI Engineer schedules, plus NYC's chapter-sliced recording pages.

The public data guide (https://ai.engineer/data) documents per-edition
sessions.json feeds. Those are the preferred source: exact titles, speakers,
descriptions, days and rooms for the complete structured schedule. Published
recording records are deliberately not matched to schedule sessions by title.

NYC 2026 has no structured feed. Its Watch & read page instead turns two
full-day YouTube streams into per-session cards. Every card's video and offset
matches a stream chapter, and its reading-edition page has a full transcript.
Administrative Remarks cards are dropped. Other layouts with neither source
return zero items rather than a made-up program.
"""

from __future__ import annotations

import re
from urllib.parse import parse_qs, urljoin, urlparse

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED


def _text(value) -> str:
    if hasattr(value, "get_text"):
        value = value.get_text(" ", strip=True)
    return re.sub(r"\s+", " ", str(value or "")).strip()


def _recording(href: str) -> str:
    """Canonical watch URL plus a numeric chapter offset, when published."""
    query = parse_qs(urlparse(href).query)
    vid = (query.get("v") or [""])[0]
    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", vid):
        return ""
    url = f"https://www.youtube.com/watch?v={vid}"
    start = (query.get("t") or [""])[0]
    if re.fullmatch(r"\d+s?", start):
        url += f"&t={start.rstrip('s')}s"
    return url


class AiEngineerFetcher(Fetcher):
    name = "aiengineer"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        data_url = url.rstrip("/") + "/sessions.json"
        try:
            resp = http_get(data_url, timeout=60)
            if resp.status_code == 200:
                # Talk descriptions can discuss CAPTCHAs; JSON is not a challenge page.
                if "application/json" not in resp.headers.get("content-type", ""):
                    return self.manual(entry, "schedule endpoint returned non-JSON content")
                payload = resp.json()
                text, count = self._parse_schedule(payload)
                return FetchResult(
                    status=OK if count else NOT_PUBLISHED,
                    program_text=text, source_url=data_url, item_count=count,
                    detail=f"parsed {count} sessions from the public JSON schedule",
                )
            if resp.status_code != 404:
                return self.manual(entry, f"schedule endpoint blocked or unexpected status {resp.status_code}")

            # A missing JSON feed is expected on the NYC Watch & read layout.
            resp = http_get(url, timeout=60)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="event page not published yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse_cards(BeautifulSoup(resp.text, "html.parser"), resp.url)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count,
                           detail=f"parsed {count} chapter-sliced talks with transcript pages")

    def _parse_schedule(self, payload: dict) -> tuple[str, int]:
        rows = payload.get("sessions")
        if not isinstance(rows, list) or payload.get("totalSessions") != len(rows):
            raise ValueError("incomplete or invalid public schedule")
        groups: dict[str, list[str]] = {}
        count = 0
        for row in rows:
            title = _text(row.get("title"))
            if not title:
                continue
            count += 1
            block = [f"### {title}"]
            speakers = [_text(s) for s in row.get("speakers") or [] if _text(s)]
            if speakers:
                block.append("Speakers: " + ", ".join(speakers))
            schedule = " · ".join(filter(None, (
                _text(row.get("time")), _text(row.get("room")), _text(row.get("type"))
            )))
            if schedule:
                block.append("Schedule: " + schedule)
            block.append(_text(row.get("description")) or
                         "No description published; title, speakers and schedule only.")
            block.append("")
            heading = " — ".join(filter(None, (_text(row.get("day")), _text(row.get("track"))))) or "Program"
            groups.setdefault(heading, []).extend(block)

        lines = []
        for heading, block in groups.items():
            lines.append(f"## {heading}")
            lines.extend(block)
        return "\n".join(lines), count

    def _parse_cards(self, soup: BeautifulSoup, source_url: str) -> tuple[str, int]:
        groups: dict[str, list[str]] = {}
        count = 0
        for card in soup.select("article[data-session]"):
            title_link = card.select_one('h3 a[href*="/talks/"]')
            title = _text(title_link)
            meta = _text(card.select_one("p.text-xs.uppercase")) or "Program"
            if not title or meta.endswith("· Remarks"):
                continue
            count += 1

            speakers = []
            for person in card.select("p"):
                name = _text(person.select_one("span.font-semibold"))
                company = _text(person.select_one("strong"))
                if name:
                    speakers.append(f"{name} ({company})" if company else name)

            links = [f"page: {urljoin(source_url, title_link['href'])}"]
            for anchor in card.select('a[href*="youtube.com/watch"]'):
                if video := _recording(anchor["href"]):
                    links.append(f"video: {video}")
                    break

            block = [f"### {title}"]
            if speakers:
                block.append("Speakers: " + ", ".join(speakers))
            block.append(" | ".join(links))
            synopsis = _text(card.select_one("p.mt-5.text-base"))
            block.append(synopsis or "No synopsis published; use the linked reading edition or recording.")
            block.append("")
            groups.setdefault(meta, []).extend(block)

        lines = []
        for heading, block in groups.items():
            lines.append(f"## {heading}")
            lines.extend(block)
        return "\n".join(lines), count
