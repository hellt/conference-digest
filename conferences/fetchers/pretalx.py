"""Any Pretalx schedule export: full talks with abstracts and attachments.

Several conferences (hack.lu, CfgMgmtCamp) run their CfP on Pretalx and expose
the public schedule as JSON at <host>/<event>/schedule/export/schedule.json.
The export gives every talk's title, speakers, abstract, attachments and the
talk's public page on the Pretalx instance. The series template points
`program_url` straight at the export; this fetcher is deliberately
host-agnostic. No key, no bot blocking observed. Missing recordings are left
to the normal verified links search.
"""

from __future__ import annotations

import re
from datetime import date
from urllib.parse import urlparse

from .base import Fetcher, FetchResult, ProbeResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_SKIP = re.compile(r"^(?:opening|closing|welcome|break|lunch|registration|coffee|goodbye|see you)", re.I)


class PretalxFetcher(Fetcher):
    name = "pretalx"

    def _load(self, url: str):
        resp = http_get(url, timeout=120)
        if resp.status_code == 404:
            return None
        if resp.status_code != 200:
            raise RuntimeError(f"unexpected status {resp.status_code}")
        # No looks_blocked() here: the body is JSON, and a talk abstract that
        # merely mentions "captcha" must not be mistaken for bot detection.
        return resp.json()["schedule"]

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            data = self._load(url)
            if data is None:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="schedule not published yet")
            text, count = self._parse(data)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} talks")

    def _parse(self, data: dict) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        for day in data["conference"].get("days", []):
            for room, events in day.get("rooms", {}).items():
                lines.append(f"## {day['date']} — {room}\n")
                for event in events:
                    title = (event.get("title") or "").strip()
                    page = event.get("url")
                    if not title or not page or page in seen or _SKIP.match(title):
                        continue
                    seen.add(page)
                    lines.append(f"### {title}")
                    if event.get("persons"):
                        lines.append("Speakers: " + ", ".join(
                            p.get("name") or p.get("public_name") or "" for p in event["persons"]
                        ).rstrip(","))
                    links = [f"page: {page}"]
                    # PDF first, so the writer can read it when a PPTX also exists.
                    for attachment in sorted(event.get("attachments", []),
                                             key=lambda a: not urlparse(a.get("url", "")).path.lower().endswith(".pdf")):
                        href = attachment.get("url", "")
                        if urlparse(href).path.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
                            links.append(f"slides: {href}")
                    lines.append(" | ".join(links))
                    body = " ".join(t.strip() for t in (event.get("abstract"), event.get("description")) if t)
                    lines.append(re.sub(r"<[^>]+>", "", body).strip() or
                                 "No abstract published; title and speakers only.")
                    lines.append("")
        return "\n".join(lines), len(seen)

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            data = self._load(url)
            if data is None:
                return ProbeResult(False, "no published schedule", source_url=url)
            end = date.fromisoformat(data["conference"]["end"])
            if years is not None and end.year not in set(years):
                end = None
            return ProbeResult(True, "Pretalx conference dates", end_date=end, source_url=url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
