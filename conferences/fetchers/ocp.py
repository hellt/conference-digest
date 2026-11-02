"""OCP Global Summit: the schedule JSON baked into the fnVirtual app bundle.

Every OCP summit lives on the FN TECH event platform as its own host
(``{year}ocpglobal.fnvirtual.app``). The schedule page is a Gatsby app whose
data is not on the wire: the whole program — sessions, speakers with
companies, HTML abstracts, tracks, rooms, YouTube recordings and material
links — is embedded in the ``app-*.js`` bundle the page loads, as
``JSON.parse('...')`` literals. The fetcher resolves that bundle from the
page's script tags, unescapes the JS string literals and parses the two blobs
it needs: the summit config (name, dates, timezone) and the events array.

Per-edition hosts stay up after the event (2024 still serves), so a missing
host means a future edition's site is not built yet — the probe's "not yet"
signal. An HTTP error or a blocked page is a manual fallback, never a guess.

The events array lists ~630 entries of every kind. The fetcher keeps
presentations with an abstract (~550 for 2026) and drops the non-talk kinds:
staff/internal ``SummitEvents``, posters (``Symposium: Poster and
Presentation``) and placeholder rows without a description. Executive,
expo-hall and panel sessions are real talks with abstracts and stay.

Recordings: many presentations carry their YouTube upload among their
``links`` (OCP's channel), filed here as ``video:``. Others gain one through
the links step's verified YouTube search; the session pages themselves are
client-rendered, so the ``page:`` link contributes nothing extra there —
the platform also logs viewers into Mux streams we cannot use.
"""

from __future__ import annotations

import json
import re
import socket
from datetime import date, datetime
from typing import Iterable, Optional
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse
from zoneinfo import ZoneInfo

from bs4 import BeautifulSoup

from .base import (
    Fetcher, FetchResult, ProbeResult, http_get, looks_blocked,
    OK, NOT_PUBLISHED,
)

_SCRIPT_SRC = re.compile(r'src="(/[A-Za-z0-9._-]+\.js)"')
# Where a PDF-ish link lives (papers and preprints); everything else on the
# web is a materials page (OCP wiki/spec pages, GitHub repos, white papers).
_PAPER_HOSTS = ("arxiv.org", "ieeexplore.ieee.org", "dl.acm.org", "doi.org")
# YouTube, in all its URL shapes.
_VIDEO_HOSTS = ("youtube.com", "youtu.be")

# Event types that are not digestible talks.
DROP_TYPES = {"Symposium: Poster and Presentation"}


class NotUp(Exception):
    """This edition's site does not exist yet (DNS: not built)."""


class Unreadable(Exception):
    """The source served something we cannot parse (or blocked us)."""


def _host(url: str) -> str:
    return urlparse(url).netloc


def _host_up(url: str) -> bool:
    try:
        socket.getaddrinfo(_host(url), 443)
        return True
    except socket.gaierror:
        return False


def _js_unescape(raw: str) -> str:
    """Turn a JS single-quoted string literal's body into its value.

    Only JS escapes are resolved left-to-right ('\\' and \\' collapse);
    JSON escapes like \\" survive for the JSON decoder afterwards.
    """
    out: list[str] = []
    k, n = 0, len(raw)
    while k < n:
        c = raw[k]
        if c == "\\" and k + 1 < n:
            nxt = raw[k + 1]
            if nxt in ("\\", "'"):
                out.append(nxt)
                k += 2
                continue
            if nxt == "n":
                out.append("\n")
                k += 2
                continue
            if nxt == "t":
                out.append("\t")
                k += 2
                continue
            # any other escape stays for the JSON layer (\", \/, \uXXXX...)
            out.append(raw[k:k + 2])
            k += 2
            continue
        out.append(c)
        k += 1
    return "".join(out)


def _blobs(js_text: str) -> list[object]:
    """Every ``JSON.parse('...')`` literal in a bundle, parsed.

    A literal that does not decode is skipped, not fatal: bundles also bake
    small config strings that are not JSON.
    """
    out: list[object] = []
    for m in re.finditer(r"JSON\.parse\('", js_text):
        i = m.end()
        j = i
        while j < len(js_text):  # find the closing, unescaped quote
            if js_text[j] == "'":
                nb = 0
                k = j - 1
                while k >= i and js_text[k] == "\\":
                    nb += 1
                    k -= 1
                if nb % 2 == 0:
                    break
            j += 1
        try:
            out.append(json.loads(_js_unescape(js_text[i:j])))
        except (json.JSONDecodeError, ValueError):
            continue
    return out


def _clean_html(fragment: str) -> str:
    text = (fragment or "").strip()
    if "<" in text:
        text = BeautifulSoup(text, "html.parser").get_text(" ", strip=True)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def _link_key(url: str) -> str:
    """file a material URL under the program text's link keys, by its host."""
    host = urlparse(url).netloc.lower().removeprefix("www.")
    if any(host == h or host.endswith("." + h) for h in _VIDEO_HOSTS):
        return "video"
    if any(host == h or host.endswith("." + h) for h in _PAPER_HOSTS):
        return "pdf"
    return "materials"


def _strip_playlist(url: str) -> str:
    """Drop a YouTube URL's playlist-positioning params, keep the video."""
    p = urlparse(url)
    if "youtube.com" not in p.netloc:
        return url
    q = [(k, v) for k, v in parse_qsl(p.query) if k not in ("list", "index")]
    return urlunparse(p._replace(query=urlencode(q)))


class OcpFetcher(Fetcher):
    name = "ocp"

    def _resolve(self, url: str) -> tuple[dict, list[dict]]:
        """(summit config, events) from the app bundle behind the schedule
        page. Raises NotUp / Unreadable."""
        if not _host_up(url):
            raise NotUp(f"no site for this edition yet (DNS: {_host(url)})")
        try:
            page = http_get(url)
        except Exception as e:
            raise Unreadable(f"request error: {e}")
        if page.status_code == 404:
            raise NotUp("404 (no such edition yet)")
        if looks_blocked(page):
            raise Unreadable(f"blocked ({page.status_code}); paste the program by hand")
        if page.status_code != 200:
            raise NotUp(f"unexpected status {page.status_code}")

        # The schedule data sits in the app bundle; other chunks are small.
        # Try the app-* script first, then any other script on the page.
        srcs = _SCRIPT_SRC.findall(page.text)
        srcs.sort(key=lambda s: (not s.startswith("/app-"), s))
        for src in srcs[:20]:
            try:
                resp = http_get(f"https://{_host(url)}{src}")
            except Exception:
                continue
            if resp.status_code != 200 or looks_blocked(resp):
                continue
            summit: Optional[dict] = None
            events: Optional[list] = None
            for blob in _blobs(resp.text):
                if summit is None and isinstance(blob, dict) \
                        and "dates_label" in blob and "start_date" in blob:
                    summit = blob
                elif events is None and isinstance(blob, list) \
                        and any(isinstance(e, dict)
                                and e.get("class_name") == "Presentation"
                                for e in blob):
                    events = blob
            if summit and events:
                return summit, events
        raise Unreadable(
            "no schedule data found in the event app's bundles"
            " (layout change?); paste the program by hand"
        )

    def _kept(self, events: list[dict]) -> list[dict]:
        out = []
        for e in events:
            if e.get("class_name") != "Presentation":
                continue
            if (e.get("type") or {}).get("name") in DROP_TYPES:
                continue
            if not (e.get("description") or "").strip():
                continue
            out.append(e)
        return out

    def _parse(self, kept: list[dict], page_url: str) -> tuple[str, int]:
        base = f"https://{_host(page_url)}"
        by_track: dict[str, list[dict]] = {}
        for e in kept:
            track = ((e.get("track") or {}).get("name") or "Untracked")
            by_track.setdefault(track, []).append(e)

        lines: list[str] = []
        for track in sorted(by_track):
            items = sorted(
                by_track[track],
                key=lambda e: (e.get("start_date") or 0, e.get("title", "")),
            )
            lines.append(f"## {track}")
            lines.append("")
            for e in items:
                lines.append(f"### {(e.get('title') or '').strip()}")
                speakers = ", ".join(
                    f"{sp.get('first_name', '').strip()} {sp.get('last_name', '').strip()}".strip()
                    + (f" ({sp['company'].strip()})" if sp.get("company") else "")
                    for sp in (e.get("speakers") or [])
                    if (sp.get("first_name") or sp.get("last_name"))
                )
                if speakers:
                    lines.append(f"Speakers: {speakers}")
                parts = [f"page: {base}/a/schedule/{e['id']}/"]
                seen: set[str] = set()
                # The links step keeps one link per key, so keep only the
                # first (lowest `order`: the speaker's own ordering, the
                # canonical one) of each kind.
                for l in sorted((e.get("links") or []),
                                key=lambda l: l.get("order", 0)):
                    link = (l.get("link") or "").strip()
                    if not link.startswith("http"):
                        continue
                    link = _strip_playlist(link)
                    if link in seen:
                        continue
                    key = _link_key(link)
                    if key in seen:
                        continue
                    seen.update((link, key))
                    parts.append(f"{key}: {link}")
                lines.append(" | ".join(parts))
                abstract = _clean_html(e.get("description", ""))
                if abstract:
                    lines.append(abstract)
                lines.append("")
        return "\n".join(lines).rstrip() + "\n", len(kept)

    def fetch(self, entry: dict) -> FetchResult:
        url = entry.get("program_url", "")
        try:
            _summit, events = self._resolve(url)
        except NotUp as e:
            return FetchResult(status=NOT_PUBLISHED, detail=str(e), source_url=url)
        except Unreadable as e:
            return self.manual(entry, str(e))
        except Exception as e:
            return self.manual(entry, f"request error: {e}")

        kept = self._kept(events)
        if not kept:
            return FetchResult(
                status=NOT_PUBLISHED,
                detail="app bundle lists no presentations with abstracts yet",
                source_url=url,
            )

        try:
            text, count = self._parse(kept, url)
        except Exception as e:
            return self.manual(entry, f"parse error: {e}")

        return FetchResult(
            status=OK,
            program_text=text,
            source_url=url,
            item_count=count,
            detail=f"parsed {count} talks of {len(events)} events "
                   f"(posters, internal events and items without abstracts dropped)",
        )

    def probe(self, entry: dict, years: Optional[Iterable[int]] = None) -> ProbeResult:
        """The schedule data states the edition's dates outright, so discovery
        reads them here instead of scanning page text.

        The last day a session starts is the end date, NOT the platform's
        own `end_date`: that one can trail into a post-event on-demand
        window (2025 says October 23 for an October 13-16 summit).
        """
        url = entry.get("program_url", "")
        try:
            summit, events = self._resolve(url)
        except (NotUp, Unreadable) as e:
            return ProbeResult(False, str(e), source_url=url)
        except Exception as e:
            return ProbeResult(False, f"request error: {e}", source_url=url)

        kept = self._kept(events)
        if not kept:
            return ProbeResult(
                False, "app bundle up but lists no presentations yet",
                source_url=url,
            )

        end: Optional[date] = None
        try:
            tz = ZoneInfo(summit.get("time_zone_id") or "UTC")
            starts = [e["start_date"] for e in kept if e.get("start_date")]
            if starts:
                end = datetime.fromtimestamp(max(starts), tz=tz).date()
        except Exception:
            end = None
        return ProbeResult(
            True,
            f"app bundle: {len(kept)} talks, {summit.get('dates_label', '')}",
            end_date=end,
            source_url=url,
        )
