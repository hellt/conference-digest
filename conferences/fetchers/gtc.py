"""NVIDIA GTC (San Jose): the session-catalog JSON API behind the catalog app.

www.nvidia.com/gtc/session-catalog/ is a client-rendered app; its data comes
from api-prod.nvidia.com/services/sessioncatalog/api/v1, which serves plain
JSON with no auth and no observed bot-block. The event id is an opaque
RainFocus id ("175570351919000gtc26") that changes every year, and the only
place it is published is the per-year JS bundle the catalog page embeds
(www.nvidia.com/content/dam/en-zz/Solutions/gtc/rf/gtc26.js), which also
carries a day->date map. Resolution: the year's own bundle first (it 404s
until the site for that edition is built), then the bundle the catalog page
embeds. Either way the bundle's year must match the edition, so a candidate
for a year the catalog does not serve yet probes as absent.

Only the current edition's bundle exists — older ones 404 once the site has
moved on — so re-fetching a past edition after that returns manual/not
published; redo those from the committed prompt instead.

The API lists every session type. Only presentation-like types with an
abstract become program items (Talk, Panel, Tutorial, Lightning Talk, Theater
Talk, Fireside Chat, Full-Day Workshop, Keynote). Posters, hands-on training
labs, Connect office hours, watch parties, certifications, studio episodes
and the post-event Chinese-language livestream days are dropped: they are not
talks, or not ones this digest's reader can watch, and they would nearly
double the program.

Recordings are not in the catalog API: sessions are produced for NVIDIA
on-demand, and many are later uploaded to NVIDIA's YouTube channel, which the
links step searches and verifies. Links Refresh maps the per-session page to
its /en-us/on-demand/session/<code>/ page, reads the public on-demand session
API for that page's Kaltura video and PDF assets, and keeps the on-demand URL
as the pick's "Talk page" link. PDF downloads are signed, so GTC refreshes
renew them instead of retaining an expired signature.
"""

from __future__ import annotations

import html
import re
from datetime import date
from typing import Iterable, Optional
from urllib.parse import urlencode

from bs4 import BeautifulSoup

from .base import (
    Fetcher, FetchResult, ProbeResult, http_get, looks_blocked,
    OK, NOT_PUBLISHED,
)

API = "https://api-prod.nvidia.com/services/sessioncatalog/api/v1"
CATALOG_PAGE = "https://www.nvidia.com/gtc/session-catalog/"
BUNDLE_URL = "https://www.nvidia.com/content/dam/en-zz/Solutions/gtc/rf/gtc{yy}.js"
PAGE_SIZE = 1000          # the API accepts up to 1000 per page
MAX_PAGES = 20            # GTC26 needed one; bound the loop anyway

# Session types that are talks. Everything else the API lists — posters,
# training labs, Connect office hours, watch parties, certifications, studio
# episodes, Q&As, hackathons — is not a digestible talk.
KEEP_TYPES = {
    "Talk", "Panel", "Tutorial", "Lightning Talk", "Theater Talk",
    "Fireside Chat", "Full-Day Workshop", "Keynote",
}

_EVENT_ID = re.compile(r'DEFAULT_EVENT_ID:"([^"]+)"')
_EVENT_YEAR = re.compile(r"gtc(\d{2})$")
_BUNDLE_SRC = re.compile(
    r'src="(/content/dam/en-zz/Solutions/gtc/rf/[A-Za-z0-9._-]+\.js)"'
)
_ISO_DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")


class ResolveError(Exception):
    """The catalog could not be resolved to this edition's event id."""


def _entry_year(entry: dict) -> Optional[int]:
    m = re.search(r"-(\d{4})$", entry.get("key", ""))
    return int(m.group(1)) if m else None


def _cjk_ratio(text: str) -> float:
    """Share of CJK characters — used to drop the Chinese-language days."""
    if not text:
        return 0.0
    return sum(1 for c in text if ord(c) >= 0x2E80) / len(text)


def _clean_abstract(html_fragment: str) -> str:
    text = (html_fragment or "").strip()
    if "<" in text:  # only pay the BeautifulSoup cost when there is markup
        text = BeautifulSoup(text, "html.parser").get_text(" ", strip=True)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def _bundle_event(js_text: str) -> tuple[str, Optional[int]]:
    """(event_id, year) out of a catalog bundle; year None when unmarked."""
    m = _EVENT_ID.search(js_text)
    if not m:
        return "", None
    event_id = m.group(1)
    ym = _EVENT_YEAR.search(event_id)
    return event_id, (2000 + int(ym.group(1)) if ym else None)


def _bundle_dates(js_text: str) -> list[date]:
    """The day->date map in the bundle, e.g. sd={Tuesday:"2026-03-17",...}."""
    i = js_text.find("sd={")
    window = js_text[i:i + 500] if i != -1 else ""
    out = []
    for y, m, d in ((s.split("-") for s in _ISO_DATE.findall(window))):
        try:
            out.append(date(int(y), int(m), int(d)))
        except ValueError:
            pass
    return out


class GtcFetcher(Fetcher):
    name = "gtc"

    def _resolve(self, entry: dict) -> tuple[str, list[date], str]:
        """The event id for THIS edition, from its year bundle or the page's.

        Raises ResolveError. `seen_year` tracks what the catalog does serve, so
        the caller can tell "not up yet" (earlier year) from "gone" (later
        year) apart.
        """
        year = _entry_year(entry)
        if not year:
            raise ResolveError(f"cannot derive a year from key '{entry.get('key')}'")

        seen_year: Optional[int] = None

        def bundle_text(url: str) -> Optional[str]:
            nonlocal seen_year
            try:
                resp = http_get(url)
            except Exception as e:
                raise ResolveError(f"request error on {url}: {e}")
            if resp.status_code == 404:
                return None
            if looks_blocked(resp):
                raise ResolveError(f"blocked ({resp.status_code}) on {url}")
            if resp.status_code != 200:
                return None
            return resp.text

        # 1. The year's own bundle — a 404 simply means that edition's site
        #    is not built yet (or is gone).
        text = bundle_text(BUNDLE_URL.format(yy=f"{year % 100:02d}"))
        if text:
            event_id, bundle_year = _bundle_event(text)
            if event_id and bundle_year == year:
                return event_id, _bundle_dates(text), CATALOG_PAGE
            if bundle_year:
                seen_year = bundle_year

        # 2. Whatever bundle the catalog page embeds today (covers a renamed
        #    bundle path, as long as it serves this edition's year).
        try:
            page = http_get(CATALOG_PAGE)
        except Exception as e:
            raise ResolveError(f"request error on {CATALOG_PAGE}: {e}")
        if page.status_code != 200 or looks_blocked(page):
            raise ResolveError(f"catalog page unreadable ({page.status_code})")
        m = _BUNDLE_SRC.search(page.text)
        if not m:
            raise ResolveError("no session-catalog bundle on the catalog page")
        text = bundle_text(f"https://www.nvidia.com{m.group(1)}")
        if text:
            event_id, bundle_year = _bundle_event(text)
            if event_id and bundle_year == year:
                return event_id, _bundle_dates(text), CATALOG_PAGE
            if bundle_year:
                seen_year = bundle_year

        if seen_year and seen_year > year:
            raise ResolveError(
                f"catalog has moved on to GTC {seen_year}; GTC {year} is no "
                f"longer served — redo from the committed prompt"
            )
        if seen_year:
            raise ResolveError(
                f"catalog still serves GTC {seen_year}; GTC {year} not up yet"
            )
        raise ResolveError("no session-catalog bundle found")

    def _session_count(self, event_id: str) -> int:
        """How many sessions the API lists for this event (one small page)."""
        url = f"{API}/search?" + urlencode(
            {"eventid": event_id, "view": "data", "page": 0, "size": 1}
        )
        resp = http_get(url)
        if resp.status_code != 200:
            raise ResolveError(f"session API returned {resp.status_code}")
        try:
            return int(resp.json().get("totalResults", 0))
        except Exception as e:
            raise ResolveError(f"session API parse error: {e}")

    def _sessions(self, event_id: str) -> list[dict]:
        """Every session of the event, all pages."""
        out: list[dict] = []
        for page in range(MAX_PAGES):
            url = f"{API}/search?" + urlencode(
                {"eventid": event_id, "view": "data", "page": page, "size": PAGE_SIZE}
            )
            resp = http_get(url)
            if resp.status_code != 200:
                raise ResolveError(f"session API returned {resp.status_code}")
            try:
                data = resp.json()
                batch = data.get("data") or []
                total = int(data.get("totalResults", 0))
            except Exception as e:
                raise ResolveError(f"session API parse error: {e}")
            out.extend(batch)
            if not batch or len(out) >= total:
                break
        return out

    def _parse(self, sessions: list[dict], event_code: str) -> tuple[str, int]:
        kept = []
        for s in sessions:
            if s.get("sessionType") not in KEEP_TYPES:
                continue
            if not (s.get("abstract") or "").strip():
                continue
            if _cjk_ratio(s.get("title", "")) > 0.3:
                continue
            kept.append(s)

        def sort_key(s: dict):
            t = (s.get("times") or [{}])[0]
            return (t.get("date") or "9999-12-31", t.get("startTime") or "99:99",
                    s.get("title", ""))

        kept.sort(key=sort_key)

        groups: dict[str, list[dict]] = {}
        for s in kept:
            t = (s.get("times") or [{}])[0]
            head = t.get("dateFormatted") or "Unscheduled sessions"
            groups.setdefault(head, []).append(s)

        lines: list[str] = []
        for head in sorted(groups, key=lambda h: min(
                (t.get("date") or "9999-12-31")
                for s in groups[h]
                for t in (s.get("times") or [{}]))):
            lines.append(f"## {head}")
            lines.append("")
            for s in groups[head]:
                lines.append(f"### {s.get('title', '').strip()}")
                speakers = ", ".join(
                    f"{sp.get('fullName', '').strip()}"
                    + (f" ({sp['companyName'].strip()})" if sp.get("companyName") else "")
                    for sp in (s.get("speakers") or [])
                    if sp.get("fullName")
                )
                if speakers:
                    lines.append(f"Speakers: {speakers}")
                abbr = (s.get("abbreviation") or "").lower()
                if abbr:
                    lines.append(
                        f"page: https://www.nvidia.com/gtc/session-catalog/sessions/"
                        f"{event_code}-{abbr}/"
                    )
                if s.get("sessionType"):
                    lines.append(f"Type: {s['sessionType']}")
                abstract = _clean_abstract(s.get("abstract", ""))
                if abstract:
                    lines.append(abstract)
                lines.append("")
        return "\n".join(lines).rstrip() + "\n", len(kept)

    def fetch(self, entry: dict) -> FetchResult:
        url = entry.get("program_url", CATALOG_PAGE)
        try:
            event_id, _dates, _page = self._resolve(entry)
            sessions = self._sessions(event_id)
        except ResolveError as e:
            detail = str(e)
            if "moved on to GTC" in detail or "blocked" in detail \
                    or "request error" in detail or "unreadable" in detail:
                return self.manual(entry, detail)
            return FetchResult(status=NOT_PUBLISHED, detail=detail, source_url=url)

        if not sessions:
            return FetchResult(
                status=NOT_PUBLISHED,
                detail="session API lists no sessions for this event yet",
                source_url=url,
            )

        try:
            text, count = self._parse(sessions, sessions[0].get("eventCode", "gtc"))
        except Exception as e:
            return self.manual(entry, f"parse error: {e}")

        return FetchResult(
            status=OK,
            program_text=text,
            source_url=url,
            item_count=count,
            detail=f"parsed {count} talks of {len(sessions)} sessions "
                   f"(posters, labs, office hours and Chinese-day items dropped)",
        )

    def probe(self, entry: dict, years: Optional[Iterable[int]] = None) -> ProbeResult:
        url = entry.get("program_url", CATALOG_PAGE)
        try:
            event_id, dates, _page = self._resolve(entry)
            count = self._session_count(event_id)
        except ResolveError as e:
            return ProbeResult(False, str(e), source_url=url)

        if not count:
            return ProbeResult(
                False, "catalog up but the session API lists no sessions",
                source_url=url,
            )
        end = max(dates) if dates else None
        return ProbeResult(
            True,
            f"catalog bundle + session API ({count} sessions)",
            end_date=end,
            source_url=url,
        )
