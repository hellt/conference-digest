"""DENOG: follow the official agenda's schedule link to its Pretalx JSON export.

DENOG17 uses pretalx.com; DENOG18 moved to cfp.denog.de. The official agenda
provides the host, so discovery doesn't guess where future schedules live.
The export supplies full abstracts and attachments. Missing recordings are
left to the normal verified links search. No bot blocking observed.
"""

from __future__ import annotations

import re
from datetime import date
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_SKIP = re.compile(r"(?:DENOG\d+ (?:Opening|Closing)|Day \d+ Closing|Newcomm?er Sessions?)", re.I)


def _schedule(url: str):
    resp = http_get(url)
    if resp.status_code == 404:
        return None
    if resp.status_code != 200 or looks_blocked(resp):
        raise RuntimeError(f"blocked or unexpected status {resp.status_code}")
    soup = BeautifulSoup(resp.text, "html.parser")
    # Match the edition from the official page, never a site's current-event nav.
    edition = urlparse(url).path.rstrip("/").split("/")[-2]
    for a in soup.select("a[href]"):
        schedule_url = urljoin(url, a["href"])
        parsed = urlparse(schedule_url)
        if parsed.hostname not in ("pretalx.com", "cfp.denog.de", "pretalx.denog.de"):
            continue
        if parsed.path.rstrip("/") != f"/{edition}/schedule":
            continue
        export = http_get(schedule_url.rstrip("/") + "/export/schedule.json")
        if export.status_code == 404:
            return None
        if export.status_code != 200 or looks_blocked(export):
            raise RuntimeError(f"blocked or unexpected export status {export.status_code}")
        data = export.json()["schedule"]
        if data["conference"]["acronym"].lower() != edition.lower():
            raise ValueError("schedule belongs to another edition")
        return data
    return None


class DenogFetcher(Fetcher):
    name = "denog"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            data = _schedule(url)
            if data is None:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="schedule not published yet")
            text, count = self._parse(data)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} talks/workshops")

    def _parse(self, data: dict) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        for day in data["conference"].get("days", []):
            for room, events in day.get("rooms", {}).items():
                lines.append(f"## {day['date']} — {room}\n")
                for event in events:
                    title = (event.get("title") or "").strip()
                    page = event.get("url")
                    if not title or not page or page in seen or not event.get("persons") or _SKIP.fullmatch(title):
                        continue
                    seen.add(page)
                    lines.append(f"### {title}")
                    lines.append("Speakers: " + ", ".join(p["name"] for p in event["persons"]))
                    links = [f"page: {page}"]
                    attachments = event.get("attachments", [])
                    # PDF first, so the writer can read it when a PPTX also exists.
                    for attachment in sorted(attachments, key=lambda a: not urlparse(a["url"]).path.lower().endswith(".pdf")):
                        href = urljoin(data["base_url"], attachment["url"])
                        if urlparse(href).path.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
                            links.append(f"slides: {href}")
                    lines.append(" | ".join(links))
                    for field in ("abstract", "description"):
                        text = event.get(field)
                        if text:
                            lines.append(text.strip())
                    if not event.get("abstract") and not event.get("description"):
                        lines.append("No abstract published; title and materials only.")
                    lines.append("")
        return "\n".join(lines), len(seen)

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            data = _schedule(url)
            if data is None:
                return ProbeResult(False, "no published schedule", source_url=url)
            end = date.fromisoformat(data["conference"]["end"])
            if years is not None and end.year not in years:
                end = None
            return ProbeResult(True, "Pretalx conference dates", end_date=end, source_url=url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
