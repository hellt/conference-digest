"""Offline regressions for RIPE, NLNOG Day and DENOG's public sources."""

from copy import deepcopy
from datetime import date
from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock, patch

import yaml
from bs4 import BeautifulSoup

from conferences.fetchers import get_fetcher
from conferences.fetchers.base import MANUAL_FALLBACK, NOT_PUBLISHED, OK
from conferences.fetchers.denog import DenogFetcher
from conferences.fetchers.nlnog import NlnogFetcher
from conferences.fetchers.ripe import RipeFetcher
from conferences.links import Context, enrich, program_items, scrape_page
from scripts.discover_editions import candidates, fill, latest_ident

RIPE = "https://ripe91.ripe.net/programme/meeting-plan/"
SESSION = RIPE + "sessions/15/"
TALK = SESSION + "ABCDEF/"
RIPE_INDEX = """
<div class="date">20 – 24 October 2025</div>
<main><a href="/programme/meeting-plan/sessions/15/">Plenary</a>
<a href="/programme/meeting-plan/sessions/15/">Duplicate mobile navigation</a>
<a href="/programme/meeting-plan/sessions/15/transcript/">Not a session</a></main>
<p>CFP closes 31 December 2025</p>
"""
RIPE_SESSION = """
<main><h1>Plenary</h1><div class="talk">
<a class="talk-title" href="ABCDEF/">Routing &amp; Security</a>
<div class="talk-speaker">Jane Doe, Example<br>John Roe, Other</div>
<div class="talk-abstract">Truncated excerpt…</div></div>
<div class="talk"><a class="talk-title" href="AOB/">A.O.B.</a></div>
<div class="talk"><a class="talk-title" href="OPEN/">Routing-wg Opening remarks</a></div>
</main>
"""
RIPE_TALK = """
<main><h1>Routing &amp; Security</h1><article class="block-talk">
<dl><dd class="talk-resources"><a href="/media/route.pdf" title="Download slides as PDF"></a>
<a href="/media/route.pptx" title="Download slides as PPTX"></a></dd></dl>
<h2>Abstract</h2><div><p>The complete routing abstract.</p><p>Security controls.</p></div>
<h2 id="video">Recording</h2><video><source src="/media/videos/route.mp4"></video>
<h2>Speakers</h2><p>Biography, not the abstract.</p></article></main>
"""
NLNOG = "https://nlnog.net/events/nlnog-day-2026/"
NLNOG_ARCHIVE = "https://nlnog.net/events/past-events/nlnog-day-2026/"
NLNOG_ALIAS = f'<meta http-equiv="refresh" content="0; url={NLNOG_ARCHIVE}"><link rel="canonical" href="{NLNOG_ARCHIVE}">'
NLNOG_PROGRAM = """
<main><h1>NLNOG Day 2026</h1><p>Held Friday, September 4th 2026 in Hilversum.</p>
<table><thead><tr><th>Time (UTC+2)</th><th>Topic</th><th>Presenter (Affiliation)</th><th>Slides</th><th>Video</th></tr></thead>
<tbody><tr><td>09:30</td><td>Welcome &amp; Opening</td><td>NLNOG crew</td><td><a href="/welcome.pdf">PDF</a></td></tr>
<tr><td>10:00</td><td>VPP eVPN Controlplane</td><td>Pim van Pelt (IPng)</td>
<td><a href="/events/nlnog-day-2026/presentations/vpp.pdf">PDF</a></td>
<td><a href="https://youtu.be/aaaaaaaaaaa?si=tracking">Video</a></td></tr>
<tr><td>10:30</td><td>Networking without the Internet</td><td>Marlies Heijkoop</td>
<td></td><td><a href="https://youtu.be/bbbbbbbbbbb?si=one">Video</a></td></tr>
<tr><td>11:00</td><td>NLNAM</td><td>Bart Dorlandt</td>
<td></td><td><a href="https://youtu.be/bbbbbbbbbbb?si=two">Video</a></td></tr>
<tr><td>12:00</td><td>Coffee Break</td><td></td></tr>
<tr><td>16:45</td><td>The Merciless NLNOG Quiz!</td><td>PowerDNS</td></tr>
</tbody></table></main><footer><a href="https://youtube.com/@NLNOG">YouTube</a></footer>
"""
DENOG = "https://www.denog.de/de/meetings/denog17/agenda.html"
DENOG_AGENDA = """<a href="https://cfp.denog.de/denog18/schedule/">Next edition navigation</a>
<a href="https://pretalx.com/denog17/schedule/">click here</a>"""
EVENT = {"title": "EVPN Flex Cross Connect", "url": "https://pretalx.com/denog17/talk/ABCDEF/",
         "persons": [{"name": "Jane Doe"}], "abstract": "Agile L2 VPNs.", "description": "Full details.",
         "attachments": [{"url": "/media/denog17/submissions/ABCDEF/resources/deck.pptx"},
                         {"url": "/media/denog17/submissions/ABCDEF/resources/deck.pdf"}]}
SCHEDULE = {"base_url": "https://pretalx.com", "conference": {
    "acronym": "denog17", "end": "2025-11-11", "days": [{"date": "2025-11-10", "rooms": {
        "Saal A": [EVENT, EVENT, {"title": "Lunch", "url": "https://example.org/lunch", "persons": []}]}}]}}


def response(html="", status=200, data=None):
    return Mock(text=html, status_code=status, headers={"content-type": "text/html"}, json=Mock(return_value=data))


def entry(url):
    return {"program_url": url, "manual_fallback_url": url}


class RipeTests(TestCase):
    def test_full_talks_not_truncated_session_cards(self):
        with patch("conferences.fetchers.ripe.http_get", side_effect=[
            response(RIPE_INDEX), response(RIPE_SESSION), response(RIPE_TALK),
        ]) as get:
            result = RipeFetcher().fetch(entry(RIPE))
        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 1)
        self.assertEqual(get.call_count, 3)
        item = program_items(result.program_text)[0]
        self.assertEqual(item.title, "Routing & Security")
        self.assertIn("Jane Doe, Example John Roe, Other", item.text)
        self.assertIn("complete routing abstract. Security controls.", item.text)
        self.assertNotIn("Truncated", item.text)
        self.assertNotIn("Biography", item.text)
        self.assertEqual(item.links, {"page": TALK, "slides": "https://ripe91.ripe.net/media/route.pdf",
                                     "slides2": "https://ripe91.ripe.net/media/route.pptx",
                                     "video": "https://ripe91.ripe.net/media/videos/route.mp4"})

    def test_failed_enrichment_uses_explicitly_labelled_excerpt(self):
        with patch("conferences.fetchers.ripe.http_get", side_effect=[
            response(RIPE_INDEX), response(RIPE_SESSION), response(status=403),
        ]):
            result = RipeFetcher().fetch(entry(RIPE))
        self.assertEqual(result.status, OK)
        self.assertIn("Truncated excerpt", result.program_text)
        self.assertIn("Full talk page unavailable; session excerpt only", result.program_text)
        self.assertNotIn("video:", result.program_text)

    def test_refresh_native_recording_and_both_decks(self):
        prompt = f"### Routing & Security\npage: {TALK}\n"
        with patch("conferences.links.HTTP.get", return_value=response(RIPE_TALK)):
            refreshed, _ = enrich("## Core\n### Routing & Security\nA pick.\n", prompt,
                                  Context(key="ripe-91", search=False, delay=0))
        self.assertIn("route.mp4", refreshed)
        self.assertIn("route.pdf", refreshed)
        self.assertIn("route.pptx", refreshed)
        with patch("conferences.links.HTTP.get", return_value=response(RIPE_SESSION)):
            self.assertEqual(scrape_page(SESSION), {})

    def test_discovery_ignores_cfp_date(self):
        with patch("conferences.fetchers.ripe.http_get", return_value=response(RIPE_INDEX)):
            probe = RipeFetcher().probe(entry(RIPE), [2025])
            self.assertTrue(probe.exists)
            self.assertEqual(probe.end_date, date(2025, 10, 24))
            self.assertIsNone(RipeFetcher().probe(entry(RIPE), [2026]).end_date)


class NlnogTests(TestCase):
    def test_alias_exact_titles_no_abstract_invention_or_shared_page(self):
        with patch("conferences.fetchers.nlnog.http_get", side_effect=[response(NLNOG_ALIAS), response(NLNOG_PROGRAM)]):
            result = NlnogFetcher().fetch(entry(NLNOG))
        self.assertEqual(result.status, OK)
        self.assertEqual(result.source_url, NLNOG_ARCHIVE)
        self.assertEqual(result.item_count, 3)
        items = program_items(result.program_text)
        self.assertEqual(items[0].title, "VPP eVPN Controlplane")
        self.assertIn("Pim van Pelt (IPng)", items[0].text)
        self.assertEqual(items[0].links["slides"], "https://nlnog.net/events/nlnog-day-2026/presentations/vpp.pdf")
        self.assertEqual(items[0].links["video"], "https://youtu.be/aaaaaaaaaaa?si=tracking")
        self.assertTrue(all("No abstract published" in i.text and "page" not in i.links for i in items))
        # A real source error in 2026: one video assigned to two different talks.
        self.assertNotIn("video", items[1].links)
        self.assertNotIn("video", items[2].links)
        self.assertNotIn("Quiz", result.program_text)

    def test_dates_and_outside_canonical_rejected(self):
        with patch("conferences.fetchers.nlnog.http_get", side_effect=[response(NLNOG_ALIAS), response(NLNOG_PROGRAM)]):
            probe = NlnogFetcher().probe(entry(NLNOG), [2026])
        self.assertEqual(probe.end_date, date(2026, 9, 4))
        with patch("conferences.fetchers.nlnog.http_get", return_value=response(NLNOG_ALIAS.replace("nlnog.net", "elsewhere.example"))) as get:
            self.assertEqual(NlnogFetcher().fetch(entry(NLNOG)).status, MANUAL_FALLBACK)
            self.assertEqual(get.call_count, 1)


class DenogTests(TestCase):
    def test_export_materials_full_abstracts_and_deduplication(self):
        with patch("conferences.fetchers.denog.http_get", side_effect=[
            response(DENOG_AGENDA), response(data={"schedule": SCHEDULE}),
        ]) as get:
            result = DenogFetcher().fetch(entry(DENOG))
        self.assertEqual(get.call_args.args[0], "https://pretalx.com/denog17/schedule/export/schedule.json")
        self.assertEqual(result.status, OK)
        self.assertEqual(result.item_count, 1)
        item = program_items(result.program_text)[0]
        self.assertEqual(item.title, EVENT["title"])
        self.assertIn("Agile L2 VPNs.\nFull details.", item.text)
        self.assertTrue(item.links["slides"].endswith("deck.pdf"))
        self.assertTrue(item.links["slides2"].endswith("deck.pptx"))
        self.assertNotIn("video", item.links)
        self.assertNotIn("Lunch", result.program_text)

    def test_new_schedule_host_and_exact_dates(self):
        schedule = deepcopy(SCHEDULE)
        schedule["base_url"] = "https://cfp.denog.de"
        schedule["conference"].update(acronym="denog18", end="2026-11-17")
        with patch("conferences.fetchers.denog.http_get", side_effect=[
            response('<a href="https://cfp.denog.de/denog18/schedule/">Agenda</a>'), response(data={"schedule": schedule}),
        ]) as get:
            probe = DenogFetcher().probe(entry(DENOG.replace("17", "18")), [2026])
        self.assertEqual(probe.end_date, date(2026, 11, 17))
        self.assertEqual(get.call_args.args[0], "https://cfp.denog.de/denog18/schedule/export/schedule.json")

    def test_wrong_export_edition_and_invalid_json_fail_safely(self):
        wrong = deepcopy(SCHEDULE)
        wrong["conference"]["acronym"] = "denog18"
        for data in ({"schedule": wrong}, None):
            with patch("conferences.fetchers.denog.http_get", side_effect=[response(DENOG_AGENDA), response(data=data)]):
                self.assertEqual(DenogFetcher().fetch(entry(DENOG)).status, MANUAL_FALLBACK)

    def test_refresh_unlabelled_decks(self):
        url = EVENT["url"]
        html = '<a href="/media/denog17/submissions/ABCDEF/resources/deck.pdf">PDF</a>'
        with patch("conferences.links.HTTP.get", return_value=response(html)):
            self.assertTrue(scrape_page(url)["slides"].endswith("deck.pdf"))


class OperatorIntegrationTests(TestCase):
    def test_failure_modes_and_empty_programs(self):
        for name, cls, url in (("ripe", RipeFetcher, RIPE), ("nlnog", NlnogFetcher, NLNOG), ("denog", DenogFetcher, DENOG)):
            self.assertIsInstance(get_fetcher(name), cls)
            for status, expected in ((404, NOT_PUBLISHED), (403, MANUAL_FALLBACK), (429, MANUAL_FALLBACK), (500, MANUAL_FALLBACK)):
                with self.subTest(name=name, status=status), patch(f"conferences.fetchers.{name}.http_get", return_value=response(status=status)):
                    self.assertEqual(cls().fetch(entry(url)).status, expected)
                    self.assertFalse(cls().probe(entry(url)).exists)
            with patch(f"conferences.fetchers.{name}.http_get", return_value=response("<main>Coming soon</main>")):
                self.assertEqual(cls().fetch(entry(url)).status, NOT_PUBLISHED)
            with patch(f"conferences.fetchers.{name}.http_get", return_value=response("Please solve CAPTCHA")):
                self.assertEqual(cls().fetch(entry(url)).status, MANUAL_FALLBACK)
            with patch(f"conferences.fetchers.{name}.http_get", side_effect=RuntimeError("offline")):
                self.assertEqual(cls().fetch(entry(url)).status, MANUAL_FALLBACK)
                self.assertFalse(cls().probe(entry(url)).exists)

    def test_new_sources_never_use_extraction_to_bypass_blocks(self):
        for url in (TALK, NLNOG, EVENT["url"], "https://cfp.denog.de/denog18/talk/ABCDEF/"):
            with self.subTest(url=url), patch("conferences.links.HTTP.get", return_value=response(status=403)), \
                 patch("conferences.links.tavily_page") as extract:
                self.assertEqual(scrape_page(url, "key"), {})
                extract.assert_not_called()

    def test_registry_and_future_series(self):
        root = Path(__file__).resolve().parents[1]
        registry = yaml.safe_load((root / "conferences/registry.yaml").read_text())["conferences"]
        series = yaml.safe_load((root / "conferences/series.yaml").read_text())["series"]
        keys = [e["key"] for e in registry]
        self.assertEqual(len(keys), len(set(keys)))
        for name, last, future, mode in (("ripe", 93, 94, "ordinal"), ("nlnog", 2026, 2027, "year"), ("denog", 18, 19, "ordinal")):
            spec = next(s for s in series if s["series"] == name)
            self.assertEqual(latest_ident(keys, spec), last)
            self.assertEqual(candidates(spec, keys, date(2026, 11, 1))[0], future)
            self.assertEqual(fill(spec["key_template"], future, mode), f"{name}-{future}")
            for e in (e for e in registry if e["fetcher"] == name):
                self.assertEqual(e["type"], "operator")
                self.assertTrue((root / "conferences/prompt/types/operator.md").exists())
                self.assertLessEqual(e.get("start_date", e["end_date"]), e["end_date"])
