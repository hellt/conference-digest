"""MORE-IP (AMS-IX) agenda: talks, speaker affiliations, blurbs and recordings.

more-ip-event.net/more-ip-<year>/agenda/ is a WordPress page — one day-wrap
per day, one article per slot with the title, a speaker line ("Name -
Company"), a short description and, for some items, the YouTube recording.
Breaks carry a grey class. The day titles have no year, so the series uses an
end_date_hint. No bot blocking. looks_blocked()'s body markers are not
applied: the theme's CSS mentions captcha form classes, which is not a
challenge — status codes alone decide.
"""

from __future__ import annotations

import re

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, scan_end_date, OK, NOT_PUBLISHED

_SKIP = re.compile(r"^(?:registration|coffee break|lunch break|networking time|boat transfer|dinner|welcome back)", re.I)


class MoreIpFetcher(Fetcher):
    name = "moreip"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="agenda not published yet")
            if resp.status_code != 200 or resp.status_code in (403, 429, 503):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            text, count = self._parse(BeautifulSoup(resp.text, "html.parser"))
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text=text,
                           source_url=url, item_count=count, detail=f"parsed {count} agenda items")

    def probe(self, entry: dict, years=None) -> ProbeResult:
        # The default probe's looks_blocked() keys on captcha wording that the
        # theme's CSS legitimately contains, so this probe checks status only.
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return ProbeResult(False, "404 (no such edition yet)", source_url=url)
            if resp.status_code != 200:
                return ProbeResult(False, f"unexpected status {resp.status_code}", source_url=url)
            resp.encoding = "utf-8"
            end = scan_end_date(resp.text, years)
            return ProbeResult(True, "200; agenda page" + ("; dates scanned" if end else ""),
                               end_date=end, source_url=url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)

    def _parse(self, soup: BeautifulSoup) -> tuple[str, int]:
        lines: list[str] = []
        seen: set[str] = set()
        count = 0
        for day in soup.select("div.day-wrap"):
            heading = day.select_one(".day-title h2")
            when = day.select_one(".day-title span")
            if not heading:
                continue
            lines.append(f"## {heading.get_text(' ', strip=True)} — {when.get_text(' ', strip=True) if when else ''}".rstrip(" —"))
            for article in day.select("article.event-item"):
                title_el = article.select_one("h3")
                if not title_el:
                    continue
                title = title_el.get_text(" ", strip=True)
                classes = " ".join(article.get("class") or [])
                if not title or "bg-color-grey" in classes or _SKIP.match(title) or title in seen:
                    continue
                seen.add(title)
                count += 1
                lines.append(f"### {title}")
                speakers = [p.get_text(" ", strip=True) for p in article.select(".agenda-item-speaker p")]
                if speakers:
                    lines.append("Speakers: " + ", ".join(speakers))
                links = []
                for a in article.select('a[href*="youtube.com"]'):
                    links.append(f"video: {a['href']}")
                    break
                if links:
                    lines.append(" | ".join(links))
                description = article.select_one(".event-title > p")
                body = description.get_text(" ", strip=True) if description else ""
                lines.append(body if body else "No description published; title and speakers only.")
                lines.append("")
        return "\n".join(lines), count
