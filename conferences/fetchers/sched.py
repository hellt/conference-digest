"""Sched fetcher: KubeCon / CNCF and other Sched-hosted events.

The Sched *management* API needs an organizer key we don't have. But the
public schedule is plain HTML and needs no key. The cleanest public surface is
the "list with descriptions" view:

    https://<event>.sched.com/list/descriptions/

which renders every session's title, time, speakers, and full description in
one long page. We parse that. Sched challenges are sometimes transient: try
the direct request three times before falling back to Tavily Extract, when a
key is available. The repository owner approved that fallback for Sched on
2026-11-10. Only a persistent direct failure plus an unavailable/unparseable
Tavily result becomes MANUAL_FALLBACK.

If the event's Sched is set Private, the descriptions view won't expose
content -> NOT_PUBLISHED (or MANUAL_FALLBACK on an outright block).
"""

from __future__ import annotations

import os
import re
import time
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED
from .nanog import tavily_extract

DIRECT_ATTEMPTS = 3
EVENT_LINK = re.compile(r"\[([^\]\n]+)\]\((https://[^\s)]*/event/[^\s)]+)\)")


class SchedFetcher(Fetcher):
    name = "sched"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        last_error = ""
        for attempt in range(1, DIRECT_ATTEMPTS + 1):
            try:
                resp = http_get(url)
            except Exception as e:
                last_error = f"request error: {e}"
            else:
                if looks_blocked(resp):
                    last_error = f"Sched returned {resp.status_code} / challenge"
                elif resp.status_code != 200:
                    return self.manual(entry, f"unexpected status {resp.status_code}")
                else:
                    text, count = self._parse(resp.text, url)
                    if count == 0:
                        return FetchResult(
                            status=NOT_PUBLISHED,
                            detail="schedule reachable but no sessions parsed (not published / private?)",
                            source_url=url,
                        )
                    return FetchResult(
                        status=OK,
                        program_text=text,
                        source_url=url,
                        item_count=count,
                        detail=f"parsed {count} sessions (direct attempt {attempt})",
                    )
            if attempt < DIRECT_ATTEMPTS:
                time.sleep(2)

        key = os.environ.get("TAVILY_API_KEY", "").strip()
        if not key:
            return self.manual(
                entry,
                f"{last_error}; {DIRECT_ATTEMPTS} direct attempts failed and "
                "TAVILY_API_KEY is not set; open the schedule and paste it manually.",
            )
        try:
            markdown = tavily_extract(url, key)
            text, count = self._parse_markdown(markdown)
        except Exception as e:
            return self.manual(
                entry,
                f"{last_error}; {DIRECT_ATTEMPTS} direct attempts failed; "
                f"Tavily Extract also failed: {e}; open the schedule and paste it manually.",
            )
        if count == 0:
            return self.manual(
                entry,
                f"{last_error}; {DIRECT_ATTEMPTS} direct attempts failed; "
                "Tavily Extract returned no parseable sessions; open the schedule and paste it manually.",
            )
        return FetchResult(
            status=OK,
            program_text=text,
            source_url=url,
            item_count=count,
            detail=f"parsed {count} sessions via Tavily Extract after direct retries",
        )

    @staticmethod
    def _parse_markdown(markdown: str) -> tuple[str, int]:
        """Normalize Tavily's session links into the fetcher's program format."""
        matches = []
        seen = set()
        for match in EVENT_LINK.finditer(markdown):
            page = match.group(2).split("?", 1)[0].split("#", 1)[0].rstrip("/")
            if page not in seen:
                matches.append((match, page))
                seen.add(page)

        lines = []
        for i, (match, page) in enumerate(matches):
            end = matches[i + 1][0].start() if i + 1 < len(matches) else len(markdown)
            body = EVENT_LINK.sub("", markdown[match.end():end]).strip()
            lines.append(f"### {match.group(1).strip()}")
            lines.append(f"page: {page}")
            if body:
                lines.append(body)
            lines.append("")
        return "\n".join(lines), len(matches)

    def _parse(self, html: str, base: str = "") -> tuple[str, int]:
        soup = BeautifulSoup(html, "html.parser")
        lines: list[str] = []
        count = 0

        # In the descriptions list view each session is an article/row with an
        # event title link and a description block. Sched markup uses
        # .sched-container / .event classes; we stay tolerant.
        rows = soup.select(
            "div.sched-container, article.sched-event, div.event, "
            "div.list-simple .sched-container-inner"
        )

        for row in rows:
            title_el = row.select_one("h2, h3, a.name, span.event-name, .sched-event-name")
            title = title_el.get_text(" ", strip=True) if title_el else ""
            if not title:
                continue

            speakers_el = row.select_one(".sched-event-details-roles, .speakers, .sched-person")
            speakers = speakers_el.get_text(" ", strip=True) if speakers_el else ""

            desc_el = row.select_one(".tip-description, .sched-event-description, .description")
            desc = desc_el.get_text(" ", strip=True) if desc_el else ""

            if not (speakers or desc):
                continue

            # The session's own page gains uploaded slides and the recording
            # after the event; the digest's links row reads it then.
            link = row.select_one("a[href*='event/']")
            page = urljoin(urljoin(base, "/"), link["href"].lstrip("/")) if link and base else ""

            count += 1
            lines.append(f"### {title}")
            if speakers:
                lines.append(f"Speakers: {speakers}")
            if page.startswith("https://"):
                lines.append(f"page: {page}")
            if desc:
                lines.append(desc)
            lines.append("")

        return "\n".join(lines), count
