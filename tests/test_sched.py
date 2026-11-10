import unittest
from unittest.mock import Mock, patch

from conferences.fetchers.base import MANUAL_FALLBACK, OK
from conferences.fetchers.sched import SchedFetcher

URL = "https://example.sched.com/list/descriptions/"
ENTRY = {"key": "example", "program_url": URL, "manual_fallback_url": URL}
HTML = """
<div class="sched-container">
  <h2>Opening</h2>
  <div class="sched-event-details-roles">Ada Example</div>
  <div class="tip-description">The opening talk.</div>
  <a href="/event/abc123/opening">Opening</a>
</div>
"""
MARKDOWN = """
# Schedule
[Opening](https://example.sched.com/event/abc123/opening)
Ada Example

The opening talk.
[Second talk](https://example.sched.com/event/def456/second-talk)
Grace Example

The second talk.
[Opening duplicate](https://example.sched.com/event/abc123/opening?utm_source=duplicate)
"""


def response(status, text=""):
    return Mock(status_code=status, text=text)


class SchedFetchTest(unittest.TestCase):
    def test_direct_retry_recovers_transient_challenge(self):
        with (
            patch("conferences.fetchers.sched.http_get", side_effect=[response(503), response(200, HTML)]) as get,
            patch("conferences.fetchers.sched.time.sleep") as sleep,
            patch("conferences.fetchers.sched.tavily_extract") as extract,
        ):
            result = SchedFetcher().fetch(ENTRY)

        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 1)
        self.assertIn("direct attempt 2", result.detail)
        self.assertEqual(get.call_count, 2)
        sleep.assert_called_once_with(2)
        extract.assert_not_called()

    def test_tavily_is_used_after_all_direct_attempts_are_blocked(self):
        with (
            patch("conferences.fetchers.sched.http_get", return_value=response(403)) as get,
            patch("conferences.fetchers.sched.time.sleep"),
            patch("conferences.fetchers.sched.tavily_extract", return_value=MARKDOWN) as extract,
            patch.dict("os.environ", {"TAVILY_API_KEY": "test-key"}),
        ):
            result = SchedFetcher().fetch(ENTRY)

        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 2)
        self.assertIn("### Opening\npage: https://example.sched.com/event/abc123/opening", result.program_text)
        self.assertIn("### Second talk", result.program_text)
        self.assertNotIn("utm_source=duplicate", result.program_text)
        self.assertEqual(get.call_count, 3)
        extract.assert_called_once_with(URL, "test-key")

    def test_manual_requires_direct_and_tavily_failures(self):
        with (
            patch("conferences.fetchers.sched.http_get", return_value=response(503)) as get,
            patch("conferences.fetchers.sched.time.sleep"),
            patch("conferences.fetchers.sched.tavily_extract", side_effect=RuntimeError("fetch failed")),
            patch.dict("os.environ", {"TAVILY_API_KEY": "test-key"}),
        ):
            result = SchedFetcher().fetch(ENTRY)

        self.assertEqual(result.status, MANUAL_FALLBACK)
        self.assertEqual(get.call_count, 3)
        self.assertIn("3 direct attempts failed", result.detail)
        self.assertIn("Tavily Extract also failed", result.detail)

    def test_empty_reachable_schedule_is_not_retried_or_sent_to_tavily(self):
        with (
            patch("conferences.fetchers.sched.http_get", return_value=response(200, "<html></html>")) as get,
            patch("conferences.fetchers.sched.tavily_extract") as extract,
        ):
            result = SchedFetcher().fetch(ENTRY)

        self.assertEqual(result.status, "not_published")
        get.assert_called_once()
        extract.assert_not_called()


if __name__ == "__main__":
    unittest.main()
