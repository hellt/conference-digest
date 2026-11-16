"""Small persistent cache for deterministic link-enrichment network probes."""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

# Recordings can arrive days late, but a daily refresh should not repeat every
# unsuccessful search. The same bound limits how long a cached liveness answer
# can keep a link that has since changed state.
CACHE_TTL_SECONDS = 48 * 60 * 60


class LinkCache:
    def __init__(self, path: Path):
        self.path = path
        self.dirty = False
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            self.entries = data["entries"] if isinstance(data, dict) else {}
            if not isinstance(self.entries, dict):
                self.entries = {}
        except (OSError, ValueError, KeyError):
            self.entries = {}

    @staticmethod
    def _key(kind: str, key: str) -> str:
        return hashlib.sha256(f"{kind}\0{key}".encode()).hexdigest()

    def get(self, kind: str, key: str) -> tuple[bool, object]:
        """Return (found, value), ignoring entries older than the cache TTL."""
        entry = self.entries.get(self._key(kind, key))
        if not isinstance(entry, dict) or not isinstance(entry.get("time"), (int, float)):
            return False, None
        if time.time() - entry["time"] >= CACHE_TTL_SECONDS:
            return False, None
        return True, entry.get("value")

    def put(self, kind: str, key: str, value: object) -> None:
        self.entries[self._key(kind, key)] = {"time": time.time(), "value": value}
        self.dirty = True

    def save(self) -> None:
        if not self.dirty:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        temporary.write_text(json.dumps({"version": 1, "entries": self.entries}, sort_keys=True), encoding="utf-8")
        temporary.replace(self.path)
        self.dirty = False
