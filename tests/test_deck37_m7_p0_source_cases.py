"""Bounded source-mapped Deck 37 M7 P0 mechanics, not a Magic rules engine.

These finite fixtures explicitly test both positive and invalid preconditions
for the five M6 P0 blueprint cases on the exact approved 100-card revision.
They complement (not replace) the October 26 Scryfall source snapshot.
"""

import hashlib
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "refinement/decklists/Mishra_Eminent_One_M7_Rev1_Approved_2026-10-26.txt"
if not DECK.is_file() and (ROOT / "mishra_eminent_one_m7_rev1_candidate.txt").is_file():
    DECK = ROOT / "mishra_eminent_one_m7_rev1_candidate.txt"  # local test-only mirror
SHA = "0fa7b00d9d74b208f3fd5783b30aa190c4e5b17e72ea64851f895315f05083a0"


def combat_warform(*, mishra_present, own_combat_start, owned_source,
                   source_noncreature_artifact, source_exists_on_resolution,
                   source_mv):
    """Model exact basic conditions of Mishra's triggered token copy."""
    if not (mishra_present and own_combat_start and owned_source
            and source_noncreature_artifact and source_exists_on_resolution):
        return None
    return {"name": "Mishra's Warform", "mv": source_mv,
            "artifact": True, "creature": True, "power": 4,
            "toughness": 4, "haste": True, "sacrifice_next_end_step": True}


def iteration_populate(*, mishra_resolves_first, existing_tokens):
    """Beginning-combat trigger order controls token population opportunities."""
    tokens = list(existing_tokens)
    if mishra_resolves_first:
        tokens.append("Warform")
    if tokens:
        tokens.append(tokens[-1])
    if not mishra_resolves_first:
        tokens.append("Warform")
    return tokens


def bay_finds_mv(*, warform_source_mv, artifact_in_play_at_main_phase,
                 target_artifact_mv):
    """Repurposing Bay searches exact one-greater MV after its cost."""
    return artifact_in_play_at_main_phase and target_artifact_mv == warform_source_mv + 1


def transmute_additional_cost(*, sacrificed_mv, searched_mv):
    """Transmute Artifact resolution payment when searched MV exceeds sacrificed."""
    return max(0, searched_mv - sacrificed_mv)


def effigy_to_warform(*, effigy_is_noncreature, copied_creature_abilities,
                      artifact_tap_blue_ability):
    """Effigy copy-as-noncreature keeps its copied values through Warform copy."""
    if not effigy_is_noncreature:
        return None
    return {"name": "Mishra's Warform", "artifact_creature": True,
            "haste": True, "copied_abilities": copied_creature_abilities,
            "tap_blue": artifact_tap_blue_ability}


def removal_timing(*, mishra_present_at_combat_trigger,
                   removed_after_trigger, source_target_still_valid):
    """Removing source of an already triggered ability does not erase trigger."""
    return mishra_present_at_combat_trigger and source_target_still_valid


class Deck37M7SourceCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = DECK.read_bytes()
        if hashlib.sha256(raw).hexdigest() != SHA:
            raise AssertionError("Exact source-list SHA mismatch")
        cls.cards = {line.split("x ", 1)[1].removesuffix(" [Commander]")
                     for line in raw.decode("utf-8").splitlines()}

    def test_C1_mishra_trigger_target_and_next_end_step(self):
        self.assertIn("Mishra, Eminent One", self.cards)
        token = combat_warform(mishra_present=True, own_combat_start=True,
                               owned_source=True, source_noncreature_artifact=True,
                               source_exists_on_resolution=True, source_mv=6)
        self.assertEqual((token["name"], token["power"], token["toughness"],
                          token["mv"], token["haste"], token["sacrifice_next_end_step"]),
                         ("Mishra's Warform", 4, 4, 6, True, True))
        for missing in ("mishra_present", "own_combat_start", "owned_source",
                        "source_noncreature_artifact", "source_exists_on_resolution"):
            args = dict(mishra_present=True, own_combat_start=True,
                        owned_source=True, source_noncreature_artifact=True,
                        source_exists_on_resolution=True, source_mv=6)
            args[missing] = False
            self.assertIsNone(combat_warform(**args), missing)

    def test_K1_iteration_beginning_combat_ordering(self):
        self.assertTrue({"Mishra, Eminent One", "Determined Iteration"} <= self.cards)
        self.assertEqual(iteration_populate(mishra_resolves_first=True,
                                            existing_tokens=[]), ["Warform", "Warform"])
        # If Iteration resolves first without a prior token, there is nothing
        # to populate. Mishra's Warform appears only afterward.
        self.assertEqual(iteration_populate(mishra_resolves_first=False,
                                            existing_tokens=[]), ["Warform"])

    def test_K2_warform_mana_value_bay_and_transmute(self):
        self.assertTrue({"Mishra, Eminent One", "Repurposing Bay", "Transmute Artifact"} <= self.cards)
        token = combat_warform(mishra_present=True, own_combat_start=True,
                               owned_source=True, source_noncreature_artifact=True,
                               source_exists_on_resolution=True, source_mv=5)
        self.assertEqual(token["mv"], 5)
        self.assertTrue(bay_finds_mv(warform_source_mv=token["mv"],
                                     artifact_in_play_at_main_phase=True,
                                     target_artifact_mv=6))
        self.assertFalse(bay_finds_mv(warform_source_mv=5,
                                      artifact_in_play_at_main_phase=True,
                                      target_artifact_mv=7))
        self.assertFalse(bay_finds_mv(warform_source_mv=5,
                                      artifact_in_play_at_main_phase=False,
                                      target_artifact_mv=6))
        self.assertEqual(transmute_additional_cost(sacrificed_mv=5, searched_mv=7), 2)
        self.assertEqual(transmute_additional_cost(sacrificed_mv=5, searched_mv=3), 0)

    def test_K3_machine_gods_effigy_copiable_values(self):
        self.assertTrue({"Mishra, Eminent One", "Machine God's Effigy", "Master Transmuter"} <= self.cards)
        token = effigy_to_warform(effigy_is_noncreature=True,
                                  copied_creature_abilities=("Master Transmuter activated ability",),
                                  artifact_tap_blue_ability=True)
        self.assertTrue(token["artifact_creature"] and token["haste"] and token["tap_blue"])
        self.assertIn("Master Transmuter activated ability", token["copied_abilities"])
        self.assertIsNone(effigy_to_warform(effigy_is_noncreature=False,
                                            copied_creature_abilities=(),
                                            artifact_tap_blue_ability=True))

    def test_F1_mishra_removed_before_vs_after_combat_trigger(self):
        self.assertTrue(removal_timing(mishra_present_at_combat_trigger=True,
                                       removed_after_trigger=True,
                                       source_target_still_valid=True))
        self.assertFalse(removal_timing(mishra_present_at_combat_trigger=False,
                                        removed_after_trigger=False,
                                        source_target_still_valid=True))
        self.assertFalse(removal_timing(mishra_present_at_combat_trigger=True,
                                        removed_after_trigger=True,
                                        source_target_still_valid=False))


if __name__ == "__main__":
    unittest.main()
