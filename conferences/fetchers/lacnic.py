"""LACNIC meetings through the open WordPress REST API behind the event sites.

Each lacnic<n>.lacnic.net site is a React app that loads from
apievt.lacnic.net — a plain WP REST API. The `our_events` taxonomy maps
edition numbers to term ids; the `agenda` post type then lists every agenda
item with an English and Spanish title, description, speakers, room, session
group, YouTube recordings (per language) and presentation media ids, which the
media endpoint resolves to slide URLs. Talks are emitted with their English
title when one exists. No key, no bot blocking.
"""

from __future__ import annotations

import re
from datetime import date, datetime

from .base import Fetcher, FetchResult, ProbeResult, http_get, OK, NOT_PUBLISHED

API = "https://apievt.lacnic.net/wp-json/wp/v2"
_TAGS = re.compile(r"<[^>]+>")
_SKIP = re.compile(r"^(?:break|registro|registration|coffee|almuerzo|lunch|apertura|cierre)", re.I)


def _terms() -> dict[str, int]:
    resp = http_get(f"{API}/our_events?per_page=100")
    resp.raise_for_status()
    return {t["name"].replace(" ", ""): t["id"] for t in resp.json()}


def _agenda(term_id: int) -> list[dict]:
    posts: list[dict] = []
    page = 1
    while True:
        resp = http_get(f"{API}/agenda?our_events={term_id}&per_page=100&page={page}")
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        posts += batch
        total = int(resp.headers.get("X-WP-TotalPages", 1))
        page += 1
        if page > total:
            break
    return posts


def _media(ids: list[int]) -> dict[int, str]:
    out: dict[int, str] = {}
    for i in range(0, len(ids), 100):
        resp = http_get(f"{API}/media?include={','.join(map(str, ids[i:i+100]))}&per_page=100&_fields=id,source_url")
        if resp.status_code != 200:
            continue
        for m in resp.json():
            out[m["id"]] = m.get("source_url", "")
    return out


def _dates(posts: list[dict]) -> list[date]:
    found = []
    for post in posts:
        for raw in (post.get("acf", {}).get("ending_time"), post.get("acf", {}).get("start_time")):
            try:
                found.append(datetime.strptime(raw, "%d/%m/%Y %H:%M").date())
            except (ValueError, TypeError):
                continue
    return found


class LacnicFetcher(Fetcher):
    name = "lacnic"

    def fetch(self, entry: dict) -> FetchResult:
        try:
            n = int(re.search(r"(\d+)$", entry["key"]).group(1))
            terms = _terms()
            if f"LACNIC{n}" not in terms:
                return FetchResult(status=NOT_PUBLISHED, source_url=API,
                                   detail=f"LACNIC {n} not in the events taxonomy yet")
            posts = _agenda(terms[f"LACNIC{n}"])
            text, count = self._parse(posts)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=entry.get("manual_fallback_url", API), item_count=count,
                           detail=f"parsed {count} agenda items")

    def _parse(self, posts: list[dict]) -> tuple[str, int]:
        media_ids = [pid for post in posts for pid in (post.get("acf", {}).get("presentation") or [])]
        media = _media(list(dict.fromkeys(media_ids)))
        lines: list[str] = []
        seen: set[str] = set()
        count = 0
        groups: dict[str, list[str]] = {}
        for post in sorted(posts, key=lambda p: p.get("acf", {}).get("start_time", "9" * 20)):
            acf = post.get("acf", {})
            if acf.get("break"):
                continue
            info = acf.get("info_en") or {}
            title = (info.get("title") or (acf.get("info_es") or {}).get("title") or "").strip()
            if not title or title in seen or _SKIP.match(title):
                continue
            seen.add(title)
            count += 1
            speakers = ", ".join(s.get("post_title", "").strip() for s in acf.get("speakers") or [])
            links = []
            for media_id in acf.get("presentation") or []:
                href = media.get(media_id)
                if href and href.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
                    links.append(f"slides: {href}")
            for videos in (acf.get("videos_en"), acf.get("videos"), acf.get("videos_pt_br")):
                for video in videos or []:
                    href = video.get("video_url_en") or video.get("video_url") or video.get("video_url_pt_br")
                    if href:
                        links.append(f"video: {href}")
                        break
                if any("video:" in l for l in links):
                    break
            body = " ".join(t for t in (info.get("description"), (acf.get("info_es") or {}).get("description")) if t)
            body = re.sub(r"\s+", " ", _TAGS.sub(" ", body)).strip()
            session = (acf.get("sessions") or [{}])[0].get("name", "").strip()
            day = (acf.get("start_time") or "").split(" ")[0]
            group = f"{session} ({day})" if session else day or "Program"
            block = groups.setdefault(group, [])
            block.append(f"### {title}")
            if speakers:
                block.append(f"Speakers: {speakers}")
            if links:
                block.append(" | ".join(links))
            block.append(body if body else "No description published; title, speakers and materials only.")
            block.append("")
        for group in groups:
            lines.append(f"## {group}")
            lines += groups[group]
        return "\n".join(lines), count

    def probe(self, entry: dict, years=None) -> ProbeResult:
        try:
            n = int(re.search(r"(\d+)$", entry["key"]).group(1))
            terms = _terms()
            if f"LACNIC{n}" not in terms:
                return ProbeResult(False, "edition not in the events taxonomy", source_url=API)
            dates = _dates(_agenda(terms[f"LACNIC{n}"]))
            end = max(dates) if dates else None
            if years is not None and (not end or end.year not in set(years)):
                end = None
            return ProbeResult(True, "agenda items with timestamps" if end else "agenda without usable dates",
                               end_date=end, source_url=API)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=API)
