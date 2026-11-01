"""Links for every pick in a digest: abstract page, paper, slides, recording.

A digest pick is only useful if the reader can get to the material fast. This
module gives each `### pick` one row, built by code from verified sources:

    **Links:** [Abstract](…) · [Paper](…) · [Slides](…) · [Recording](…)

Where each link comes from, in order:

1. The program item's link line (`page:`, `pdf:`, `slides:`, `video:`,
   `materials:`), written by the fetcher from the conference's own pages.
2. The item's `page:` (the talk or paper page), fetched again now: USENIX,
   Sched and netdev pages gain slides and an embedded recording after the event.
3. For a pick still without a recording: a YouTube search, falling back to
   Tavily search when YouTube cannot be reached (TAVILY_API_KEY). A candidate
   is linked only after `verify()` accepts it: the talk's title is in the
   video's title or description, the conference or its channel is named, and
   the upload date falls in the window after the event. Otherwise no link —
   the same "zero rather than wrong" rule the fetchers follow.

Links found earlier are kept when a later run cannot reach a source, so a
refresh only ever adds. The model never writes these rows; `enrich()` removes
any `**Links:**` line it finds in a pick and puts its own in its place.
"""

from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import Optional
from urllib.parse import parse_qs, quote, urlparse

import requests
from bs4 import BeautifulSoup

from conferences.fetchers.base import BROWSER_HEADERS, looks_blocked

KEYS = ("page", "pdf", "slides", "video", "materials")
# A URL runs to the end of its " | " part: some file names contain spaces.
LINK_LINE = re.compile(r"^(page|pdf|slides|video|materials):\s*(https?://.+?)\s*$")
SEPARATOR = re.compile(r"^=+ *PROGRAM TEXT *=+$", re.M)
ROW = re.compile(r"^\s*(?:[-*]\s+)?\*\*Links?:?\*\*:?\s*(.*)$")
MD_LINK = re.compile(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)")
YT_HEADERS = {**BROWSER_HEADERS, "Accept-Language": "en", "Cookie": "CONSENT=YES+1"}

# Words that name a conference in a video's title, description or channel,
# keyed by the first segment of the registry key.
CHANNELS = {
    "kubecon": ("cncf", "cloud native computing foundation"),
    "nsdi": ("usenix",),
    "srecon": ("usenix",),
    "usenix": ("usenix",),
    "sigcomm": ("acm sigcomm", "sigcomm"),
    "netdev": ("netdev",),
}
DISPLAY = {"kubecon": "KubeCon", "nsdi": "NSDI", "sigcomm": "SIGCOMM", "srecon": "SREcon",
           "usenix": "USENIX", "netdev": "netdev", "ietf": "IETF"}
STOP = {"the", "and", "for", "with", "from", "into", "over", "using", "via", "its", "our", "your",
        "of", "to", "in", "on", "a", "an", "at", "by", "is", "are", "how", "what", "why"}


@dataclass
class Item:
    title: str
    text: str
    links: dict[str, str] = field(default_factory=dict)


@dataclass
class Context:
    """What a recording must match: the conference and when it ended."""

    key: str
    end_date: Optional[date] = None
    search: bool = True
    fetch_pages: bool = True
    tavily_key: str = ""
    delay: float = 0.4

    @property
    def marker(self) -> str:
        return self.key.split("-")[0]

    @property
    def query_term(self) -> str:
        return DISPLAY.get(self.marker, self.marker)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def words(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2}


# ------------------------------------------------------------------ program --

def program_items(prompt: str) -> list[Item]:
    """Items (### headings) of a prompt's PROGRAM TEXT, with their link lines."""
    m = SEPARATOR.search(prompt)
    program = prompt[m.end():] if m else prompt
    items: list[Item] = []
    for block in re.split(r"^(?=### )", program, flags=re.M):
        if not block.startswith("### "):
            continue
        title, _, text = block.partition("\n")
        item = Item(title[4:].strip(), text)
        for line in text.splitlines():
            for part in line.split(" | "):
                lm = LINK_LINE.match(part.strip())
                if lm and lm.group(1) not in item.links:
                    item.links[lm.group(1)] = lm.group(2)
        items.append(item)
    return items


def match_item(heading: str, items: list[Item]) -> Optional[Item]:
    """The program item a pick heading names (the longest title that fits)."""
    n = norm(MD_LINK.sub(r"\1", heading))
    best = None
    for item in items:
        t = norm(item.title)
        if len(t) >= 8 and (t in n or (len(n) >= 12 and n in t)):
            if best is None or len(t) > len(norm(best.title)):
                best = item
    return best


# --------------------------------------------------------------- talk pages --

def _session() -> requests.Session:
    s = requests.Session()
    s.headers.update(BROWSER_HEADERS)
    return s


HTTP = _session()


def youtube_id(url: str) -> Optional[str]:
    try:
        u = urlparse(url)
    except ValueError:
        return None
    host = (u.hostname or "").removeprefix("www.").removeprefix("m.")
    if host == "youtu.be":
        vid = u.path.strip("/").split("/")[0]
    elif host in ("youtube.com", "youtube-nocookie.com"):
        if u.path == "/watch":
            vid = (parse_qs(u.query).get("v") or [""])[0]
        else:
            m = re.match(r"/(?:embed|live|shorts|v)/([^/?#]+)", u.path)
            vid = m.group(1) if m else ""
    else:
        return None
    return vid if re.fullmatch(r"[A-Za-z0-9_-]{11}", vid or "") else None


def classify(found: dict[str, str], href: str, text: str) -> None:
    """File a PDF link as slides or paper."""
    if not href.startswith("https://"):
        return
    label = f"{text} {href}".lower()
    if not (href.lower().split("?")[0].endswith(".pdf") or "static.sched.com/hosted_files/" in href):
        return
    if "slide" in label or "static.sched.com/hosted_files/" in href:
        found.setdefault("slides", href)
    elif "paper" in label or "/system/files/" in href:
        found.setdefault("pdf", href)


def scrape_page(url: str, tavily_key: str = "") -> dict[str, str]:
    """Slides, paper and recording links on a talk's own page.

    A page that blocks this runner (USENIX blocks datacenter IPs) is read
    through Tavily Extract instead, when a key is set.
    """
    try:
        resp = HTTP.get(url, timeout=20)
        ok = resp.status_code == 200 and not looks_blocked(resp) and "html" in resp.headers.get("content-type", "")
    except Exception:
        ok = False
    if not ok:
        return tavily_page(url, tavily_key) if tavily_key else {}
    soup = BeautifulSoup(resp.text, "html.parser")
    found: dict[str, str] = {}
    embeds = [youtube_id(f.get("src", "")) for f in soup.find_all("iframe")]
    embeds = [v for v in embeds if v]
    linked = {v for a in soup.find_all("a", href=True) if (v := youtube_id(a["href"]))}
    # An embedded player is the talk; a lone watch link is too. Several watch
    # links are a channel's promo strip, not evidence.
    vid = embeds[0] if embeds else (next(iter(linked)) if len(linked) == 1 else None)
    if vid:
        found["video"] = f"https://www.youtube.com/watch?v={vid}"
    for a in soup.find_all("a", href=True):
        classify(found, requests.compat.urljoin(url, a["href"].strip()), a.get_text(" ", strip=True))
    return found


def tavily_page(url: str, key: str) -> dict[str, str]:
    try:
        resp = requests.post("https://api.tavily.com/extract", timeout=90,
                             headers={"Authorization": f"Bearer {key}"},
                             json={"urls": [url], "format": "markdown", "extract_depth": "advanced"})
        resp.raise_for_status()
        content = "".join(r.get("raw_content", "") for r in resp.json().get("results", []))
    except Exception:
        return {}
    found: dict[str, str] = {}
    for text, href in MD_LINK.findall(content):
        classify(found, href, text)
    for href in re.findall(r"https://[^\s)\]\"'<>]+", content):
        classify(found, href.rstrip(".,};"), "")
    vids = {v for href in re.findall(r"https://[^\s)\]\"'<>]+", content) if (v := youtube_id(href))}
    if len(vids) == 1:
        found["video"] = f"https://www.youtube.com/watch?v={vids.pop()}"
    return found


# ---------------------------------------------------------------- recordings --

@dataclass
class Video:
    id: str
    title: str
    author: str
    description: str = ""
    published: Optional[date] = None
    seconds: int = 0


def youtube_search(query: str) -> list[str]:
    """Video IDs from YouTube's public search page, in result order."""
    resp = HTTP.get("https://www.youtube.com/results", params={"search_query": query, "hl": "en"},
                    headers=YT_HEADERS, timeout=30)
    resp.raise_for_status()
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", resp.text)
    if not m:
        raise RuntimeError("YouTube search page without results data (consent or bot check)")
    ids: list[str] = []

    def walk(o) -> None:
        if isinstance(o, dict):
            v = o.get("videoRenderer")
            if isinstance(v, dict) and v.get("videoId") and v["videoId"] not in ids:
                ids.append(v["videoId"])
            for x in o.values():
                walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)

    walk(json.loads(m.group(1)))
    return ids


def tavily_search(query: str, key: str) -> list[str]:
    resp = requests.post("https://api.tavily.com/search", timeout=60,
                         headers={"Authorization": f"Bearer {key}"},
                         json={"query": query, "include_domains": ["youtube.com"], "max_results": 5})
    resp.raise_for_status()
    return [v for r in resp.json().get("results", []) if (v := youtube_id(r.get("url", "")))]


def youtube_video(vid: str) -> Optional[Video]:
    """Title, channel, description and upload date from the watch page; oEmbed as a fallback."""
    try:
        resp = HTTP.get(f"https://www.youtube.com/watch?v={vid}&hl=en", headers=YT_HEADERS, timeout=30)
        m = re.search(r"var ytInitialPlayerResponse = (\{.*?\});(?:var |</script>)", resp.text)
        if m:
            p = json.loads(m.group(1))
            vd = p.get("videoDetails") or {}
            mf = (p.get("microformat") or {}).get("playerMicroformatRenderer") or {}
            published = None
            for k in ("publishDate", "uploadDate"):
                if mf.get(k):
                    published = date.fromisoformat(mf[k][:10])
                    break
            if vd.get("title"):
                return Video(vid, vd["title"], vd.get("author", ""), vd.get("shortDescription", ""),
                             published, int(vd.get("lengthSeconds") or 0))
    except Exception:
        pass
    try:
        o = HTTP.get("https://www.youtube.com/oembed", timeout=20,
                     params={"format": "json", "url": f"https://www.youtube.com/watch?v={vid}"}).json()
        return Video(vid, o.get("title", ""), o.get("author_name", ""))
    except Exception:
        return None


def title_matches(talk: str, video: Video) -> bool:
    t = norm(talk)
    haystack = f"{video.title}\n{video.description[:600]}"
    if len(t) >= 12 and t in norm(haystack):
        return True
    # Titles cut with "..." ("Multi-Network Step-by-Step: ... Kubernetes... Speaker").
    for part in re.split(r"\.\.\.|…", video.title)[:1]:
        stem = norm(re.sub(r"^[^:|-]{0,40}['’]?\d{2}\s*[-:|]\s*", "", part))
        if len(stem) >= 25 and stem in t:
            return True
    # Word overlap, for retitled uploads; most words must be in the video's own
    # title, so a description that merely mentions the talk is not enough.
    want = words(talk)
    return (len(want) >= 4 and len(want & words(haystack)) / len(want) >= 0.85
            and len(want & words(video.title)) / len(want) >= 0.6)


def event_matches(video: Video, ctx: Context) -> bool:
    names = (ctx.marker, *CHANNELS.get(ctx.marker, ()))
    text = f"{video.title}\n{video.description[:600]}".lower()
    named = any(n in text for n in names) or any(n in video.author.lower() for n in names)
    if not named:
        return False
    if video.published is None:
        # oEmbed only (no date): accept only a title that names the conference
        # and the edition's year ("NSDI '25 - …", "SIGCOMM'25: …").
        year = ctx.end_date.year if ctx.end_date else None
        return bool(year) and ctx.marker in video.title.lower() and bool(
            re.search(rf"(?:'|’|\b|{ctx.marker}){str(year)[2:]}\b|\b{year}\b", video.title.lower()))
    if ctx.end_date is None:
        return True
    return ctx.end_date - timedelta(days=14) <= video.published <= ctx.end_date + timedelta(days=240)


def verify(talk: str, video: Video, ctx: Context) -> bool:
    if video.seconds and video.seconds < 90:
        return False
    return title_matches(talk, video) and event_matches(video, ctx)


def find_recording(talk: str, ctx: Context) -> Optional[str]:
    query = f"{talk} {ctx.query_term}"
    try:
        ids = youtube_search(query)[:6]
    except Exception:
        ids = []
        if ctx.tavily_key:
            try:
                ids = tavily_search(query, ctx.tavily_key)
            except Exception:
                return None
    accepted: list[Video] = []
    for vid in ids:
        time.sleep(ctx.delay)
        v = youtube_video(vid)
        if v and verify(talk, v, ctx):
            accepted.append(v)
            if v.published is None or ctx.end_date is None:
                break
    if not accepted:
        return None
    # A talk given at two editions: take the upload closest after this one.
    best = min(accepted, key=lambda v: abs((v.published - ctx.end_date).days) if v.published and ctx.end_date else 0)
    return f"https://www.youtube.com/watch?v={best.id}"


# --------------------------------------------------------------------- rows --

def label(kind: str, url: str, links: dict[str, str]) -> str:
    if kind == "page":
        return "Draft" if "datatracker.ietf.org/doc/" in url else "Abstract"
    if kind == "video":
        return "Session recording" if "materials" in links else "Recording"
    return {"pdf": "Paper", "slides": "Slides", "materials": "Materials"}[kind]


def safe_url(url: str) -> str:
    """Spaces and parentheses would end a Markdown link early."""
    return quote(url.strip(), safe=":/?#[]@!$&'*+,;=%~")


def tidy(links: dict[str, str]) -> dict[str, str]:
    """A `pdf:` that is really the slides is shown once, as Slides."""
    links = {k: safe_url(v) for k, v in links.items() if v}
    if links.get("pdf") and re.search(r"slide", links["pdf"], re.I):
        links.setdefault("slides", links["pdf"])
        if links["slides"] == links["pdf"]:
            del links["pdf"]
    seen: set[str] = set()
    for k in KEYS:
        if k in links:
            if links[k] in seen:
                del links[k]
            else:
                seen.add(links[k])
    return links


def links_row(links: dict[str, str]) -> str:
    links = tidy(links)
    parts = [f"[{label(k, links[k], links)}]({links[k]})" for k in KEYS if links.get(k)]
    return f"**Links:** {' · '.join(parts)}" if parts else ""


def parse_row(rest: str) -> dict[str, str]:
    """Links from an existing row: this module's labels, or a writer's own words."""
    out: dict[str, str] = {}
    # Markdown links, and the bare "pdf https://… · video https://…" form.
    pairs = MD_LINK.findall(rest) + re.findall(r"(?:^|·|,|\|)\s*([A-Za-z][\w ]{0,20}?)[:\s]\s*(https?://[^\s·,|)]+)",
                                               MD_LINK.sub("", rest))
    for text, url in pairs:
        t = text.lower()
        kind = ("video" if any(w in t for w in ("recording", "video")) else
                "slides" if "slide" in t else
                "materials" if "material" in t else
                "pdf" if any(w in t for w in ("paper", "pdf")) else
                "page" if any(w in t for w in ("abstract", "draft", "session", "page", "talk")) else None)
        if kind and kind not in out:
            out[kind] = url
    return out


def enrich(markdown: str, prompt: str, ctx: Context, log=print) -> tuple[str, dict]:
    """Put a verified links row under every `###` pick; returns (markdown, stats)."""
    items = program_items(prompt)
    lines = markdown.split("\n")
    heads = []
    fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and line.startswith("### "):
            heads.append(i)
    stats = {"picks": len(heads), "matched": 0, "page": 0, "pdf": 0, "slides": 0, "video": 0,
             "video_from_page": 0, "video_from_search": 0, "unmatched": [], "added": []}
    out: list[str] = []
    cursor = 0
    for n, h in enumerate(heads):
        end = next((j for j in range(h + 1, len(lines)) if re.match(r"^#{1,3} ", lines[j])), len(lines))
        end = min(end, heads[n + 1]) if n + 1 < len(heads) else end
        out.extend(lines[cursor:h + 1])
        heading = lines[h][4:].strip()
        block = lines[h + 1:end]
        existing: dict[str, str] = {}
        kept: list[str] = []
        for line in block:
            m = ROW.match(line)
            if m:
                existing.update({k: v for k, v in parse_row(m.group(1)).items() if k not in existing})
            else:
                kept.append(line)

        item = match_item(heading, items)
        # The program's links win; links found by an earlier run fill the gaps.
        links = dict(item.links) if item else {}
        for k, v in existing.items():
            links.setdefault(k, v)
        if item:
            stats["matched"] += 1
            if ctx.fetch_pages and links.get("page") and not (links.get("video") and links.get("slides")):
                time.sleep(ctx.delay)
                for k, v in scrape_page(links["page"], ctx.tavily_key).items():
                    if not links.get(k):
                        links[k] = v
                        if k == "video":
                            stats["video_from_page"] += 1
        else:
            stats["unmatched"].append(heading[:120])
        if ctx.search and not links.get("video") and ctx.marker != "ietf":
            title = item.title if item else re.split(r"\s+[—–]\s+", MD_LINK.sub(r"\1", heading))[0]
            found = find_recording(title, ctx)
            if found:
                links["video"] = found
                stats["video_from_search"] += 1
                log(f"  recording found for {title[:70]!r}: {found}")
        links = tidy(links)
        for k in ("page", "pdf", "slides", "video"):
            stats[k] += bool(links.get(k))
        before = tidy(existing)
        new = [label(k, links[k], links) for k in KEYS if links.get(k) and before.get(k) != links[k]]
        if new:
            stats["added"].append({"pick": re.split(r"\s+[—–]\s+", heading)[0][:120], "links": new})

        row = links_row(links)
        while kept and not kept[0].strip():
            kept.pop(0)
        out.extend([""] + ([row, ""] if row else []) + kept)
        cursor = end
    out.extend(lines[cursor:])
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return text, stats


def context_for(entry: dict, **kw) -> Context:
    end = entry.get("end_date")
    if isinstance(end, datetime):
        end = end.date()
    elif isinstance(end, str):
        end = date.fromisoformat(end)
    return Context(key=entry["key"], end_date=end, tavily_key=os.environ.get("TAVILY_API_KEY", ""), **kw)
