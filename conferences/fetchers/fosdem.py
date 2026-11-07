"""FOSDEM's Pentabarf schedule XML, filtered to the reader's tracks.

fosdem.org publishes the whole edition (71 tracks, ~1000 events) as one
schedule XML — the same feed the mobile apps use. Every event carries its page
URL, abstract, speakers, slide attachments and video.fosdem.org recordings.
FOSDEM is far broader than this digest's reader, so the fetcher keeps a
curated track set (edit RELEVANT_TRACKS as interests shift, like the IETF
fetcher's WG list) and drops workshops and lightning talks. No bot blocking.
"""

from __future__ import annotations

import re
from datetime import date
from xml.etree import ElementTree

from .base import Fetcher, FetchResult, ProbeResult, http_get, OK, NOT_PUBLISHED

# Track slugs relevant to networking, cloud, Kubernetes, and AI. "main" is
# kept for the keynotes; "junior" (young makers) is not.
RELEVANT_TRACKS = {
    "main",
    "network",
    "ebpf",
    "dns",
    "ai",
    "hpc-big-data-data-science",
    "containers",
    "virtualization-and-cloud-infrastructure",
    "kernel",
}
_SKIP = re.compile(r"^(?:welcome|opening|closing|about the .* devroom|q&a|break|lunch)", re.I)


class FosdemFetcher(Fetcher):
    name = "fosdem"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url, timeout=120)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="schedule not published yet")
            if resp.status_code != 200:
                return self.manual(entry, f"unexpected status {resp.status_code}")
            text, count, end = self._parse(resp.content)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        detail = f"parsed {count} events from {len(RELEVANT_TRACKS)} relevant tracks"
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=detail,
                           meta={"end_date": end.isoformat() if end else ""})

    def _parse(self, content: bytes):
        root = ElementTree.fromstring(content)
        conference = root.find("conference")
        end = date.fromisoformat(conference.findtext("end", "")) if conference is not None else None
        lines: list[str] = []
        seen: set[str] = set()
        current_track = None
        for event in root.iter("event"):
            track_el = event.find("track")
            track_slug = (track_el.get("slug") or "") if track_el is not None else ""
            track = (track_el.text or "").strip() if track_el is not None else ""
            if event.findtext("type") in ("workshop", "lightningtalk"):
                continue
            if track_slug not in RELEVANT_TRACKS:
                continue
            title = (event.findtext("title") or "").strip()
            url = (event.findtext("url") or "").strip()
            if not title or url in seen or _SKIP.match(title):
                continue
            seen.add(url)
            if track_slug != current_track:
                current_track = track_slug
                lines.append(f"## {track} ({track_slug})")
            lines.append(f"### {title}")
            persons = [p.text for p in event.iter("person") if p.text]
            if persons:
                lines.append("Speakers: " + ", ".join(persons))
            links = [f"page: {url}"]
            attachments = event.find("attachments")
            if attachments is not None:
                for attachment in attachments.findall("attachment"):
                    href = attachment.get("href", "")
                    if href.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
                        links.append(f"slides: {href}")
            event_links = event.find("links")
            recording = ""
            if event_links is not None:
                for link in event_links.findall("link"):
                    href = link.get("href", "")
                    if "youtube.com" in href or "youtu.be" in href:
                        recording = href
                        break
                    if href.endswith(".mp4"):
                        recording = href
            if recording:
                links.append(f"video: {recording}")
            lines.append(" | ".join(links))
            body = " ".join(t.strip() for t in (event.findtext("abstract"), event.findtext("description")) if t)
            body = re.sub(r"<[^>]+>", " ", body)
            body = re.sub(r"\s+", " ", body).strip()
            lines.append(body if body else "No abstract published; title, speakers and materials only.")
            lines.append("")
        return "\n".join(lines), len(seen), end

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            resp = http_get(url, timeout=120)
            if resp.status_code == 404:
                return ProbeResult(False, "404 (schedule not up yet)", source_url=url)
            if resp.status_code != 200:
                return ProbeResult(False, f"unexpected status {resp.status_code}", source_url=url)
            root = ElementTree.fromstring(resp.content)
            end = date.fromisoformat(root.findtext("conference/end", ""))
            if years is not None and end.year not in set(years):
                end = None
            return ProbeResult(True, "schedule XML; exact conference dates", end_date=end, source_url=url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
