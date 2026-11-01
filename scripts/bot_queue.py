#!/usr/bin/env python3
"""List the prompts ToFaRev should turn into digests on this run.

A key is queued when prompts/<key>.md exists and has program text, the key is
in the registry, there is no digests/<key>.md yet (invariant 1: the digest file
is the only "done" signal) and no open digest pull request covers it.
`--conference <key>` forces that one key, digest or not, like the generator's
flag. Newest editions go first; `--max` bounds the cost of one run.

Writes `keys=<json array>` to $GITHUB_OUTPUT and prints the array.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts"
DIGESTS = ROOT / "digests"
REGISTRY = ROOT / "conferences" / "registry.yaml"
SEPARATOR = re.compile(r"^=+ PROGRAM TEXT =+[ \t]*$", re.M)


def has_program(prompt: Path) -> bool:
    text = prompt.read_text(encoding="utf-8")
    m = SEPARATOR.search(text)
    program = text[m.end():].strip() if m else ""
    return bool(program) and program != "{PROGRAM_TEXT}"


def end_date(entry: dict) -> date:
    value = entry.get("end_date")
    if isinstance(value, date):
        return value
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except ValueError:
        return date.min


def queue(registry: list[dict], exclude: set[str], forced: str, limit: int) -> list[str]:
    keys = []
    for entry in sorted(registry, key=end_date, reverse=True):
        key = entry["key"]
        prompt = PROMPTS / f"{key}.md"
        if forced and key != forced:
            continue
        if not prompt.exists() or not has_program(prompt):
            continue
        if not forced and ((DIGESTS / f"{key}.md").exists() or key in exclude):
            continue
        keys.append(key)
    return keys[:limit]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--conference", default="", help="force one registry key")
    ap.add_argument("--exclude", default="", help="comma-separated keys with an open digest PR")
    ap.add_argument("--max", type=int, default=3, help="most digests to write in one run")
    args = ap.parse_args()

    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))["conferences"]
    forced = args.conference.strip()
    if forced and forced not in {e["key"] for e in registry}:
        print(f"unknown registry key: {forced}", file=sys.stderr)
        return 1
    exclude = {k.strip() for k in args.exclude.split(",") if k.strip()}
    keys = queue(registry, exclude, forced, max(args.max, 1))
    if forced and not keys:
        print(f"{forced}: no prompts/{forced}.md with program text to digest", file=sys.stderr)
        return 1

    print(json.dumps(keys))
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
            f.write(f"keys={json.dumps(keys)}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
