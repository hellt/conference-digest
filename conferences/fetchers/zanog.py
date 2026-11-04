"""ZANOG's programs, read from wherever the edition actually ran.

ZANOG hosts each annual somewhere new: standalone plenaries (ZANOG25,
Umhlanga; ZANOG27, Stellenbosch) and combined ZANOG@iWeek editions (2024
and 2026, at iweek.org.za), while its own events portal is registration
shells only — the ZANOG25 program page it once linked is already a 404.
So editions are added to the registry by hand, one block per edition with
the program page that year's site actually serves; no URL template would
survive a venue change, and there is no series to discover them.

For a ZANOG@iWeek edition the agenda at iweek.org.za lists the combined
program, and each session row links to a Drupal session page carrying the
full abstract, the speakers with affiliations, and the schedule slot. The
fetcher reads both: rows for the talk list, pages for the detail. Breaks,
meals and socials are skipped; every real session is kept, because the
model picks what matters for the reader out of a combined program. Every
2026 session is recorded on ZANOG's YouTube channel (@nognetza), which the
links step finds by channel.

The session pages state their slot twice — as visible local text and as a
datetime attribute two hours off — and only the text is right, so the
program text is grouped by the dates the page shows, not the attributes.
"""

from __future__ import annotations

import re
import time
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_SKIP = re.compile(r"^(?:registration|tea break|lunch|coffee break|coffee|whiskey bof|"
                   r"beers for peers|closing drinks)\b", re.I)
_SLOT = re.compile(r"^(\w{3}), (\d{2})/(\d{2})/(\d{4}) - (\d{2}:\d{2})$")
_DAYS = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday",
         "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"}
_MONTHS = ("january february march april may june july august september october november december"
           ).split()


class ZanogFetcher(Fetcher):
    name = "zanog"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url, timeout=120)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="no agenda yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            rows = self._rows(BeautifulSoup(resp.text, "html.parser"), url)
            days: dict[str, list[str]] = {}
            count = 0
            for slug, title in rows:
                time.sleep(0.3)
                try:
                    sresp = http_get(slug, timeout=60)
                    if sresp.status_code != 200:
                        continue
                    sresp.encoding = "utf-8"
                except Exception:
                    continue
                item, day = self._session(BeautifulSoup(sresp.text, "html.parser"), slug)
                if item:
                    days.setdefault(day, []).extend(item)
                    count += 1
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        lines: list[str] = []
        for day, items in days.items():   # agenda order is already chronological
            lines.append(f"## {day}")
            lines.append("")
            lines.extend(items)
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text="\n".join(lines),
                           source_url=url, item_count=count, detail=f"parsed {count} sessions")

    def _rows(self, soup: BeautifulSoup, url: str) -> list[tuple[str, str]]:
        """(session page, title) for every agenda session worth reading."""
        rows = []
        for row in soup.select("div.views-row"):
            a = row.select_one(".views-field-title a")
            if not a or not a.get("href"):
                continue
            title = a.get_text(" ", strip=True)
            if not title or _SKIP.match(title):
                continue
            rows.append((urljoin(url, a["href"]), title))
        return rows

    def _session(self, soup: BeautifulSoup, url: str) -> tuple[list[str], str]:
        """(item lines, day heading) for one session page, or ([], '') if unusable."""
        full = soup.find("article", class_="node--view-mode-full")
        teaser = soup.find("article", class_="node--type-mt-session")
        title = soup.h1.get_text(" ", strip=True) if soup.h1 else ""
        if not full or not teaser or not title:
            return [], ""
        speakers = []
        for spk in full.select(".field--name-field-mt-ses-speaker article"):
            name = spk.select_one(".field--name-title")
            org = spk.select_one(".field--name-field-mt-spk-subtitle")
            speakers.append(name.get_text(" ", strip=True)
                            + (f" - {org.get_text(' ', strip=True)}" if org else ""))
        slot = teaser.select_one(".field--name-field-mt-ses-date time")
        room = teaser.select_one(".field--name-field-mt-ses-location")
        topic = full.select_one(".field--name-field-mt-ses-topics")
        day = ""
        tail = ""
        if slot:
            m = _SLOT.match(slot.get_text(" ", strip=True))
            if m:
                dow, d, mo, y, hm = m.groups()
                day = f"{_DAYS[dow]} {int(d)} {_MONTHS[int(mo) - 1].capitalize()}"
                tail = f"{hm}, {room.get_text(' ', strip=True)}" if room else hm
        out = [f"### {title}", f"page: {url}"]
        if speakers:
            out.append("Speakers: " + ", ".join(speakers))
        if tail:
            out.append(f"When: {tail}")
        if topic:
            track = topic.get_text(" ", strip=True)
            if track:
                out.append(f"Track: {track}")
        abstract = full.select_one(".field--name-field-mt-ses-body")
        if abstract:
            text = abstract.get_text(" ", strip=True)
            if text:
                out.append(text)
        out.append("")
        return out, day or "Program"
