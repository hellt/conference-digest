"""Offline regressions for Meta's @Scale agenda and recording pages."""

from datetime import date
from unittest import TestCase
from unittest.mock import Mock, patch

from conferences.fetchers import get_fetcher
from conferences.fetchers.atscale import AtScaleFetcher
from conferences.fetchers.base import MANUAL_FALLBACK, NOT_PUBLISHED, OK
from conferences.links import CHANNELS, UPLOAD_CHANNELS, program_items

URL = "https://atscaleconference.com/events/networking-2026/"
ENTRY = {"program_url": URL, "manual_fallback_url": URL}
TALK = """
<div class="event-agenda__accordion" id="agenda-item-4">
  <div class="event-agenda__accordion-header-title">MetaRoCE: From Spec to NIC</div>
  <div class="event-agenda__accordion-body-left">
    <a href="/videos/metaroce/">WATCH NOW</a>
  </div>
  <div class="event-agenda__accordion-body-center-text">
    <p>A multipath transport for AI fabrics.</p><p>Running in production.</p>
  </div>
  <div class="event-agenda__accordion-body-center-speaker">
    <span class="event-agenda__accordion-body-center-speaker-name">Jane Doe,
      <span class="event-agenda__accordion-body-center-speaker-company">Meta</span>
    </span>
  </div>
  <div class="event-agenda__accordion-body-center-resources">
    <a href="/metaroce-article/">read more</a>
  </div>
</div>
"""
DUPLICATE_ID = """
<div class="event-agenda__accordion" id="agenda-item-0">
  <div class="event-agenda__accordion-header-title">Keynote from Meta</div>
  <div class="event-agenda__accordion-body-center-text"><p>{description}</p></div>
</div>
"""
POSTER = """
<div class="event-agenda__accordion" id="agenda-item-20">
  <div class="event-agenda__accordion-header-title">Agent Memory at Meta Scale</div>
  <div class="event-agenda__accordion-body-center-text">
    <p><strong>Authors</strong>: Jane Doe, John Roe</p><p>A graph, vector and memory query layer.</p>
  </div>
</div>
"""
PROGRAM = f"""
<div class="hero__section">August 25, 2026 @ 8:30 AM PDT</div>
<p>July 23, 2026 July 23, 2026 July 23, 2026</p>
<div class="event-agenda__section">
  <div class="event-agenda__agenda-tab" data-tab="agenda-tab-0">
    <h3 class="event-agenda__agenda-tab-title">August 25</h3>
  </div>
  <div class="event-agenda__agenda-tab-content" id="agenda-tab-0">
    {TALK}
    <div class="event-agenda__accordion" id="agenda-item-5">
      <div class="event-agenda__accordion-header-title">Networking Happy Hour</div>
    </div>
    {DUPLICATE_ID.format(description="Opening keynote.")}
    {DUPLICATE_ID.format(description="Closing keynote.")}
  </div>
  <div class="event-agenda__agenda-tab" data-tab="agenda-tab-1">
    <h3 class="event-agenda__agenda-tab-title">Poster Sessions</h3>
  </div>
  <div class="event-agenda__agenda-tab-content" id="agenda-tab-1">{POSTER}</div>
</div>
"""
VIDEO = '<iframe id="ytplayer" src="https://www.youtube.com/embed/abcdefghijk?autoplay=0"></iframe>'


def response(html="", status=200, url=URL):
    return Mock(text=html, status_code=status, url=url)


class AtScaleTests(TestCase):
    def test_agenda_speakers_abstracts_posters_and_recording(self):
        with patch("conferences.fetchers.atscale.http_get", side_effect=[
            response(PROGRAM), response(VIDEO, url="https://atscaleconference.com/videos/metaroce/"),
        ]):
            result = AtScaleFetcher().fetch(ENTRY)
        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 4)
        items = program_items(result.program_text)
        talk = items[0]
        self.assertEqual(talk.title, "MetaRoCE: From Spec to NIC")
        self.assertIn("Speakers: Jane Doe (Meta)", talk.text)
        self.assertIn("A multipath transport for AI fabrics.\nRunning in production.", talk.text)
        self.assertEqual(talk.links, {
            "page": URL + "#agenda-item-4",
            "video": "https://www.youtube.com/watch?v=abcdefghijk",
            "materials": "https://atscaleconference.com/metaroce-article/",
        })
        # Two real talks share a title and the site's broken duplicate id=0.
        self.assertEqual([item.title for item in items[1:3]], ["Keynote from Meta"] * 2)
        self.assertTrue(all("page" not in item.links for item in items[1:3]))
        self.assertIn("Opening keynote.", items[1].text)
        self.assertIn("Closing keynote.", items[2].text)
        self.assertIn("Authors: Jane Doe, John Roe", items[3].text)
        self.assertNotIn("Authors", items[3].text.split("A graph", 1)[1])
        self.assertNotIn("Happy Hour", result.program_text)
        self.assertIn("## Poster Sessions", result.program_text)

    def test_recording_page_failure_keeps_official_watch_link(self):
        with patch("conferences.fetchers.atscale.http_get", return_value=response(status=500)):
            self.assertEqual(AtScaleFetcher()._recording("https://atscaleconference.com/videos/talk/"),
                             "https://atscaleconference.com/videos/talk/")

    def test_probe_reads_hero_not_article_dates(self):
        with patch("conferences.fetchers.atscale.http_get", return_value=response(PROGRAM)):
            result = AtScaleFetcher().probe(ENTRY, [2026])
        self.assertTrue(result.exists)
        self.assertEqual(result.end_date, date(2026, 8, 25))
        with patch("conferences.fetchers.atscale.http_get", return_value=response(PROGRAM)):
            self.assertIsNone(AtScaleFetcher().probe(ENTRY, [2027]).end_date)

    def test_failure_modes_and_empty_program(self):
        fetcher = get_fetcher("atscale")
        self.assertIsInstance(fetcher, AtScaleFetcher)
        for status, expected in ((404, NOT_PUBLISHED), (403, MANUAL_FALLBACK),
                                 (429, MANUAL_FALLBACK), (500, MANUAL_FALLBACK)):
            with self.subTest(status=status), patch("conferences.fetchers.atscale.http_get", return_value=response(status=status)):
                self.assertEqual(fetcher.fetch(ENTRY).status, expected)
                self.assertFalse(fetcher.probe(ENTRY).exists)
        with patch("conferences.fetchers.atscale.http_get", return_value=response("<main>Coming soon</main>")):
            self.assertEqual(fetcher.fetch(ENTRY).status, NOT_PUBLISHED)
        with patch("conferences.fetchers.atscale.http_get", side_effect=RuntimeError("offline")):
            self.assertEqual(fetcher.fetch(ENTRY).status, MANUAL_FALLBACK)
            self.assertFalse(fetcher.probe(ENTRY).exists)

    def test_official_channel_is_used_for_later_recordings(self):
        self.assertEqual(UPLOAD_CHANNELS["atscale"], "@scaleconference")
        self.assertIn("@scale", CHANNELS["atscale"])
