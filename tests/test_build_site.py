"""Offline regressions for media viewers in generated site pages."""

from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, skipUnless
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

try:
    import markdown
except ImportError:  # Installed by the site's docs dependency group.
    markdown = None

from bs4 import BeautifulSoup
import yaml

from scripts.build_site import (
    annotate_employers,
    decorate,
    employer_spans,
    link_employers,
    links_block,
    load_registry,
    media_block,
    render_companies,
    render_post,
    render_talks,
)


RECORDING = "https://ripe93.ripe.net/media/videos/routing.mp4"


class EmployerTests(TestCase):
    def test_plain_parenthetical_and_legal_suffix_attributions(self):
        cases = (
            ("Mark Tinka, TransmissionCo", "[TransmissionCo](../companies/transmissionco.md)"),
            ("Christoph Glingener (CEO, ADTRAN)", "[ADTRAN](../companies/adtran.md)"),
            ("Speakers: Eelco Chaudron, Red Hat, Inc.", "[Red Hat, Inc.](../companies/red-hat.md)"),
            ("Yoshiyuki Tabata, Hitachi, Ltd.", "[Hitachi, Ltd.](../companies/hitachi.md)"),
            ("Thomas Holterbach, University of Strasbourg",
             "[University of Strasbourg](../companies/university-of-strasbourg.md)"),
        )
        for line, link in cases:
            with self.subTest(line=line):
                self.assertIn(link, link_employers(line))

    def test_every_employer_in_compound_attribution_is_linked(self):
        line = "Murayyiam Parvez et al. (Purdue, Michigan, UCSB, Open U. Israel, NIKSUN)"
        linked = link_employers(line)
        self.assertEqual(
            {canonical for _, _, canonical in employer_spans(line)},
            {"Purdue University", "University of Michigan", "University of California, Santa Barbara",
             "Open University of Israel", "NIKSUN"},
        )
        for spelling in ("Purdue", "Michigan", "UCSB", "Open U. Israel", "NIKSUN"):
            self.assertIn(f"[{spelling}](", linked)

    def test_repeated_employer_is_linked_for_each_speaker(self):
        line = "Numan Siddique, Crusoe; Ketan Supanekar, Crusoe"
        linked = link_employers(line)
        self.assertEqual(
            [(line[s:e], canonical) for s, e, canonical in employer_spans(line)],
            [("Crusoe", "Crusoe"), ("Crusoe", "Crusoe")],
        )
        self.assertEqual(linked.count("[Crusoe](../companies/crusoe.md)"), 2)

    def test_headed_attributions_aliases_and_pick_records(self):
        rest = (
            "## Core\n"
            "### InfiniteHBD — Chenchen Shou et al. (Peking U. / StepFun / Lightelligence) — Core\n"
            "**Links:** [Abstract](https://example.org/paper)\n"
        )
        rendered, picks = annotate_employers(rest)
        self.assertEqual(len(picks), 1)
        self.assertEqual(picks[0]["employers"], ["Lightelligence", "Peking University", "StepFun"])
        for spelling in ("Peking U.", "StepFun", "Lightelligence"):
            self.assertIn(f"[{spelling}](", rendered)

    def test_missing_or_unknown_affiliation_is_not_invented(self):
        rest = "## Core\n### Routing\n\nJane Doe (no affiliation listed)\n\n**Why:** Routing matters."
        rendered, picks = annotate_employers(rest)
        self.assertEqual(rendered, rest)
        self.assertEqual(picks, [])

    def test_short_acronym_does_not_match_an_ordinary_word(self):
        self.assertEqual(employer_spans("Orderlock and its implications for protocol design"), [])
        self.assertEqual(employer_spans("Dave Ferry (ITS)"), [(12, 15, "ITS")])

    def test_employer_that_is_also_a_surname_does_not_link_speaker_name(self):
        self.assertEqual(employer_spans("Jaakko Rautanen"), [])
        line = "Jaakko Rautanen — Rautanen"
        spans = employer_spans(line)
        self.assertEqual([(line[s:e], canonical) for s, e, canonical in spans], [("Rautanen", "Rautanen")])
        self.assertEqual(link_employers(line).count("]("), 1)

    def test_employers_index_has_name_filter_and_table(self):
        with TemporaryDirectory() as tmp, patch("scripts.build_site.COMPANIES", Path(tmp) / "companies"):
            render_companies({"Cisco": [], "Arista Networks": []}, {})
            index = (Path(tmp) / "companies" / "index.md").read_text(encoding="utf-8")
        self.assertIn('<div class="conf-filter">', index)
        self.assertIn('id="company-search"', index)
        self.assertIn('placeholder="Filter by employer name"', index)
        self.assertIn('aria-label="Filter employers by name"', index)
        self.assertIn("| Employer | Talks |\n|---|---|", index)
        self.assertIn("| [Arista Networks](arista-networks.md) | 0 |", index)
        self.assertIn("| [Cisco](cisco.md) | 0 |", index)
        self.assertLess(index.index("| [Arista Networks]"), index.index("| [Cisco]"))


class PostMetadataTests(TestCase):
    def test_card_uses_registry_summary_and_location_without_changing_intro(self):
        body = "# Conference\n\nThe full digest introduction.\n\n## Core\n"
        entry = {
            "name": "Conference",
            "description": "A short conference summary.",
            "location": "Prague · Czechia",
        }
        page, _, _, _ = render_post("test-2026", entry, {}, body)
        front = yaml.safe_load(page.split("---", 2)[1])
        self.assertEqual(front["description"], "A short conference summary.")
        self.assertEqual(front["location"], "Prague · Czechia")
        self.assertIn("\nThe full digest introduction.\n\n<!-- more -->", page)

    def test_missing_registry_description_fails_instead_of_using_digest_intro(self):
        with self.assertRaisesRegex(ValueError, "test-2026: add a short description"):
            render_post("test-2026", {"name": "Conference"}, {},
                        "# Conference\n\nA long digest introduction.\n\n## Core\n")

    def test_every_registry_edition_has_a_short_card_description(self):
        for key, entry in load_registry().items():
            with self.subTest(conference=key):
                self.assertTrue(entry.get("description"))
                self.assertLessEqual(len(entry["description"]), 180)

    def test_every_published_digest_has_card_summary_and_city_country(self):
        registry = load_registry()
        for digest in (Path(__file__).parent.parent / "digests").glob("*.md"):
            with self.subTest(digest=digest.stem):
                entry = registry[digest.stem]
                self.assertTrue(entry.get("description"))
                self.assertLessEqual(len(entry["description"]), 180)
                self.assertRegex(entry.get("location", ""), r"^\S.* · .*\S$")


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


class SlideViewerTests(TestCase):
    PDF = "https://example.org/deck.pdf"
    PPTX = "https://example.org/deck.pptx"

    def test_single_format_viewer(self):
        for fmt, url in (("PDF", self.PDF), ("PPTX", self.PPTX)):
            with self.subTest(fmt=fmt):
                markup = "\n".join(media_block(f"[Slides]({url})", "Routing"))
                self.assertIn(f'=== "{fmt}"', markup)
                frames = BeautifulSoup(markup, "html.parser").find_all("iframe")
                self.assertEqual(len(frames), 1)
                frame = frames[0]
                self.assertEqual(frame["title"], f"{fmt} slides: Routing")
                self.assertEqual(frame["loading"], "lazy")
                self.assertIn("allowfullscreen", frame.attrs)
                viewer = urlsplit(frame["src"])
                if fmt == "PDF":
                    self.assertEqual(frame["src"], url)
                    self.assertNotIn("docs.google.com", markup)
                else:
                    self.assertEqual(viewer.netloc, "view.officeapps.live.com")
                    self.assertEqual(parse_qs(viewer.query), {"src": [url]})

    def test_both_formats_pptx_first_regardless_of_link_order(self):
        for decks in ((self.PDF, self.PPTX), (self.PPTX, self.PDF)):
            with self.subTest(decks=decks):
                row = " · ".join(f"[Slides ({url.rsplit('.', 1)[1].upper()})]({url})" for url in decks)
                markup = "\n".join(media_block(row, "Routing"))
                self.assertLess(markup.index('=== "PPTX"'), markup.index('=== "PDF"'))
                frames = BeautifulSoup(markup, "html.parser").find_all("iframe")
                self.assertEqual(len(frames), 2)
                self.assertIn("officeapps", frames[0]["src"])
                self.assertEqual(frames[1]["src"], self.PDF)
                self.assertEqual(markup.count('    <iframe '), 2)

    def test_url_encoding_and_html_escaping(self):
        for extension in ("PPTX", "PDF"):
            with self.subTest(extension=extension):
                url = f'https://example.org/slide%20deck.{extension}?download=1&token="value"#page=2'
                markup = "\n".join(media_block(f"[Slides]({url})", 'Routing <&> "Security"'))
                frame = BeautifulSoup(markup, "html.parser").find("iframe")
                src = frame["src"]
                self.assertEqual(parse_qs(urlsplit(src).query)["src"][0] if extension == "PPTX" else src, url)
                self.assertEqual(frame["title"], f'{extension} slides: Routing <&> "Security"')
                self.assertIn("&quot;", markup)

    def test_non_slides_and_unsupported_formats_stay_links_only(self):
        for row in (f"[Paper]({self.PDF})", "[Slides](https://example.org/talk)",
                    "[Slides (Keynote)](https://example.org/deck.key)", "No links"):
            with self.subTest(row=row):
                self.assertEqual(media_block(row, "Routing"), [])

    def test_multiple_decks_of_same_format_are_kept(self):
        row = f"[Slides (PPTX)]({self.PPTX}) · [Slides (PPTX)](https://example.org/part2.pptx)"
        markup = "\n".join(media_block(row, "Routing"))
        self.assertIn('=== "PPTX 1"', markup)
        self.assertIn('=== "PPTX 2"', markup)
        self.assertEqual(markup.count("<iframe "), 2)

    def test_viewers_only_on_talk_pages_with_source_links_preserved(self):
        row = f"**Links:** [Slides (PDF)]({self.PDF}) · [Slides (PPTX)]({self.PPTX}) · [Recording]({RECORDING})"
        body = f"# Conference\n\nIntro\n\n## Core\n### Routing\n{row}\n\n*Jane Doe*\n\n**Why:** Routing matters.\n"
        digest, _, _, talks = render_post("test-2026", {"name": "Conference", "description": "A conference."}, {}, body)
        talk = talks[0][1]
        self.assertNotIn("<iframe ", digest)
        self.assertNotIn("pick-media", digest)
        self.assertEqual(talk.count("<iframe "), 2)
        for page in (digest, talk):
            self.assertIn(f"[Slides (PDF)]({self.PDF}){{ .pick-link }}", page)
            self.assertIn(f"[Slides (PPTX)]({self.PPTX}){{ .pick-link }}", page)
            self.assertEqual(page.count("<video "), 1)
        self.assertLess(talk.index("*Jane Doe*"), talk.index("<video "))
        self.assertLess(talk.index('=== "Video"'), talk.index('=== "PPTX"'))
        self.assertLess(talk.index('=== "PPTX"'), talk.index('=== "PDF"'))
        self.assertNotIn("\n\n\n", "\n".join(media_block(row, "Routing")))
        self.assertLess(talk.index("pick-media"), talk.index("**Why:**"))

    @skipUnless(markdown, "requires the docs dependency group")
    def test_markdown_renders_one_group_with_all_three_tabs(self):
        for recording in (RECORDING, "https://youtu.be/abcdefghijk"):
            with self.subTest(recording=recording):
                row = f"[Slides]({self.PDF}) · [Slides]({self.PPTX}) · [Recording]({recording})"
                markup = "\n".join(media_block(row, "Routing"))
                html = markdown.markdown(markup, extensions=["md_in_html", "pymdownx.tabbed"],
                                         extension_configs={"pymdownx.tabbed": {"alternate_style": True}})
                soup = BeautifulSoup(html, "html.parser")
                groups = soup.select(".pick-media .tabbed-set")
                self.assertEqual(len(groups), 1)
                self.assertEqual([label.get_text() for label in groups[0].select("label")],
                                 ["Video", "PPTX", "PDF"])
                self.assertEqual(len(groups[0].select(".tabbed-block")), 3)

    def test_github_pdf_download_uses_browser_blob_loader(self):
        for host in ("media.githubusercontent.com", "raw.githubusercontent.com"):
            with self.subTest(host=host):
                url = f"https://{host}/org/repo/main/slide%20deck.pdf?raw=1&version=2"
                markup = "\n".join(media_block(f"[Slides]({url})", "Routing"))
                frame = BeautifulSoup(markup, "html.parser").find("iframe")
                self.assertEqual(frame["data-pdf-src"], url)
                self.assertNotIn("src", frame.attrs)
                self.assertNotIn("docs.google.com", markup)

    def test_youtube_video_tab_before_slides(self):
        row = f"[Slides]({self.PDF}) · [Recording](https://youtu.be/abcdefghijk?t=30s)"
        markup = "\n".join(media_block(row, "Routing"))
        self.assertLess(markup.index('=== "Video"'), markup.index('=== "PDF"'))
        thumb = BeautifulSoup(markup, "html.parser").select_one(".pick-video__thumb")
        self.assertEqual(thumb["data-yt"], "abcdefghijk")
        self.assertEqual(thumb["data-start"], "30")

    def test_recording_page_does_not_create_empty_video_tab(self):
        row = f"[Slides]({self.PDF}) · [Recording](https://vimeo.com/123456)"
        markup = "\n".join(media_block(row, "Routing"))
        self.assertNotIn('=== "Video"', markup)
        self.assertIn('=== "PDF"', markup)

    def test_viewer_without_writeup_does_not_leak_to_next_pick(self):
        rest = f"## Core\n### Routing\n**Links:** [Slides]({self.PDF})\n\n### Other talk\n**Why:** Other."
        page = decorate(rest, media_tabs=True)
        self.assertEqual(page.count("<iframe "), 1)
        self.assertLess(page.index("<iframe "), page.index("### Other talk"))
