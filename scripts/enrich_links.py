#!/usr/bin/env python3
"""Put a verified links row (abstract, paper, slides, recording) under every pick.

  enrich_links.py KEY [--digest FILE] [--no-search] [--no-pages] [--stats FILE]
                  [--summary FILE]

Reads prompts/<KEY>.md for the program's links and rewrites the digest in place
(default digests/<KEY>.md). Safe to run again: rows are rebuilt, links found
before are kept, new recordings and slides are added. See conferences/links.py
for where each link comes from and how a found recording is verified.

TAVILY_API_KEY, when set, is the fallback search if YouTube cannot be reached.
Exit status: 0 on success (even if nothing was found), 1 on bad input.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from conferences.links import context_for, enrich  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("key")
    ap.add_argument("--digest", type=Path, help="digest file (default digests/KEY.md)")
    ap.add_argument("--no-search", action="store_true", help="do not search for missing recordings")
    ap.add_argument("--no-pages", action="store_true", help="do not fetch talk pages")
    ap.add_argument("--stats", type=Path, help="write the link counts as JSON here")
    ap.add_argument("--summary", type=Path, help="write a Markdown list of the links this run added")
    args = ap.parse_args()

    registry = {e["key"]: e for e in yaml.safe_load((ROOT / "conferences" / "registry.yaml").read_text(encoding="utf-8"))["conferences"]}
    entry = registry.get(args.key)
    if not entry:
        print(f"error: {args.key} is not in the registry", file=sys.stderr)
        return 1
    digest = args.digest or ROOT / "digests" / f"{args.key}.md"
    prompt = ROOT / "prompts" / f"{args.key}.md"
    if not digest.is_file():
        print(f"error: {digest} does not exist", file=sys.stderr)
        return 1

    ctx = context_for(entry, search=not args.no_search, fetch_pages=not args.no_pages)
    text, stats = enrich(digest.read_text(encoding="utf-8"), prompt.read_text(encoding="utf-8") if prompt.is_file() else "", ctx)
    digest.write_text(text, encoding="utf-8")
    if args.stats:
        args.stats.write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    if args.summary:
        args.summary.write_text("".join(f"- {a['pick']}: {', '.join(a['links'])}\n" for a in stats["added"]),
                                encoding="utf-8")
    print(f"{args.key}: {stats['picks']} picks, {stats['matched']} matched to the program; "
          f"links: {stats['page']} abstract, {stats['pdf']} paper, {stats['slides']} slides, "
          f"{stats['video']} recording ({stats['video_from_page']} from talk pages, {stats['video_from_search']} found by search)")
    for h in stats["unmatched"]:
        print(f"  not in the program: {h}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
