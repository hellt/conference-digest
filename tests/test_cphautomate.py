"""Offline regressions for CPH^Automate's static conference pages."""

from datetime import date
from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock, patch

import yaml

from conferences.fetchers import get_fetcher
from conferences.fetchers.base import MANUAL_FALLBACK, NOT_PUBLISHED, OK
from conferences.fetchers.cphautomate import CphAutomateFetcher
from conferences.links import program_items
from scripts.discover_editions import fill

URL = "https://cph-automate.network/2026/schedule/"
ENTRY = {"program_url": URL, "manual_fallback_url": URL}
SCHEDULE = """
<h1>CPH^Automate 2026 Schedule</h1>
<div class="cph-timetable">
  <div class="cph-tt-row cph-tt-registration"><p class="cph-tt-title">Registration</p></div>
  <div class="cph-tt-row cph-tt-talk">
    <p class="cph-tt-title"><a href="/talks/json-freedom-or-chaos/">JSON freedom or chaos; how to trust your data</a></p>
    <p class="cph-tt-speaker"><a href="/speakers/#bart">Bart Dorlandt</a></p>
  </div>
  <div class="cph-tt-row cph-tt-break"><p class="cph-tt-title">Coffee break</p></div>
  <div class="cph-tt-row cph-tt-talk">
    <p class="cph-tt-title"><a href="/talks/community/">Transformation Through Community</a></p>
    <p class="cph-tt-speaker"><a>Andreas Bækdahl</a>, <a>Emil Commerou</a></p>
  </div>
</div>
"""
JSON_TALK = """
<div class="cph-talk-detail">
  <p><a href="/2026/">CPH^Automate 2026</a></p>
  <p>Slides: <a href="json_freedom_or_chaos_cphautomate.pdf">PDF</a></p>
  <div class="cph-talk-detail-abstract"><p>Can you trust your data?<br>Pydantic and pytest are used.</p></div>
</div>
"""
COMMUNITY_TALK = """
<div class="cph-talk-detail">
  <div class="cph-talk-detail-abstract"><p>We built a network automation community.</p></div>
</div>
"""
OVERVIEW = "<h1>CPH^Automate 2026</h1><p>CPH^Automate 2026 took place on Friday, October 2, 2026 at IDA Conference in Copenhagen.</p>"


def response(html="", status=200):
    return Mock(text=html, status_code=status)


class CphAutomateTests(TestCase):
    def test_schedule_talks_abstracts_speakers_and_slides(self):
        with patch("conferences.fetchers.cphautomate.http_get", side_effect=[
            response(SCHEDULE), response(JSON_TALK), response(COMMUNITY_TALK),
        ]) as get:
            result = CphAutomateFetcher().fetch(ENTRY)

        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 2)
        items = program_items(result.program_text)
        self.assertEqual(items[0].title, "JSON freedom or chaos; how to trust your data")
        self.assertIn("Speakers: Bart Dorlandt", items[0].text)
        self.assertIn("Pydantic and pytest are used.", items[0].text)
        self.assertEqual(items[0].links, {
            "page": "https://cph-automate.network/talks/json-freedom-or-chaos/",
            "slides": "https://cph-automate.network/talks/json-freedom-or-chaos/json_freedom_or_chaos_cphautomate.pdf",
        })
        self.assertIn("Speakers: Andreas Bækdahl, Emil Commerou", items[1].text)
        self.assertEqual(list(items[1].links), ["page"])
        self.assertNotIn("Registration", result.program_text)
        self.assertNotIn("Coffee break", result.program_text)
        self.assertEqual(get.call_args_list[1].args[0], items[0].links["page"])

    def test_probe_reads_edition_overview(self):
        with patch("conferences.fetchers.cphautomate.http_get", return_value=response(OVERVIEW)) as get:
            result = CphAutomateFetcher().probe(ENTRY, [2026])
        self.assertTrue(result.exists)
        self.assertEqual(result.end_date, date(2026, 10, 2))
        self.assertEqual(result.location, "Copenhagen")
        self.assertEqual(get.call_args.args[0], "https://cph-automate.network/2026/")
        with patch("conferences.fetchers.cphautomate.http_get", return_value=response(OVERVIEW)):
            self.assertIsNone(CphAutomateFetcher().probe(ENTRY, [2027]).end_date)

    def test_failure_modes_and_empty_schedule(self):
        fetcher = get_fetcher("cphautomate")
        self.assertIsInstance(fetcher, CphAutomateFetcher)
        for status, expected in ((404, NOT_PUBLISHED), (403, MANUAL_FALLBACK),
                                 (429, MANUAL_FALLBACK), (500, MANUAL_FALLBACK)):
            with self.subTest(status=status), patch("conferences.fetchers.cphautomate.http_get",
                                                    return_value=response(status=status)):
                self.assertEqual(fetcher.fetch(ENTRY).status, expected)
                self.assertFalse(fetcher.probe(ENTRY).exists)
        with patch("conferences.fetchers.cphautomate.http_get", return_value=response("<h1>Coming soon</h1>")):
            self.assertEqual(fetcher.fetch(ENTRY).status, NOT_PUBLISHED)
        with patch("conferences.fetchers.cphautomate.http_get", side_effect=RuntimeError("offline")):
            self.assertEqual(fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)
            self.assertFalse(fetcher.probe(ENTRY).exists)
        with patch("conferences.fetchers.cphautomate.http_get", side_effect=[
            response(SCHEDULE), response(status=404),
        ]):
            self.assertEqual(fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)

    def test_series_templates(self):
        root = Path(__file__).resolve().parents[1]
        specs = yaml.safe_load((root / "conferences/series.yaml").read_text())["series"]
        spec = next(s for s in specs if s["series"] == "cph-automate")
        self.assertEqual(spec["start"], 2026)
        self.assertEqual(spec["key_template"], "cph-automate-{year}")
        self.assertEqual(fill(spec["program_url_template"], 2026, "year"), URL)
