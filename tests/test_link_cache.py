"""Persistent caching for expensive, deterministic link probes."""

from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

from conferences.link_cache import CACHE_TTL_SECONDS, LinkCache
from conferences.links import Context, enrich


PROGRAM = "### A talk without a recording\n"
DIGEST = ("## Core\n### A talk without a recording\n"
          "**Links:** [Slides](https://example.org/slides.pdf)\nA pick.\n")


class LinkCacheTests(TestCase):
    def test_none_and_boolean_values_round_trip_and_expire(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "cache.json"
            with patch("conferences.link_cache.time.time", return_value=1000):
                cache = LinkCache(path)
                cache.put("missing-recording", "talk", None)
                cache.put("link-alive", "url", True)
                cache.save()

            cached = LinkCache(path)
            with patch("conferences.link_cache.time.time", return_value=1000 + CACHE_TTL_SECONDS - 1):
                self.assertEqual(cached.get("missing-recording", "talk"), (True, None))
                self.assertEqual(cached.get("link-alive", "url"), (True, True))
            with patch("conferences.link_cache.time.time", return_value=1000 + CACHE_TTL_SECONDS):
                self.assertEqual(cached.get("missing-recording", "talk"), (False, None))
                self.assertEqual(cached.get("link-alive", "url"), (False, None))

    def test_enrich_reuses_unsuccessful_search_and_liveness_results(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "cache.json"
            cache = LinkCache(path)
            with patch("conferences.links.find_recording", return_value=None) as search, \
                    patch("conferences.links.link_alive", return_value=True) as alive:
                refreshed, _ = enrich(DIGEST, PROGRAM, Context(key="pytorch-2026", delay=0, cache=cache))
            search.assert_called_once()
            alive.assert_called_once()
            cache.save()

            with patch("conferences.links.find_recording") as search, \
                    patch("conferences.links.link_alive") as alive:
                repeated, _ = enrich(refreshed, PROGRAM,
                                     Context(key="pytorch-2026", delay=0, cache=LinkCache(path)))
            search.assert_not_called()
            alive.assert_not_called()
            self.assertEqual(repeated, refreshed)

    def test_inconclusive_liveness_is_retried(self):
        cache = LinkCache(Path("unused.json"))
        for _ in range(2):
            with patch("conferences.links.link_alive", return_value=None) as alive:
                enrich(DIGEST, PROGRAM, Context(key="pytorch-2026", search=False, delay=0, cache=cache))
            alive.assert_called_once()
        self.assertFalse(cache.dirty)
