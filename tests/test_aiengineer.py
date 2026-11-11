"""Offline regressions for AI Engineer public schedules and chapter cards."""

from unittest import TestCase
from unittest.mock import Mock, patch

from conferences.fetchers import get_fetcher
from conferences.fetchers.aiengineer import AiEngineerFetcher, _recording
from conferences.fetchers.base import MANUAL_FALLBACK, NOT_PUBLISHED, OK
from conferences.links import CHANNELS, UPLOAD_CHANNELS, program_items

URL = "https://ai.engineer/nyc/2026"
DATA_URL = URL + "/sessions.json"
ENTRY = {"program_url": URL, "manual_fallback_url": URL}
PROGRAM = """
<article data-session="opening-13" id="recording-company-session-opening-13">
  <p class="text-xs uppercase">October 13 · Main stage</p>
  <h3><a href="/nyc/2026/talks/opening-13">Opening Remarks</a></h3>
  <p><span class="font-semibold">Jane Doe</span><strong>AI Engineer</strong></p>
  <p class="mt-5 text-base">The opening chapter of the first daily stream.</p>
  <a href="https://www.youtube.com/watch?v=abcdefghijk&amp;t=22s">Watch at 0:00:22</a>
</article>
<article data-session="ramp">
  <p class="text-xs uppercase">October 14 · Main stage</p>
  <h3><a href="/nyc/2026/talks/ramp">Chasing capabilities while waiting for the frontier</a></h3>
  <p><span class="font-semibold">Alexander Shevchenko</span></p>
  <a href="https://www.youtube.com/watch?v=lmnopqrstuv&amp;t=1229s">Watch at 0:20:29</a>
</article>
<article data-session="closing-13">
  <p class="text-xs uppercase">October 13 · Remarks</p>
  <h3><a href="/nyc/2026/talks/closing-13">Closing Remarks</a></h3>
</article>
<article data-session="related"><h3>Not a session card</h3></article>
"""
SCHEDULE = {
    "totalSessions": 2,
    "sessions": [
        {"title": "GPUs in Production", "description": "Measured inference lessons; CAPTCHA is only a word in this abstract.",
         "day": "April 9", "time": "2:30-2:50pm", "room": "Abbey",
         "track": "GPUs & LLM Infrastructure", "type": "talk", "speakers": ["Jane Doe"]},
        {"title": "Opening Keynote", "description": None, "day": "April 10",
         "time": None, "room": None, "track": None, "type": "keynote", "speakers": []},
    ],
}


def response(html="", status=200, url=URL, json_data=None):
    result = Mock(text=html, status_code=status, url=url)
    result.headers = {"content-type": "application/json" if json_data is not None else "text/html"}
    result.json = Mock(return_value=json_data)
    return result


class AiEngineerTests(TestCase):
    def test_public_json_schedule_is_preferred(self):
        with patch("conferences.fetchers.aiengineer.http_get",
                   return_value=response(url=DATA_URL, json_data=SCHEDULE)) as get:
            result = AiEngineerFetcher().fetch(ENTRY)
        get.assert_called_once_with(DATA_URL, timeout=60)
        self.assertEqual(result.status, OK)
        self.assertEqual(result.source_url, DATA_URL)
        self.assertEqual(result.item_count, 2)
        items = program_items(result.program_text)
        self.assertEqual(items[0].title, "GPUs in Production")
        self.assertIn("Speakers: Jane Doe", items[0].text)
        self.assertIn("Schedule: 2:30-2:50pm · Abbey · talk", items[0].text)
        self.assertIn("Measured inference lessons; CAPTCHA", items[0].text)
        self.assertIn("No description published", items[1].text)
        self.assertIn("## April 9 — GPUs & LLM Infrastructure", result.program_text)

    def test_session_cards_keep_chapter_links_and_transcript_pages(self):
        with patch("conferences.fetchers.aiengineer.http_get", side_effect=[
                response(status=404, url=DATA_URL), response(PROGRAM)]):
            result = AiEngineerFetcher().fetch(ENTRY)
        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 2)
        items = program_items(result.program_text)
        self.assertEqual(items[0].links, {
            "page": URL + "/talks/opening-13",
            "video": "https://www.youtube.com/watch?v=abcdefghijk&t=22s",
        })
        self.assertIn("Speakers: Jane Doe (AI Engineer)", items[0].text)
        self.assertIn("opening chapter", items[0].text)
        self.assertEqual(items[1].title, "Chasing capabilities while waiting for the frontier")
        self.assertEqual(items[1].links["video"],
                         "https://www.youtube.com/watch?v=lmnopqrstuv&t=1229s")
        self.assertIn("No synopsis published", items[1].text)
        self.assertIn("Speakers: Alexander Shevchenko", items[1].text)
        self.assertIn("## October 13 · Main stage", result.program_text)
        self.assertIn("## October 14 · Main stage", result.program_text)
        self.assertNotIn("Not a session card", result.program_text)
        self.assertNotIn("Closing Remarks", result.program_text)

    def test_recording_url_is_canonical_and_rejects_non_video_links(self):
        self.assertEqual(_recording("https://www.youtube.com/watch?v=abcdefghijk&t=1m2s"),
                         "https://www.youtube.com/watch?v=abcdefghijk")
        self.assertEqual(_recording("https://www.youtube.com/watch?v=short&t=22s"), "")

    def test_partial_or_non_json_schedule_fails_closed(self):
        partial = {"totalSessions": 3, "sessions": SCHEDULE["sessions"]}
        for resp in (response(url=DATA_URL, json_data=partial),
                     response("<html>not JSON</html>", url=DATA_URL)):
            with self.subTest(resp=resp), patch("conferences.fetchers.aiengineer.http_get", return_value=resp):
                self.assertEqual(AiEngineerFetcher().fetch(ENTRY).status, MANUAL_FALLBACK)

    def test_failure_modes_and_empty_program(self):
        fetcher = get_fetcher("aiengineer")
        self.assertIsInstance(fetcher, AiEngineerFetcher)
        for status in (403, 429, 500):
            with self.subTest(status=status), patch("conferences.fetchers.aiengineer.http_get",
                                                    return_value=response(status=status, url=DATA_URL)):
                self.assertEqual(fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)
        with patch("conferences.fetchers.aiengineer.http_get", side_effect=[
                response(status=404, url=DATA_URL), response(status=404)]):
            self.assertEqual(fetcher.fetch(ENTRY).status, NOT_PUBLISHED)
        with patch("conferences.fetchers.aiengineer.http_get", side_effect=[
                response(status=404, url=DATA_URL), response("Coming soon")]):
            self.assertEqual(fetcher.fetch(ENTRY).status, NOT_PUBLISHED)
        with patch("conferences.fetchers.aiengineer.http_get", side_effect=RuntimeError("offline")):
            self.assertEqual(fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)

    def test_official_channel_is_known_for_later_links(self):
        self.assertEqual(UPLOAD_CHANNELS["aiengineer"], "@aiDotEngineer")
        self.assertIn("ai engineer", CHANNELS["aiengineer"])
