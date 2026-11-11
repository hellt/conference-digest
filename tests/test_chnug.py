"""Offline regressions for CHNUG's static meetup agendas."""

from datetime import date
from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock, patch

import yaml

from conferences.fetchers import get_fetcher
from conferences.fetchers.base import MANUAL_FALLBACK, NOT_PUBLISHED, OK
from conferences.fetchers.chnug import ChnugFetcher
from conferences.links import CHANNELS, UPLOAD_CHANNELS, program_items
from scripts.discover_editions import fill

URL = "https://chnug.ch/chnug002"
ENTRY = {"program_url": URL, "manual_fallback_url": URL}
PROGRAM = """
<h1>meetups</h1><h1>CHNUG #2 - Thu, 12th of March 2026 @ Init7</h1>
<h2>Agenda 17:30 – 22:00</h2>
<ul>
  <li>17:30 – 18:00: Arrival, Welcome Drinks, and Networking</li>
  <li>18:00 - 18:10: Welcome and Introduction (Speaker: Severin Dellsperger @CHNUG/OST)
    <ul><li><a href="/chnug002/slides/welcome.pdf">Slides</a></li></ul></li>
  <li>18:10 - 18:30: Network Configuration in the Real World: Standards, Surprises and ‘Creative’ Implementations (Speaker: Jens Vogler @Init7)
    <ul><li><a href="/chnug002/slides/network.pdf">Slides</a></li>
        <li><a href="https://www.youtube.com/watch?v=uQ3UDeY73OE">Recording</a></li></ul></li>
  <li>19:00 – 19:30: Connecting Clouds over FTTH: How Easy Can CES Be? (Speaker: Darragh Grealish @56K.Cloud)
    <ul><li><a href="https://www.youtube.com/watch?v=9g8QD-Mjd4o">Recording</a></li>
        <li><a href="/chnug002/slides/cloud.pdf">Slides</a></li></ul></li>
  <li>20:10 – 22:00: Networking, Exchange, and Pizza!</li>
</ul>
"""
MULTI_SPEAKER = """
<h1>CHNUG #4 - Wed, 26th of August 2026 @ OST</h1><h2>Agenda</h2><ul>
<li>18:10 – 18:40: Network Monitoring with the gNMIc Operator (Speakers: Roman Weber + Valentino Diller @OST Students)
<ul><li><a href="/chnug004/slides/gnmic.pdf">Slides</a></li>
<li><a href="https://youtu.be/Tq85WB6UK7c">Recording</a></li></ul></li>
<li>18:45 – 19:15: DDI: Managing IP Allocation with an Open-Source DDI (Speaker: Marco Martinez)
<ul><li><a href="/chnug004/slides/ddi.pdf">Slides</a></li>
<li><a href="https://youtu.be/i8VJbY-0uO4">Recording</a></li></ul></li>
<li>19:50 – 19:55: Further Education @OST (Speaker: Christoph Göldi @OST)</li>
<li>19:55 – 20:05: Outro (Speaker: Severin Dellsperger @CHNUG/OST)</li>
</ul>
"""


def response(html="", status=200):
    return Mock(text=html, status_code=status)


class ChnugTests(TestCase):
    def test_exact_titles_affiliations_slides_and_recordings(self):
        with patch("conferences.fetchers.chnug.http_get", return_value=response(PROGRAM)):
            result = ChnugFetcher().fetch(ENTRY)
        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 2)
        items = program_items(result.program_text)
        self.assertEqual(items[0].title,
                         "Network Configuration in the Real World: Standards, Surprises and ‘Creative’ Implementations")
        self.assertIn("Speakers: Jens Vogler (Init7)", items[0].text)
        self.assertEqual(items[0].links, {
            "slides": "https://chnug.ch/chnug002/slides/network.pdf",
            "video": "https://www.youtube.com/watch?v=uQ3UDeY73OE",
        })
        self.assertEqual(items[1].links["slides"], "https://chnug.ch/chnug002/slides/cloud.pdf")
        self.assertEqual(items[1].links["video"], "https://www.youtube.com/watch?v=9g8QD-Mjd4o")
        cloud_block = result.program_text.split("### Connecting Clouds", 1)[1]
        self.assertIn("\nslides: https://chnug.ch/chnug002/slides/cloud.pdf | video:", cloud_block)
        self.assertTrue(all("No abstract published" in item.text and "page" not in item.links for item in items))
        self.assertNotIn("Welcome and Introduction", result.program_text)
        self.assertNotIn("Pizza", result.program_text)

    def test_shared_affiliation_and_administrative_slots(self):
        with patch("conferences.fetchers.chnug.http_get", return_value=response(MULTI_SPEAKER)):
            result = ChnugFetcher().fetch(ENTRY)
        self.assertEqual(result.item_count, 2)
        self.assertIn("Speakers: Roman Weber (OST Students), Valentino Diller (OST Students)",
                      result.program_text)
        self.assertIn("Speakers: Marco Martinez\n", result.program_text)
        self.assertNotIn("Further Education", result.program_text)
        self.assertNotIn("Outro", result.program_text)

    def test_probe_reads_day_of_month_wording(self):
        with patch("conferences.fetchers.chnug.http_get", return_value=response(PROGRAM)):
            result = ChnugFetcher().probe(ENTRY)
        self.assertTrue(result.exists)
        self.assertEqual(result.end_date, date(2026, 3, 12))
        with patch("conferences.fetchers.chnug.http_get", return_value=response(PROGRAM)):
            self.assertIsNone(ChnugFetcher().probe(ENTRY, [2027]).end_date)

    def test_failure_modes_and_empty_agenda(self):
        fetcher = get_fetcher("chnug")
        self.assertIsInstance(fetcher, ChnugFetcher)
        for status, expected in ((404, NOT_PUBLISHED), (403, MANUAL_FALLBACK),
                                 (429, MANUAL_FALLBACK), (500, MANUAL_FALLBACK)):
            with self.subTest(status=status), patch("conferences.fetchers.chnug.http_get",
                                                    return_value=response(status=status)):
                self.assertEqual(fetcher.fetch(ENTRY).status, expected)
                self.assertFalse(fetcher.probe(ENTRY).exists)
        for html in ("<h1>CHNUG #5</h1><h2>Agenda</h2><h2>Tickets</h2>",
                     "<h1>CHNUG #5</h1><h2>Agenda</h2><ul><li>CfP opens soon</li></ul>"):
            with patch("conferences.fetchers.chnug.http_get", return_value=response(html)):
                self.assertEqual(fetcher.fetch(ENTRY).status, NOT_PUBLISHED)
        with patch("conferences.fetchers.chnug.http_get", side_effect=RuntimeError("offline")):
            self.assertEqual(fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)
            self.assertFalse(fetcher.probe(ENTRY).exists)

    def test_series_pads_urls_and_knows_official_channel(self):
        root = Path(__file__).resolve().parents[1]
        specs = yaml.safe_load((root / "conferences/series.yaml").read_text())["series"]
        spec = next(s for s in specs if s["series"] == "chnug")
        self.assertEqual(spec["start"], 2)
        self.assertEqual(fill(spec["program_url_template"], 2, "ordinal"), URL)
        self.assertEqual(fill(spec["program_url_template"], 10, "ordinal"), "https://chnug.ch/chnug010")
        self.assertEqual(UPLOAD_CHANNELS["chnug"], "@CH-NUG")
        self.assertIn("swiss network user group", CHANNELS["chnug"])
