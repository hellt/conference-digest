#!/usr/bin/env python3
"""Install one ToFaRev digest artifact and describe it for review.

  propose_digest.py KEY ARTIFACT_DIR --message FILE --body FILE
                    [--run-url URL] [--issue N]

ARTIFACT_DIR is the downloaded `tofarev-digest-<key>` artifact: digest.md plus
result.json (stats and check notes). The digest is validated and written to
digests/<key>.md; the commit message follows the repo convention (`digest:
<key>`, where the program came from, the core signal) and the PR body lists the
automatic checks for the human who merges it. Exits non-zero, writing nothing,
if the artifact does not belong to KEY.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "conferences" / "registry.yaml"
STATE = ROOT / "conferences" / "state.json"
MAX_BYTES = 400_000


def fail(message: str) -> int:
    print(f"error: {message}", file=sys.stderr)
    return 1


def themes(markdown: str, limit: int = 3) -> list[str]:
    m = re.search(r"^## +Themes\b.*?$(.*)", markdown, re.M | re.S | re.I)
    bullets = re.findall(r"^[-*] +(.+)$", m.group(1), re.M) if m else []
    out = []
    for b in bullets[:limit]:
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", b).replace("**", "").strip()
        out.append(text if len(text) <= 160 else text[:159].rsplit(" ", 1)[0] + "…")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("key")
    ap.add_argument("artifact", type=Path)
    ap.add_argument("--message", type=Path, required=True)
    ap.add_argument("--body", type=Path, required=True)
    ap.add_argument("--run-url", default="")
    ap.add_argument("--issue", default="")
    args = ap.parse_args()
    key = args.key

    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]{0,99}", key):
        return fail(f"invalid key {key!r}")
    registry = {e["key"]: e for e in yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))["conferences"]}
    if key not in registry:
        return fail(f"{key} is not in the registry")
    entry = registry[key]
    digest_file = args.artifact / "digest.md"
    result_file = args.artifact / "result.json"
    if not digest_file.is_file() or not result_file.is_file():
        return fail(f"{args.artifact} has no digest.md and result.json")
    if digest_file.stat().st_size > MAX_BYTES:
        return fail("digest.md is too large")
    result = json.loads(result_file.read_text(encoding="utf-8"))
    markdown = digest_file.read_text(encoding="utf-8")
    if result.get("failed") or result.get("key") not in (None, key):
        return fail(f"result.json is failed or belongs to {result.get('key')!r}")
    meta = re.match(r"<!--\n(.*?)\n-->", markdown, re.S)
    if not meta or not re.search(rf"^registry_key: {re.escape(key)}$", meta.group(1), re.M):
        return fail(f"digest.md does not start with the metadata block for {key}")
    written_by = re.search(r"^written_by: *(.+)$", meta.group(1), re.M)
    written_by = written_by.group(1).strip() if written_by else "ToFaRev"

    (ROOT / "digests" / f"{key}.md").write_text(markdown, encoding="utf-8")

    state = json.loads(STATE.read_text(encoding="utf-8")).get(key, {}) if STATE.exists() else {}
    if state.get("status") == "manual":
        source = f"a program pasted into prompts/{key}.md by hand"
    else:
        source = f"a program auto-fetched by the {entry.get('fetcher', '?')} fetcher"
    stats = result.get("stats", {})
    notes = result.get("notes", [])
    signal = themes(markdown)

    message = [f"digest: {key}", "", f"Written by {written_by} from prompts/{key}.md, built from {source}."]
    message.append(
        f"{stats.get('picks', '?')} picks from {stats.get('items', '?')} program items "
        f"({stats.get('mode', '?')} run, {stats.get('calls', '?')} model calls)."
    )
    if signal:
        message += ["", "Themes:"] + [f"- {t}" for t in signal]
    if args.run_url:
        message += ["", f"Workflow run: {args.run_url}"]
    args.message.write_text("\n".join(message) + "\n", encoding="utf-8")

    staged = stats.get("mode") == "staged"
    rows = [
        ("Program", f"{stats.get('items', '?')} items from {source}"),
        ("Selection", f"{stats.get('batches', 0)} shortlist batches → {stats.get('shortlisted', 0)} shortlisted → "
                      f"{stats.get('selected', 0)} sent to the writer" if staged else "whole program sent to the writer"),
        ("Picks", str(stats.get("picks", "?"))),
        ("Model", f"{written_by}, {stats.get('calls', '?')} calls in {stats.get('seconds', '?')} s"),
    ]
    if args.run_url:
        rows.append(("Workflow run", f"[logs]({args.run_url})"))
    body = [
        f"ToFaRev drafted the digest for **{entry['name']}**.",
        "",
        f"Merging publishes it to the site and closes the conference issue{f' (closes #{args.issue})' if args.issue else ''}.",
        "",
        "| | |",
        "|---|---|",
        *[f"| {k} | {v} |" for k, v in rows],
        "",
        "### Automatic checks",
        "",
        *([f"- {n}" for n in notes] or ["- Nothing to flag. Links come only from the program, and every heading matches a program item."]),
        "",
        "### Before merging",
        "",
        "- [ ] Picks and tiers make sense for this program.",
        "- [ ] Spot-check two or three write-ups against their abstracts.",
        "- [ ] Any heading flagged above is a real program item.",
        "",
        "Edit the digest on this branch if needed. To redo it, close this PR and run **Digest Bot** with this key.",
    ]
    args.body.write_text("\n".join(body) + "\n", encoding="utf-8")
    print(f"installed digests/{key}.md ({len(markdown)} bytes, {len(notes)} note(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
