"""JANOG's program timetable, with per-session pages for abstracts and materials.

www.janog.gr.jp/meeting/janog<n>/program-timetable/ is a plain HTML table
whose cells link every session (WG meetings, LTs, tutorials) to its own page.
The fetcher walks the timetable for titles, then reads each session page for
the overview text (概要), slide PDFs (uploads, survey PDFs excluded) and the
YouTube live links, which double as the archived recordings. Everything is in
Japanese; the digest writer presents it as-is. No bot blocking.
"""

from __future__ import annotations

import re
from datetime import date
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, looks_blocked, scan_end_date, OK, NOT_PUBLISHED

_SELF = re.compile(r"/(?:program-timetable|agenda|archive|surveyresults|map|traffic|faq|contact)/?$", re.I)
_SURVEY = re.compile(r"アンケート|survey", re.I)
_DAY = re.compile(r"(Day\s*[0-9]+)")
_WHEN = re.compile(r"Day\s*[0-9]+\s+([0-9]{4})年([0-9]{1,2})月([0-9]{1,2})日")


def _clean(text: str) -> str:
    text = re.sub(r"\[tmm_summary[^\]]*\]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


class JanogFetcher(Fetcher):
    name = "janog"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url, timeout=120)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="timetable not published yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            soup = BeautifulSoup(resp.text, "html.parser")
            session_urls: list[str] = []
            for a in soup.select("table a[href]"):
                href = urljoin(url, a["href"])
                if "program-timetable" in href or _SELF.search(href):
                    continue
                if re.search(rf"/meeting/janog[\d.]+/[a-z0-9-]+/?$", href, re.I) and href not in session_urls:
                    session_urls.append(href)
            lines: list[str] = []
            seen: set[str] = set()
            for session_url in session_urls:
                item = self._session(session_url)
                if not item or item["title"] in seen:
                    continue
                seen.add(item["title"])
                lines.append(f"### {item['title']}")
                if item["speakers"]:
                    lines.append(f"Speakers: {item['speakers']}")
                if item["links"]:
                    lines.append(" | ".join(item["links"]))
                if item["when"]:
                    lines.append(item["when"])
                lines.append(item["abstract"] or "No overview published; title and speakers only.")
                lines.append("")
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if seen else NOT_PUBLISHED, program_text="\n".join(lines),
                           source_url=url, item_count=len(seen),
                           detail=f"parsed {len(seen)} sessions (Japanese program)")

    def _session(self, url: str) -> dict | None:
        resp = http_get(url)
        if resp.status_code != 200:
            return None
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
        title_el = soup.select_one("h1.entry-title")
        if not title_el:
            return None
        body = _clean((soup.select_one("main, article, .entry-content") or soup).get_text(" ", strip=True))
        abstract = ""
        head = body.find("概要")
        tail = body.find("場所", head) if head >= 0 else -1
        if head >= 0:
            abstract = body[head + len("概要"): tail if tail > 0 else head + 2500].strip()
        links: list[str] = []
        for href in dict.fromkeys(a.get("href", "") for a in soup.select("a[href]")):
            if not href:
                continue
            if href.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")) and not _SURVEY.search(href):
                links.append(f"slides: {href}")
            elif re.search(r"youtube\.com/(live|watch)", href):
                links.append(f"video: {href}")
        speakers = ""
        m = re.search(r"発表者[：:]\s*([^\n]{2,120})", body)
        if m:
            speakers = m.group(1).strip()
        when = ""
        m = _WHEN.search(body)
        day = _DAY.search(body[: body.find("場所")] if body.find("場所") > 0 else body)
        if m and day:
            when = f"{day.group(1)}, {m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
        return {"title": title_el.get_text(" ", strip=True), "speakers": speakers,
                "links": links[:4], "abstract": abstract, "when": when}

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            resp = http_get(url, timeout=120)
            if resp.status_code == 404:
                return ProbeResult(False, "404 (no such meeting yet)", source_url=url)
            if resp.status_code != 200 or looks_blocked(resp):
                return ProbeResult(False, f"blocked ({resp.status_code} / challenge)", source_url=url)
            resp.encoding = "utf-8"
            end = scan_end_date(resp.text, years)
            if end is None:
                # Japanese dates ("2026年7月15日") are invisible to scan_end_date.
                found = [date(int(y), int(m), int(d)) for y, m, d in
                          re.findall(r"([0-9]{4})年\s*([0-9]{1,2})月\s*([0-9]{1,2})日", resp.text)
                          if 1 <= int(m) <= 12 and 1 <= int(d) <= 31]
                found = [d for d in found if years is None or d.year in set(years)]
                end = max(found) if found else None
            return ProbeResult(True, "timetable; dates scanned" if end else "dates not found",
                               end_date=end, source_url=url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
