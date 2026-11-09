"""TNC (GÉANT): WordPress dates via Tavily; programme via its public app API.

tnc{yy}.geant.org serves a plain-403 to datacenter clients, so discovery's
probe still reads the WordPress page through Tavily Extract (owner-approved,
2026-11-01). The programme's WordPress source embeds Pretty Event's loader;
that loader exposes one public JSON endpoint for the whole programme and one
for its configuration. Those endpoints are directly readable and include all
sessions, nested presentations, abstracts, speakers and attachments, so the
programme itself does not need a browser, Indico or Tavily.
"""

from __future__ import annotations

import os
import re
from datetime import datetime
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .nanog import tavily_extract
from .base import Fetcher, FetchResult, ProbeResult, http_get, scan_end_date, OK, NOT_PUBLISHED

API = "https://pretty-event-dnm-ieventi-production.apps.bst2.paas.psnc.pl"
_SKIP_TYPES = {"break", "socials"}
_FILE_RE = re.compile(r"\.(pdf|pptx?|key|odp)$", re.I)


def _text(html: str) -> str:
    return re.sub(r"\s+", " ", BeautifulSoup(html or "", "html.parser").get_text(" ", strip=True)).strip()


def _people(people: list[dict]) -> str:
    named = []
    for person in people:
        name = (person.get("name") or "").strip()
        affiliation = (person.get("affiliation") or "").strip()
        if name:
            named.append(f"{name} ({affiliation})" if affiliation else name)
    return ", ".join(dict.fromkeys(named))


class TncFetcher(Fetcher):
    name = "tnc"

    def _page(self, entry: dict) -> str:
        key = os.environ.get("TAVILY_API_KEY", "").strip()
        if not key:
            raise RuntimeError("TAVILY_API_KEY not set; tnc.geant.org blocks datacenter clients")
        return tavily_extract(entry["program_url"], key)

    @staticmethod
    def _project(entry: dict) -> str:
        host = urlparse(entry["program_url"]).hostname or ""
        project = host.split(".")[0]
        if not re.fullmatch(r"tnc\d{2}", project):
            raise ValueError(f"cannot derive the Pretty Event project from {host!r}")
        return project

    def fetch(self, entry: dict) -> FetchResult:
        programme_url = entry.get("manual_fallback_url", entry["program_url"])
        try:
            project = self._project(entry)
            url = f"{API}/api/programme/{project}"
            resp = http_get(url, timeout=120)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=programme_url,
                                   detail=f"{project} programme API not available yet")
            if resp.status_code != 200:
                raise RuntimeError(f"programme API returned {resp.status_code}")
            sessions = resp.json()
            if not isinstance(sessions, list):
                raise ValueError("programme API did not return a session list")

            config_url = f"{API}/api/config/{project}"
            config_resp = http_get(config_url, timeout=120)
            if config_resp.status_code != 200:
                raise RuntimeError(f"programme config API returned {config_resp.status_code}")
            config = config_resp.json()
            text, count = self._parse(sessions, programme_url, config.get("indicoBaseUrl", ""))
        except Exception as e:
            return self.manual(entry, f"programme API fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=programme_url, item_count=count,
                           detail=f"parsed {count} programme items from {len(sessions)} sessions")

    def _parse(self, sessions: list[dict], programme_url: str, attachment_base: str) -> tuple[str, int]:
        lines: list[str] = []
        count = 0
        base_url = programme_url.split("#", 1)[0]
        for session in sorted(sessions, key=lambda s: (s.get("day", 0), s.get("start", ""))):
            title = _text(session.get("title", ""))
            if not title or (session.get("type_name") or "").casefold() in _SKIP_TYPES:
                continue
            try:
                day = datetime.strptime(str(session["day"]), "%Y%m%d")
            except (KeyError, ValueError):
                continue

            page = f"{base_url}#{day:%A}/all/{session['id']}" if session.get("id") else base_url
            meta = " | ".join(x for x in (
                f"{session.get('start', '')[:5]}–{session.get('end', '')[:5]}",
                session.get("room", ""), session.get("type_name", ""),
            ) if x)
            lines.append(f"## {day:%Y-%m-%d} · {title}")
            if meta:
                lines.append(meta)

            session_body = _text(session.get("description", ""))
            chairs = _people(session.get("chairs") or [])
            presentations = [p for p in session.get("presentations") or [] if _text(p.get("title", ""))]
            actual_presentations = bool(presentations)
            if not presentations:
                presentations = [{
                    "title": title, "description": session.get("description", ""),
                    "start": session.get("start", ""), "end": session.get("end", ""),
                }]

            for presentation in presentations:
                lines.append(f"### {_text(presentation['title'])}")
                if actual_presentations:
                    times = f"{presentation.get('start', '')[:5]}–{presentation.get('end', '')[:5]}"
                    if times != "–":
                        lines.append(times)
                    if chairs:
                        lines.append(f"Chairs: {chairs}")
                speakers = _people(presentation.get("speakers") or ([] if actual_presentations else session.get("chairs") or []))
                if speakers:
                    lines.append(f"Speakers: {speakers}")

                links = [f"page: {page}"]
                for attachment in presentation.get("attachments") or []:
                    href = urljoin(attachment_base, attachment.get("url", ""))
                    if href.startswith(("http://", "https://")) and _FILE_RE.search(urlparse(href).path):
                        links.append(f"slides: {href}")
                lines.append(" | ".join(links))

                body = _text(presentation.get("description", ""))
                if actual_presentations and session_body:
                    body = f"Session abstract: {session_body}" + (f"\n{body}" if body else "")
                lines.append(body or "No description published; title, speakers and materials only.")
                lines.append("")
                count += 1
        return "\n".join(lines), count

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            page = self._page(entry)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
        end = scan_end_date(page, years)
        return ProbeResult(True, "site readable through Tavily; dates scanned" if end
                           else "site readable; dates not found", end_date=end, source_url=url)
