"""Offline regressions for OVScon's three published program layouts.

Run: python -m unittest discover -s tests
"""

from datetime import date
from unittest import TestCase
from unittest.mock import Mock, patch

from bs4 import BeautifulSoup

from conferences.fetchers import get_fetcher
from conferences.fetchers.base import MANUAL_FALLBACK, NOT_PUBLISHED, OK
from conferences.fetchers.ovscon import OvsconFetcher, talk_links
from conferences.links import Context, enrich, program_items, scrape_page
from scripts.discover_editions import candidates, fill, latest_ident


URL = "https://www.openvswitch.org/support/ovscon2024/"
ENTRY = {"key": "ovscon-2024", "program_url": URL, "manual_fallback_url": URL}
LEGACY = """
<main><h1>Open vSwitch and OVN 2024 Fall Conference</h1>
<p>Hosted on November 20&amp;21, 2024 in Prague.</p>
<table>
<tr><td>Opening Remarks</td><td><a href="https://youtu.be/xxxxxxxxxxx">Video</a></td></tr>
<tr><td><a href="#t1">Fabric Integration</a></td>
<td><a href="https://youtu.be/aaaaaaaaaaa?t=2">YouTube</a></td>
<td><a href="slides/Deck (1).pdf">PDF</a><a href="slides/Deck 2.pptx">PPTX</a></td></tr>
<tr><td><a href="#t2">Missing Slides</a></td><td><a href="https://youtu.be/bbbbbbbbbbb">YouTube</a></td></tr>
<tr><td><a href="#t3">Unpublished abstract</a></td></tr>
<tr><td><a href="#t1">Duplicate navigation</a></td></tr>
</table>
<h2>Talks</h2>
<h3 id="t1">Fabric Integration</h3><p>Speaker(s): Jane Doe, Example</p>
<p>Route advertisement via BGP.</p><ul><li>Active-active gateways.</li></ul>
<h3 id="t2">Missing Slides</h3><p>Speaker(s): John Roe, Other</p>
<p>Hardware offload trade-offs.</p>
<h3 id="t3">Unpublished abstract</h3><p>Speaker(s): Nobody</p>
</main>
"""
PRE = """
<main><h1>Open vSwitch and OVN 2025 Fall Conference</h1>
<p>Hosted on November 19 - 20, 2025 in Prague.</p>
<table><tr><td><a href="#t1">OVN and BGP</a></td><td><a href="slides/BGP.odp">ODP</a></td></tr></table>
<h3 id="t1">OVN and BGP <a href="#day1">|TOP|</a></h3>
<h3>Speaker(s): Jane Doe, Example</h3><pre>Native BGP
  integration and EVPN.</pre>
<h2>Other information</h2><p>Not part of the abstract.</p>
</main>
"""
CARDS = """
<main><h1>Open vSwitch and OVN 2026 Fall Conference</h1>
<p>Will host on November 3 - 4, 2026 in Heilbronn.</p>
<div class="sponsors"><h3>Platinum</h3><p>Not a talk</p></div>
<table><tr><td>Lunch</td></tr><tr><td><a href="#t1">No-Overlay Mode</a></td><td>10:00</td></tr></table>
<div class="talk" id="t1"><h3 class="talk-title">No-Overlay Mode<a href="#r1">Top</a></h3>
<p class="speakers">Jane Doe, Example</p><div class="abstract"><p>Remove Geneve.</p><p>Keep network policy.</p></div></div>
<p>Submissions close December 31, 2026.</p>
</main>
"""


def response(html=LEGACY, status=200):
    return Mock(text=html, status_code=status, headers={"content-type": "text/html"})


class OvsconTests(TestCase):
    def setUp(self):
        self.fetcher = OvsconFetcher()

    def test_registered(self):
        self.assertIsInstance(get_fetcher("ovscon"), OvsconFetcher)

    def test_legacy_abstracts_materials_and_missing_decks(self):
        text, count = self.fetcher._parse(LEGACY, URL)
        items = program_items(text)
        self.assertEqual(count, 2)
        self.assertEqual([i.title for i in items], ["Fabric Integration", "Missing Slides"])
        first = items[0]
        self.assertIn("Speakers: Jane Doe, Example", first.text)
        self.assertIn("Active-active gateways.", first.text)
        self.assertNotIn("Hardware offload", first.text)
        self.assertEqual(first.links["page"], URL + "#t1")
        self.assertEqual(first.links["slides"], URL + "slides/Deck%20%281%29.pdf")
        self.assertEqual(first.links["slides2"], URL + "slides/Deck%202.pptx")
        self.assertEqual(first.links["video"], "https://youtu.be/aaaaaaaaaaa?t=2")
        self.assertNotIn("slides", items[1].links)

    def test_pre_layout(self):
        text, count = self.fetcher._parse(PRE, URL)
        self.assertEqual(count, 1)
        self.assertIn("### OVN and BGP\nSpeakers: Jane Doe, Example", text)
        self.assertIn("Native BGP integration and EVPN.", text)
        self.assertIn("slides/BGP.odp", text)
        self.assertNotIn("TOP", text)
        self.assertNotIn("Other information", text)

    def test_cards_without_recordings(self):
        text, count = self.fetcher._parse(CARDS, URL)
        self.assertEqual(count, 1)
        self.assertIn("Remove Geneve. Keep network policy.", text)
        self.assertIn("Speakers: Jane Doe, Example", text)
        self.assertNotIn("video:", text)
        self.assertNotIn("Platinum", text)
        self.assertNotIn("Top", text)

    def test_refresh_does_not_borrow_other_talks_materials(self):
        soup = BeautifulSoup(LEGACY, "html.parser")
        self.assertEqual(talk_links(soup, URL + "#t2"), {"video": "https://youtu.be/bbbbbbbbbbb"})
        for fragment in ("", "#t99", "#day1"):
            self.assertEqual(talk_links(soup, URL + fragment), {})
        with patch("conferences.links.HTTP.get", return_value=response()):
            self.assertEqual(scrape_page(URL + "#t2"), {"video": "https://youtu.be/bbbbbbbbbbb"})
            self.assertEqual(scrape_page(URL), {})
            # Prompt fetched before slides were posted: refresh recovers only t1's row.
            prompt = "### Fabric Integration\npage: " + URL + "#t1\n"
            digest, stats = enrich("## Core\n### Fabric Integration\nA pick.\n", prompt,
                                   Context(key="ovscon-2024", search=False, delay=0))
        self.assertEqual(stats["video_from_page"], 1)
        self.assertIn("Deck%20%281%29.pdf", digest)
        self.assertIn("aaaaaaaaaaa?t=2", digest)
        self.assertNotIn("bbbbbbbbbbb", digest)

    def test_failed_refresh_does_not_extract_whole_program(self):
        with patch("conferences.links.HTTP.get", return_value=response(status=403)), \
             patch("conferences.links.tavily_page") as extract:
            self.assertEqual(scrape_page(URL + "#t2", "key"), {})
            extract.assert_not_called()

    def test_fetch_outcomes(self):
        for resp, expected in ((response(), OK), (response("<main>Coming soon</main>"), NOT_PUBLISHED),
                               (response(status=404), NOT_PUBLISHED), (response(status=403), MANUAL_FALLBACK),
                               (response(status=500), MANUAL_FALLBACK)):
            with self.subTest(status=resp.status_code), patch("conferences.fetchers.ovscon.http_get", return_value=resp):
                self.assertEqual(self.fetcher.fetch(ENTRY).status, expected)
        with patch("conferences.fetchers.ovscon.http_get", side_effect=RuntimeError("offline")):
            self.assertEqual(self.fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)
        with patch("conferences.fetchers.ovscon.http_get", return_value=response()), \
             patch.object(self.fetcher, "_parse", side_effect=ValueError("layout changed")):
            self.assertEqual(self.fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)

    def test_discovery_dates_and_errors(self):
        for html, end in ((LEGACY, date(2024, 11, 21)), (PRE, date(2025, 11, 20)), (CARDS, date(2026, 11, 4))):
            with patch("conferences.fetchers.ovscon.http_get", return_value=response(html)):
                probe = self.fetcher.probe(ENTRY, [end.year])
                self.assertTrue(probe.exists)
                self.assertEqual(probe.end_date, end)
                self.assertIsNone(self.fetcher.probe(ENTRY, [2030]).end_date)
        for status in (403, 404, 500):
            with patch("conferences.fetchers.ovscon.http_get", return_value=response(status=status)):
                self.assertFalse(self.fetcher.probe(ENTRY).exists)
        with patch("conferences.fetchers.ovscon.http_get", side_effect=RuntimeError("offline")):
            self.assertFalse(self.fetcher.probe(ENTRY).exists)

    def test_registry_and_future_series(self):
        from pathlib import Path
        import yaml
        root = Path(__file__).resolve().parents[1]
        registry = yaml.safe_load((root / "conferences/registry.yaml").read_text())["conferences"]
        spec = next(s for s in yaml.safe_load((root / "conferences/series.yaml").read_text())["series"] if s["series"] == "ovscon")
        keys = [e["key"] for e in registry]
        self.assertEqual(len(keys), len(set(keys)))
        for year in (2024, 2025):
            entry = next(e for e in registry if e["key"] == f"ovscon-{year}")
            self.assertEqual(entry["fetcher"], "ovscon")
            self.assertTrue((root / "conferences/prompt/types" / f"{entry['type']}.md").exists())
        self.assertEqual(fill(spec["program_url_template"], 2027, "year"),
                         "https://www.openvswitch.org/support/ovscon2027/")
        # Excluding already-discovered editions reproduces the initial scan.
        historical = [k for k in keys if not k.startswith("ovscon-") or k in ("ovscon-2024", "ovscon-2025")]
        self.assertEqual(latest_ident(historical, spec), 2025)
        self.assertEqual(candidates(spec, historical, date(2026, 11, 1)), [2026, 2027])
