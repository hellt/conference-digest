"""Cisco Live's public RainFocus on-demand catalog (US and Europe).

The site's catalog.js publishes the widget/profile IDs used below. These are
public catalog identifiers, not login credentials. Anonymous search returns
abstracts and speakers, but currently withholds files and videos: do not guess
PDF URLs or request authenticated downloads. No bot blocking observed; a block
or API/layout error falls back to manual paste, never an extraction service.

Editions are selected by year AND host city, not keyword search (which mixes
editions). Unknown cities fail closed; update CITIES when a region moves.
The API caps each search at 500 results. Larger programs use the site's public
session-type, technical-level, track and technology filters, with coverage
checks; an incomplete partition is a manual fallback, never a partial program.
Discovery only sees editions after their on-demand catalog is published. The
API has no event dates, so series end_date_hint values are conservative estimates.
"""

from __future__ import annotations

import re
from html import unescape
from typing import Iterable, Optional
from urllib.parse import parse_qs, urlparse

import requests
from bs4 import BeautifulSoup

from .base import (
    BROWSER_HEADERS, Fetcher, FetchResult, ProbeResult, OK, NOT_PUBLISHED,
)

LIBRARY = "https://www.ciscolive.com/on-demand/on-demand-library.html"
API = "https://events.rainfocus.com/api/search"
HEADERS = {
    **BROWSER_HEADERS,
    "Accept": "application/json",
    "rfWidgetId": "M7n14I8sz0pklW1vybwVRdKrgdREj8sR",
    "rfApiProfileId": "HEedDIRblcZk7Ld3KHm1T0VUtZog9eG9",
}
CITIES = {
    "us": ("Las Vegas", "San Diego", "San Francisco"),
    "eu": ("Amsterdam", "Barcelona", "Berlin", "London"),
}
PAGE_SIZE = 100


def _clean(value: str) -> str:
    text = BeautifulSoup(value, "html.parser").get_text(" ", strip=True) if "<" in value else unescape(value)
    return re.sub(r"\s+", " ", text).strip()


def _search(**data) -> dict:
    resp = requests.post(API, headers=HEADERS, data={"type": "session", **data}, timeout=60)
    resp.raise_for_status()
    payload = resp.json()
    if payload.get("responseCode") != "0":
        raise ValueError(f"catalog API: {payload.get('responseMessage', 'invalid response')}")
    return payload


def _edition(entry: dict) -> tuple[str, str] | None:
    match = re.fullmatch(r"ciscolive-(us|eu)-(\d{4})", entry["key"])
    if not match:
        raise ValueError("expected key ciscolive-us-YYYY or ciscolive-eu-YYYY")
    region, year = match.groups()
    payload = _search(size=0)
    events = next(a["values"] for a in payload["attributes"] if a["id"] == "event")
    matches = [e for e in events if e["name"] in {f"{year} {city}" for city in CITIES[region]}]
    if len(matches) > 1:
        raise ValueError("multiple regional editions found; refusing to mix programs")
    if not matches:
        return None
    event = matches[0]
    # A hand-registered URL must agree with the edition resolved from its key.
    expected = parse_qs(urlparse(entry["program_url"]).query).get("search.event")
    if expected and expected != [event["id"]]:
        raise ValueError("program_url event does not match registry key")
    return event["id"], event["name"]


def _program(items: list[dict], event: str) -> tuple[str, int]:
    lines = [f"## {event}", ""]
    count = 0
    for item in items:
        title = _clean(item.get("title", ""))
        abstract = _clean(item.get("abstract", ""))
        if not title or not abstract:
            continue
        speakers = []
        for person in item.get("participants", []):
            name = _clean(person.get("fullName") or person.get("globalFullName") or "")
            company = _clean(person.get("companyName") or person.get("globalCompany") or "")
            if name:
                speaker = f"{name} ({company})" if company else name
                if speaker not in speakers:
                    speakers.append(speaker)
        lines.append(f"### {title}")
        if speakers:
            lines.append("Speakers: " + ", ".join(speakers))
        # The public widget's session-detail route; IDs come from this event only.
        lines.append(f"page: {LIBRARY}#/session/{item['sessionID']}")
        lines.extend([abstract, ""])
        count += 1
    return "\n".join(lines), count


def _sessions(event_id: str, event: str, filters: dict,
              facets=("sessiontype", "technicallevel", "track", "technology")) -> dict[str, dict]:
    """Read a complete search, narrowing by public facets above its result cap."""
    payload = _search(size=PAGE_SIZE, **{"from": 0, "search.event": event_id, **filters})
    if payload.get("totalSearchItems") == 0 and not payload.get("sectionList"):
        return {}
    section, = payload["sectionList"]
    total = section["total"]
    cap = section.get("paginationMax", 500)
    items: dict[str, dict] = {}

    def add(section: dict, offset: int, paginating: bool = True) -> None:
        if section["sectionId"] != event_id or section["from"] != offset or section["total"] != total:
            raise ValueError("catalog returned a wrong edition/page or changed during pagination")
        batch = section["items"]
        if not batch and offset < total:
            raise ValueError("catalog pagination stopped before the complete program")
        for item in batch:
            if item.get("event") != event or (paginating and item["sessionID"] in items):
                raise ValueError("wrong edition or duplicate session in paginated catalog")
            items[item["sessionID"]] = item

    add(section, 0)
    if total > cap:
        if not facets:
            raise ValueError("catalog exceeds result cap after all supported filters")
        # Some sessions have no technical level/type. Retain the public first
        # page as well as facet results, then require exact union coverage.
        first = _search(size=cap, **{"from": 0, "search.event": event_id, **filters})
        first_section, = first["sectionList"]
        add(first_section, 0, paginating=False)
        for index, facet in enumerate(facets):
            values = next(a["values"] for a in payload["attributes"] if a["id"] == facet)
            for value in values:
                items.update(_sessions(event_id, event, {**filters, f"search.{facet}": value["id"]},
                                       facets[index + 1:]))
                if len(items) == total:
                    break
            if len(items) == total:
                break
    else:
        offset = len(items)
        while offset < total:
            payload = _search(size=min(PAGE_SIZE, cap - offset),
                              **{"from": offset, "search.event": event_id, **filters})
            section, = payload["sectionList"]
            add(section, offset)
            offset += len(section["items"])
    if len(items) != total:
        raise ValueError(f"incomplete catalog: retrieved {len(items)} of {total} sessions")
    return items


class CiscoLiveFetcher(Fetcher):
    name = "ciscolive"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            edition = _edition(entry)
            if edition is None:
                return FetchResult(status=NOT_PUBLISHED, source_url=url,
                                   detail="no matching regional on-demand edition published")
            event_id, event = edition
            url = f"{LIBRARY}?search.event={event_id}"
            items = _sessions(event_id, event, {})
            text, count = _program(sorted(items.values(), key=lambda i: i.get("title", "")), event)
        except Exception as e:
            return self.manual(entry, f"catalog fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text if count else "",
                           source_url=url, item_count=count,
                           detail=f"parsed {count} sessions with abstracts; slides/recordings require login")

    def probe(self, entry: dict, years: Optional[Iterable[int]] = None) -> ProbeResult:
        try:
            edition = _edition(entry)
            if edition is None:
                return ProbeResult(False, "regional edition not in on-demand catalog", source_url=entry["program_url"])
            event_id, event = edition
            return ProbeResult(True, "edition listed; API has no event dates (use series estimate)",
                               location=event.split(" ", 1)[1],
                               source_url=f"{LIBRARY}?search.event={event_id}")
        except Exception as e:
            return ProbeResult(False, f"catalog probe error: {e}", source_url=entry["program_url"])
