#!/usr/bin/env python3
"""List the digests whose links rows the Links Refresh workflow should rebuild.

  links_queue.py [--conference KEY] [--days N]

Recordings and slides are published weeks after a conference, so every digest
whose conference ended in the last N days (default 120) is refreshed; a key
given with --conference is refreshed whatever its age. Prints one key per line
and, under GitHub Actions, writes `keys=<json list>` to $GITHUB_OUTPUT.
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import date, datetime, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def ended(entry: dict) -> date | None:
    value = entry.get("end_date")
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value))
    except ValueError:
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--conference", default="")
    ap.add_argument("--days", type=int, default=120)
    args = ap.parse_args()
    registry = yaml.safe_load((ROOT / "conferences" / "registry.yaml").read_text(encoding="utf-8"))["conferences"]
    since = date.today() - timedelta(days=args.days)
    keys = [
        e["key"] for e in registry
        if (ROOT / "digests" / f"{e['key']}.md").is_file()
        and (e["key"] == args.conference if args.conference else (ended(e) or date.min) >= since)
    ]
    if args.conference and not keys:
        raise SystemExit(f"error: {args.conference} has no digest to refresh")
    print("\n".join(keys))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
            f.write(f"keys={json.dumps(keys)}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
