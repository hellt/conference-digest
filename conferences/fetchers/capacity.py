"""Capacity Europe's agenda page: server-rendered session library.

www.capacityeurope.com/agenda/ looks like a JS app, but the whole session
library is server-rendered HTML: one day wrapper per day (id="13-oct-2026"),
one column per stage, one li per session — title link, description, speakers
with "Name, Role - COMPANY", stream tags and times. Exhibition, coffee and
lunch items are separate classes and are skipped. A commercial event: no
recordings or slides are published, so items carry the session page only. The
day wrapper ids give exact dates. No bot blocking.
"""

from __future__ import annotations

import re
from datetime import date

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_ITEM = "m-seeminar"  # placeholder, real selectors below
_DAY = re.compile(r"^(\d{1,2})-([a-z]{3})-(\d{4})$")
_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7,
           "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
_SKIP = re.compile(r"^(?:registration|welcome party|conversations over dinner|brunch|happy hour|delegate breakfast)", re.I)


class CapacityFetcher(Fetcher):
    name = "capacity"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            year = int(re.search(r"(\d{4})$", entry["key"]).group(1))
            resp = http_get(url, timeout=120)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="agenda not published yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            # The agenda URL always serves the current edition; a candidate year
            # whose days are not on the page yet is not published for it.
            shown = {int(m[2]) for m in re.findall(r'id="(\d{1,2})-([a-z]{3})-(\d{4})"', resp.text)}
            if shown and year not in shown:
                return FetchResult(status=NOT_PUBLISHED, source_url=url,
                                   detail=f"agenda still shows {', '.join(map(str, sorted(shown)))}")
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"), url)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} sessions")

    def _parse(self, soup: BeautifulSoup, url: str) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        count = 0
        for wrapper in soup.select("div.m-seminar-list__list__content__wrapper"):
            day_match = _DAY.match(wrapper.get("id", ""))
            day_label = None
            if day_match:
                d, mon, year = day_match.groups()
                month = _MONTHS.get(mon)
                if month:
                    try:
                        day_label = date(int(year), month, int(d)).strftime("%d %B %Y")
                    except ValueError:
                        day_label = wrapper["id"]
            for column in wrapper.select("div.m-seminar-list__list__content__column"):
                stage_el = column.select_one(".m-seminar-list__list__content__column__header__description")
                stage = stage_el.get_text(" ", strip=True) if stage_el else ""
                for item in column.select("li.m-seminar-list__list__content__column__items__item--session"):
                    title_link = item.select_one(".m-seminar-list__list__content__column__items__item__title a")
                    if not title_link:
                        continue
                    title = title_link.get_text(" ", strip=True)
                    if not title or title in seen or _SKIP.match(title):
                        continue
                    seen.add(title)
                    count += 1
                    lines.append(f"### {title}")
                    speakers = [a.get_text(" ", strip=True) for a in item.select(
                        ".m-seminar-list__list__content__column__items__item__speakers__speaker__name a")]
                    if speakers:
                        lines.append("Speakers: " + ", ".join(speakers))
                    href = title_link.get("href", "")
                    if href:
                        lines.append(f"page: {href if href.startswith('http') else url.rstrip('/') + '/' + href.lstrip('/')}")
                    streams = [i.get("title", "") for i in item.select(
                        ".m-seminar-list__list__content__column__items__item__streams__item__shape")]
                    streams = ", ".join(dict.fromkeys(s for s in streams if s))
                    description = item.select_one(
                        ".m-seminar-list__list__content__column__items__item__description")
                    body = re.sub(r"\s+", " ", description.get_text(" ", strip=True)) if description else ""
                    meta = " · ".join(x for x in (day_label, stage, f"Streams: {streams}" if streams else "") if x)
                    if meta:
                        lines.append(meta)
                    lines.append(body if body else "No description published; title, speakers and stream only.")
                    lines.append("")
        if lines:
            lines.insert(0, "## Capacity Europe sessions")
        return "\n".join(lines), count

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            resp = http_get(url, timeout=120)
            if resp.status_code == 404:
                return ProbeResult(False, "404 (agenda not up yet)", source_url=url)
            if resp.status_code != 200 or looks_blocked(resp):
                return ProbeResult(False, f"blocked ({resp.status_code} / challenge)", source_url=url)
            resp.encoding = "utf-8"
            soup = BeautifulSoup(resp.text, "html.parser")
            found = []
            for wrapper in soup.select("div.m-seminar-list__list__content__wrapper"):
                day_match = _DAY.match(wrapper.get("id", ""))
                if day_match:
                    d, mon, year = day_match.groups()
                    month = _MONTHS.get(mon)
                    if month:
                        try:
                            found.append(date(int(year), month, int(d)))
                        except ValueError:
                            pass
            end = max(found) if found else None
            if years is not None and (not end or end.year not in set(years)):
                end = None
            return ProbeResult(True, "agenda page; day wrapper ids" if end else "agenda page; dates not found",
                               end_date=end, source_url=url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
