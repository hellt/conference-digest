"""Offline regressions for TNC's Pretty Event programme API."""

from datetime import date
from unittest import TestCase
from unittest.mock import Mock, patch

from conferences.fetchers import get_fetcher
from conferences.fetchers.base import MANUAL_FALLBACK, NOT_PUBLISHED, OK
from conferences.fetchers.tnc import TncFetcher
from conferences.links import program_items

URL = "https://tnc26.geant.org/"
PROGRAMME = "https://tnc26.geant.org/programme/"
ENTRY = {"program_url": URL, "manual_fallback_url": PROGRAMME}
CONFIG = {"indicoBaseUrl": "https://indico.geant.org"}
SESSIONS = [
    {
        "id": "break", "title": "Coffee Break", "day": 20260608,
        "start": "10:30:00", "end": "11:00:00", "type_name": "Break",
    },
    {
        "id": "s1", "title": "Modern Software for Modern Networks", "day": 20260609,
        "start": "11:00:00", "end": "12:30:00", "room": "Paavo", "type_name": "Sessions",
        "description": "The <b>session</b> overview.",
        "chairs": [{"name": "Chair One", "affiliation": "GÉANT"}],
        "presentations": [{
            "id": "c1", "title": "Intent-driven Operations", "start": "11:00:00", "end": "11:30:00",
            "description": "An abstract with &amp; without markup.",
            "speakers": [{"name": "Jane Doe", "affiliation": "Example NREN"}],
            "attachments": [
                {"title": "Slides PDF", "url": "/event/6/slides.pdf"},
                {"title": "Slides PPTX", "url": "https://indico.geant.org/event/6/slides.pptx"},
            ],
        }],
    },
    {
        "id": "s2", "title": "Security tooling and services for NRENs", "day": 20260610,
        "start": "14:00:00", "end": "17:30:00", "room": "Room 22", "type_name": "Side Meeting",
        "description": "A side-meeting abstract.",
        "chairs": [{"name": "Chair Two", "affiliation": "GÉANT"}],
        "presentations": [],
    },
]


def response(data=None, status=200):
    result = Mock(status_code=status)
    result.json.return_value = data
    return result


class TncTests(TestCase):
    def test_parse_presentations_standalone_sessions_and_links(self):
        text, count = TncFetcher()._parse(SESSIONS, PROGRAMME, CONFIG["indicoBaseUrl"])
        self.assertEqual(count, 2)
        self.assertNotIn("Coffee Break", text)
        items = program_items(text)
        self.assertEqual([item.title for item in items], [
            "Intent-driven Operations", "Security tooling and services for NRENs",
        ])
        self.assertEqual(items[0].links, {
            "page": PROGRAMME + "#Tuesday/all/s1",
            "slides": "https://indico.geant.org/event/6/slides.pdf",
            "slides2": "https://indico.geant.org/event/6/slides.pptx",
        })
        self.assertIn("Speakers: Jane Doe (Example NREN)", items[0].text)
        self.assertIn("Chairs: Chair One (GÉANT)", items[0].text)
        self.assertIn("An abstract with & without markup.", items[0].text)
        self.assertIn("Session abstract: The session overview.", items[0].text)
        self.assertEqual(items[1].links["page"], PROGRAMME + "#Wednesday/all/s2")
        self.assertIn("Speakers: Chair Two (GÉANT)", items[1].text)
        self.assertIn("A side-meeting abstract.", items[1].text)

    def test_fetch_uses_public_programme_and_config_apis(self):
        with patch("conferences.fetchers.tnc.http_get", side_effect=[
            response(SESSIONS), response(CONFIG),
        ]) as get:
            result = get_fetcher("tnc").fetch(ENTRY)
        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 2)
        self.assertEqual(result.source_url, PROGRAMME)
        self.assertEqual([call.args[0] for call in get.call_args_list], [
            "https://pretty-event-dnm-ieventi-production.apps.bst2.paas.psnc.pl/api/programme/tnc26",
            "https://pretty-event-dnm-ieventi-production.apps.bst2.paas.psnc.pl/api/config/tnc26",
        ])

    def test_fetch_failure_modes_and_empty_program(self):
        fetcher = TncFetcher()
        for status, expected in ((404, NOT_PUBLISHED), (403, MANUAL_FALLBACK),
                                 (429, MANUAL_FALLBACK), (500, MANUAL_FALLBACK)):
            with self.subTest(status=status), patch("conferences.fetchers.tnc.http_get",
                                                     return_value=response(status=status)):
                self.assertEqual(fetcher.fetch(ENTRY).status, expected)
        with patch("conferences.fetchers.tnc.http_get", side_effect=[
            response([]), response(CONFIG),
        ]):
            result = fetcher.fetch(ENTRY)
            self.assertEqual(result.status, NOT_PUBLISHED)
            self.assertEqual(result.item_count, 0)
        with patch("conferences.fetchers.tnc.http_get", side_effect=RuntimeError("offline")):
            self.assertEqual(fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)
        with patch("conferences.fetchers.tnc.http_get", side_effect=[
            response(SESSIONS), response(CONFIG, status=403),
        ]):
            self.assertEqual(fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)

    def test_probe_still_reads_blocked_wordpress_page_through_tavily(self):
        with patch.object(TncFetcher, "_page", return_value="Helsinki, 8-12 June 2026"):
            result = TncFetcher().probe(ENTRY, [2026])
        self.assertTrue(result.exists)
        self.assertEqual(result.end_date, date(2026, 6, 12))
