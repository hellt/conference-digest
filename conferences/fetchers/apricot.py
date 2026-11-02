"""APRICOT's schedule through APNIC's open conference API.

api.apnic.net serves the schedule app behind every APRICOT site. The events
listing (/web/v1/events) states each edition's id, dates and city; the event
document (/web/v1/event/<id>) carries every session with its agenda items —
talk title, speaker and affiliation, abstract and slide files — plus the
session's YouTube live link, which is attached only to single-talk sessions.
The listing is also the probe's source of exact dates. No key, no bot blocking.
"""

from __future__ import annotations

import re
from datetime import date

import requests
from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, OK, NOT_PUBLISHED

EVENTS_URL = "https://api.apnic.net/web/v1/events"
EVENT_URL = "https://api.apnic.net/web/v1/event/{id}"
# APRICOT week-long workshops, meals and sponsor invites are not digest items.
KEEP_CATEGORIES = {"session", "tutorial", "bof", "other event"}
_TAGS = re.compile(r"<[^>]+>")


def _listing() -> list[dict]:
    resp = http_get(EVENTS_URL)
    resp.raise_for_status()
    return resp.json().get("events", [])


def _find(listing: list[dict], year: int) -> dict | None:
    for event in listing:
        if event.get("name", "").strip() == f"APRICOT {year}":
            return event
    return None


def _year(entry: dict) -> int:
    return int(re.search(r"(\d{4})$", entry["key"]).group(1))


class ApricotFetcher(Fetcher):
    name = "apricot"

    def fetch(self, entry: dict) -> FetchResult:
        try:
            year = _year(entry)
            listing = _listing()
            event = _find(listing, year)
            if not event:
                return FetchResult(status=NOT_PUBLISHED, source_url=EVENTS_URL,
                                   detail=f"APRICOT {year} not in the events listing yet")
            resp = http_get(EVENT_URL.format(id=event["id"]))
            resp.raise_for_status()
            data = resp.json()
            text, count = self._parse(data)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=event.get("url", EVENTS_URL), item_count=count,
                           detail=f"parsed {count} talks from {len(data.get('days', {}))} days")

    def _parse(self, data: dict) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        for key in sorted(data.get("days", {})):
            day = data["days"][key]
            for session in day.get("sessions", []):
                if session.get("category") not in KEEP_CATEGORIES:
                    continue
                agenda = [a for a in (session.get("agenda") or []) if (a.get("topic") or "").strip()]
                if not agenda:
                    continue
                talks = [a for a in agenda if a.get("type") != "chair"]
                heading = session.get("name", "").strip()
                when = f"{session.get('start_time', '')}–{session.get('end_time', '')}, {session.get('location', '')}".strip(", ")
                lines.append(f"## {heading}" + (f" ({when})" if when else ""))
                video = (session.get("video") or "").strip() if len(talks) == 1 else ""
                for talk in agenda:
                    title = talk["topic"].strip()
                    if not title or (title, talk.get("id")) in seen:
                        continue
                    seen.add((title, talk.get("id")))
                    lines.append(f"### {title}")
                    speaker = " ".join(x for x in (talk.get("name"), talk.get("organisation")) if x)
                    if speaker:
                        lines.append(f"Speakers: {speaker}")
                    links = [f"slides: {f['file']}" for f in talk.get("presentation_files") or []]
                    if video:
                        links.append(f"video: {video}")
                    if links:
                        lines.append(" | ".join(links))
                    abstract = _TAGS.sub(" ", talk.get("abstract") or "")
                    abstract = re.sub(r"\s+", " ", abstract).strip()
                    lines.append(abstract if abstract else "No abstract published; title, speaker and materials only.")
                    lines.append("")
        return "\n".join(lines), len(seen)

    def probe(self, entry: dict, years=None) -> ProbeResult:
        try:
            year = _year(entry)
            event = _find(_listing(), year)
            if not event:
                return ProbeResult(False, "edition not in the events listing", source_url=EVENTS_URL)
            end = date.fromisoformat(event.get("end", "")[:10]) if event.get("end") else None
            if years is not None and (not end or end.year not in set(years)):
                end = None
            return ProbeResult(True, "APNIC events listing; API dates",
                               end_date=end, location=event.get("location", ""), source_url=EVENTS_URL)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=EVENTS_URL)
