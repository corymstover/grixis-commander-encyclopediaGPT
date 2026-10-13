import tempfile
import unittest
from pathlib import Path

from scripts.probe_forge_card_coverage import (
    REQUIRED_CONTROLS,
    audit,
    normalize_name,
    parse_deck_names,
)


class ForgeCoverageProbeTests(unittest.TestCase):
    def test_normalization_ignores_case_punctuation_and_accents(self):
        self.assertEqual(normalize_name("Lion's Eye Diamond"), normalize_name("Lions Eye Diamond"))
        self.assertEqual(normalize_name("Jóseph, the Æther-Born"), normalize_name("Joseph the Aether Born"))

    def test_parser_preserves_double_faced_name_and_copy_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "deck.txt"
            path.write_text(
                "1x Birgi, God of Storytelling // Harnfel, Horn of Bounty\n"
                "3x Island [Land]\n"
                "1x Abaddon the Despoiler [Commander]\n",
                encoding="utf-8",
            )
            names, copies = parse_deck_names(path)
            self.assertEqual(names, [
                "Birgi, God of Storytelling // Harnfel, Horn of Bounty",
                "Island",
                "Abaddon the Despoiler",
            ])
            self.assertEqual(copies["Island"], 3)
            self.assertEqual(sum(copies.values()), 5)

    def test_audit_checks_baseline_only_comparison_card_and_excludes_nonstandard_trees(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "cardsfolder"
            root.mkdir()
            variant = Path(tmp) / "variant.txt"
            variant.write_text("1x Aurora Phoenix\n", encoding="utf-8")
            control_names = list(REQUIRED_CONTROLS)
            for index, name in enumerate(control_names):
                sub = root / chr(ord("a") + index)
                sub.mkdir()
                slug = f"card_{index}.txt"
                (sub / slug).write_text(f"Name:{name}\nTypes:Instant\nOracle:{name} test text\n", encoding="utf-8")
            # A duplicate copy under a nonstandard subtree must not cause false ambiguity.
            for folder in ("rebalanced", "upcoming"):
                sub = root / folder
                sub.mkdir()
                (sub / "duplicate.txt").write_text(
                    "Name:Aurora Phoenix\nOracle:Alternate implementation\n",
                    encoding="utf-8",
                )
            report = audit(
                variant,
                root,
                ["Abaddon the Despoiler", "Mind's Desire", "Underworld Breach", "Brain Freeze", "Lion's Eye Diamond"],
            )
            self.assertTrue(report["passes_source_coverage_gate"])
            self.assertEqual(report["variant_unique_card_names"], 1)
            self.assertEqual(report["unique_names_checked"], 6)
            self.assertEqual(report["missing_or_invalid_count"], 0)
            self.assertEqual(report["standard_script_files_scanned"], 6)

    def test_audit_fails_closed_on_missing_required_control(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "cardsfolder"
            (root / "a").mkdir(parents=True)
            (root / "a" / "aurora_phoenix.txt").write_text(
                "Name:Aurora Phoenix\nOracle:Flying and cascade\n",
                encoding="utf-8",
            )
            variant = Path(tmp) / "variant.txt"
            variant.write_text("1x Aurora Phoenix\n", encoding="utf-8")
            report = audit(variant, root, [])
            self.assertFalse(report["passes_source_coverage_gate"])
            self.assertIn("Abaddon the Despoiler", report["missing_or_invalid_cards"])

    def test_empty_source_root_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "empty"
            root.mkdir()
            variant = Path(tmp) / "variant.txt"
            variant.write_text("1x Aurora Phoenix\n", encoding="utf-8")
            with self.assertRaises(RuntimeError):
                audit(variant, root, [])


if __name__ == "__main__":
    unittest.main()
