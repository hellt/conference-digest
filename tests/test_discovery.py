from pathlib import Path
from unittest import TestCase

import yaml

from scripts.discover_editions import render_entry


class DiscoveryMetadataTests(TestCase):
    def test_discovered_edition_keeps_short_conference_description(self):
        description = "A short conference summary for digest list cards."
        rendered = render_entry({
            "key": "example-41",
            "name": "Example 41",
            "description": description,
            "end_date": "2027-06-15",
            "fetcher": "example",
            "program_url": "https://example.org/program",
            "manual_fallback_url": "https://example.org/program",
            "discovered": "2026-11-15",
        })
        self.assertEqual(yaml.safe_load(rendered)[0]["description"], description)

    def test_every_series_has_a_short_card_description(self):
        path = Path(__file__).parent.parent / "conferences" / "series.yaml"
        series = yaml.safe_load(path.read_text(encoding="utf-8"))["series"]
        for spec in series:
            with self.subTest(series=spec["series"]):
                self.assertTrue(spec.get("description"))
                self.assertLessEqual(len(spec["description"]), 180)
