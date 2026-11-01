"""RIPE Meetings, from RIPE 91's public meeting-plan and talk pages onward.

Session cards truncate abstracts; follow each talk for the full text, slides
and native MP4 recording. No bot blocking observed; never use extraction services.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, looks_blocked, scan_end_date, OK, NOT_PUBLISHED

_SESSION = re.compile(r"^/programme/meeting-plan/sessions/\d+/$")
_SKIP = re.compile(
    r"\b(?:opening|closing) remarks\b|administrative matters|agenda bashing|"
    r"^(?:welcome|closure|introduction|newcomer's introduction|a\.?o\.?b\.?[, ]*(?:open mic)?|"
    r"open mic|open session|thanks, wrap up and rate the talks)$", re.I,
)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def talk_links(soup: BeautifulSoup, url: str) -> dict[str, str]:
    """Materials only from a single talk, not the session or shared program."""
    article = soup.select_one("article.block-talk")
    if article is None:
        return {}
    found: dict[str, str] = {}
    for a in article.select(".talk-resources a[href]"):
        href = urljoin(url, a["href"])
        if urlparse(href).path.lower().endswith((".pdf", ".pptx", ".ppt", ".odp", ".key")):
            if href not in found.values():
                found.setdefault("slides" if "slides" not in found else "slides2", href)
    video = article.select_one("video source[src]")
    if video:
        found["video"] = urljoin(url, video["src"])
    return found


def _get(url: str):
    resp = http_get(url)
    if resp.status_code != 200 or looks_blocked(resp):
        raise RuntimeError(f"blocked or unexpected status {resp.status_code}: {url}")
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


class RipeFetcher(Fetcher):
    name = "ripe"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
            if resp.status_code == 404:
                return FetchResult(status=NOT_PUBLISHED, source_url=url, detail="program not posted yet")
            if resp.status_code != 200 or looks_blocked(resp):
                return self.manual(entry, f"blocked or unexpected status {resp.status_code}")
            resp.encoding = "utf-8"
            soup = BeautifulSoup(resp.text, "html.parser")
            sessions = dict.fromkeys(urljoin(url, a["href"]) for a in soup.select("main a[href]")
                                     if _SESSION.fullmatch(urlparse(a["href"]).path))
            lines: list[str] = []
            seen: set[str] = set()
            for session_url in sessions:
                session = _get(session_url)
                heading = session.select_one("main h1")
                if heading:
                    lines.append(f"## {clean(heading.get_text(' '))}\n")
                for card in session.select("main .talk"):
                    title_node = card.select_one("a.talk-title[href]")
                    if title_node is None:
                        continue
                    title = clean(title_node.get_text(" "))
                    page = urljoin(session_url, title_node["href"])
                    if not title or page in seen or _SKIP.search(title):
                        continue
                    seen.add(page)
                    speaker = card.select_one(".talk-speaker")
                    speakers = clean(speaker.get_text(" ")) if speaker else ""
                    excerpt = card.select_one(".talk-abstract")
                    abstract = clean(excerpt.get_text(" ")) if excerpt else ""
                    links = {"page": page}
                    try:
                        detail = _get(page)
                        article = detail.select_one("article.block-talk")
                        if article is None:
                            raise ValueError("no talk detail")
                        abstract_heading = article.find("h2", string="Abstract")
                        abstract_node = abstract_heading.find_next_sibling("div") if abstract_heading else None
                        abstract = clean(abstract_node.get_text(" ")) if abstract_node else ""
                        links.update(talk_links(detail, page))
                    except Exception:
                        abstract += "\nFull talk page unavailable; session excerpt only."
                    lines.append(f"### {title}")
                    if speakers:
                        lines.append(f"Speakers: {speakers}")
                    lines.append(" | ".join(f"{'slides' if k == 'slides2' else k}: {v}" for k, v in links.items()))
                    lines.append(abstract or "No abstract published; title and materials only.")
                    lines.append("")
            count = len(seen)
        except Exception as e:
            return self.manual(entry, f"fetch/parse error: {e}")
        return FetchResult(status=OK if count else NOT_PUBLISHED, program_text="\n".join(lines),
                           source_url=url, item_count=count, detail=f"parsed {count} talks")

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            soup = _get(url)
            date_node = soup.select_one(".date")
            end = scan_end_date(date_node.get_text(" ") if date_node else "", years)
            return ProbeResult(True, "meeting-plan date banner", end_date=end, source_url=url)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
