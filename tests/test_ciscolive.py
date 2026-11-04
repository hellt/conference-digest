"""Offline regressions for Cisco Live's public RainFocus catalog."""

from copy import deepcopy
from datetime import date
from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock, patch

import requests
import yaml

from conferences.fetchers import get_fetcher
from conferences.fetchers.base import MANUAL_FALLBACK, NOT_PUBLISHED, OK
from conferences.fetchers.ciscolive import CiscoLiveFetcher, LIBRARY, _search
from conferences.links import Context, enrich, program_items, scrape_page
from scripts.discover_editions import candidates, fill, latest_ident, resolve_end_date


ENTRY = {"key": "ciscolive-us-2025", "program_url": LIBRARY, "manual_fallback_url": LIBRARY}
EVENTS = {"responseCode": "0", "attributes": [{"id": "event", "values": [
    {"id": "us25", "name": "2025 San Diego"},
    {"id": "eu25", "name": "2025 Amsterdam"},
    {"id": "us26", "name": "2026 Las Vegas"},
    {"id": "au25", "name": "2025 Melbourne"},
]}]}
ITEM = {
    "sessionID": "session1", "event": "2025 San Diego",
    "title": "Fabric Design &amp; Security - BRKDCN-2000",
    "abstract": "<p>Design <b>EVPN</b> fabrics.</p><ul><li>Apply identity policy.</li></ul>",
    "participants": [{"fullName": "Jane Doe", "companyName": "Cisco"},
                     {"globalFullName": "John Roe", "globalCompany": "Example"}],
    "files": [], "videos": [],
}


def page(items=None, offset=0, total=1, event_id="us25"):
    return {"responseCode": "0", "sectionList": [{
        "sectionId": event_id, "from": offset, "total": total,
        "items": deepcopy([ITEM] if items is None else items),
    }]}


class CiscoLiveTests(TestCase):
    def setUp(self):
        self.fetcher = CiscoLiveFetcher()

    def test_registered(self):
        self.assertIsInstance(get_fetcher("ciscolive"), CiscoLiveFetcher)

    def test_exact_titles_speakers_abstracts_and_public_route(self):
        with patch("conferences.fetchers.ciscolive._search", side_effect=[EVENTS, page()]):
            result = self.fetcher.fetch(ENTRY)
        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 1)
        item, = program_items(result.program_text)
        self.assertEqual(item.title, "Fabric Design & Security - BRKDCN-2000")
        self.assertIn("Speakers: Jane Doe (Cisco), John Roe (Example)", item.text)
        self.assertIn("Design EVPN fabrics. Apply identity policy.", item.text)
        self.assertEqual(item.links, {"page": LIBRARY + "#/session/session1"})
        self.assertEqual(result.source_url, LIBRARY + "?search.event=us25")

    def test_pagination_fetches_every_session(self):
        second = {**ITEM, "sessionID": "session2", "title": "Second talk"}
        with patch("conferences.fetchers.ciscolive._search", side_effect=[
            EVENTS, page(total=2), page([second], offset=1, total=2),
        ]) as search:
            result = self.fetcher.fetch(ENTRY)
        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 2)
        self.assertEqual(search.call_args.kwargs["from"], 1)
        self.assertEqual(search.call_args.kwargs["search.event"], "us25")

    def test_capped_catalog_uses_public_facets_and_deduplicates(self):
        second = {**ITEM, "sessionID": "session2", "title": "Second talk"}
        third = {**ITEM, "sessionID": "session3", "title": "Third talk"}
        capped = page(total=3)
        capped["sectionList"][0]["paginationMax"] = 2
        capped["attributes"] = [{"id": "sessiontype", "values": [{"id": "breakout"}]}]
        with patch("conferences.fetchers.ciscolive._search", side_effect=[
            EVENTS, capped, page([ITEM, second], total=3), page([second, third], total=2),
        ]) as search:
            result = self.fetcher.fetch(ENTRY)
        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 3)
        self.assertEqual(search.call_args.kwargs["search.sessiontype"], "breakout")
        self.assertEqual(search.call_args_list[2].kwargs["size"], 2)

    def test_uncategorized_sessions_require_additional_facets_or_manual(self):
        second = {**ITEM, "sessionID": "session2"}
        third = {**ITEM, "sessionID": "session3"}
        facets = ("sessiontype", "technicallevel", "track", "technology")
        capped = page(total=3)
        capped["sectionList"][0]["paginationMax"] = 2
        capped["attributes"] = [{"id": f, "values": [{"id": f}]} for f in facets]
        # One session has no sessiontype or level; its track still accounts for it.
        with patch("conferences.fetchers.ciscolive._search", side_effect=[
            EVENTS, capped, page([ITEM, second], total=3), page(),
            {"totalSearchItems": 0}, page([third]),
        ]) as search:
            result = self.fetcher.fetch(ENTRY)
        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 3)
        self.assertEqual(search.call_args.kwargs["search.track"], "track")
        with patch("conferences.fetchers.ciscolive._search", side_effect=[
            EVENTS, capped, page([ITEM, second], total=3), *[page() for _ in facets],
        ]):
            result = self.fetcher.fetch(ENTRY)
        self.assertEqual(result.status, MANUAL_FALLBACK)
        self.assertIn("incomplete catalog", result.detail)
        self.assertEqual(result.program_text, "")

    def test_oversized_partition_without_remaining_facets_fails_closed(self):
        capped = page(total=501)
        capped["attributes"] = [{"id": f, "values": [{"id": f}]} for f in
                                ("sessiontype", "technicallevel", "track", "technology")]
        with patch("conferences.fetchers.ciscolive._search", side_effect=[EVENTS] + [capped] * 9):
            result = self.fetcher.fetch(ENTRY)
        self.assertEqual(result.status, MANUAL_FALLBACK)
        self.assertIn("exceeds result cap", result.detail)

    def test_europe_is_not_us_or_another_year(self):
        eu = {**ITEM, "event": "2025 Amsterdam"}
        entry = {**ENTRY, "key": "ciscolive-eu-2025"}
        with patch("conferences.fetchers.ciscolive._search", side_effect=[EVENTS, page([eu], event_id="eu25")]) as search:
            result = self.fetcher.fetch(entry)
        self.assertEqual(result.status, OK)
        self.assertEqual(search.call_args.kwargs["search.event"], "eu25")
        self.assertNotIn("San Diego", result.program_text)

    def test_missing_editions_and_unknown_cities_are_not_published(self):
        unknown = deepcopy(EVENTS)
        unknown["attributes"][0]["values"] = [{"id": "unknown", "name": "2025 Unknown City"}]
        for entry, events in (({**ENTRY, "key": "ciscolive-us-2027"}, EVENTS), (ENTRY, unknown)):
            with patch("conferences.fetchers.ciscolive._search", return_value=events):
                self.assertEqual(self.fetcher.fetch(entry).status, NOT_PUBLISHED)
                self.assertFalse(self.fetcher.probe(entry).exists)

    def test_empty_program_and_sessions_without_abstracts(self):
        for response in (page([], total=0), page([{**ITEM, "abstract": ""}])):
            with patch("conferences.fetchers.ciscolive._search", side_effect=[EVENTS, response]):
                result = self.fetcher.fetch(ENTRY)
            self.assertEqual(result.status, NOT_PUBLISHED)
            self.assertEqual(result.item_count, 0)
            self.assertEqual(result.program_text, "")

    def test_partial_mixed_duplicate_or_changed_program_is_never_ok(self):
        cases = [
            [EVENTS, page(total=2), page([], offset=1, total=2)],
            [EVENTS, page(total=2), page(offset=1, total=2)],
            [EVENTS, page(total=2), page([], offset=1, total=3)],
            [EVENTS, page(event_id="eu25")],
            [EVENTS, page(offset=10)],
            [EVENTS, page([{**ITEM, "event": "2026 Las Vegas"}])],
            [EVENTS, {"responseCode": "0"}],
        ]
        for responses in cases:
            with self.subTest(responses=responses), patch("conferences.fetchers.ciscolive._search", side_effect=responses):
                result = self.fetcher.fetch(ENTRY)
                self.assertEqual(result.status, MANUAL_FALLBACK)
                self.assertEqual(result.program_text, "")

    def test_key_url_mismatch_and_ambiguous_region_fail_closed(self):
        ambiguous = deepcopy(EVENTS)
        ambiguous["attributes"][0]["values"].append({"id": "second", "name": "2025 Las Vegas"})
        for entry, events in (({**ENTRY, "program_url": LIBRARY + "?search.event=eu25"}, EVENTS),
                              ({**ENTRY, "key": "ciscolive-2025"}, EVENTS), (ENTRY, ambiguous)):
            with patch("conferences.fetchers.ciscolive._search", return_value=events):
                self.assertEqual(self.fetcher.fetch(entry).status, MANUAL_FALLBACK)

    def test_probe_does_not_invent_dates_and_still_requires_fetch(self):
        with patch("conferences.fetchers.ciscolive._search", return_value=EVENTS):
            probe = self.fetcher.probe(ENTRY, [2025])
        self.assertTrue(probe.exists)
        self.assertEqual(probe.location, "San Diego")
        self.assertIsNone(probe.end_date)
        self.assertFalse(self.fetcher.probe_is_sufficient)

    def test_api_and_transport_failures_are_manual(self):
        for error in (requests.Timeout("offline"), ValueError("not JSON"), KeyError("attributes")):
            with patch("conferences.fetchers.ciscolive._search", side_effect=error):
                self.assertEqual(self.fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)
                self.assertFalse(self.fetcher.probe(ENTRY).exists)
        for status in (403, 429, 500):
            response = Mock()
            response.raise_for_status.side_effect = requests.HTTPError(f"status {status}")
            with patch("conferences.fetchers.ciscolive.requests.post", return_value=response):
                self.assertEqual(self.fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)
        response = Mock()
        response.json.return_value = {"responseCode": "1", "responseMessage": "login required"}
        with patch("conferences.fetchers.ciscolive.requests.post", return_value=response):
            self.assertEqual(self.fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)
        response.json.return_value = EVENTS
        with patch("conferences.fetchers.ciscolive.requests.post", return_value=response) as post:
            self.assertEqual(_search(size=1), EVENTS)
            self.assertNotIn("rfAuthToken", post.call_args.kwargs["headers"])
            self.assertEqual(post.call_args.kwargs["data"], {"type": "session", "size": 1})

    def test_links_refresh_never_reads_shared_catalog_or_extracts_it(self):
        with patch("conferences.links.HTTP.get") as get, patch("conferences.links.tavily_page") as extract:
            for url in (LIBRARY, LIBRARY + "#/session/session1", LIBRARY + "?search.event=us25#/session/session1"):
                self.assertEqual(scrape_page(url, "tavily-key"), {})
            with patch("conferences.fetchers.ciscolive._search", side_effect=[EVENTS, page()]):
                program = self.fetcher.fetch(ENTRY).program_text
            title = program_items(program)[0].title
            digest, stats = enrich(f"## Core\n### {title}\nA pick.\n", program,
                                   Context(key=ENTRY["key"], search=False, delay=0))
            self.assertIn(f"[Abstract]({LIBRARY}#/session/session1)", digest)
            self.assertEqual(stats["video_from_page"], 0)
            get.assert_not_called()
            extract.assert_not_called()
        self.assertEqual(Context(key=ENTRY["key"]).query_term, "Cisco Live")

    def test_registry_series_and_date_estimates(self):
        root = Path(__file__).resolve().parents[1]
        registry = yaml.safe_load((root / "conferences/registry.yaml").read_text())["conferences"]
        specs = yaml.safe_load((root / "conferences/series.yaml").read_text())["series"]
        keys = [e["key"] for e in registry]
        self.assertEqual(len(keys), len(set(keys)))
        for region, hint in (("us", "06-30"), ("eu", "03-31")):
            key = f"ciscolive-{region}-2026"
            entry = next(e for e in registry if e["key"] == key)
            spec = next(s for s in specs if s["series"] == f"ciscolive-{region}")
            self.assertEqual(entry["fetcher"], "ciscolive")
            self.assertGreaterEqual(latest_ident(keys, spec), 2026)
            self.assertEqual(fill(spec["key_template"], 2027, "year"), f"ciscolive-{region}-2027")
            self.assertTrue(all(c > latest_ident(keys, spec)
                               for c in candidates(spec, keys, date(2026, 11, 1))))
            self.assertEqual(resolve_end_date(spec, latest_ident(keys, spec) + 1, None, None, date(2026, 11, 1)),
                             (f"{latest_ident(keys, spec) + 1}-{hint}", True))
