"""Mishra, Eminent One original P1: actual bounded Helm/Urza cost transitions.

Verifies an inductively extendable combo in a deliberately restricted engine
and its negative cases; original broad W3 and table-speed F3 remain deferred.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DECK = "Mishra__Eminent_One"
SHA = "0fa7b00d9d74b208f3fd5783b30aa190c4e5b17e72ea64851f895315f05083a0"
CASES = {"K4", "K6", "E1", "E2", "W2", "F2"}


def helm_urza_warform_trace(*, mishra=True, helm=True, urza=True,
                           elixir=True, original_helm_untapped=True, max_activations=8):
    """Source-paid copy chain. Assumes no opponents disrupt declared targets.

    Urza allows tapping *any untapped artifact* as the cost of HIS ability
    (no tap-symbol on the summoning-sick Map). First Mishra Warform has haste.
    Later Helm copies of Warform do not copy that noncopiable temporary haste.
    Each live Helm replacement adds exactly one Map to a single token event.
    """
    if not (mishra and helm and urza):
        return {"activations": 0, "warforms": 0, "maps": 0,
                "helm_replacements": int(helm), "excess_blue_potential": 0,
                "failed": "missing-required-permanent"}
    # Mishra combat creates one Helm Warform plus one Map from original Helm.
    warforms = 1
    helms = 2  # original + the first 4/4 Helm Warform, both with replacement effect
    maps = 1
    untapped_original_helm = int(original_helm_untapped)
    fresh_warform_haste = True
    activations = 0
    for _ in range(max_activations):
        if not (fresh_warform_haste or elixir):
            return {"activations": activations, "warforms": warforms,
                    "maps": maps, "helm_replacements": helms,
                    "excess_blue_potential": max(0, maps - 2),
                    "failed": "summoning-sickness"}
        # Each ability costs {1}{U}, tap the current fresh Warform; Urza's
        # separate mana ability taps other untapped artifact(s) for blue.
        available = maps + untapped_original_helm
        if available < 2:
            return {"activations": activations, "warforms": warforms,
                    "maps": maps, "helm_replacements": helms,
                    "excess_blue_potential": 0, "failed": "cannot-pay-1U"}
        needed = 2
        tapped_original = min(untapped_original_helm, needed)
        untapped_original_helm -= tapped_original
        needed -= tapped_original
        maps -= needed
        # The copy event sees only the helm replacement sources that existed
        # BEFORE it; the new copied Warform can't modify its own creation.
        maps_added = helms
        warforms += 1
        maps += maps_added
        helms += 1
        fresh_warform_haste = False
        activations += 1
    # Preserve two untapped Maps for the next cost; all others can be tapped
    # at no additional resource cost through Urza to produce blue mana.
    return {"activations": activations, "warforms": warforms,
            "maps": maps, "helm_replacements": helms,
            "excess_blue_potential": max(0, maps - 2), "failed": None}


def slaver_warform_controls(*, original_mindslaver, mana, copied_trigger,
                           separate_legend_resolution, haste):
    """Mindslaver Warform copies preserve original legendary supertype."""
    if not original_mindslaver or not haste:
        return 0
    activation_cost = 4
    copy_trigger_cost = 2 if copied_trigger else 0
    if mana < activation_cost + copy_trigger_cost:
        return 0
    if not copied_trigger:
        return 1
    # Two legendary Warforms named Mishra's Warform cannot coexist.
    # Need activate/sacrifice the first between two trigger resolutions.
    return 2 if separate_legend_resolution and mana >= copy_trigger_cost + 2 * activation_cost else 1


def wellspring_warform_draws(*, copied_wellspring, token_enters,
                            went_from_battlefield_to_graveyard):
    return int(copied_wellspring and token_enters) + int(
        copied_wellspring and token_enters and went_from_battlefield_to_graveyard)


def kci_warform_mana(*, artifact_token_present, kci_present):
    return 2 if artifact_token_present and kci_present else 0


def transmuter_uses_warform(*, token_available, untapped_transmuter,
                            blue_paid, actual_artifact_card_in_hand):
    return bool(token_available and untapped_transmuter and blue_paid and actual_artifact_card_in_hand)


def mishra_combat_trigger_result(*, mishra_present, legal_noncreature_artifact_target,
                                 target_survives_to_resolution):
    return int(mishra_present and legal_noncreature_artifact_target and target_survives_to_resolution)


class MishraEminentP1Trace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        row = next(x for x in index["decks"] if x["deck_id"] == DECK)
        raw = (ROOT / row["source_file"]).read_bytes()
        assert sha256(raw).hexdigest() == row["source_sha256"] == SHA
        cls.cards = Counter()
        for line in raw.decode().splitlines():
            count, card = line.split("x ", 1)
            cls.cards[card.replace(" [Commander]", "")] += int(count)
        assert sum(cls.cards.values()) == 100
        receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                              / f"{DECK}_{SHA[:16]}.json").read_text())
        assert receipt["approved_raw_sha256"] == SHA
        cls.deferred = {r["case_id"] for r in receipt["m6_transfer"]["P1"]
                        if r["status"] == "DEFERRED"}

    def source(self, case, *cards):
        self.assertIn(case, self.deferred)
        for card in cards:
            self.assertIn(card, self.cards)

    def test_K4_mindslaver_warform_paid_priority_and_legendary_conflict(self):
        self.source("K4", "Mishra, Eminent One", "Mindslaver", "Strionic Resonator")
        self.assertEqual(slaver_warform_controls(original_mindslaver=True, mana=4,
                                                copied_trigger=False,
                                                separate_legend_resolution=False, haste=True), 1)
        self.assertEqual(slaver_warform_controls(original_mindslaver=True, mana=10,
                                                copied_trigger=True,
                                                separate_legend_resolution=True, haste=True), 2)
        self.assertEqual(slaver_warform_controls(original_mindslaver=True, mana=10,
                                                copied_trigger=True,
                                                separate_legend_resolution=False, haste=True), 1)
        self.assertEqual(slaver_warform_controls(original_mindslaver=True, mana=9,
                                                copied_trigger=True,
                                                separate_legend_resolution=True, haste=True), 1)
        self.assertEqual(slaver_warform_controls(original_mindslaver=False, mana=10,
                                                copied_trigger=True,
                                                separate_legend_resolution=True, haste=True), 0)

    def test_K6_helm_urza_elixir_repeats_and_produces_maps_without_new_mana(self):
        self.source("K6", "Mishra, Eminent One", "Worldwalker Helm",
                    "Urza, Lord High Artificer", "Thousand-Year Elixir")
        first = helm_urza_warform_trace(max_activations=1)
        self.assertEqual((first["warforms"], first["maps"], first["helm_replacements"]), (2, 2, 3))
        longer = helm_urza_warform_trace(max_activations=8)
        self.assertEqual(longer["activations"], 8)
        self.assertEqual(longer["warforms"], 9)
        self.assertEqual(longer["helm_replacements"], 10)
        self.assertGreater(longer["maps"], 20)
        self.assertGreater(longer["excess_blue_potential"], 20)
        self.assertIsNone(longer["failed"])
        self.assertEqual(helm_urza_warform_trace(elixir=False)["failed"], "summoning-sickness")
        self.assertEqual(helm_urza_warform_trace(urza=False)["activations"], 0)
        self.assertEqual(helm_urza_warform_trace(original_helm_untapped=False)["failed"],
                         "cannot-pay-1U")

    def test_E1_wellspring_enters_and_is_sacrificed_at_next_endstep(self):
        self.source("E1", "Mishra, Eminent One", "Ichor Wellspring")
        self.assertEqual(wellspring_warform_draws(copied_wellspring=True,
                                                 token_enters=True,
                                                 went_from_battlefield_to_graveyard=True), 2)
        self.assertEqual(wellspring_warform_draws(copied_wellspring=True,
                                                 token_enters=True,
                                                 went_from_battlefield_to_graveyard=False), 1)
        self.assertEqual(wellspring_warform_draws(copied_wellspring=False,
                                                 token_enters=False,
                                                 went_from_battlefield_to_graveyard=False), 0)

    def test_E2_warform_sacrifice_mana_and_transmuter_require_actual_assets(self):
        self.source("E2", "Krark-Clan Ironworks", "Master Transmuter", "Mishra, Eminent One")
        self.assertEqual(kci_warform_mana(artifact_token_present=True, kci_present=True), 2)
        self.assertEqual(kci_warform_mana(artifact_token_present=False, kci_present=True), 0)
        self.assertTrue(transmuter_uses_warform(token_available=True, untapped_transmuter=True,
                                               blue_paid=True, actual_artifact_card_in_hand=True))
        self.assertFalse(transmuter_uses_warform(token_available=True, untapped_transmuter=True,
                                                blue_paid=True, actual_artifact_card_in_hand=False))

    def test_W2_helm_combo_inductive_unbounded_token_and_mana_growth(self):
        self.source("W2", "Mishra, Eminent One", "Worldwalker Helm", "Urza, Lord High Artificer",
                    "Thousand-Year Elixir")
        a = helm_urza_warform_trace(max_activations=4)
        b = helm_urza_warform_trace(max_activations=8)
        self.assertEqual(a["activations"], 4)
        self.assertEqual(b["activations"], 8)
        self.assertGreater(b["maps"], a["maps"])
        self.assertGreater(b["excess_blue_potential"], a["excess_blue_potential"])
        self.assertGreater(b["helm_replacements"], a["helm_replacements"])
        self.assertIsNone(b["failed"])
        # Induction: each completed activation adds one future Warform Helm
        # source plus N Maps, where N is the pre-existing Helm count (>=2).
        # Leave >=2 untapped Maps each time to pay the next {1}{U}; any excess
        # generates arbitrarily many extra U via Urza as turns repeat.
        self.assertEqual(helm_urza_warform_trace(elixir=False)["activations"], 1)
        self.assertEqual(helm_urza_warform_trace(helm=False)["activations"], 0)

    def test_F2_removed_target_before_resolution_fails_not_after_token_exists(self):
        self.source("F2", "Mishra, Eminent One", "Ichor Wellspring", "Chaos Warp")
        self.assertEqual(mishra_combat_trigger_result(mishra_present=True,
                                                     legal_noncreature_artifact_target=True,
                                                     target_survives_to_resolution=True), 1)
        self.assertEqual(mishra_combat_trigger_result(mishra_present=True,
                                                     legal_noncreature_artifact_target=True,
                                                     target_survives_to_resolution=False), 0)
        self.assertEqual(mishra_combat_trigger_result(mishra_present=False,
                                                     legal_noncreature_artifact_target=True,
                                                     target_survives_to_resolution=True), 0)

    def test_unproven_W3_and_F3_not_assumed_resolved(self):
        self.assertEqual(self.deferred, CASES | {"W3", "F3"})


if __name__ == "__main__":
    unittest.main()
