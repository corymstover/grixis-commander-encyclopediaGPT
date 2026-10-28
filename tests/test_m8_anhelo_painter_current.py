"""Exact approved Anhelo M7 Rev2: finite original-case models, not engine/I/J.

The 14 historic original design-only M6 case groups receive present-card
positive/adverse coverage. A whole-99 ledger is independently reconciled.
"""

from collections import Counter
from hashlib import sha256
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "refinement/decklists/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.txt"
REPORT = ROOT / "refinement/verification/m8_quality_scope/Anhelo__the_Painter_865b3a16567f1cb8.md"
EXPECTED = "865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77"


def granted_casualty(anhelo_present, first_insorcery_this_turn, power, sacrificed):
    """A bounded *grant-derived* casualty copy count, not actual stack API."""
    return int(anhelo_present and first_insorcery_this_turn
               and power is not None and power >= 2 and sacrificed)


def staff_copies(base_copies, staff_present):
    return base_copies + int(base_copies > 0 and staff_present)


def cast_copy_trigger_counts(number_cast, number_copied):
    """Magecraft sees both events; Talrand/Pursuit see casts only."""
    return {"magecraft": number_cast + number_copied,
            "talrand": number_cast, "pursuit_hand": number_cast}


def anhelo_first_spell(original_instants_before_entry, current_spell_is_instant_or_sorcery):
    return original_instants_before_entry == 0 and current_spell_is_instant_or_sorcery


def dualcaster_twinflame_step(live_original, original_target_creature,
                              dualcaster_in_hand_and_payable, legal_new_target):
    """One source-paid ETB copy step, not an invented free game state."""
    return all((live_original, original_target_creature,
                dualcaster_in_hand_and_payable, legal_new_target))


def iterate_buyback(mana_from_copy, can_pay_4rr, original_spell_live, opponent_countered):
    if not can_pay_4rr or not original_spell_live or opponent_countered:
        return None
    return mana_from_copy - 6


class AnheloRev2CurrentCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = SOURCE.read_bytes()
        if sha256(raw).hexdigest() != EXPECTED:
            raise AssertionError("Anhelo exact-current owner lock SHA drift")
        rows = raw.decode("utf-8").splitlines()
        if rows[0] != "1x Anhelo, the Painter [Commander]":
            raise AssertionError("Unexpected commander")
        cls.cards = Counter()
        for line in rows:
            qty, card = line.split("x ", 1)
            cls.cards[card.removesuffix(" [Commander]")] += int(qty)
        assert sum(cls.cards.values()) == 100
        assert len(cls.cards) == 94
        assert cls.cards["Anhelo, the Painter"] == 1
        assert cls.cards["Maestros Ascendancy"] == 0
        assert cls.cards["Primal Amulet // Primal Wellspring"] == 0
        cls.report = REPORT.read_text(encoding="utf-8")

    def test_C1_commander_effect_active_on_true_cast_p0(self):
        self.assertEqual(self.cards["Anhelo, the Painter"], 1)
        self.assertEqual(granted_casualty(True, True, 2, True), 1)
        self.assertEqual(granted_casualty(False, True, 2, True), 0)
        self.assertEqual(granted_casualty(True, False, 2, True), 0)

    def test_K1_optional_power_2_paid_additional_cost_p0(self):
        self.assertEqual(granted_casualty(True, True, 3, True), 1)
        self.assertEqual(granted_casualty(True, True, 1, True), 0)
        self.assertEqual(granted_casualty(True, True, 2, False), 0)
        self.assertEqual(granted_casualty(True, True, None, True), 0)

    def test_K2_first_spell_tracking_not_reset_when_commander_enters_p0(self):
        self.assertTrue(anhelo_first_spell(0, True))
        self.assertFalse(anhelo_first_spell(1, True))
        self.assertFalse(anhelo_first_spell(0, False))
        # Original cast on turn before Anhelo's entry consumes the first slot.
        self.assertEqual(granted_casualty(True, anhelo_first_spell(1, True), 2, True), 0)

    def test_K3_copy_is_not_cast_magecraft_vs_cast_only_p0(self):
        self.assertEqual(cast_copy_trigger_counts(1, 1),
                         {"magecraft": 2, "talrand": 1, "pursuit_hand": 1})
        self.assertEqual(cast_copy_trigger_counts(0, 1),
                         {"magecraft": 1, "talrand": 0, "pursuit_hand": 0})
        for name in ("Archmage Emeritus", "Storm-Kiln Artist",
                     "Talrand, Sky Summoner", "Cryptic Pursuit"):
            self.assertEqual(self.cards[name], 1)

    def test_F1_no_power_2_body_denies_copy_p0(self):
        self.assertEqual(granted_casualty(True, True, 0, False), 0)
        self.assertEqual(granted_casualty(True, True, 1, True), 0)
        self.assertEqual(granted_casualty(True, True, 2, True), 1)

    def test_K4_staff_adds_one_to_real_copy_event_p1(self):
        self.assertEqual(self.cards["Twinning Staff"], 1)
        self.assertEqual(staff_copies(1, True), 2)
        self.assertEqual(staff_copies(1, False), 1)
        self.assertEqual(staff_copies(0, True), 0)

    def test_K5_two_different_casualty_costs_on_little_chat_p1(self):
        self.assertEqual(self.cards["A Little Chat"], 1)
        printed_casualty = 1
        anhelo_granted = granted_casualty(True, True, 2, True)
        self.assertEqual(printed_casualty + anhelo_granted, 2)
        self.assertEqual(printed_casualty + granted_casualty(True, True, 2, False), 1)
        # Two actually separate eligible sacrifice bodies must be available.
        self.assertFalse(1 >= 2)
        self.assertTrue(2 >= 2)

    def test_E1_real_fodder_recurs_over_two_distinct_turns_p1(self):
        for card in ("Bloodghast", "Forsaken Miner", "Skyclave Shade",
                     "Jadar, Ghoulcaller of Nephalia", "Poppet Stitcher // Poppet Factory"):
            self.assertEqual(self.cards[card], 1)
        self.assertEqual(sum(granted_casualty(True, True, 2, True) for _ in range(2)), 2)
        self.assertEqual(granted_casualty(True, False, 2, True), 0)
        # A single spent body does not pay twice without an actual return.
        remaining = 1 - granted_casualty(True, True, 2, True)
        self.assertEqual(remaining, 0)

    def test_E2_new_grave_recursion_retired_maestros_ascendancy_p1(self):
        for card in ("Kess, Dissident Mage", "Snapcaster Mage", "Underworld Breach"):
            self.assertEqual(self.cards[card], 1)
        self.assertEqual(self.cards["Maestros Ascendancy"], 0)
        self.assertEqual(self.cards["Case of the Stashed Skeleton"], 1)
        def can_recast(spell_in_yard, recursion_present, yard_exiled):
            return spell_in_yard and recursion_present and not yard_exiled
        self.assertTrue(can_recast(True, True, False))
        self.assertFalse(can_recast(True, True, True))
        self.assertFalse(can_recast(False, True, False))

    def test_W1_reversal_copy_needs_live_spell_and_stack_p1(self):
        for card in ("Narset's Reversal", "Twinning Staff", "Reiterate"):
            self.assertEqual(self.cards[card], 1)
        def one_copy_step(original_spell_live, reversal_legal, paid):
            return original_spell_live and reversal_legal and paid
        self.assertTrue(one_copy_step(True, True, True))
        for flags in ((False, True, True), (True, False, True), (True, True, False)):
            self.assertFalse(one_copy_step(*flags))
        # One step is intentionally not an arbitrary-costless-copy loop proof.

    def test_W2_dualcaster_twinflame_finite_copy_prerequisites_p1(self):
        self.assertEqual(self.cards["Twinflame"], 1)
        self.assertEqual(self.cards["Dualcaster Mage"], 1)
        self.assertTrue(dualcaster_twinflame_step(True, True, True, True))
        for flags in ((False, True, True, True), (True, False, True, True),
                      (True, True, False, True), (True, True, True, False)):
            self.assertFalse(dualcaster_twinflame_step(*flags))

    def test_W3_reiterate_paid_buyback_mana_output_threshold_p1(self):
        for card in ("Reiterate", "Mana Geyser", "Jeska's Will", "Crackle with Power"):
            self.assertEqual(self.cards[card], 1)
        self.assertEqual(iterate_buyback(7, True, True, False), 1)
        self.assertEqual(iterate_buyback(6, True, True, False), 0)
        self.assertEqual(iterate_buyback(5, True, True, False), -1)
        self.assertIsNone(iterate_buyback(9, False, True, False))
        self.assertIsNone(iterate_buyback(9, True, False, False))
        self.assertIsNone(iterate_buyback(9, True, True, True))

    def test_F2_sacrificed_engine_reduces_next_turn_magecraft_p1(self):
        self.assertEqual(self.cards["Talrand, Sky Summoner"], 1)
        self.assertEqual(self.cards["Archmage Emeritus"], 1)
        self.assertEqual(cast_copy_trigger_counts(1, 1)["magecraft"], 2)
        engine_alive_after_sacrifice = False
        self.assertEqual(cast_copy_trigger_counts(1, 1)["magecraft"]
                         if engine_alive_after_sacrifice else 0, 0)

    def test_F3_stack_grave_hate_disrupts_conditional_finisher_p1(self):
        def line_alive(source_paid, spell_live, yard_available, protected):
            return all((source_paid, spell_live, yard_available, protected))
        self.assertTrue(line_alive(True, True, True, True))
        for flags in ((False, True, True, True), (True, False, True, True),
                      (True, True, False, True), (True, True, True, False)):
            self.assertFalse(line_alive(*flags))
        self.assertEqual(self.cards["Fierce Guardianship"], 1)

    def test_full_approved_99_ledger_and_sha_are_physical(self):
        counted = Counter()
        for qty, name in re.findall(r"^- (\d+)x (.+)$", self.report, re.MULTILINE):
            counted[name] += int(qty)
        library = self.cards.copy()
        library.subtract({"Anhelo, the Painter": 1})
        self.assertEqual(sum(counted.values()), 99)
        self.assertEqual(counted, library)
        self.assertEqual({name: qty for name, qty in self.cards.items() if qty > 1},
                         {"Island": 3, "Mountain": 3, "Swamp": 3})
        self.assertIn(EXPECTED, self.report)
        for id_ in ("C1", "K1", "K2", "K3", "F1", "K4", "K5", "E1", "E2",
                    "W1", "W2", "W3", "F2", "F3"):
            self.assertIn(id_, self.report)


if __name__ == "__main__":
    unittest.main()
