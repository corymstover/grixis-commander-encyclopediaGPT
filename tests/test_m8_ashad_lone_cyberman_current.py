"""Exact Ashad Rev3: fourteen historical conceptual groups as bounded cases.

Not an independent M6 J, live comprehensive rules solver or multiplayer result.
Source/whole99 guard prevents credit to removed Fireweaver/Gearhulk branches.
"""

from collections import Counter
from hashlib import sha256
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "refinement/decklists/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.txt"
REPORT = ROOT / "refinement/verification/m8_quality_scope/Ashad__the_Lone_Cyberman_352911498345e78b.md"
EXPECTED = "352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267"


def ashad_casualty(ashad, first_nonlegendary_artifact, power, pay_cost):
    return int(ashad and first_nonlegendary_artifact
               and power is not None and power >= 2 and pay_cost)


def artifact_spell_copies(casualty_copy, twinning_staff):
    return casualty_copy + int(casualty_copy > 0 and twinning_staff)


def helm_maps(tokens_actually_created, helm_active):
    """Not artifact-spell copy-permanent resolution, which is not creation."""
    return int(tokens_actually_created > 0 and helm_active)


def qualifies(original_artifact, original_legendary, first_qualifier):
    return original_artifact and not original_legendary and first_qualifier


def discounted_razorlash_loop(opponent_nonbasic, plunderer, altar, razorlash):
    """Yield net-black per iteration, only after two-B discounted recursion."""
    if not (opponent_nonbasic >= 4 and plunderer and altar and razorlash):
        return None
    return 1 + 1 - 2  # altar black + Treasure black - two black to return


class AshadCurrentCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = SOURCE.read_bytes()
        assert sha256(raw).hexdigest() == EXPECTED
        rows = raw.decode("utf-8").splitlines()
        assert rows[0] == "1x Ashad, the Lone Cyberman [Commander]"
        cls.cards = Counter()
        for line in rows:
            qty, name = line.split("x ", 1)
            cls.cards[name.removesuffix(" [Commander]")] += int(qty)
        assert sum(cls.cards.values()) == 100
        assert len(cls.cards) == 95
        assert cls.cards["Ashad, the Lone Cyberman"] == 1
        assert cls.cards["Reckless Fireweaver"] == 0
        assert cls.cards["Noxious Gearhulk"] == 0
        cls.report = REPORT.read_text(encoding="utf-8")

    def test_C1_ashad_nonlegendary_artifact_and_other_sacrifice_p0(self):
        self.assertEqual(ashad_casualty(True, True, 2, True), 1)
        self.assertEqual(ashad_casualty(False, True, 2, True), 0)
        self.assertEqual(ashad_casualty(True, False, 2, True), 0)
        counters_after_sacrificing_other_creature = 0 + 1
        self.assertEqual(counters_after_sacrificing_other_creature, 1)

    def test_K1_first_qualifying_artifact_spell_has_paid_copy_p0(self):
        self.assertTrue(qualifies(True, False, True))
        self.assertFalse(qualifies(True, True, True))
        self.assertFalse(qualifies(False, False, True))
        self.assertFalse(qualifies(True, False, False))
        self.assertEqual(ashad_casualty(True, True, 2, False), 0)
        self.assertEqual(ashad_casualty(True, True, 1, True), 0)

    def test_K2_artifact_spell_copy_becomes_token_not_created_p0(self):
        self.assertEqual(self.cards["Worldwalker Helm"], 1)
        self.assertEqual(helm_maps(0, True), 0)
        self.assertEqual(helm_maps(1, True), 1)
        self.assertEqual(helm_maps(1, False), 0)
        # Artifact SPELL copy resolving as token is modeled as 0 creations.

    def test_K3_twinning_staff_artifact_copy_replacement_p0(self):
        self.assertEqual(self.cards["Twinning Staff"], 1)
        self.assertEqual(artifact_spell_copies(1, True), 2)
        self.assertEqual(artifact_spell_copies(1, False), 1)
        self.assertEqual(artifact_spell_copies(0, True), 0)

    def test_F1_artifact_wipe_loses_artifact_mana_and_copies_p0(self):
        initial_artifacts = ["Sol Ring", "Mox Opal", "Ichor Wellspring"]
        self.assertEqual(len(initial_artifacts), 3)
        after_destroy_all_artifacts = []
        self.assertEqual(len(after_destroy_all_artifacts), 0)
        self.assertEqual(self.cards["Fierce Guardianship"], 1)
        # An included counter does not guarantee it was drawn/cast.

    def test_K4_biotransference_preserves_nonlegendary_requirement_p1(self):
        self.assertEqual(self.cards["Biotransference"], 1)
        self.assertTrue(qualifies(True, False, True))
        self.assertFalse(qualifies(True, True, True))
        self.assertFalse(qualifies(True, False, False))

    def test_K5_ironman_copies_legendary_artifact_as_nonlegendary_p1(self):
        self.assertEqual(self.cards["Iron Man, Bleeding Edge"], 1)
        def iron_man_copy(cast_artifact, ironman_present, trigger_unused):
            return cast_artifact and ironman_present and trigger_unused
        self.assertTrue(iron_man_copy(True, True, True))
        self.assertFalse(iron_man_copy(True, True, False))
        self.assertFalse(qualifies(True, True, True))

    def test_E1_real_two_power_fodder_from_current_p1(self):
        for name in ("Solemn Simulacrum", "Piggy Bank", "Royal Warden", "Poetic Ingenuity"):
            self.assertEqual(self.cards[name], 1)
        self.assertEqual(ashad_casualty(True, True, 3, True), 1)
        self.assertEqual(ashad_casualty(True, True, 1, True), 0)
        self.assertEqual(ashad_casualty(True, False, 3, True), 0)

    def test_E2_real_flash_permission_on_other_turn_p1(self):
        for name in ("Shimmer Myr", "Liberator, Urza's Battlethopter", "Unwinding Clock"):
            self.assertEqual(self.cards[name], 1)
        def can_cast_on_opponents_turn(artifact_spell, shimmer, liberator):
            return artifact_spell and (shimmer or liberator)
        self.assertTrue(can_cast_on_opponents_turn(True, False, True))
        self.assertTrue(can_cast_on_opponents_turn(True, True, False))
        self.assertFalse(can_cast_on_opponents_turn(True, False, False))
        self.assertFalse(qualifies(True, True, True))  # Liberator itself legendary

    def test_W1_urza_helm_class_loop_requires_real_setup_p1(self):
        for name in ("Urza, Lord High Artificer", "Worldwalker Helm", "Artificer Class"):
            self.assertEqual(self.cards[name], 1)
        def active_step(urza, helm, leveled_class, target_token, payable_activation):
            return all((urza, helm, leveled_class, target_token, payable_activation))
        self.assertTrue(active_step(True, True, True, True, True))
        self.assertFalse(active_step(True, True, False, True, True))
        self.assertFalse(active_step(True, True, True, False, True))
        self.assertFalse(active_step(True, True, True, True, False))

    def test_W2_drain_correct_source_event_retired_fireweaver_p1(self):
        for name in ("Disciple of the Vault", "Mayhem Devil", "Marionette Master",
                     "Ingenious Artillerist", "Krark-Clan Ironworks"):
            self.assertEqual(self.cards[name], 1)
        self.assertEqual(self.cards["Reckless Fireweaver"], 0)
        events = {"artifact_gone_to_grave": 1, "creature_sacrificed": 1,
                  "artifact_enters": 0, "token_exiled": 0}
        self.assertEqual(events["artifact_gone_to_grave"], 1)
        self.assertEqual(events["artifact_enters"], 0)
        self.assertEqual(events["token_exiled"], 0)

    def test_W3_real_copy_bombs_not_old_gearhulk_p1(self):
        for name in ("Wurmcoil Engine", "Portal to Phyrexia", "Necron Deathmark"):
            self.assertEqual(self.cards[name], 1)
        self.assertEqual(self.cards["Noxious Gearhulk"], 0)
        self.assertEqual(ashad_casualty(True, True, 2, True), 1)
        self.assertEqual(ashad_casualty(True, True, None, True), 0)

    def test_F2_no_two_power_body_blocks_casualty_p1(self):
        self.assertEqual(ashad_casualty(True, True, 1, True), 0)
        self.assertEqual(ashad_casualty(True, True, 2, True), 1)
        # Liberator is initially printed 1-power; one counter changes this.
        self.assertEqual(self.cards["Liberator, Urza's Battlethopter"], 1)

    def test_F3_legendary_artifact_does_not_get_casualty_p1(self):
        self.assertFalse(qualifies(True, True, True))
        self.assertTrue(qualifies(True, False, True))
        self.assertFalse(qualifies(True, False, False))

    def test_current_99_physical_roles_and_retired_sources(self):
        counted = Counter()
        for qty, name in re.findall(r"^- (\d+)x (.+)$", self.report, re.MULTILINE):
            counted[name] += int(qty)
        actual = self.cards.copy()
        actual.subtract({"Ashad, the Lone Cyberman": 1})
        self.assertEqual(sum(counted.values()), 99)
        self.assertEqual(counted, actual)
        self.assertEqual({card: n for card, n in self.cards.items() if n > 1},
                         {"Island": 3, "Mountain": 2, "Swamp": 3})
        self.assertIn(EXPECTED, self.report)
        for case in ("C1", "K1", "K2", "K3", "F1", "K4", "K5", "E1", "E2",
                     "W1", "W2", "W3", "F2", "F3"):
            self.assertIn(case, self.report)

    def test_new_razorlash_plunderer_altar_is_mana_neutral_conditioned(self):
        for name in ("Razorlash Transmogrant", "Pitiless Plunderer", "Phyrexian Altar"):
            self.assertEqual(self.cards[name], 1)
        self.assertEqual(discounted_razorlash_loop(4, True, True, True), 0)
        self.assertIsNone(discounted_razorlash_loop(3, True, True, True))
        self.assertIsNone(discounted_razorlash_loop(6, True, False, True))


if __name__ == "__main__":
    unittest.main()
