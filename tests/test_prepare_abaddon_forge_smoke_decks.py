import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.prepare_abaddon_forge_smoke_decks import (
    COMMANDER,
    EXPECTED_BASELINE_SHA256,
    parse_deck_text,
    prepare,
)


BASELINE_TEXT = (
    "1x Abaddon the Despoiler (40k) 171 [Commander{top}]\n"
    "1x Mind's Desire (c21) 123 [Draw]\n"
    "98x Island (m21) 310 [Land]\n"
)
VARIANT_TEXT = (
    "1x Abaddon the Despoiler [Commander]\n"
    "1x Aurora Phoenix\n"
    "98x Island\n"
)


class AbaddonForgeSmokeDeckTests(unittest.TestCase):
    def test_parser_strips_printing_and_role_metadata(self):
        counts, meta = parse_deck_text(BASELINE_TEXT, "baseline fixture")
        self.assertEqual(counts[COMMANDER], 1)
        self.assertEqual(counts["Mind's Desire"], 1)
        self.assertEqual(counts["Island"], 98)
        self.assertEqual(meta["line_copy_count"], 100)
        self.assertEqual(meta["commander_copy_count"], 1)

    def test_prepare_generates_only_the_registered_one_card_swap(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "archive.tar.gz"
            archive.write_bytes(b"mocked archive")
            variant = root / "variant.txt"
            variant.write_text(VARIANT_TEXT, encoding="utf-8")
            outdir = root / "forge-decks"
            with patch(
                "scripts.prepare_abaddon_forge_smoke_decks.read_frozen_baseline",
                return_value=(BASELINE_TEXT.encode("utf-8"), EXPECTED_BASELINE_SHA256),
            ):
                report = prepare(archive, variant, outdir)
            self.assertEqual(report["comparison"]["removed"], {"Mind's Desire": 1})
            self.assertEqual(report["comparison"]["added"], {"Aurora Phoenix": 1})
            self.assertEqual(report["baseline"]["line_copy_count"], 100)
            self.assertEqual(report["variant"]["line_copy_count"], 100)
            baseline = (outdir / "Abaddon baseline.dck").read_text(encoding="utf-8")
            variant_dck = (outdir / "Abaddon Aurora Phoenix variant.dck").read_text(encoding="utf-8")
            self.assertIn("[Commander]\n1 Abaddon the Despoiler\n[Main]", baseline)
            self.assertIn("1 Mind's Desire", baseline)
            self.assertNotIn("Mind's Desire", variant_dck)
            self.assertIn("1 Aurora Phoenix", variant_dck)
            baseline_main = baseline.split("[Main]\n", 1)[1].split("[Sideboard]", 1)[0].strip().splitlines()
            variant_main = variant_dck.split("[Main]\n", 1)[1].split("[Sideboard]", 1)[0].strip().splitlines()
            self.assertEqual(variant_main, ["1 Aurora Phoenix", "98 Island"])
            self.assertEqual(baseline_main, ["1 Mind's Desire", "98 Island"])
            self.assertEqual(len(baseline_main), len(variant_main))
            manifest = json.loads((outdir / "smoke-deck-manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["comparison"]["added"], {"Aurora Phoenix": 1})
            self.assertTrue(manifest["decklist_text_order_check"]["deck_text_lines_differ_only_at_registered_slot"])
            self.assertEqual(
                manifest["decklist_text_order_check"]["differences"],
                [{"slot": 0, "baseline": "Mind's Desire", "variant": "Aurora Phoenix"}],
            )

    def test_prepare_rejects_unregistered_list_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "archive.tar.gz"
            archive.write_bytes(b"mocked archive")
            variant = root / "variant.txt"
            variant.write_text(
                "1x Abaddon the Despoiler [Commander]\n1x Aurora Phoenix\n97x Island\n1x Sol Ring\n",
                encoding="utf-8",
            )
            with patch(
                "scripts.prepare_abaddon_forge_smoke_decks.read_frozen_baseline",
                return_value=(BASELINE_TEXT.encode("utf-8"), EXPECTED_BASELINE_SHA256),
            ):
                with self.assertRaisesRegex(ValueError, "exact comparison"):
                    prepare(archive, variant, root / "out")


if __name__ == "__main__":
    unittest.main()
