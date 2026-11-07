"""Offline regressions for OPI Summit material links."""

from datetime import date
from unittest import TestCase

from conferences.links import Context, Video, classify, verify


TALK = ("KV Cache in the Agentic Era: The Five Forces that Decide Where the Cache Lives, "
        "and What a DPU Can Do About It - Jigar Kuverji Savla, Tensordyne")
VIDEO = Video(
    "noXNOdN-rsA",
    "KV Cache in the Agentic Era",
    "Open Programmable Infrastructure (OPI) Project",
    published=date(2026, 10, 26),
    seconds=2227,
)


class OpiLinksTest(TestCase):
    def test_shortened_recording_title_on_official_channel(self):
        ctx = Context("opi-2026", end_date=date(2026, 10, 15))
        self.assertTrue(verify(TALK, VIDEO, ctx))

    def test_shortened_recording_title_requires_the_conference(self):
        ctx = Context("opi-2026", end_date=date(2026, 10, 15))
        unrelated = Video(VIDEO.id, VIDEO.title, "Another channel", published=VIDEO.published)
        self.assertFalse(verify(TALK, unrelated, ctx))

    def test_current_sched_deck_host_is_slides(self):
        found = {}
        classify(found, "https://hosted-files.sched.co/opisummit2026/2e/deck.pdf", "OPI deck")
        self.assertEqual(found["slides"], "https://hosted-files.sched.co/opisummit2026/2e/deck.pdf")
