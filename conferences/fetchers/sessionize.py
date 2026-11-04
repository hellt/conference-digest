"""Sessionize fetcher: events whose schedule runs on Sessionize.

The Linux Foundation's event sites (currently the PyTorch Conference) link
their Sessionize schedule right in the page, and Sessionize publishes a clean
per-event markdown view that needs no key:

    https://sessionize.com/api/v2/<event-id>/view/markdown

The fetcher reads the LF event page (the registry's `program_url`, a stable
per-series URL), finds the sessionize id in it, then reads the schedule
markdown and every session's own markdown page — title, speakers, room, and
the full description.

The sessionize event id is new each edition and the LF URL stays the same, so
both probe() and fetch() compare the event year stated by the schedule
("PyTorch Conference North America 2026 · Dates: … 2026") with the edition's
year read from the registry key (`pytorch-2026`). A page still showing the
previous edition is NOT_PUBLISHED for the next one, which is also what keeps
discovery from adding an edition from a stale page.

Recordings are not in the schedule; the links step finds them on YouTube
(CHANNELS/DISPLAY in conferences/links.py, keyed by the registry key).
"""

from __future__ import annotations

import re
from datetime import date
from typing import Optional

from .base import (
    Fetcher,
    FetchResult,
    ProbeResult,
    find_dates,
    http_get,
    looks_blocked,
    OK,
    NOT_PUBLISHED,
)

# The schedule URL as the event page links it (in its ChatGPT/Claude prompts).
_SZ_API = re.compile(r"https://sessionize\.com/api/v2/([a-z0-9]+)/view/markdown")
# The schedule markdown's header: "# <event name>".
_SZ_EVENT = re.compile(r"^#\s+(.+)$", re.M)
# A session entry: title in a markdown link, the rest of the line after it.
_SZ_SESSION = re.compile(
    r"^-\s+\[([^\]]+)\]\((https://sessionize\.com/api/v2/[a-z0-9]+/view/markdown/session/\d+)\)\s*\n?([^\n]*)$",
    re.M,
)
# Logistics rows a program is better off without, however they are titled.
_SKIP = re.compile(
    r"\b(registration|badge pick|check.?in|breakfast|lunch|coffee break|reception|"
    r"expo hours|zen zone|hallway track|closing remarks|raffle|photo booth)\b",
    re.I,
)


def edition_year(entry: dict) -> Optional[int]:
    """The edition's year from the registry key (`pytorch-2026`)."""
    m = re.search(r"-(\d{4})$", str(entry.get("key", "")))
    return int(m.group(1)) if m else None


class SessionizeFetcher(Fetcher):
    name = "sessionize"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        year = edition_year(entry)
        try:
            resp = http_get(url)
        except Exception as e:
            return self.manual(entry, f"request error: {e}")
        if looks_blocked(resp) or resp.status_code != 200:
            return self.manual(entry, f"event page status {resp.status_code} / challenge")
        api = _SZ_API.search(resp.text)
        if not api:
            return FetchResult(
                status=NOT_PUBLISHED,
                detail="event page has no Sessionize schedule (program not up yet)",
                source_url=url,
            )

        schedule_url = api.group(0)
        try:
            sched = http_get(schedule_url)
        except Exception as e:
            return self.manual(entry, f"sessionize request error: {e}")
        if sched.status_code != 200 or not _SZ_EVENT.search(sched.text):
            return FetchResult(
                status=NOT_PUBLISHED,
                detail=f"sessionize schedule not readable (status {sched.status_code})",
                source_url=schedule_url,
            )
        event = _SZ_EVENT.search(sched.text).group(1).strip()
        if year and not re.search(rf"\b{year}\b", event):
            return FetchResult(
                status=NOT_PUBLISHED,
                detail=f"schedule still shows '{event}', not {year}",
                source_url=schedule_url,
            )

        text = self._parse_sessions(sched.text)
        if text == "":
            return FetchResult(
                status=NOT_PUBLISHED,
                detail="schedule reachable but no talks with a description parsed yet",
                source_url=schedule_url,
            )
        return FetchResult(
            status=OK,
            program_text=text,
            source_url=schedule_url,
            item_count=text.count("\n### "),
            detail=f"parsed {text.count(chr(10) + '### ')} sessions from {event}",
        )

    def _parse_sessions(self, schedule_markdown: str) -> str:
        """One program-text item per session that has speakers and a description."""
        lines: list[str] = []
        for m in _SZ_SESSION.finditer(schedule_markdown):
            title, page, rest = m.group(1), m.group(2), (m.group(3) or "").strip()
            if _SKIP.search(title) or _SKIP.search(rest):
                continue
            speaker = rest.split("·")[0].strip() if "·" in rest else ""
            # a speaker-less row (breaks, registration) starts its line with the time
            if not speaker or re.match(r"^\d{1,2}:\d{2}\s", speaker):
                continue
            detail = self._session_page(page)
            description = detail.get("description", "")
            speakers = detail.get("speakers") or speaker
            if not description:
                continue   # no description yet -> the program is not fully published
            lines.append(f"### {title}")
            lines.append(f"Speakers: {speakers}")
            lines.append(f"page: {page}")
            lines.append(description)
            lines.append("")
        return "\n".join(lines)

    @staticmethod
    def _session_page(url: str) -> dict:
        """Title, speakers and description of one session's markdown page."""
        try:
            resp = http_get(url)
            if resp.status_code != 200:
                return {}
            text = resp.text
        except Exception:
            return {}
        out: dict = {}
        m = re.search(r"^\*\*Speakers:\*\* (.+)$", text, re.M)
        if m:
            out["speakers"] = m.group(1).strip()
        m = re.search(r"^## Description\s*\n\s*\n(.+?)(?:\n## |\Z)", text, re.M | re.S)
        if m:
            out["description"] = re.sub(r"\n{3,}", "\n\n", m.group(1)).strip()
        return out

    def probe(self, entry: dict, years=None) -> ProbeResult:
        """The Sessionize header names the event and its dates, which decides
        whether the current edition on this (year-less) URL is the candidate."""
        url = entry["program_url"]
        year = edition_year(entry)
        try:
            resp = http_get(url)
        except Exception as e:
            return ProbeResult(False, f"request error: {e}", source_url=url)
        if resp.status_code == 404:
            return ProbeResult(False, "404 (no such event yet)", source_url=url)
        if looks_blocked(resp) or resp.status_code != 200:
            return ProbeResult(False, f"blocked / status {resp.status_code}", source_url=url)
        api = _SZ_API.search(resp.text)
        if not api:
            return ProbeResult(False, "page reachable but no Sessionize schedule yet", source_url=url)

        try:
            head = http_get(api.group(0))
        except Exception as e:
            return ProbeResult(False, f"sessionize request error: {e}", source_url=api.group(0))
        event = _SZ_EVENT.search(head.text)
        if not event:
            return ProbeResult(False, "sessionize schedule not readable", source_url=api.group(0))
        if year and not re.search(rf"\b{year}\b", event.group(1)):
            return ProbeResult(
                False,
                f"schedule still shows '{event.group(1).strip()}', not {year}",
                source_url=api.group(0),
            )
        end = max(find_dates(head.text[:2000]), default=None)
        return ProbeResult(
            True,
            f"200; {event.group(1).strip()}" + (f", ends {end}" if end else ""),
            end_date=end,
            source_url=api.group(0),
        )
