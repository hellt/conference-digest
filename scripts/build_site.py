#!/usr/bin/env python3
"""Render digests/*.md into the Zensical site sources under docs/.

digests/<key>.md stays the only source of truth (invariant 1). This script
reads it and writes derived, gitignored files that `zensical build` publishes:

  docs/posts/<key>.md    one blog post per digest: front matter, an excerpt,
                         a facts strip, and the digest body with its tier
                         sections and picks marked up for styling
  docs/conferences.md    every registry edition and where it stands

The digest text itself is not rewritten: headings and wording pass through
unchanged. Each pick's `**Links:**` row (written by conferences/links.py)
becomes a row of link chips, and a talk recording on YouTube also gets a
click-to-play thumbnail (docs/javascripts/video.js swaps in the player).
Run it before every build (`make site` does).
"""

from __future__ import annotations

import json
import re
import shutil
from datetime import date, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DIGESTS = ROOT / "digests"
PROMPTS = ROOT / "prompts"
REGISTRY = ROOT / "conferences" / "registry.yaml"
STATE = ROOT / "conferences" / "state.json"
DOCS = ROOT / "docs"
POSTS = DOCS / "posts"
TRACKER = DOCS / "conferences.md"
REPO = "https://github.com/hellt/conference-digest"

TYPES = {
    "academic": "Academic",
    "standards": "Standards",
    "vendor": "Vendor",
    "operator": "Operator",
    "security": "Security",
}
TIERS = ("core", "adjacent", "wildcard")
LABEL = re.compile(r"^\*\*[A-Z][\w /-]{0,40}(?::\*\*|\*\*:)")
LINKS_ROW = re.compile(r"^\s*(?:[-*]\s+)?\*\*Links?:?\*\*:?\s*(.+)$")
MD_LINK = re.compile(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)")
ICONS = {
    "abstract": "material-text-box-outline",
    "draft": "material-file-document-edit-outline",
    "paper": "material-file-document-outline",
    "slides": "material-presentation",
    "recording": "material-play-circle-outline",
    "session recording": "material-play-circle-outline",
    "materials": "material-folder-open-outline",
}


def youtube_start(url: str) -> int:
    """Seconds from a `t=` / `start=` parameter (356, 356s, 5m56s, 1h2m3s); 0 if none."""
    m = re.search(r"[?&#](?:t|start)=((?:\d+h)?(?:\d+m)?\d+s?)\b", url)
    if not m:
        return 0
    parts = re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?(\d+)s?", m.group(1))
    h, mi, sec = (int(x or 0) for x in parts.groups()) if parts else (0, 0, 0)
    return h * 3600 + mi * 60 + sec


def youtube_id(url: str) -> str | None:
    m = re.match(r"https?://(?:www\.|m\.)?(?:youtube(?:-nocookie)?\.com/(?:watch\?(?:.*&)?v=|embed/|live/)|youtu\.be/)"
                 r"([A-Za-z0-9_-]{11})", url)
    return m.group(1) if m else None


def links_block(row: str, title: str) -> tuple[list[str], list[str]]:
    """A pick's links row as chips, and its click-to-play recording (which
    decorate() puts first in the card)."""
    links = MD_LINK.findall(row)
    if not links:
        return [f"**Links:** {row}"], []
    chips = " ".join(
        f"[:{ICONS.get(text.lower()) or ICONS.get(re.sub(r'\s*\(.*\)$|\s+\d+$', '', text.lower()), 'material-link-variant')}: {text}]({url}){{ .pick-link }}"
        for text, url in links
    )
    out = ['<div class="pick-links" markdown>', "", chips, "", "</div>", ""]
    player: list[str] = []
    recording = next((url for text, url in links if text.lower() == "recording" and youtube_id(url)), None)
    video = youtube_id(recording) if recording else None
    if video:
        start = youtube_start(recording)
        alt = re.sub(r"[\"<>&]", "", f"Play the recording: {title}")[:160]
        player = [
            f'<div class="pick-video"><a class="pick-video__thumb" data-yt="{video}" data-start="{start}" '
            f'href="https://www.youtube.com/watch?v={video}{f"&t={start}s" if start else ""}" target="_blank" rel="noopener">'
            f'<img src="https://i.ytimg.com/vi/{video}/hqdefault.jpg" '
            f'data-hd="https://i.ytimg.com/vi/{video}/maxresdefault.jpg" alt="{alt}" loading="lazy">'
            f'<span class="pick-video__play" aria-hidden="true"></span></a></div>',
            "",
        ]
    return out, player


def load_registry() -> dict[str, dict]:
    entries = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))["conferences"]
    return {e["key"]: e for e in entries}


def as_date(value) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    try:
        return datetime.strptime(str(value).strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def read_digest(path: Path) -> tuple[dict, str]:
    """Split a digest into its metadata and Markdown body.

    New digests start with an HTML-comment block (invariant 11); two older
    ones use YAML front matter or a non-standard field set. Accept all three.
    """
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    meta: dict = {}
    m = re.match(r"<!--\n(.*?)\n-->\s*", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            k, sep, v = line.partition(":")
            if sep and re.fullmatch(r"[a-z_]+", k.strip()):
                meta[k.strip()] = v.strip()
        text = text[m.end():]
    else:
        m = re.match(r"---\n(.*?)\n---\s*", text, re.S)
        if m:
            meta = yaml.safe_load(m.group(1)) or {}
            text = text[m.end():]
    return meta, text.strip() + "\n"


def split_body(body: str) -> tuple[str, str, str]:
    """Return (h1 text, intro before the first ##, rest from the first ##)."""
    lines = body.split("\n")
    title = ""
    if lines and lines[0].startswith("# "):
        title = lines.pop(0)[2:].strip()
    for i, line in enumerate(lines):
        if line.startswith("## "):
            return title, "\n".join(lines[:i]).strip(), "\n".join(lines[i:]).strip()
    return title, "", "\n".join(lines).strip()


def clean_title(title: str, fallback: str) -> str:
    title = re.sub(r"\s*[—–-]+\s*Digest\s*$", "", title).strip()
    title = re.sub(r"\s+Digest\b", "", title).strip()
    return title or fallback


def tier_of(heading: str) -> str | None:
    word = heading.strip().lower()
    for tier in (*TIERS, "theme"):
        if word.startswith(tier):
            return "themes" if tier == "theme" else tier
    return None


def nest_lists(text: str) -> str:
    """GitHub nests lists at 2 spaces; Python-Markdown needs 4."""
    if not re.search(r"^ {2}(?:[-*+]|\d+\.) ", text, re.M):
        return text
    return re.sub(r"^( +)(?=(?:[-*+]|\d+\.) )", lambda m: m.group(1) * 2, text, flags=re.M)


def decorate(rest: str) -> tuple[str, dict[str, int]]:
    """Mark tier sections and wrap each pick in a card, leaving text as is."""
    out: list[str] = []
    counts = {t: 0 for t in TIERS}
    tier = None
    in_card = in_fence = False
    pick_title = ""
    card_top = 0   # where a pick's recording goes: first in its card

    def close() -> None:
        nonlocal in_card
        if in_card:
            out.extend(["", "</div>", ""])
            in_card = False

    for line in rest.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if in_fence:
            out.append(line)
            continue
        if line.startswith("## "):
            close()
            heading = line[3:].strip()
            slug = tier_of(heading)
            tier = slug if slug in TIERS else None
            out.append(f"## {heading} {{ #{slug} .tier .tier-{slug} }}" if slug else line)
            continue
        if line.startswith("### ") and tier:
            close()
            counts[tier] += 1
            out.extend([f'<div class="pick pick-{tier}" markdown>', ""])
            card_top = len(out)
            out.append(line)
            in_card = True
            pick_title = line[4:].strip()
            continue
        row = LINKS_ROW.match(line) if in_card else None
        if row:
            chips, player = links_block(row.group(1), pick_title)
            out.extend(chips)
            out[card_top:card_top] = player
            continue
        # `**Why:** ...` lines written back to back would merge into one
        # paragraph; give each labelled line its own.
        if LABEL.match(line) and out and out[-1].strip() and not re.match(r"\s*(?:[-*+]\s|\d+\.\s|#|<)", out[-1]):
            out.append("")
        out.append(line)
    close()
    return "\n".join(out).strip() + "\n", counts


def plain(markdown: str, limit: int = 300) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", markdown)
    text = re.sub(r"[*_`>#]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rsplit(" ", 1)[0] + "…"


def human(d: date | None) -> str:
    return f"{d:%B} {d.day}, {d.year}" if d else "unknown"


def render_post(key: str, entry: dict, meta: dict, body: str) -> tuple[str, dict]:
    h1, intro, rest = split_body(nest_lists(body))
    name = entry.get("name") or meta.get("conference") or key
    title = clean_title(h1, name)
    kind = entry.get("type") or meta.get("type") or ""
    category = TYPES.get(kind, kind.title() or "Other")
    written_by = str(meta.get("written_by", "")).strip()
    bot = written_by.lower().startswith("tofarev")
    # Posts are dated by the conference, not by when the digest was written,
    # so the blog lists the most recent conference first.
    published = as_date(entry.get("end_date")) or as_date(meta.get("generated")) or date.today()
    ended = as_date(entry.get("end_date"))
    # The human-facing page; a fetcher's source_url can be an API endpoint.
    source = entry.get("manual_fallback_url") or meta.get("source_url") or entry.get("program_url") or ""
    decorated, counts = decorate(rest)
    total = sum(counts.values())
    picks = " · ".join(f"{counts[t]} {t}" for t in TIERS if counts[t])
    if not intro:
        intro = f"{total} picks from the {name} program: {picks}."

    front = {
        "date": published.isoformat(),
        "slug": key,
        "title": title,
        "description": plain(intro),
        "categories": [category],
    }
    if bot:
        front["authors"] = ["tofarev"]
    facts = [
        f":material-shape-outline: {category}",
        f":material-calendar-check-outline: Ended {human(ended)}" if ended else "",
        f":material-cards-outline: {total} picks ({picks})" if total else "",
        f":material-link-variant: [Program]({source})" if source.startswith("http") else "",
        f":material-robot-outline: {written_by}" if bot else ":material-account-edit-outline: Prompt run by hand",
    ]
    facts_html = "\n".join(f'<span class="digest-fact" markdown>{f}</span>' for f in facts if f)
    if bot:
        about = (
            f"ToFaRev picked and wrote this digest with {written_by.removeprefix('ToFaRev').strip(' ()') or 'its model'} "
            "on Nebius Token Factory, from the conference's published program. A person reviewed it in a pull request "
            "before it was published. Write-ups marked \"from abstract only\" had no fuller source to read."
        )
    else:
        about = "This digest was produced by running the repository's digest prompt by hand, from the conference's published program."
    footer = (
        f'!!! info "About this digest"\n\n'
        f"    {about} Source: [`digests/{key}.md`]({REPO}/blob/main/digests/{key}.md)"
        + (f" · prompt: [`prompts/{key}.md`]({REPO}/blob/main/prompts/{key}.md)" if (PROMPTS / f"{key}.md").exists() else "")
        + "\n"
    )
    page = (
        "---\n"
        + "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in front.items())
        + "---\n\n"
        + f"# {title}\n\n{intro}\n\n<!-- more -->\n\n"
        + f'<div class="digest-facts" markdown>\n{facts_html}\n</div>\n\n'
        + decorated
        + "\n"
        + footer
    )
    return page, {"key": key, "title": title, "date": published, "bot": bot, "picks": total}


STATUS = {
    "local_required": ":material-laptop: Needs a local fetch",
    "manual": ":material-content-paste: Needs a manual paste",
    "waiting": ":material-timer-sand: Waiting for the program",
    "stalled": ":material-alert-outline: Fetcher stalled",
    "pending": ":material-timer-sand: Queued",
}


def render_tracker(registry: dict[str, dict], posts: dict[str, dict]) -> str:
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    today = date.today()
    rows = []
    entries = sorted(registry.values(), key=lambda e: as_date(e.get("end_date")) or date.min, reverse=True)
    for e in entries:
        key = e["key"]
        ended = as_date(e.get("end_date"))
        url = e.get("manual_fallback_url") or e.get("program_url") or ""
        name = e["name"].replace("|", "\\|")
        if key in posts:
            status = f"[:material-check-circle: Read the digest](posts/{key}.md)"
        elif ended and ended > today:
            status = ":material-calendar-clock: Upcoming"
        elif (PROMPTS / f"{key}.md").exists():
            status = ":material-robot-outline: Digest in progress"
        else:
            status = STATUS.get(state.get(key, {}).get("status", "pending"), STATUS["pending"])
        conference = f"[{name}]({url})" if url.startswith("http") else name
        rows.append(f"| {conference} | {TYPES.get(e.get('type', ''), e.get('type', ''))} | {ended or '?'} | {status} |")
    return (
        "---\ntitle: Conferences\nhide:\n  - toc\n---\n\n"
        "# Conferences\n\n"
        "Every conference edition the pipeline tracks, newest first. A digest is written after the "
        "event ends and its program is published. [How it works](how-it-works.md) explains each status.\n\n"
        "| Conference | Type | Ended | Status |\n|---|---|---|---|\n" + "\n".join(rows) + "\n"
    )


def main() -> int:
    registry = load_registry()
    if POSTS.exists():
        shutil.rmtree(POSTS)
    POSTS.mkdir(parents=True)
    posts: dict[str, dict] = {}
    for path in sorted(DIGESTS.glob("*.md")):
        key = path.stem
        meta, body = read_digest(path)
        page, info = render_post(key, registry.get(key, {}), meta, body)
        (POSTS / f"{key}.md").write_text(page, encoding="utf-8")
        posts[key] = info
    TRACKER.write_text(render_tracker(registry, posts), encoding="utf-8")
    print(f"rendered {len(posts)} digest post(s) and the tracker of {len(registry)} edition(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
