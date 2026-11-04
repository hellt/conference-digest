"""MLSys fetcher: the conference's own virtual site.

mlsys.org runs a virtual-conference site per edition at
https://mlsys.org/virtual/<year>/ with every accepted paper on its own page
(and the invited talks under eventlistwithbios). The papers index lists every
title; each paper page carries the authors, the full abstract, an OpenReview
link (page/pdf) and a SlidesLive embed (video). The fetcher reads the index and
then each paper page, like netdev follows its session pages.

  index:  https://mlsys.org/virtual/<year>/papers.html?filter=titles
  paper:  https://mlsys.org/virtual/<year>/poster/<id>

The paper page's SlidesLive embed id maps straight to
https://slideslive.com/<id>, which the site shows as the Recording link.

Discovery: the conference page https://mlsys.org/Conferences/<year> states the
dates in a "May 18th - 22nd, 2026" form the base scanner can't parse, so
probe() reads them with its own regex (falling back to the base scan).
"""

from __future__ import annotations

import re
import time
from datetime import date
from typing import Iterable, Optional

from bs4 import BeautifulSoup

from .base import (
    Fetcher,
    FetchResult,
    ProbeResult,
    http_get,
    looks_blocked,
    scan_end_date,
    OK,
    NOT_PUBLISHED,
)

# "May 18th - 22nd, 2026" / "May 18-22 2026" — month, first day, last day, year.
_RANGE = re.compile(
    r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+"
    r"(\d{1,2})(?:st|nd|rd|th)?\s*[-–]\s*(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})",
    re.I,
)
_MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
# OpenReview forum link on a paper page; the pdf link is derived from it.
_OPENREVIEW = re.compile(r"https://openreview\.net/forum\?id=([\w-]+)")
# SlidesLive's embed element, id first.
_SLIDESLIVE = re.compile(r"presentation-embed-(\d+)")


# The virtual site's show-more/less UI text leaks into the abstract text.
_SHOW_MORE = re.compile(r"\s*Show (more|less)\s*$", re.I)


def _clean(text: str) -> str:
    return _SHOW_MORE.sub("", text).strip()


def edition_year(entry: dict) -> Optional[int]:
    """The edition's year from the key (`mlsys-2026`), else from end_date."""
    m = re.search(r"-(\d{4})$", str(entry.get("key", "")))
    if m:
        return int(m.group(1))
    d = entry.get("end_date")
    if isinstance(d, date):
        return d.year
    try:
        return date.fromisoformat(str(d)).year
    except (TypeError, ValueError):
        return None


class MlsysFetcher(Fetcher):
    name = "mlsys"

    def fetch(self, entry: dict) -> FetchResult:
        year = edition_year(entry)
        if year is None:
            return self.manual(entry, "cannot tell the edition year from key or end_date")
        base = f"https://mlsys.org/virtual/{year}"
        try:
            resp = http_get(f"{base}/papers.html?filter=titles")
        except Exception as e:
            return self.manual(entry, f"request error: {e}")
        if looks_blocked(resp):
            return self.manual(entry, f"blocked ({resp.status_code}); paste the program by hand")
        if resp.status_code == 404:
            return FetchResult(status=NOT_PUBLISHED, detail=f"no virtual site for {year} yet",
                               source_url=entry["program_url"])
        if resp.status_code != 200:
            return self.manual(entry, f"unexpected status {resp.status_code}")

        soup = BeautifulSoup(resp.text, "html.parser")
        papers = []
        poster = re.compile(rf"/virtual/{year}/poster/\d+")
        for a in soup.select("a[href]"):
            href, title = a.get("href", ""), a.get_text(" ", strip=True)
            if poster.fullmatch(href) and title and (href, title) not in papers:
                papers.append((href, title))
        if not papers:
            return FetchResult(status=NOT_PUBLISHED,
                               detail="papers page reachable but no papers listed yet",
                               source_url=entry["program_url"])

        invited, invited_count = self._invited(base)

        lines = ["## Papers", ""]
        fetched = 0
        for href, title in papers:
            page = f"https://mlsys.org{href}" if href.startswith("/") else href
            detail = self._paper_page(page)
            lines.append(f"### {title}")
            if detail.get("authors"):
                lines.append(f"Authors: {detail['authors']}")
            links = []
            if detail.get("openreview"):
                links.append(f"page: {detail['openreview']}")
                links.append(f"pdf: https://openreview.net/pdf?id={detail['openreview_id']}")
            else:
                links.append(f"page: {page}")   # the virtual-site paper page as the abstract link
            if detail.get("video"):
                links.append(f"video: {detail['video']}")
            if links:
                lines.append(" | ".join(links))
            if detail.get("abstract"):
                lines.append(detail["abstract"])
            lines.append("")
            fetched += 1
            time.sleep(0.1)   # a listing plus ~170 paper pages in one run: be polite

        if invited:
            lines = ["## Invited talks", "", *invited, "", *lines]

        return FetchResult(
            status=OK,
            program_text="\n".join(lines),
            source_url=entry["program_url"],
            item_count=fetched + invited_count,
            detail=f"parsed {fetched} papers plus {invited_count} invited talks",
        )

    def _paper_page(self, url: str) -> dict:
        """Authors, abstract, OpenReview link and SlidesLive video of one paper."""
        try:
            resp = http_get(url)
            if resp.status_code != 200:
                return {}
            soup = BeautifulSoup(resp.text, "html.parser")
            out: dict = {}
            org = soup.select_one(".event-organizers")
            if org:
                out["authors"] = ", ".join(
                    p.strip() for p in org.get_text(" ", strip=True).split("⋅") if p.strip()
                )
            abstract = soup.select_one(".abstract-content")
            if abstract:
                out["abstract"] = _clean(abstract.get_text(" ", strip=True))
            forum = _OPENREVIEW.search(resp.text)
            if forum:
                out["openreview"] = forum.group(0)
                out["openreview_id"] = forum.group(1)
            slideslive = _SLIDESLIVE.search(resp.text)
            if slideslive:
                out["video"] = f"https://slideslive.com/{slideslive.group(1)}"
            return out
        except Exception:
            return {}   # a paper page that fails costs that paper its extras, not the run

    def _invited(self, base: str) -> tuple[list[str], int]:
        """The invited talks as program-text lines, fetched before the paper
        pages so the burst of paper requests can't starve them."""
        try:
            resp = http_get(f"{base}/eventlistwithbios/Invited%20Talk")
            if resp.status_code != 200:
                return [], 0
            soup = BeautifulSoup(resp.text, "html.parser")
            urls = []
            for a in soup.select(f'a[href*="/virtual/"]:not([href*="papers"])'):
                href = a.get("href", "")
                if "/invited-talk/" in href and href not in urls:
                    urls.append(href)
        except Exception:
            return [], 0
        lines: list[str] = []
        for href in urls:
            try:
                resp = http_get(f"https://mlsys.org{href}" if href.startswith("/") else href)
                if resp.status_code != 200:
                    continue
                soup = BeautifulSoup(resp.text, "html.parser")
                title = soup.select_one(".event-title")
                speaker = soup.select_one(".event-organizers")
                abstract = soup.select_one(".abstract-content")
                if not title or not speaker or not abstract:
                    continue
                lines.append(f"### {title.get_text(' ', strip=True)}")
                lines.append(f"Speakers: {speaker.get_text(' ', strip=True)}")
                lines.append(f"page: https://mlsys.org{href}")
                lines.append(_clean(abstract.get_text(" ", strip=True)))
                lines.append("")
            except Exception:
                continue
        return lines, sum(1 for l in lines if l.startswith("### "))

    def probe(self, entry: dict, years: Optional[Iterable[int]] = None) -> ProbeResult:
        """The conference page states the dates as 'May 18th - 22nd, 2026'."""
        year = edition_year(entry)
        url = f"https://mlsys.org/Conferences/{year}" if year else entry["program_url"]
        try:
            resp = http_get(url)
        except Exception as e:
            return ProbeResult(False, f"request error: {e}", source_url=url)
        if resp.status_code == 404:
            return ProbeResult(False, "404 (no such edition yet)", source_url=url)
        if looks_blocked(resp) or resp.status_code != 200:
            return ProbeResult(False, f"blocked / status {resp.status_code}", source_url=url)

        end: Optional[date] = None
        m = _RANGE.search(resp.text)
        if m:
            month = _MONTHS.get(m.group(1).lower()[:3])
            if month and int(m.group(4)) == year:
                try:
                    end = date(int(m.group(4)), month, int(m.group(3)))
                except ValueError:
                    pass
        if end is None:
            end = scan_end_date(resp.text, [year] if year else years)
        return ProbeResult(
            True,
            f"200; {'dates ' + str(end) if end else 'dates not found on page'}",
            end_date=end,
            source_url=url,
        )
