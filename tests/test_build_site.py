"""Offline regressions for recording players in generated site pages."""

from unittest import TestCase

from bs4 import BeautifulSoup

from scripts.build_site import decorate, links_block, render_talks


RECORDING = "https://ripe93.ripe.net/media/videos/routing.mp4"


class RecordingTests(TestCase):
    def test_native_recording_player(self):
        links, player = links_block(f"[Recording]({RECORDING})", "Routing & Security")
        video = BeautifulSoup("\n".join(player), "html.parser").find("video")
        self.assertIsNotNone(video)
        self.assertEqual(video["src"], RECORDING)
        self.assertIn("controls", video.attrs)
        self.assertIn("playsinline", video.attrs)
        self.assertEqual(video["preload"], "none")
        self.assertNotIn("autoplay", video.attrs)
        self.assertIn(RECORDING, "\n".join(links))

    def test_native_formats_and_html_escaping(self):
        for extension in ("mp4", "webm", "ogv"):
            with self.subTest(extension=extension):
                url = f'https://example.org/talk.{extension}?a=1&token="value"#t=30'
                _, player = links_block(f"[Recording]({url})", 'Routing <&> "Security"')
                markup = "\n".join(player)
                video = BeautifulSoup(markup, "html.parser").find("video")
                self.assertIsNotNone(video)
                self.assertEqual(video["src"], url)
                self.assertIn("&amp;", markup)
                self.assertIn("&quot;", markup)

    def test_youtube_keeps_click_to_play_and_timestamp(self):
        _, player = links_block("[Recording](https://youtu.be/abcdefghijk?t=1m30s)", "Routing")
        soup = BeautifulSoup("\n".join(player), "html.parser")
        self.assertIsNone(soup.find("video"))
        thumb = soup.select_one(".pick-video__thumb")
        self.assertEqual(thumb["data-yt"], "abcdefghijk")
        self.assertEqual(thumb["data-start"], "90")

    def test_recording_pages_remain_links_not_video_sources(self):
        for row in ("[Recording](https://vimeo.com/123456)", "[Slides](https://example.org/deck.pdf)"):
            with self.subTest(row=row):
                links, player = links_block(row, "Routing")
                self.assertTrue(links)
                self.assertEqual(player, [])

    def test_player_placement_in_digest_and_talk_page(self):
        lines = [f"**Links:** [Recording]({RECORDING})", "", "*Jane Doe*", "", "**Why:** Routing matters."]
        digest = decorate("## Core\n### Routing\n" + "\n".join(lines))
        pages, _ = render_talks("ripe-93", "RIPE 93", "RIPE 93", None, None,
                                [{"heading": "Routing", "tier": "core", "lines": lines}])
        for page in (digest, pages[0][1]):
            with self.subTest(page=page):
                self.assertEqual(page.count("<video "), 1)
                self.assertLess(page.index("*Jane Doe*"), page.index("<video "))
                self.assertLess(page.index("<video "), page.index("**Why:**"))
