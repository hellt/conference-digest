"""Generic Indico fetcher: one open export API, several NOG instances.

Indico exposes the whole event as JSON at /export/event/<id>.json?detail=
contributions — every contribution with its title, description, speakers,
page URL and material. several conferences in this digest run on Indico:
nog.fi, NetUK (indico.netuk.org), GRNOG (nogalliance) and DKNOG (whose
per-edition subdomains redirect to a shared events.dknog.dk backend, which
also serves the exports). The series template points `program_url` either at
an event page (/event/<id>/), or at a listing page (site root or category)
whose event links the fetcher resolves by the edition's name.
"""

from __future__ import annotations

import re
from datetime import date
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, OK, NOT_PUBLISHED

_SKIP = re.compile(r"^(?:registration|welcome|opening|closing|break|lunch|coffee|get.?together|social|bus|dinner|party|quiz)", re.I)
_EVENT = re.compile(r"/event/(\d+)(?:/|$)")
_TAGS = re.compile(r"<[^>]+>")


def _norm(text: str) -> str:
    return re.sub(r"[\s#]+", "", text or "").casefold()


def _text(html: str) -> str:
    return re.sub(r"\s+", " ", _TAGS.sub(" ", html or "")).strip()


class IndicoFetcher(Fetcher):
    name = "indico"

    # ---- event resolution ------------------------------------------------ #

    def _resolve(self, entry: dict) -> tuple[str, str, str] | None:
        """(export_base, event_id, source_url); None when not found."""
        url = entry["program_url"]
        match = _EVENT.search(url)
        if match:
            return f"{urlparse(url).scheme}://{urlparse(url).netloc}", match.group(1), url
        # listing page: pick the event whose title matches the edition name
        try:
            resp = http_get(url, timeout=60)
            if resp.status_code != 200:
                return None
            resp.encoding = "utf-8"
            # A listing that redirects straight to an event page resolves
            # itself, and the redirect's host is the export host — DKNOG's
            # per-edition subdomains point at the shared events.dknog.dk.
            match = _EVENT.search(resp.url)
            if match:
                base = f"{urlparse(resp.url).scheme}://{urlparse(resp.url).netloc}"
                return base, match.group(1), resp.url
            soup = BeautifulSoup(resp.text, "html.parser")
        except Exception:
            return None
        base = f"{urlparse(resp.url).scheme}://{urlparse(resp.url).netloc}"
        events = {}
        for a in soup.select('a[href*="/event/"]'):
            href = a.get("href", "")
            if href.endswith(".ics") or any("icon" in c for c in (a.get("class") or [])):
                continue
            match = _EVENT.search(href)
            if not match:
                continue
            title = a.get_text(" ", strip=True)
            if title:
                events.setdefault(match.group(1), title)
        wanted = _norm(entry.get("name", ""))
        if wanted:
            for event_id, title in events.items():
                if _norm(title) == wanted:
                    return base, event_id, url
        if len(events) == 1:
            event_id, _ = next(iter(events.items()))
            return base, event_id, url
        return None

    def _load(self, export_base: str, event_id: str) -> dict | None:
        resp = http_get(f"{export_base}/export/event/{event_id}.json?detail=contributions", timeout=120)
        if resp.status_code == 404:
            return None
        if resp.status_code != 200 or not resp.content.startswith(b"{"):
            raise RuntimeError(f"unexpected export status {resp.status_code}")
        return resp.json()["results"][0]

    # ---- pipeline fetch -------------------------------------------------- #

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resolved = self._resolve(entry)
            if not resolved:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="no event found on the listing page")
            export_base, event_id, _ = resolved
            data = self._load(export_base, event_id)
            if data is None:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="event export not available")
            text, count = self._parse(data)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=f"{export_base}/event/{event_id}/", item_count=count,
                           detail=f"parsed {count} contributions")

    def _parse(self, data: dict) -> tuple[str, int]:
        groups: dict[str, list[str]] = {}
        seen: set[str] = set()
        for item in data.get("contributions", []):
            title = (item.get("title") or "").strip()
            if not title or _SKIP.match(title) or title in seen:
                continue
            seen.add(title)
            block = groups.setdefault(item.get("track") or item.get("session") or "Program", [])
            block.append(f"### {title}")
            speakers = []
            for speaker in (item.get("speakers") or []) + (item.get("primaryauthors") or []):
                name = speaker.get("fullName") or f"{speaker.get('first_name', '')} {speaker.get('last_name', '')}".strip()
                affiliation = speaker.get("affiliation")
                if name:
                    speakers.append(f"{name} ({affiliation})" if affiliation else name)
            if speakers:
                block.append("Speakers: " + ", ".join(dict.fromkeys(speakers)))
            links = [f"page: {item['url']}"] if item.get("url") else []
            for material in item.get("material") or []:
                href = material.get("url") or material.get("link") or ""
                if isinstance(href, dict):
                    href = href.get("url", "")
                if href and href.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
                    links.append(f"slides: {href}")
            if links:
                block.append(" | ".join(links))
            description = _text(item.get("description") or "")
            block.append(description if description else "No description published; title and speakers only.")
            block.append("")
        lines: list[str] = []
        for group in groups:
            lines.append(f"## {group}")
            lines += groups[group]
        return "\n".join(lines), len(seen)

    # ---- discovery probe -------------------------------------------------- #

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            resolved = self._resolve(entry)
            if not resolved:
                return ProbeResult(False, "no event found on the listing page", source_url=url)
            export_base, event_id, _ = resolved
            data = self._load(export_base, event_id)
            if data is None:
                return ProbeResult(False, "event export not available", source_url=url)
            end = date.fromisoformat(data["endDate"]["date"]) if data.get("endDate") else None
            if years is not None and (not end or end.year not in set(years)):
                end = None
            return ProbeResult(True, "Indico export; exact event dates", end_date=end,
                               location=data.get("location", ""), source_url=f"{export_base}/event/{event_id}/")
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
