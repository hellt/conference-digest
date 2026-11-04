"""Links for every pick in a digest: abstract page, paper, slides, recording.

A digest pick is only useful if the reader can get to the material fast. This
module gives each `### pick` one row, built by code from verified sources:

    **Links:** [Abstract](…) · [Paper](…) · [Slides](…) · [Recording](…)

Where each link comes from, in order:

1. The program item's link line (`page:`, `pdf:`, `slides:`, `video:`,
   `materials:`), written by the fetcher from the conference's own pages.
2. The item's `page:` (the talk or paper page), fetched again now: USENIX,
   Sched and netdev pages gain slides and an embedded recording after the event.
3. For a pick still without a recording: the conference's own YouTube
   channel when one is known (UPLOAD_CHANNELS), then a general YouTube
   search, falling back to Tavily search when YouTube cannot be reached
   (TAVILY_API_KEY). A candidate is linked only after `verify()` accepts it:
   the talk's title is in the video's title or description, the conference or
   its channel is named, and the upload date falls in the window after the
   event — on the conference's own channel a title shortened to its start is
   enough (`channel_verify`). Otherwise no link — the same "zero rather than
   wrong" rule the fetchers follow.

Links found earlier are kept when a later run cannot reach a source, so a
refresh only ever adds. Every file and video link is also probed before its
row goes out (`link_alive`: direct request, Tavily Extract as the second
opinion for a source that blocks the runner) and one confirmed dead is
dropped instead of published. The model never writes these rows; `enrich()`
removes any `**Links:**` line it finds in a pick and puts its own in its place.
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
from conferences.fetchers.ovscon import talk_links as ovscon_talk_links
from conferences.fetchers.ripe import talk_links as ripe_talk_links

# slides2 holds a second format of the deck (PDF and PPTX both shown).
KEYS = ("page", "pdf", "slides", "slides2", "video", "materials")
# A URL runs to the end of its " | " part: some file names contain spaces.
LINK_LINE = re.compile(r"^(page|pdf|slides|video|materials):\s*(https?://.+?)\s*$")
SEPARATOR = re.compile(r"^=+ *PROGRAM TEXT *=+$", re.M)
ROW = re.compile(r"^\s*(?:[-*]\s+)?\*\*Links?:?\*\*:?\s*(.*)$")
MD_LINK = re.compile(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)")
# SOCS=CAI is YouTube's "reject all" cookie choice; playlist pages show the
# consent screen without it.
YT_HEADERS = {**BROWSER_HEADERS, "Accept-Language": "en", "Cookie": "CONSENT=YES+1; SOCS=CAI"}

# Words that name a conference in a video's title, description or channel,
# keyed by the first segment of the registry key.
CHANNELS = {
    "kubecon": ("cncf", "cloud native computing foundation"),
    "nsdi": ("usenix",),
    "srecon": ("usenix",),
    "usenix": ("usenix",),
    "sigcomm": ("acm sigcomm", "sigcomm"),
    "netdev": ("netdev",),
    "nanog": ("nanog",),
    "autocon": ("autocon", "network automation forum"),
    "ovscon": ("openvswitch", "open vswitch", "ovs+ovncon", "ovscon"),
    "ciscolive": ("cisco live", "ciscolive"),
    "ripe": ("ripe", "ripe ncc"),
    "nlnog": ("nlnog",),
    "denog": ("denog",),
    "gtc": ("nvidia",),
    "ccs": ("acm ccs", "acm ccs 2026", "computer and communications security"),
    "imc": ("acm imc", "internet measurement conference", "imc"),
    "conext": ("conext", "acm conext"),
    "apricot": ("apricot", "apnic", "apnog"),
    "fosdem": ("fosdem",),
    "hacklu": ("hack.lu", "hacklu", "circl"),
    "tnc": ("geant", "géant", "tnc"),
    "arin": ("arin", "american registry for internet numbers"),
    "lacnic": ("lacnic", "lacnog"),
    "pets": ("pets", "popets", "privacy enhancing technologies"),
    "ausnog": ("ausnog",),
    "nznog": ("nznog",),
    "zanog": ("zanog", "iweek"),
    "peeringdays": ("peering days", "peeringdays", "nix.cz"),
    "moreip": ("more-ip", "ams-ix"),
    "swinog": ("swinog",),
    "capacity": ("capacity europe", "capacity media"),
    "nogfi": ("nog.fi", "nogfi"),
    "netuk": ("netuk",),
    "grnog": ("grnog",),
    "dknog": ("dknog",),
    "itnog": ("itnog",),
    "netnod": ("netnod",),
    "cfgmgmtcamp": ("cfgmgmtcamp", "config management camp"),
    "ocp": ("open compute project", "ocp global summit"),
    "mlsys": ("mlsys",),
    "pytorch": ("pytorch",),
}
DISPLAY = {"kubecon": "KubeCon", "nsdi": "NSDI", "sigcomm": "SIGCOMM", "srecon": "SREcon",
           "usenix": "USENIX", "netdev": "netdev", "ietf": "IETF", "nanog": "NANOG",
           "autocon": "AutoCon", "ovscon": "OVS OVN conference", "ciscolive": "Cisco Live",
           "ripe": "RIPE", "nlnog": "NLNOG", "denog": "DENOG", "gtc": "GTC", "ccs": "CCS", "imc": "IMC", "conext": "CoNEXT", "apricot": "APRICOT", "fosdem": "FOSDEM", "hacklu": "hack.lu", "tnc": "TNC GÉANT", "arin": "ARIN", "lacnic": "LACNIC", "pets": "PETS", "ausnog": "AusNOG", "nznog": "NZNOG", "zanog": "ZANOG", "peeringdays": "Peering Days", "moreip": "MORE-IP", "swinog": "SwiNOG", "capacity": "Capacity Europe", "nogfi": "nog.fi", "netuk": "NetUK", "grnog": "GRNOG", "dknog": "DKNOG", "itnog": "ITNOG", "netnod": "Netnod", "cfgmgmtcamp": "CfgMgmtCamp", "ocp": "OCP Global Summit",
           "mlsys": "MLSys", "pytorch": "PyTorch Conference"}
# YouTube channels that hold a conference's own recordings, keyed by the
# first segment of the registry key. Searched before the general YouTube
# search: uploads are often retitled or shortened when published, and the
# global results can bury them behind promo clips.
UPLOAD_CHANNELS = {
    "netnod": "@netnodix",
    "nznog": "@nznog3664",
    "zanog": "@nognetza",
}
# URLs that only ever hold presentation decks, whatever the link text says.
DECK_URLS = re.compile(
    r"static\.sched\.com/hosted_files/|storage\.googleapis\.com/site-media-prod/meetings/"
    r"|(?:pretalx\.com|cfp\.denog\.de)/media/denog\d+/submissions/"
)
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
                if not lm:
                    continue
                key = lm.group(1)
                if key == "slides" and "slides" in item.links:
                    key = "slides2"   # a second format of the deck
                item.links.setdefault(key, lm.group(2))
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
    """File a document link (PDF, or a PPTX/PPT/KEY/ODP deck) as slides or paper."""
    if not href.startswith("https://"):
        return
    label = f"{text} {href}".lower()
    path = href.lower().split("?")[0]
    deck = path.endswith((".pptx", ".ppt", ".key", ".odp")) or bool(DECK_URLS.search(href))
    if not (path.endswith(".pdf") or deck):
        return
    if deck or "slide" in label:
        if "slides" not in found:
            found["slides"] = href
        elif found["slides"] != href:
            found.setdefault("slides2", href)
    elif "paper" in label or "/system/files/" in href:
        found.setdefault("pdf", href)


def scrape_page(url: str, tavily_key: str = "") -> dict[str, str]:
    """Slides, paper and recording links on a talk's own page.

    A page that blocks this runner (USENIX blocks datacenter IPs) is read
    through Tavily Extract instead, when a key is set.
    """
    parsed = urlparse(url)
    host = parsed.hostname or ""
    if (host.removeprefix("www.") == "ciscolive.com"
            and parsed.path == "/on-demand/on-demand-library.html"):
        # #/session/... is client-side: HTML/extraction sees the shared catalog,
        # not this talk. Materials require login; never borrow promotional links.
        return {}
    ripe = re.fullmatch(r"ripe\d+\.ripe\.net", host) is not None
    operator_source = (ripe or host == "nlnog.net" or host.endswith(".denog.de")
                       or (host == "pretalx.com" and parsed.path.startswith("/denog")))
    ovscon = (host.removeprefix("www.") == "openvswitch.org"
              and re.fullmatch(r"/support/ovscon\d{4}/?", parsed.path) is not None)
    try:
        resp = HTTP.get(url, timeout=20)
        ok = resp.status_code == 200 and not looks_blocked(resp) and "html" in resp.headers.get("content-type", "")
    except Exception:
        ok = False
    if not ok:
        # Extraction of a shared program cannot safely be treated as one talk.
        return tavily_page(url, tavily_key) if tavily_key and not (ovscon or operator_source) else {}
    soup = BeautifulSoup(resp.text, "html.parser")
    if ovscon:
        return ovscon_talk_links(soup, url)
    if ripe:
        return ripe_talk_links(soup, url)
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


def _search_ids(html: str) -> list[str]:
    """Video IDs in a YouTube search page's results data, in result order."""
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html)
    if not m:
        raise RuntimeError("YouTube page without results data (consent or bot check)")
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


def youtube_search(query: str) -> list[str]:
    """Video IDs from YouTube's public search page, in result order."""
    resp = HTTP.get("https://www.youtube.com/results", params={"search_query": query, "hl": "en"},
                    headers=YT_HEADERS, timeout=30)
    resp.raise_for_status()
    return _search_ids(resp.text)


def youtube_channel_search(handle: str, query: str) -> list[str]:
    """Video IDs from a channel's own search box (`/@handle/search`)."""
    resp = HTTP.get(f"https://www.youtube.com/{handle}/search", params={"query": query, "hl": "en"},
                    headers=YT_HEADERS, timeout=30)
    resp.raise_for_status()
    return _search_ids(resp.text)


def _yt_initial_data(html: str):
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html)
    return json.loads(m.group(1)) if m else None


def _walk(o):
    if isinstance(o, dict):
        yield o
        for x in o.values():
            yield from _walk(x)
    elif isinstance(o, list):
        for x in o:
            yield from _walk(x)


def youtube_playlists(query: str) -> list[tuple[str, str, str]]:
    """(playlist id, title, channel) from YouTube's playlist search."""
    resp = HTTP.get("https://www.youtube.com/results", headers=YT_HEADERS, timeout=30,
                    params={"search_query": query, "sp": "EgIQAw==", "hl": "en"})
    data = _yt_initial_data(resp.text) or {}
    out = []
    for o in _walk(data):
        lv = o.get("lockupViewModel")
        if isinstance(lv, dict) and "PLAYLIST" in str(lv.get("contentType", "")):
            meta = (lv.get("metadata") or {}).get("lockupMetadataViewModel") or {}
            channel = re.search(r'"content": "([^"]+)"', json.dumps(meta.get("metadata", {})))
            out.append((lv.get("contentId", ""), (meta.get("title") or {}).get("content", ""),
                        channel.group(1) if channel else ""))
    return out


def youtube_playlist(playlist_id: str) -> list[tuple[str, str]]:
    """(video id, title) of a playlist's first 100 videos."""
    resp = HTTP.get("https://www.youtube.com/playlist", headers=YT_HEADERS, timeout=30,
                    params={"list": playlist_id, "hl": "en"})
    out: dict[str, str] = {}
    for o in _walk(_yt_initial_data(resp.text) or {}):
        lv = o.get("lockupViewModel")
        if isinstance(lv, dict) and "VIDEO" in str(lv.get("contentType", "")):
            meta = (lv.get("metadata") or {}).get("lockupMetadataViewModel") or {}
            out.setdefault(lv.get("contentId", ""), (meta.get("title") or {}).get("content", ""))
        v = o.get("playlistVideoRenderer")
        if isinstance(v, dict) and v.get("videoId"):
            out.setdefault(v["videoId"], "".join(x.get("text", "") for x in (v.get("title") or {}).get("runs", [])))
    return [(k, t) for k, t in out.items() if k]


def tavily_search(query: str, key: str) -> list[str]:
    resp = requests.post("https://api.tavily.com/search", timeout=60,
                         headers={"Authorization": f"Bearer {key}"},
                         json={"query": query, "include_domains": ["youtube.com"], "max_results": 5})
    resp.raise_for_status()
    return [v for r in resp.json().get("results", []) if (v := youtube_id(r.get("url", "")))]


def youtube_video(vid: str, retry: bool = True) -> Optional[Video]:
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
        # Player data withheld ("sign in to confirm you're not a bot", common
        # for datacenter IPs): the page's own data still states the title,
        # channel, upload date and description.
        page = _video_page_data(vid, resp.text)
        if page:
            return page
    except Exception:
        pass
    if retry:   # YouTube sometimes serves an empty page under load; ask once more
        time.sleep(2)
        return youtube_video(vid, retry=False)
    try:
        o = HTTP.get("https://www.youtube.com/oembed", timeout=20,
                     params={"format": "json", "url": f"https://www.youtube.com/watch?v={vid}"}).json()
        return Video(vid, o.get("title", ""), o.get("author_name", ""))
    except Exception:
        return None


def speaker_names(text: str) -> list[str]:
    """Full names from a speakers line: "Jane Doe - Org, John Roe · Role — Org & Ann Lee"."""
    names = []
    for part in re.split(r"\s*(?:,|&|;|\band\b)\s*", text or ""):
        name = re.split(r"\s+(?:·|[-–—]|\()\s*", part)[0].strip()
        if 2 <= len(name.split()) <= 4 and not re.search(r"\d", name):
            names.append(name)
    return names


def _video_page_data(vid: str, html: str) -> Optional[Video]:
    data = _yt_initial_data(html) or {}
    title = author = desc = ""
    published = None
    for o in _walk(data):
        if not title and isinstance(o.get("videoPrimaryInfoRenderer"), dict):
            title = "".join(r.get("text", "") for r in (o["videoPrimaryInfoRenderer"].get("title") or {}).get("runs", []))
        if not author and isinstance(o.get("videoOwnerRenderer"), dict):
            author = "".join(r.get("text", "") for r in (o["videoOwnerRenderer"].get("title") or {}).get("runs", []))
        if not desc and isinstance(o.get("attributedDescription"), dict):
            desc = o["attributedDescription"].get("content", "")
        if published is None and isinstance(o.get("dateText"), dict):
            m = re.search(r"([A-Z][a-z]{2})[a-z]* (\d{1,2}), (\d{4})", o["dateText"].get("simpleText", ""))
            if m:
                published = datetime.strptime(f"{m.group(1)} {m.group(2)} {m.group(3)}", "%b %d %Y").date()
    return Video(vid, title, author, desc, published) if title else None


def title_matches(talk: str, video: Video, speakers: tuple[str, ...] = ()) -> bool:
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
    if (len(want) >= 4 and len(want & words(haystack)) / len(want) >= 0.85
            and len(want & words(video.title)) / len(want) >= 0.6):
        return True
    # Retitled uploads ("Opening Keynote: Jeff Gray - Building a Business Case
    # for …"): a speaker's full name in the video title, plus half the words.
    named = any(len(norm(n)) >= 6 and norm(n) in norm(video.title) for n in speakers)
    if not named:
        return False
    # Uploads shortened to the start of the title: "Coding for infrastructure
    # is just coding - Antonio Balmaseda & …" for a much longer talk title.
    for part in re.split(r"\s+[-–—|]\s+|:\s+", video.title):
        core = norm(part)
        if len(core) >= 15 and t.startswith(core):
            return True
    return len(want) >= 2 and len(want & words(video.title)) / len(want) >= 0.5


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


# Session chrome around a title: a leading "Keynote speech: …" or "Panel
# discussion - …" label in the program, and a "… – Speaker, Company" tail on
# a channel upload.
TITLE_LABEL = re.compile(r"^[A-Za-z][A-Za-z &]{2,30}[:–—-]\s+")


def title_core(title: str) -> str:
    """The title without its session label and speaker tail."""
    return re.split(r"\s+[–—-]\s+", TITLE_LABEL.sub("", title), 1)[0]


def verify(talk: str, video: Video, ctx: Context, speakers: tuple[str, ...] = ()) -> bool:
    if video.seconds and video.seconds < 90:
        return False
    return title_matches(talk, video, speakers) and event_matches(video, ctx)


def channel_verify(talk: str, video: Video, ctx: Context, speakers: tuple[str, ...] = ()) -> bool:
    """The gate for a candidate from the conference's own channel.

    The channel and the upload window (`event_matches`) already anchor the
    event, so beyond the usual title match a title shortened to its start is
    enough: a channel titles an upload with the start of the talk plus the
    speaker, not the full program title.
    """
    if video.seconds and video.seconds < 90:
        return False
    if not event_matches(video, ctx):
        return False
    if title_matches(talk, video, speakers):
        return True
    core, want = norm(title_core(video.title)), norm(title_core(talk))
    return len(core) >= 12 and (want.startswith(core) or core.startswith(want))


def find_recording(talk: str, ctx: Context, speakers: tuple[str, ...] = ()) -> Optional[str]:
    video = find_video(talk, ctx, speakers)
    return f"https://www.youtube.com/watch?v={video.id}" if video else None


def find_video(talk: str, ctx: Context, speakers: tuple[str, ...] = ()) -> Optional[Video]:
    """The verified upload of a talk (title, channel, description, date), or None.

    When the conference has a channel of its own (UPLOAD_CHANNELS), its search
    box is tried first: the full title, then the title without a leading
    session label ("Keynote speech: …"), then the title's first words — an
    upload is often titled with only the start of a long talk. YouTube's
    general results vary besides: "title + conference" sometimes surfaces
    the conference's promo clips instead of the talk, so the bare title is
    tried next when nothing passed.
    """
    accepted: list[Video] = []
    seen: set[str] = set()

    def probe(ids: list[str], gate) -> None:
        for vid in ids:
            if vid in seen:
                continue
            seen.add(vid)
            time.sleep(ctx.delay)
            v = youtube_video(vid)
            if v and gate(talk, v, ctx, speakers):
                accepted.append(v)

    handle = UPLOAD_CHANNELS.get(ctx.marker)
    if handle:
        queries = [talk]
        for shorter in (TITLE_LABEL.sub("", talk), " ".join(talk.split()[:6])):
            if shorter and shorter not in queries:
                queries.append(shorter)
        for query in queries:
            try:
                probe(youtube_channel_search(handle, query)[:6], channel_verify)
            except Exception:
                pass
            if accepted:
                break
    for query in (f"{talk} {ctx.query_term}", talk):
        if accepted:
            break
        try:
            ids = youtube_search(query)[:6]
        except Exception:
            ids = []
            if ctx.tavily_key:
                try:
                    ids = tavily_search(query, ctx.tavily_key)
                except Exception:
                    ids = []
        probe(ids, verify)
    if not accepted:
        return None
    # A talk given at two editions: take the upload closest after this one.
    return min(accepted, key=lambda v: abs((v.published - ctx.end_date).days) if v.published and ctx.end_date else 0)


# ---------------------------------------------------------------- liveness --

def _oembed_alive(url: str) -> Optional[bool]:
    """A deleted or private video fails oEmbed; a live one answers with JSON."""
    try:
        r = HTTP.get("https://www.youtube.com/oembed", timeout=15,
                     params={"format": "json", "url": url})
    except Exception:
        return None
    if r.status_code == 200:
        return True
    return False if r.status_code in (400, 401, 404) else None


def tavily_alive(url: str, key: str) -> Optional[bool]:
    """Tavily Extract as a second opinion on a source that blocked the runner
    (approved for link checks by the repository owner, 2026-11-04)."""
    try:
        resp = requests.post("https://api.tavily.com/extract", timeout=90,
                             headers={"Authorization": f"Bearer {key}"},
                             json={"urls": [url]})
    except Exception:
        return None
    if resp.status_code != 200:
        return None
    data = resp.json()
    for r in data.get("results") or []:
        if r.get("url") == url and r.get("raw_content"):
            return True
    for f in data.get("failed_results") or []:
        if f.get("url") == url:
            return False if re.search(r"404|not found", str(f), re.I) else None
    return None


def link_alive(url: str, tavily_key: str = "") -> Optional[bool]:
    """True (confirmed reachable), False (confirmed dead), None (cannot tell).

    Videos are probed through YouTube's oEmbed; files through a direct request,
    falling back to Tavily Extract when the source blocks the direct one. Only a
    confirmed dead link is dropped: an unknown answer keeps it — the same
    zero-rather-than-wrong rule, and a refresh keeps what it cannot check.
    """
    if youtube_id(url):
        return _oembed_alive(url)
    try:
        r = HTTP.get(url, timeout=20, stream=True)
        code = r.status_code
        r.close()
    except Exception:
        code = None
    if code == 200:
        return True
    if code in (404, 410):
        return False
    if code in (403, 429, 503) or code is None or code >= 500:
        # Bot protection (or a transport failure the runner cannot tell apart
        # from one): Tavily's word, when a key is set.
        return tavily_alive(url, tavily_key) if tavily_key else None
    return None


# ----------------------------------------------------------------- rows --

FORMATS = {"pdf": "PDF", "pptx": "PPTX", "ppt": "PPT", "key": "Keynote", "odp": "ODP"}


def deck_format(url: str) -> str:
    ext = requests.utils.unquote(urlparse(url).path).rsplit(".", 1)[-1].lower()
    return FORMATS.get(ext, "")


def label(kind: str, url: str, links: dict[str, str]) -> str:
    if kind in ("slides", "slides2"):
        if links.get("slides") and links.get("slides2"):
            fmt = deck_format(url)
            return f"Slides ({fmt})" if fmt else ("Slides" if kind == "slides" else "Slides 2")
        return "Slides"
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
                ("slides2" if "slides" in out else "slides") if "slide" in t else
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
             "video_from_page": 0, "video_from_search": 0, "unmatched": [], "added": [], "dropped": []}
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
            said = re.search(r"^(?:Speakers|Authors):\s*(.+)$", item.text, re.M) if item else None
            found = find_recording(title, ctx, tuple(speaker_names(said.group(1))) if said else ())
            if found:
                links["video"] = found
                stats["video_from_search"] += 1
                log(f"  recording found for {title[:70]!r}: {found}")
        links = tidy(links)
        # A row goes out only with links that still resolve: each file and
        # video link is probed, and one confirmed dead is dropped rather than
        # published (ITNOG10 shipped fifteen 404 slide links before this).
        for k in [k for k in ("pdf", "slides", "slides2", "materials", "video") if links.get(k)]:
            time.sleep(ctx.delay)
            if link_alive(links[k], ctx.tavily_key) is False:
                log(f"  dead {k} link dropped for {re.split(r'\s+[—–]\s+', heading)[0][:60]!r}: {links[k]}")
                stats["dropped"].append({"pick": re.split(r"\s+[—–]\s+", heading)[0][:120],
                                         "kind": k, "url": links.pop(k)})
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
