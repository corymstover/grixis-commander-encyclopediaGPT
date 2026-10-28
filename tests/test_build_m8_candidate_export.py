"""Fail-closed regressions for the non-certified all-62 M8 preview."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "build_m8_candidate_export", ROOT / "scripts/build_m8_candidate_export.py"
)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class M8CandidateTests(unittest.TestCase):
    def test_exact_current_roster_and_raw_receipts(self) -> None:
        decks = module.read_current()
        self.assertEqual(62, len(decks))
        self.assertEqual(6200, sum(deck["playable"] for deck in decks))
        self.assertEqual(1, sum(bool([x for x in d["cards"] if x[2] == "Companion"]) for d in decks))

    def test_fails_on_101_playable_cards(self) -> None:
        body = b"1x Example [Commander]\n100x Island\n"
        with self.assertRaisesRegex(ValueError, "expected 100 playable cards"):
            module.parse_cards(body, "Example")

    def test_nazgul_copy_rule_is_bounded(self) -> None:
        bad = "1x Example [Commander]\n10x Nazgûl\n89x Swamp\n".encode("utf-8")
        with self.assertRaisesRegex(ValueError, "illegal copy count"):
            module.parse_cards(bad, "Example")

    def test_project_companion_not_inside_commander_100(self) -> None:
        body = (b"1x Bjorna, Nightfall Alchemist [Commander]\n"
                b"1x Cecily, Haunted Mage [Commander]\n98x Island\n"
                b"1x Lutri, the Spellchaser [Companion]\n")
        cards, playable = module.parse_cards(body, "Cecily__Bjorna__Lutri")
        self.assertEqual(100, playable)
        self.assertEqual(101, sum(q for q, _, _ in cards))

    def test_packaged_preview_remains_uncertified(self) -> None:
        module.check()


if __name__ == "__main__":
    unittest.main()
