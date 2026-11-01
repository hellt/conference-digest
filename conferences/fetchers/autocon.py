"""AutoCon fetcher: the Network Automation Forum's conference, one edition.

    https://networkautomation.forum/autocon<n>

The edition page is open HTML (no bot-block). Its "Conference Program" lists
every session as one line under a day header:

    Wednesday, 28 May
    13:15 - 14:00 — Opening Keynote: Claudia de Luna - Start at the Beginning; ...
    14:00 - 14:10 — Suhaib Saeed - Clash of the Titans: Nornir Vs Ansible

That gives title, speakers and time, but no abstract and no materials. Two
official sources fill them in:

1. A program guide repository, github.com/Network-Automation-Forum/ac<n>-guide
   (AutoCon 5 has one): each talk's title, speaker with role and company, and a
   short abstract. It is matched to the schedule by start time and speaker,
   because some talks were retitled after the website program was written.
2. NAF's YouTube channel ("Network Automation Forum") uploads every talk as
   "Title - Speaker", with the abstract as the description, a few weeks after
   the event. Each talk's upload is found with the links step's verified search
   (conferences/links.py: title, channel, upload window) and gives the
   recording and, where the guide has none, the abstract.

The page states the dates ("the week of 26-30 May 2025"). Logistics lines
(registration, meals, breaks, sponsor messages, opening and closing remarks)
are not program items.

Slides: NAF publishes each edition's decks (PDF and/or PPTX) in its handyinfo
repository, docs/autocon_coverage/slides/AutoCon<n>/<day>/, named after the
speakers and a short title ("AC4-AndyLapteff-CLILifer.pdf", "AC5 - Leo
Fleskes - ….pdf"). The files are in Git LFS, so links point at
media.githubusercontent.com, which serves the file itself. Decks are paired
with talks by speaker names, then title words; workshop and sponsor decks are
left out. A deck published as both PDF and PPTX gets both links, PDF first
(ToFaRev reads the first `slides:` link, and it can read only PDFs).
"""

from __future__ import annotations

import re
import time
import unicodedata
from datetime import date, datetime
from typing import Iterable, Optional
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, ProbeResult, http_get, OK, NOT_PUBLISHED

MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
MON = r"Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sept?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?"
DAY_RE = re.compile(rf"^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),?\s+(\d{{1,2}})\s+({MONTHS})\b")
SLOT_RE = re.compile(r"^(\d{1,2}:\d{2})\s*[-–]\s*(\d{1,2}:\d{2})\s*[—–-]+\s*(.+)$")
WEEK_RE = re.compile(rf"week of\s+(\d{{1,2}})\s*[-–]\s*(\d{{1,2}})\s+({MON})\.?\s+(20\d\d)", re.I)
KIND_RE = re.compile(r"^((?:Opening |Closing )?Keynote|Lightning Talk|Panel|Fireside Chat)\s*:\s*", re.I)
LOGISTICS = re.compile(
    r"registration|lunch|\bbreak\b|happy hour|opening and introduction|conference opening|welcome message|"
    r"message from|opening remarks|closing remarks|closing words|day (?:one|two|three) |raffle|group photo|"
    r"networking begins|check-in|ceremony|remarks from|^lightning talks!?$",
    re.I,
)
GUIDE_URL = "https://raw.githubusercontent.com/Network-Automation-Forum/ac{n}-guide/main/index.html"
HANDYINFO_TREE = "https://api.github.com/repos/Network-Automation-Forum/handyinfo/git/trees/HEAD?recursive=1"
SLIDES_DIR = "docs/autocon_coverage/slides/AutoCon{n}/"
LFS_MEDIA = "https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/"
DECK_EXT = re.compile(r"\.(pdf|pptx?|key)$", re.I)


def _week_dates(week: re.Match) -> list[date]:
    """First and last day of "the week of 16-20 Nov 2026" (full or short month)."""
    month = datetime.strptime(week.group(3)[:3].title(), "%b").month
    year = int(week.group(4))
    return [date(year, month, int(week.group(1))), date(year, month, int(week.group(2)))]


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def _surnames(speakers: str) -> set[str]:
    names = re.split(r"\s*(?:,|&|\band\b)\s*", speakers)
    return {_norm(n.split()[-1]) for n in names if n.split()}


def _text_lines(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "svg", "noscript"]):
        t.decompose()
    lines = [re.sub(r"\s+", " ", l).strip() for l in soup.get_text("\n").splitlines()]
    return [l for l in lines if l]


LIGHTNING_RE = re.compile(r"^\+\s*Speaker\s*\d+\s*[-–]\s*(.+?)\s+[-–]\s+(.+)$")
BARE_SLOT_RE = re.compile(r"^\d{1,2}:\d{2}\s*[-–]\s*\d{1,2}:\d{2}$")


def _join_slots(lines: list[str]) -> list[str]:
    """Rejoin "9:10 - 9:55" / "—" / "Speaker - Title", which some pages split."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        if BARE_SLOT_RE.match(lines[i]) and i + 2 < len(lines) and re.fullmatch(r"[—–-]", lines[i + 1]):
            out.append(f"{lines[i]} — {lines[i + 2]}")
            i += 3
            continue
        out.append(lines[i])
        i += 1
    return out


def parse_program(html: str, year_hint: Optional[int] = None) -> tuple[list[dict], list[date]]:
    """Talks from the edition page's "Conference Program", and the event's days."""
    lines = _join_slots(_text_lines(html))
    text = " ".join(lines)
    week = WEEK_RE.search(text)
    year = int(week.group(4)) if week else year_hint
    if not year:
        # The site menu names each edition with its year: "AutoCon 4 (Austin, Fall 2025)".
        n = re.search(r"AutoCon\s*(\d+)\s*[—–-]+\s*Network Automation Forum", text)
        y = re.search(rf"AutoCon\s*{n.group(1)}\s*\([^)]*?(20\d\d)\)", text) if n else None
        year = int(y.group(1)) if y else None
    days: list[date] = _week_dates(week) if week else []
    talks: list[dict] = []
    day: Optional[date] = None
    in_program = False
    program_days: set[date] = set()
    last_slot: Optional[dict] = None
    for line in lines:
        if re.fullmatch(r"Conference Program(?:me)?", line, re.I):
            in_program = True
            continue
        m = DAY_RE.match(line)
        if m and year:
            try:
                day = datetime.strptime(f"{m.group(2)} {m.group(3)} {year}", "%d %B %Y").date()
            except ValueError:
                pass
            continue
        # A track header without a date ("Thursday AM - General Session"): that
        # weekday within the event's week.
        named = re.match(r"^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b(?!,?\s+\d)", line)
        if named and in_program and day:
            day = next(d for d in (date.fromordinal(day.toordinal() + i) for i in range(7))
                       if d.strftime("%A") == named.group(1))
            continue
        # Lightning talks listed under their block: "+ Speaker 2 - Name - Title".
        lt = LIGHTNING_RE.match(line)
        if lt and in_program and day and talks is not None and last_slot:
            talks.append({**last_slot, "title": lt.group(2).strip(), "speakers": lt.group(1).strip(),
                          "kind": "Lightning Talk", "abstract": "", "video": ""})
            continue
        s = SLOT_RE.match(line)
        if not (s and in_program and day):
            continue
        start, end, rest = s.group(1), s.group(2), s.group(3).strip()
        last_slot = {"day": day, "start": start.zfill(5),
                     "when": f"{day:%A}, {day.day} {day:%B} {day.year}, {start} - {end}"}
        if LOGISTICS.search(rest):
            continue
        program_days.add(day)
        kind = ""
        k = KIND_RE.match(rest)
        if k:
            kind, rest = k.group(1).title(), rest[k.end():]
        speakers, sep, title = rest.partition(" - ")
        if not sep:  # no "Speaker - Title" split: a session without named speakers
            speakers, title = "", rest
        title = title.strip().strip('"“”')
        if len(title) < 4:
            continue
        talks.append({
            "title": title,
            "speakers": speakers.strip(),
            "kind": kind,
            "day": day,
            "start": start.zfill(5),
            "when": f"{day:%A}, {day.day} {day:%B} {day.year}, {start} - {end}",
            "abstract": "",
            "video": "",
        })
    # Without "the week of …", the program's own days give the dates.
    return talks, sorted(set(days) or program_days)


def parse_guide(html: str) -> list[dict]:
    """Talks from an ac<n>-guide page: start time, title, speaker line, abstract."""
    soup = BeautifulSoup(html, "html.parser")
    out = []
    for prefix in ("talk", "thu-cell"):
        for t in soup.select(f".{prefix}-title"):
            card = t.parent
            get = lambda cls: (card.select_one(f".{prefix}-{cls}").get_text(" ", strip=True)
                               if card.select_one(f".{prefix}-{cls}") else "")
            start = re.match(r"\d{1,2}:\d{2}", get("time"))
            out.append({
                "start": start.group(0).zfill(5) if start else "",
                "title": t.get_text(" ", strip=True),
                "speaker": re.sub(r"\s+", " ", get("speaker")).strip(),
                "abstract": get("desc"),
            })
    return out


def merge_guide(talks: list[dict], guide: list[dict]) -> int:
    """Take the guide's title, speaker line and abstract for each matching talk."""
    used = set()
    matched = 0
    for t in talks:
        names = _surnames(t["speakers"])
        for i, g in enumerate(guide):
            if i in used:
                continue
            same_title = _norm(g["title"]) == _norm(t["title"])
            same_slot = g["start"] == t["start"] and names and any(n and n in _norm(g["speaker"]) for n in names)
            if same_title or same_slot:
                used.add(i)
                t["title"], t["abstract"] = g["title"] or t["title"], g["abstract"]
                t["speakers"] = g["speaker"] or t["speakers"]
                matched += 1
                break
    return matched


def _ascii(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def _name_forms(name: str) -> set[str]:
    """How a name shows up in a file name: "Antonio Óscar Balmaseda Blanco" ->
    antonioscarbalmasedablanco, antonioblanco, antoniobalmaseda, …"""
    tokens = re.findall(r"[a-z0-9]+", _ascii(name))
    if len(tokens) < 2:
        return set()
    forms = {"".join(tokens)} | {tokens[0] + t for t in tokens[1:]} | {tokens[0] + "".join(tokens[1:3])}
    return {f for f in forms if len(f) >= 6}


def _file_words(path: str) -> set[str]:
    stem = DECK_EXT.sub("", path.rsplit("/", 1)[-1])
    stem = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", stem)   # CamelCase -> words
    return {w for w in re.findall(r"[a-z0-9]+", _ascii(stem)) if len(w) > 2} - {"ac3", "ac4", "ac5", "ac6", "ac7"}


def slide_files(n: str) -> list[list[str]]:
    """Decks of one edition in NAF's handyinfo repository: each deck's files, PDF first."""
    resp = requests.get(HANDYINFO_TREE, timeout=60, headers={"Accept": "application/vnd.github+json"})
    resp.raise_for_status()
    prefix = SLIDES_DIR.format(n=n)
    decks: dict[str, list[str]] = {}
    for item in resp.json().get("tree", []):
        path = item.get("path", "")
        if item.get("type") != "blob" or not path.startswith(prefix) or not DECK_EXT.search(path):
            continue
        if re.search(r"/workshops?/|sponsor", path, re.I):
            continue
        decks.setdefault(DECK_EXT.sub("", path), []).append(path)
    return [sorted(files, key=lambda f: (not f.lower().endswith(".pdf"), f)) for _, files in sorted(decks.items())]


def match_slides(talks: list[dict], decks: list[list[str]], names) -> int:
    """Pair decks with talks: speakers named in the file name first, then title words."""
    pairs = []
    for i, t in enumerate(talks):
        speakers = [_name_forms(n) for n in names(t["speakers"])]
        title = {w for w in re.findall(r"[a-z0-9]+", _ascii(t["title"])) if len(w) > 2}
        for j, files in enumerate(decks):
            path = files[0]
            flat = re.sub(r"[^a-z0-9]+", "", _ascii(path.rsplit("/", 1)[-1]))
            hits = sum(any(f in flat for f in forms) for forms in speakers)
            if hits:
                pairs.append((hits * 10 + len(title & _file_words(path)), i, j))
    used_t, used_f, matched = set(), set(), 0
    for _, i, j in sorted(pairs, reverse=True):
        if i in used_t or j in used_f:
            continue
        used_t.add(i); used_f.add(j)
        talks[i]["slides"] = [LFS_MEDIA + quote(f, safe="/") for f in decks[j][:2]]
        matched += 1
    return matched


def program_text(talks: list[dict]) -> str:
    lines: list[str] = []
    day = None
    for t in talks:
        if t["day"] != day:
            day = t["day"]
            lines += [f"## {day:%A}, {day.day} {day:%B} {day.year}", ""]
        lines.append(f"### {t['title']}")
        if t["speakers"]:
            lines.append(f"Speakers: {t['speakers']}")
        lines.append(f"Session: {t['when']}" + (f" ({t['kind']})" if t["kind"] else ""))
        decks = t.get("slides") or []
        links = [f"slides: {u}" for u in (decks if isinstance(decks, list) else [decks])]
        links += [f"video: {t['video']}"] if t.get("video") else []
        if links:
            lines.append(" | ".join(links))
        if t["abstract"]:
            lines.append(t["abstract"])
        lines.append("")
    return "\n".join(lines)


class AutoconFetcher(Fetcher):
    name = "autocon"

    @staticmethod
    def _number(url: str) -> str:
        m = re.search(r"/autocon(\d+)", url)
        return m.group(1) if m else ""

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
        except Exception as e:
            return self.manual(entry, f"request error: {e}")
        if resp.status_code == 404:
            return FetchResult(status=NOT_PUBLISHED, detail="edition page 404", source_url=url)
        # The page embeds a CAPTCHA for its forms, which base.looks_blocked()
        # takes for a challenge; trust the status code, and the parser, which
        # finds no program on a page that is not the real one.
        if resp.status_code != 200:
            return self.manual(entry, f"networkautomation.forum returned {resp.status_code}")
        resp.encoding = resp.encoding or "utf-8"
        end = entry.get("end_date")
        talks, days = parse_program(resp.text, end.year if hasattr(end, "year") else None)
        if not talks:
            return FetchResult(status=NOT_PUBLISHED, source_url=url,
                               detail="edition page has no conference program yet")

        n = self._number(url)
        from_guide = 0
        if n:
            try:
                g = requests.get(GUIDE_URL.format(n=n), timeout=30)
                if g.status_code == 200:
                    from_guide = merge_guide(talks, parse_guide(g.text))
            except Exception:
                pass

        from conferences.links import Context, find_video, speaker_names
        with_slides = 0
        if n:
            try:
                with_slides = match_slides(talks, slide_files(n), speaker_names)
            except Exception:
                pass

        # Each talk's upload on NAF's channel: the recording, and the abstract
        # when the guide had none. NAF keeps one playlist per edition ("AutoCon
        # 4"): list it once, match talks to its titles, and open only the
        # matches. Without a playlist, search per talk. Nothing is uploaded
        # before the event ends (discovery fetches upcoming editions), so skip
        # it until then.
        from conferences.links import Video, title_matches, youtube_playlist, youtube_playlists, youtube_video
        ctx = Context(key=entry.get("key") or f"autocon-{n}",
                      end_date=max(days) if days else (end if isinstance(end, date) else None))
        ended = ctx.end_date is not None and ctx.end_date < date.today()
        playlist = []
        if ended and n:
            try:
                pid = next((pid for pid, title, channel in youtube_playlists(f"AutoCon {n}")
                            if _norm(title) == f"autocon{n}" and "network automation forum" in channel.lower()), None)
                playlist = youtube_playlist(pid) if pid else []
            except Exception:
                playlist = []
        from conferences.links import words as title_words
        found: dict[int, Optional[Video]] = {}
        if playlist:
            # A title match in NAF's own playlist for this edition is the talk.
            # Score every talk-video pair (exact title first, then shared words)
            # and give each video to one talk only: one speaker can give two
            # talks with similar titles.
            pairs = []
            for i, t in enumerate(talks if ended else []):
                speakers = tuple(speaker_names(t["speakers"]))
                for vid, title in playlist:
                    if title_matches(t["title"], Video(vid, title, ""), speakers):
                        exact = _norm(t["title"]) in _norm(title)
                        pairs.append((exact * 100 + len(title_words(t["title"]) & title_words(title)), i, vid))
            used: set[str] = set()
            for _, i, vid in sorted(pairs, reverse=True):
                if i in found or vid in used:
                    continue
                used.add(vid)
                talks[i]["video"] = f"https://www.youtube.com/watch?v={vid}"
                # The video page adds the description (the abstract); if it
                # cannot be read, the recording stays linked without it.
                cand = youtube_video(vid)
                found[i] = cand if cand and cand.description else None
                time.sleep(0.3)
        else:
            for i, t in enumerate(talks if ended else []):
                v = find_video(t["title"], ctx, tuple(speaker_names(t["speakers"])))
                if v:
                    t["video"] = f"https://www.youtube.com/watch?v={v.id}"
                    found[i] = v
        for i, v in found.items():
            t = talks[i]
            if v and not t["abstract"]:
                desc = v.description.strip()
                first, _, rest = desc.partition("\n")
                # The description often repeats the title on its first line.
                t["abstract"] = re.sub(r"\s+", " ", rest if _norm(first) == _norm(t["title"]) else desc).strip()[:1500]

        with_video = sum(bool(t["video"]) for t in talks)
        with_abstract = sum(bool(t["abstract"]) for t in talks)
        return FetchResult(
            status=OK,
            program_text=program_text(talks),
            source_url=url,
            item_count=len(talks),
            detail=(f"{len(talks)} talks; {with_abstract} with an abstract ({from_guide} from the program guide), "
                    f"{with_slides} with slides, {with_video} with a recording"),
            meta={"end_date": max(days).isoformat() if days else ""},
        )

    def probe(self, entry: dict, years: Optional[Iterable[int]] = None) -> ProbeResult:
        """An edition is real once its page states its dates: "the week of 16-20
        Nov 2026", or day headers in its program. (Not the default probe: the
        page's form CAPTCHA would read as a bot challenge.)"""
        url = entry["program_url"]
        try:
            resp = http_get(url)
        except Exception as e:
            return ProbeResult(False, f"request error: {e}", source_url=url)
        if resp.status_code != 200:
            return ProbeResult(False, f"status {resp.status_code}", source_url=url)
        resp.encoding = resp.encoding or "utf-8"
        _, days = parse_program(resp.text)
        if not days:
            return ProbeResult(False, "edition page states no dates yet", source_url=url)
        return ProbeResult(True, f"edition page states its dates, ends {max(days)}", end_date=max(days), source_url=url)
