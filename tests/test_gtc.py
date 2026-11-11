"""Offline regressions for NVIDIA GTC's on-demand session materials."""

from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock, patch

import requests

from conferences.links import ROW, Context, enrich, link_alive, links_row, parse_row, scrape_page


CATALOG = "https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-s81625/"
ON_DEMAND = "https://www.nvidia.com/en-us/on-demand/session/gtc26-s81625/"
VIDEO = ON_DEMAND + "#watch"
UNSIGNED_KALTURA = (
    "https://cdnapisec.kaltura.com/p/2935771/sp/293577100/"
    "embedIframeJs/uiconf_id/56782552/partner_id/2935771"
    "?iframeembed=true&playerId=kaltura_player&entry_id=1_uejgczqp"
)
DOWNLOAD = (
    "https://cfvod.kaltura.com/api_v3/index.php/service/"
    "attachment_attachmentAsset/action/serve/attachmentAssetId/1_l6d19qoq/ks/signed"
)


def response(data, status=200):
    return Mock(status_code=status, json=Mock(return_value=data))


def session(assets=None, session_id="gtc26-s81625"):
    return {
        "responseCode": 200,
        "sessionData": {
            "sessionID": session_id,
            "assets": [
                {
                    "fileType": "PDF",
                    "url": "urn:nvidia:events:assets:kaltura:1_l6d19qoq",
                    "viewFileAccess": "public",
                },
                {
                    "fileType": "Video",
                    "url": "urn:nvidia:events:kaltura:1_uejgczqp",
                    "viewFileAccess": "public",
                },
            ] if assets is None else assets,
        },
    }


class GtcOnDemandTests(TestCase):
    def test_published_picks_all_have_slides_or_a_recording(self):
        digest = (Path(__file__).resolve().parents[1] / "digests/gtc-2026.md").read_text()
        heading = ""
        missing = []
        for line in digest.splitlines():
            if line.startswith("### "):
                heading = line[4:]
            row = ROW.match(line)
            if row:
                links = parse_row(row.group(1))
                if not links.get("slides") and not links.get("video"):
                    missing.append(heading)
        self.assertEqual(missing, [])

    def test_public_video_pdf_and_talk_page(self):
        escaped = DOWNLOAD.replace("/", r"\/")
        with patch("conferences.links.HTTP.get", side_effect=[
            response(session()), response({"asset-url": escaped}),
        ]) as get:
            links = scrape_page(CATALOG)
        self.assertEqual(links, {"video": VIDEO, "talk": ON_DEMAND, "slides": DOWNLOAD})
        self.assertEqual(get.call_args_list[0].args[0],
                         "https://api-prod.nvidia.com/services/nod/api/v1/session")
        self.assertEqual(get.call_args_list[0].kwargs["params"], {"id": "gtc26-s81625"})
        self.assertEqual(get.call_args_list[1].kwargs["params"],
                         {"kaltura-asset-id": "1_l6d19qoq", "session-id": "gtc26-s81625"})

    def test_talk_page_round_trips_before_pdf_and_recording(self):
        links = {"video": VIDEO, "talk": ON_DEMAND, "slides": DOWNLOAD}
        row = links_row(links)
        self.assertEqual(row, f"**Links:** [Talk page]({ON_DEMAND}) · [Slides]({DOWNLOAD}) · [Recording]({VIDEO})")
        self.assertEqual(parse_row(row.removeprefix("**Links:** ")), links)

    def test_refresh_adds_all_materials_to_the_core_pick(self):
        program = "### Build Secure AI Infrastructure With DOCA\n" + f"page: {CATALOG}\n"
        digest = "## Core\n### Build Secure AI Infrastructure With DOCA\nA pick.\n"
        with patch("conferences.links.scrape_page", return_value={
            "video": VIDEO, "talk": ON_DEMAND, "slides": DOWNLOAD,
        }), patch("conferences.links.link_alive", return_value=True):
            refreshed, stats = enrich(digest, program,
                                      Context(key="gtc-2026", search=False, delay=0))
        self.assertIn(f"[Abstract]({CATALOG}) · [Talk page]({ON_DEMAND})", refreshed)
        self.assertIn(f"[Slides]({DOWNLOAD}) · [Recording]({VIDEO})", refreshed)
        self.assertEqual(stats["video_from_page"], 1)
        self.assertEqual(stats["slides"], 1)

    def test_refresh_renews_a_signed_pdf_without_duplicating_the_video(self):
        old = DOWNLOAD.replace("signed", "expired")
        program = "### Build Secure AI Infrastructure With DOCA\n" + f"page: {CATALOG}\n"
        digest = ("## Core\n### Build Secure AI Infrastructure With DOCA\n"
                  f"**Links:** [Abstract]({CATALOG}) · [Talk page]({ON_DEMAND}) · "
                  f"[Slides]({old}) · [Recording]({VIDEO})\nA pick.\n")
        with patch("conferences.links.scrape_page", return_value={
            "video": VIDEO, "talk": ON_DEMAND, "slides": DOWNLOAD,
        }) as scrape, patch("conferences.links.link_alive", return_value=True):
            refreshed, stats = enrich(digest, program,
                                      Context(key="gtc-2026", search=False, delay=0))
        scrape.assert_called_once()
        self.assertNotIn(old, refreshed)
        self.assertEqual(refreshed.count(f"[Recording]({VIDEO})"), 1)
        self.assertEqual(stats["video_from_page"], 0)

    def test_refresh_preserves_verified_youtube_instead_of_replacing_it(self):
        youtube = "https://www.youtube.com/watch?v=FjVjaxej7Yk"
        program = "### Build Secure AI Infrastructure With DOCA\n" + f"page: {CATALOG}\n"
        digest = ("## Core\n### Build Secure AI Infrastructure With DOCA\n"
                  f"**Links:** [Abstract]({CATALOG}) · [Recording]({youtube})\nA pick.\n")
        with patch("conferences.links.scrape_page", return_value={
            "video": VIDEO, "talk": ON_DEMAND, "slides": DOWNLOAD,
        }), patch("conferences.links.link_alive", return_value=True):
            refreshed, _ = enrich(digest, program,
                                  Context(key="gtc-2026", search=False, delay=0))
        self.assertIn(f"[Recording]({youtube})", refreshed)
        self.assertNotIn(f"[Recording]({VIDEO})", refreshed)

    def test_kaltura_access_control_is_dead_despite_http_200(self):
        for headers, expected in (({"X-Kaltura-App": "exiting on error 3 - entry restricted due to access-control"}, False),
                                  ({"Content-Type": "application/pdf"}, True)):
            resp = Mock(status_code=200, headers=headers)
            with self.subTest(headers=headers), patch("conferences.links.HTTP.get", return_value=resp):
                self.assertIs(link_alive(DOWNLOAD), expected)
            resp.close.assert_called_once()

    def test_missing_or_private_assets_invent_no_links(self):
        assets = [
            {"fileType": "PDF", "url": "urn:nvidia:events:assets:kaltura:1_l6d19qoq",
             "viewFileAccess": "developer"},
            {"fileType": "Video", "url": "https://example.org/other-talk",
             "viewFileAccess": "public"},
        ]
        for data in (session([]), session(assets), {"responseCode": 404},
                     session(session_id="gtc26-other"), [], {"sessionData": []}):
            with self.subTest(data=data), patch("conferences.links.HTTP.get",
                                                return_value=response(data)) as get:
                self.assertEqual(scrape_page(CATALOG), {})
                self.assertEqual(get.call_count, 1)

    def test_unsigned_kaltura_player_is_dead(self):
        with patch("conferences.links.HTTP.get") as get:
            self.assertIs(link_alive(UNSIGNED_KALTURA), False)
        get.assert_not_called()

    def test_refresh_replaces_obsolete_kaltura_player_with_on_demand(self):
        program = "### Build Secure AI Infrastructure With DOCA\n" + f"page: {CATALOG}\n"
        digest = ("## Core\n### Build Secure AI Infrastructure With DOCA\n"
                  f"**Links:** [Abstract]({CATALOG}) · [Recording]({UNSIGNED_KALTURA})\nA pick.\n")
        with patch("conferences.links.scrape_page", return_value={
            "video": VIDEO, "talk": ON_DEMAND, "slides": DOWNLOAD,
        }), patch("conferences.links.link_alive", return_value=True):
            refreshed, _ = enrich(digest, program,
                                  Context(key="gtc-2026", search=False, delay=0))
        self.assertIn(f"[Recording]({VIDEO})", refreshed)
        self.assertNotIn(UNSIGNED_KALTURA, refreshed)

    def test_download_failure_keeps_verified_video_and_talk_page(self):
        with patch("conferences.links.HTTP.get", side_effect=[
            response(session()), requests.Timeout("offline"),
        ]):
            self.assertEqual(scrape_page(CATALOG), {"video": VIDEO, "talk": ON_DEMAND})

    def test_unexpected_download_target_is_not_linked(self):
        for download in (DOWNLOAD.replace("1_l6d19qoq", "other"),
                         DOWNLOAD.replace("cfvod.kaltura.com", "example.org"), "not a URL"):
            with self.subTest(download=download), patch("conferences.links.HTTP.get", side_effect=[
                response(session()), response({"asset-url": download}),
            ]):
                self.assertEqual(scrape_page(CATALOG), {"video": VIDEO, "talk": ON_DEMAND})
