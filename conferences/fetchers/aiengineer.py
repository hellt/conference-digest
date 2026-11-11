"""AI Engineer schedules and standalone recordings, with stream fallback.

The public data guide (https://ai.engineer/data) documents per-edition
sessions.json feeds. Those are the preferred schedule source: exact titles,
speakers, descriptions, days and rooms. Their separate recording records are
not guessed into these schedules.

NYC 2026 has no structured feed. Its Watch & read page slices two full-day
YouTube streams into chapter cards. For each real talk, the public catalog is
searched for a standalone upload. A match requires independent corroboration:
unique slide-title evidence, speaker + duration evidence, or a unique speaker
candidate whose page was uploaded in the event's recording window. Standalone
pages and recordings win; ambiguous or missing matches keep the chapter link.
Administrative Remarks cards are dropped. Other layouts with neither source
return zero items rather than a made-up program.
"""

from __future__ import annotations

import re
import unicodedata
from datetime import date, timedelta
from urllib.parse import parse_qs, urljoin, urlparse

from bs4 import BeautifulSoup
import requests

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

TALKS_URL = "https://ai.engineer/api/data/talks?format=json"
NYC_EVENTS = {"AI Engineer New York 2026", "AI Engineer NYC 2026 Online Talks"}


def _text(value) -> str:
    if hasattr(value, "get_text"):
        value = value.get_text(" ", strip=True)
    return re.sub(r"\s+", " ", str(value or "")).strip()


def _norm(value: str) -> str:
    ascii_text = unicodedata.normalize("NFKD", value or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", ascii_text.lower()).strip()


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
            soup = BeautifulSoup(resp.text, "html.parser")

            catalog_resp = http_get(TALKS_URL, timeout=120)
            if catalog_resp.status_code != 200 or "application/json" not in catalog_resp.headers.get("content-type", ""):
                return self.manual(entry, f"talk catalog blocked or unexpected status {catalog_resp.status_code}")
            catalog = catalog_resp.json()
            if not isinstance(catalog, list):
                return self.manual(entry, "talk catalog returned invalid JSON")
            text, count, standalone = self._parse_cards(soup, resp.url, catalog, entry)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count,
                           detail=f"parsed {count} talks; {standalone} standalone recordings, "
                                  f"{count - standalone} stream offsets")

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

    @staticmethod
    def _speakers(record: dict) -> list[str]:
        """Structured catalog affiliation; never mined from the recording title."""
        result = []
        for person in record.get("speakers") or []:
            name, organization = _text(person.get("name")), _text(person.get("organization"))
            if name:
                result.append(f"{name} ({organization})" if organization else name)
        return result

    def _upload_matches(self, record: dict, entry: dict) -> bool:
        """Corroborate an event-null catalog row using its own page's upload date."""
        try:
            end = date.fromisoformat(str(entry["end_date"]))
            if record.get("event") is not None:
                return True
            resp = http_get(record["url"], timeout=30)
            match = re.search(r'"uploadDate"\s*:\s*"(\d{4}-\d{2}-\d{2})', resp.text)
            if resp.status_code != 200 or not match:
                return False
            published = date.fromisoformat(match.group(1))
            return end - timedelta(days=7) <= published <= end + timedelta(days=120)
        except (KeyError, TypeError, ValueError, requests.RequestException):
            return False

    @staticmethod
    def _standalone(title: str, speakers: list[tuple[str, str]], minutes: int | None,
                    records: list[dict], events: set[str]) -> dict | None:
        """Select one independently corroborated standalone recording, or none."""
        rows = [r for r in records if r.get("event") in events
                and r.get("url") and re.fullmatch(r"[A-Za-z0-9_-]{11}", _text(r.get("videoId")))]
        normalized_title = _norm(title)
        title_hits = [r for r in rows if normalized_title and normalized_title in _norm(r.get("slideText"))]
        if len(title_hits) == 1:
            return title_hits[0]

        names = {_norm(name) for name, _ in speakers}
        speaker_hits = [r for r in rows if any(_norm(p.get("name", "")) in names
                                               for p in r.get("speakers") or [])]
        duration_hits = [r for r in speaker_hits if minutes is not None and r.get("durationMs")
                         and abs(r["durationMs"] / 60000 - minutes) <= 1]
        if len(duration_hits) == 1:
            return duration_hits[0]
        if len(speaker_hits) == 1:
            return speaker_hits[0]
        return None

    def _parse_cards(self, soup: BeautifulSoup, source_url: str,
                     catalog: list[dict], entry: dict) -> tuple[str, int, int]:
        groups: dict[str, list[str]] = {}
        count = standalone_count = 0
        events = {entry.get("name"), f"{entry.get('name')} Online Talks", None}
        if entry.get("key") == "aiengineer-nyc-2026":
            events.update(NYC_EVENTS)

        for card in soup.select("article[data-session]"):
            title_link = card.select_one('h3 a[href*="/talks/"]')
            title = _text(title_link)
            meta = _text(card.select_one("p.text-xs.uppercase")) or "Program"
            if not title or meta.endswith("· Remarks"):
                continue
            count += 1

            card_speakers = []
            for person in card.select("p"):
                name = _text(person.select_one("span.font-semibold"))
                company = _text(person.select_one("strong"))
                if name:
                    card_speakers.append((name, company))
            durations = re.findall(r"(\d+)\s+min", _text(card))
            minutes = int(durations[-1]) if durations else None
            standalone = self._standalone(title, card_speakers, minutes, catalog, events)
            if standalone and not self._upload_matches(standalone, entry):
                standalone = None

            links, synopsis = [], ""
            speakers = card_speakers
            if standalone:
                standalone_count += 1
                speakers = [(p.get("name", ""), p.get("organization", ""))
                            for p in standalone.get("speakers") or []] or card_speakers
                links = [f"page: {standalone['url']}",
                         f"video: https://www.youtube.com/watch?v={standalone['videoId']}"]
                synopsis = _text(standalone.get("summary"))
            else:
                links = [f"page: {urljoin(source_url, title_link['href'])}"]
                for anchor in card.select('a[href*="youtube.com/watch"]'):
                    if video := _recording(anchor["href"]):
                        links.append(f"video: {video}")
                        break

            block = [f"### {title}"]
            attribution = [f"{_text(name)} ({_text(company)})" if _text(company) else _text(name)
                           for name, company in speakers if _text(name)]
            if attribution:
                block.append("Speakers: " + ", ".join(attribution))
            block.append(" | ".join(links))
            block.append(synopsis or _text(card.select_one("p.mt-5.text-base")) or
                         "No synopsis published; use the linked reading edition or recording.")
            block.append("")
            groups.setdefault(meta, []).extend(block)

        lines = []
        for heading, block in groups.items():
            lines.append(f"## {heading}")
            lines.extend(block)
        return "\n".join(lines), count, standalone_count
