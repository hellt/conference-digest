from unittest import TestCase

from scripts.propose_digest import tag_note


class TagNoteTests(TestCase):
    def test_missing_keywords_and_partial_tagging_are_visible(self):
        self.assertIn("all 1 picks", tag_note("demo", "### Talk A\n", ""))
        self.assertEqual(tag_note("demo", "### Talk A\n", "```json\n{}\n```", {"Talk A": ["ai"]}), "")
        note = tag_note("demo", "### Talk A\n### Talk B\n", "```json\n{}\n```",
                        {"Talk A": ["ai"], "Talk B": []})
        self.assertIn("1/2 picks", note)
        self.assertIn("Talk B", note)
        self.assertIn("--digest demo", note)

    def test_invalid_keywords_remain_a_manual_backfill_item(self):
        note = tag_note("demo", "### Talk A\n", "```json\nnot json\n```", error="bad JSON")
        self.assertIn("Search tags unusable (bad JSON)", note)
        self.assertIn("Backfill", note)
