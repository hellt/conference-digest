"""NANOG fetcher: one NANOG meeting's agenda, from nanog.org via Tavily Extract.

    https://nanog.org/events/nanog-<n>/agenda/

The agenda is one page with every session as a table row, under a header per
day ("##### Monday, October 27, 2025" in Tavily's Markdown):

    | **11:30 - 12:00 (CDT)** | Honor Ballroom A+B | ##### [](…/agenda/)[Title](https://nanog.org/events/nanog-95/content/5522/)
      [Name - Org](member link) ###### Recordings * [Title](https://youtu.be/…)
      ###### Files * [Slides 1](https://storage.googleapis.com/…/x.pdf)
      ###### Full Abstract The abstract … |

So one request yields the whole program with each talk's page, presenters,
abstract, YouTube recording and slides (PDF or PPTX, on Google Cloud Storage).

ACCESS: nanog.org sits behind Cloudflare and blocks automated clients,
including GitHub Actions runners. The repository owner approved reading the
public agenda through Tavily Extract (2026-11-01), accepting that this goes
around the site's bot protection. Without TAVILY_API_KEY the fetcher returns
manual_fallback, and the agenda URL is the page to paste from by hand. One
fetch costs two Tavily credits (advanced extract).

Logistics rows (registration, meals, breaks, socials, opening/closing) and rows
with no abstract, recording or slides are not program items.
"""

from __future__ import annotations

import os
import re
from datetime import date, datetime
from typing import Iterable, Optional

import requests

from .base import Fetcher, FetchResult, ProbeResult, OK, NOT_PUBLISHED

TAVILY_EXTRACT = "https://api.tavily.com/extract"

DAY_RE = re.compile(r"^#{2,6}\s+(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s+([A-Z][a-z]+ \d{1,2})(?:,\s+(\d{4}))?\s*$", re.M)
# A talk is a link to its page; NANOG 96 nests it in a link to the agenda: [[Title](talk)](agenda).
TALK_RE = re.compile(r"\[\[?([^\[\]]+)\]\((https://(?:www\.)?nanog\.org/events/nanog-\d+/content/\d+/?)\)(?:\]\([^)]*\))?")
# Time slots: **10:15 - 11:15 (CDT)** up to NANOG 96, **13:30**–**14:15**EDT from NANOG 97.
TIME_RE = re.compile(r"\*\*(\d{1,2}:\d{2})\*\*\s*[–-]\s*\*\*(\d{1,2}:\d{2})\*\*\s*([A-Z]{2,4})|\*\*(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})\s*\(([A-Z]{2,4})\)\*\*")
MEMBER_RE = re.compile(r"\[([^\]]+)\]\(https://(?:www\.)?nanog\.org/public/members/[^)]*\)")
MD_LINK = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
SECTION_RE = re.compile(r"#{6}\s+(Recordings|Files|Full Abstract|Abstract)\b", re.I)
YOUTUBE_RE = re.compile(r"https?://(?:www\.)?(?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/|live/))[\w-]{11}[^\s)\]]*")
FILE_RE = re.compile(r"\.(pdf|pptx?|key|odp)(?:$|\?)", re.I)
LOGISTICS = re.compile(
    r"registration|breakfast|lunch|\bbreak\b|reception|social|mixer|happy hour|yoga|run club|nanog active|"
    r"orientation|conference opening|conference closing|welcome|survey|game night|beer|lounge|espresso|"
    r"showcase|office hours|board meeting|members meeting|election|photo",
    re.I,
)


def tavily_extract(url: str, key: str, timeout: int = 180) -> str:
    """The page as Markdown. Tavily sometimes fails one URL form and serves the
    other, so the trailing-slash variant is tried before giving up."""
    alternate = url[:-1] if url.endswith("/") else url + "/"
    errors = []
    for candidate in (url, alternate):
        resp = requests.post(TAVILY_EXTRACT, timeout=timeout, headers={"Authorization": f"Bearer {key}"},
                             json={"urls": [candidate], "format": "markdown", "extract_depth": "advanced"})
        resp.raise_for_status()
        data = resp.json()
        content = "".join(r.get("raw_content", "") for r in data.get("results", []))
        if content.strip():
            return content
        errors += [f.get("error", "no content") for f in data.get("failed_results", [])] or ["no content"]
    raise RuntimeError(f"Tavily could not read {url}: {'; '.join(errors)}")


def tavily_extract_many(urls: list[str], key: str, timeout: int = 240) -> dict[str, str]:
    """Several pages as Markdown, 20 per request (Tavily's limit); failures are left out."""
    out: dict[str, str] = {}
    for i in range(0, len(urls), 20):
        try:
            resp = requests.post(TAVILY_EXTRACT, timeout=timeout, headers={"Authorization": f"Bearer {key}"},
                                 json={"urls": urls[i:i + 20], "format": "markdown", "extract_depth": "advanced"})
            resp.raise_for_status()
            for r in resp.json().get("results", []):
                if r.get("raw_content"):
                    out[r.get("url", "").rstrip("/") + "/"] = r["raw_content"]
        except Exception:
            continue
    return out


def talk_media(md: str) -> dict[str, str]:
    """Slides and recording from a talk page ("Presentation Materials", "Recordings")."""
    files = [u for _, u in MD_LINK.findall(md) if FILE_RE.search(u) and "/site-media-prod/meetings/" in u]
    video = YOUTUBE_RE.search(md)
    return {k: v for k, v in (("slides", files[0] if files else ""), ("video", video.group(0) if video else "")) if v}


def _unescape(s: str) -> str:
    return re.sub(r"\\([\\`*_{}\[\]()#+\-.!|])", r"\1", s).strip()


def _day(month_day: str, year: Optional[str], year_hint: Optional[int]) -> Optional[date]:
    """A day header's date. Headers from NANOG 96 on carry no year: use the
    edition's year when known, else the year that puts the date nearest today."""
    try:
        if year:
            return datetime.strptime(f"{month_day} {year}", "%B %d %Y").date()
        today = date.today()
        years = [year_hint] if year_hint else [today.year - 1, today.year, today.year + 1]
        dates = [datetime.strptime(f"{month_day} {y}", "%B %d %Y").date() for y in years]
        return min(dates, key=lambda d: abs((d - today).days))
    except ValueError:
        return None


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", _unescape(MD_LINK.sub(r"\1", text))).strip(" |")


def parse_agenda(md: str, year_hint: Optional[int] = None) -> tuple[list[dict], list[date]]:
    """Talks and the meeting's days from the agenda's Markdown.

    Tavily's Markdown for this page has come in three shapes (one table row
    per session; a multi-line block per session; a time row then a talk row),
    so this reads what they share: each talk is a link to its page, its
    material runs from that link to the next time slot, talk or day, and its
    time and day are the nearest ones before it.
    """
    days = [(m.start(), _day(m.group(1), m.group(2), year_hint)) for m in DAY_RE.finditer(md)]
    days = [(pos, d) for pos, d in days if d]
    times = []
    for m in TIME_RE.finditer(md):
        a, b, tz = (m.group(1), m.group(2), m.group(3)) if m.group(1) else (m.group(4), m.group(5), m.group(6))
        tail = md[m.end():md.find("\n", m.end()) if "\n" in md[m.end():] else len(md)]
        room = re.split(r"\||#####", tail.strip(" |"))[0].strip()
        times.append((m.start(), f"{a} - {b} {tz}", room))
    links = list(TALK_RE.finditer(md))
    stops = sorted([p for p, _ in days] + [p for p, _, _ in times] + [m.start() for m in links] + [len(md)])

    best: dict[str, dict] = {}
    for m in links:
        title, page = _unescape(m.group(1)), m.group(2) if m.group(2).endswith("/") else m.group(2) + "/"
        block = md[m.end():next(p for p in stops if p > m.start())]
        parts = SECTION_RE.split(block)
        head, sections = parts[0], {}
        for label, body in zip(parts[1::2], parts[2::2]):
            sections.setdefault(label.lower().replace("full ", ""), body)
        if sections:   # sessions with labelled sections: the head is the presenters
            presenters = _clean(head)
            abstract = _clean(sections.get("abstract", ""))
        else:          # a talk row: member links are the presenters, the rest is the abstract
            presenters = ", ".join(_unescape(x) for x in MEMBER_RE.findall(head))
            abstract = _clean(MEMBER_RE.sub("", head))
        recording = YOUTUBE_RE.search(sections.get("recordings", block))
        files = [u for _, u in MD_LINK.findall(sections.get("files", block)) if FILE_RE.search(u)]
        day = next((d for pos, d in reversed(days) if pos < m.start()), None)
        slot = next(((t, r) for pos, t, r in reversed(times) if pos < m.start()), ("", ""))
        talk = {
            "title": title,
            "page": page,
            "presenters": presenters,
            "when": ", ".join(x for x in (f"{day:%A}, {day:%B} {day.day}, {day.year}" if day else "", slot[0]) if x),
            "where": _unescape(slot[1]),
            "video": recording.group(0) if recording else "",
            "slides": files[0] if files else "",
            "abstract": abstract,
        }
        if LOGISTICS.search(title) or not (abstract or talk["video"] or talk["slides"]):
            continue
        # The page lists the program more than once; keep the richest copy.
        score = lambda t: (bool(t["video"]) + bool(t["slides"]), len(t["abstract"]))
        if page not in best or score(talk) > score(best[page]):
            best[page] = talk
    order = {m.group(2) if m.group(2).endswith("/") else m.group(2) + "/": i for i, m in reversed(list(enumerate(links)))}
    talks = sorted(best.values(), key=lambda t: order[t["page"]])   # agenda order
    return talks, sorted({d for _, d in days})


def program_text(talks: list[dict]) -> str:
    lines: list[str] = []
    day = None
    for t in talks:
        d = t["when"].split(",")[0] if "," in t["when"] else ""
        if d != day:
            day = d
            lines += [f"## {t['when'].rsplit(',', 1)[0]}" if d else "## Sessions", ""]
        lines.append(f"### {t['title']}")
        if t["presenters"]:
            lines.append(f"Speakers: {t['presenters']}")
        lines.append(f"Session: {t['when']}" + (f", {t['where']}" if t["where"] else ""))
        links = [f"page: {t['page']}"]
        if t["slides"]:
            links.append(f"slides: {t['slides']}")
        if t["video"]:
            links.append(f"video: {t['video']}")
        lines.append(" | ".join(links))
        if t["abstract"]:
            lines.append(t["abstract"])
        lines.append("")
    return "\n".join(lines)


class NanogFetcher(Fetcher):
    name = "nanog"
    # The agenda's day headers state the meeting's dates, so a probe that finds
    # them proves the edition and spares discovery a full fetch (talk pages).
    probe_is_sufficient = True

    def _read(self, entry: dict) -> tuple[Optional[str], str]:
        key = os.environ.get("TAVILY_API_KEY", "").strip()
        if not key:
            return None, "nanog.org blocks automated clients; set TAVILY_API_KEY to read the agenda through Tavily Extract"
        try:
            md = tavily_extract(entry["program_url"], key)
        except Exception as e:
            return None, f"Tavily Extract failed: {e}"
        return md, ""

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        md, err = self._read(entry)
        if md is None:
            return self.manual(entry, err)
        end = entry.get("end_date")
        year = end.year if hasattr(end, "year") else (int(str(end)[:4]) if end else None)
        talks, days = parse_agenda(md, year)
        if not talks:
            return FetchResult(status=NOT_PUBLISHED, source_url=url,
                               detail="agenda read, but no talks with an abstract, recording or slides yet")
        # From NANOG 97 the agenda carries no slides or recordings; each talk's
        # page does. Read the pages of talks still missing either, 20 per call.
        missing = [t for t in talks if not (t["slides"] and t["video"])][:100]
        if missing:
            pages = tavily_extract_many([t["page"] for t in missing], os.environ["TAVILY_API_KEY"].strip())
            for t in missing:
                for k, v in talk_media(pages.get(t["page"], "")).items():
                    t[k] = t[k] or v
        with_video = sum(bool(t["video"]) for t in talks)
        with_slides = sum(bool(t["slides"]) for t in talks)
        return FetchResult(
            status=OK,
            program_text=program_text(talks),
            source_url=url,
            item_count=len(talks),
            detail=f"{len(talks)} talks over {len(days)} days; {with_video} recordings, {with_slides} slide decks",
            meta={"end_date": max(days).isoformat() if days else ""},
        )

    def probe(self, entry: dict, years: Optional[Iterable[int]] = None) -> ProbeResult:
        """The agenda's day headers give the meeting's dates; no headers, no meeting yet."""
        url = entry["program_url"]
        md, err = self._read(entry)
        if md is None:
            return ProbeResult(False, err, source_url=url)
        _, days = parse_agenda(md, None)
        if not days:
            return ProbeResult(False, "no agenda days published yet", source_url=url)
        return ProbeResult(True, f"agenda published, ends {max(days)}", end_date=max(days), source_url=url)
