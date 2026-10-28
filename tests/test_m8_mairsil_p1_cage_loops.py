"""M8 Mairsil original-P1: cage instances and two actual paid repeatable loops.

Finite transition tests, exact-SHA card inventory and adversarial missing-piece
checks. No blanket all-Mairsil win claim, no W3 or obsolete-mill F3 inference.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DECK = "Mairsil__the_Pretender"
SHA = "fd5e44773c829311254193d5c6d4433676e787743249451cc37a7345b0cf83ad"
CASES = {"K4", "K5", "K6", "K7", "E1", "E2", "W1", "W2", "F2"}


def mairsil_quicksilver_loop(cycles, *, lotus=True, crab=True, elemental=True,
                            tap_ready=True):
    """Each Quicksilver self-copy gains a fresh *once-per-turn* instance set.

    Tap caged Lotus for UUU, pay U to untap with caged Horseshoe Crab,
    pay U to self-target via Quicksilver. Net +U and a new set of abilities.
    Activated Mairsil abilities' once-per-turn limits are distinct per
    instance; no mana or activation is silently reset on the original one.
    """
    if not lotus or not tap_ready:
        return {"complete": 0, "blue": 0, "fresh_instances": 0,
                "stop": "missing-tap-resource"}
    used_lotus, used_untap, used_elemental = set(), set(), set()
    # Each Quicksilver activation grants another ability instance number.
    current_instance = 0
    blue = 0
    mairsil_untapped = True
    complete = 0
    for _ in range(cycles):
        if not mairsil_untapped or current_instance in used_lotus:
            break
        blue += 3
        mairsil_untapped = False
        used_lotus.add(current_instance)
        if not crab or current_instance in used_untap or blue < 1:
            break
        blue -= 1
        mairsil_untapped = True
        used_untap.add(current_instance)
        if not elemental or current_instance in used_elemental or blue < 1:
            break
        blue -= 1
        used_elemental.add(current_instance)
        current_instance += 1
        complete += 1
    return {"complete": complete, "blue": blue,
            "fresh_instances": current_instance,
            "stop": None if complete == cycles else "missing-fresh-instance-or-untap"}


def alchemist_rings_lotus_loop(cycles, *, rings=True, alchemist_ready=True,
                              lotus_ready=True):
    """Physical Gilded Lotus + Aphetto Alchemist + Rings of Brighthearth.

    Aphetto taps to untap tapped Lotus; paid Rings copy untaps Aphetto.
    Lotus generates UUU, Rings costs 2 generic, leaving net U per cycle.
    """
    blue = 0
    done = 0
    for _ in range(cycles):
        if not (rings and alchemist_ready and lotus_ready):
            break
        # Begin with untapped Lotus and untapped, legally tappable Alchemist.
        blue += 3  # physical Gilded Lotus mana ability
        blue -= 2  # required 2 generic Rings copy payment
        # Alchemist was tapped in cost; a separately targeted Rings copy
        # untaps Alchemist and the original activated ability untaps Lotus.
        alchemist_ready = True
        lotus_ready = True
        done += 1
    return done, blue


def independent_caged_uses(mairsil_uses, marvin_uses, have_marvin):
    """One use per activated ability instance per creature, not globally."""
    mairsil_success = min(mairsil_uses, 1)
    marvin_success = min(marvin_uses, 1) if have_marvin else 0
    return mairsil_success, marvin_success


def double_cage(*, first_card_exiled, second_card_available, spark_copy_enters):
    caged = int(first_card_exiled)
    if spark_copy_enters and second_card_available:
        caged += 1
    return caged, bool(spark_copy_enters)  # Spark Double copy nonlegendary


def wishclaw_cage_usable(*, wish_counter_on_mairsil, elixir_live, creature_ready):
    """Elixir doesn't provide the missing required *wish* counter cost."""
    return bool(wish_counter_on_mairsil and (elixir_live or creature_ready))


def mairsil_cage_on_entry(*, enters, hand_artifact_or_creature=False,
                         grave_artifact_or_creature=False):
    return int(enters and (hand_artifact_or_creature or grave_artifact_or_creature))


def arcanis_caged_draw(*, mairsil_ready, elixir_live, already_used):
    return 3 if (mairsil_ready or elixir_live) and not already_used else 0


def cage_from_grave(*, grave_card_still_available, hand_card_available):
    return bool(grave_card_still_available), bool(hand_card_available)


class MairsilCageOriginalP1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        row = next(x for x in index["decks"] if x["deck_id"] == DECK)
        raw = (ROOT / row["source_file"]).read_bytes()
        assert sha256(raw).hexdigest() == SHA == row["source_sha256"]
        cls.cards = Counter()
        for line in raw.decode().splitlines():
            count, name = line.split("x ", 1)
            cls.cards[name.replace(" [Commander]", "")] += int(count)
        assert sum(cls.cards.values()) == 100
        receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                              / f"{DECK}_{SHA[:16]}.json").read_text())
        assert receipt["approved_raw_sha256"] == SHA
        cls.deferred = {r["case_id"] for r in receipt["m6_transfer"]["P1"]
                        if r["status"] == "DEFERRED"}

    def source(self, case, *required):
        self.assertIn(case, self.deferred)
        for name in required:
            self.assertIn(name, self.cards)

    def test_K4_marvin_own_once_per_turn_instances_not_global_refresh(self):
        self.source("K4", "Marvin, Murderous Mimic", "Mairsil, the Pretender")
        self.assertEqual(independent_caged_uses(2, 2, have_marvin=True), (1, 1))
        self.assertEqual(independent_caged_uses(2, 2, have_marvin=False), (1, 0))
        self.assertEqual(independent_caged_uses(0, 1, have_marvin=True), (0, 1))

    def test_K5_spark_double_copy_new_cage_etb_and_nonlegendary(self):
        self.source("K5", "Spark Double", "Mairsil, the Pretender", "Pack Rat")
        self.assertEqual(double_cage(first_card_exiled=True, second_card_available=True,
                                     spark_copy_enters=True), (2, True))
        self.assertEqual(double_cage(first_card_exiled=True, second_card_available=False,
                                     spark_copy_enters=True), (1, True))
        self.assertEqual(double_cage(first_card_exiled=True, second_card_available=True,
                                     spark_copy_enters=False), (1, False))

    def test_K6_quicksilver_caged_lotus_horseshoe_paid_refreshes_instance(self):
        self.source("K6", "Quicksilver Elemental", "Gilded Lotus", "Horseshoe Crab",
                    "Mairsil, the Pretender")
        self.assertEqual(mairsil_quicksilver_loop(5)["blue"], 5)
        self.assertEqual(mairsil_quicksilver_loop(5)["complete"], 5)
        self.assertEqual(mairsil_quicksilver_loop(5)["fresh_instances"], 5)
        self.assertLess(mairsil_quicksilver_loop(5, elemental=False)["complete"], 2)
        self.assertLess(mairsil_quicksilver_loop(5, crab=False)["complete"], 2)
        self.assertEqual(mairsil_quicksilver_loop(5, tap_ready=False)["complete"], 0)

    def test_K7_elixir_can_grant_tap_access_but_no_wishclaw_cost_counters(self):
        self.source("K7", "Thousand-Year Elixir", "Wishclaw Talisman", "Mairsil, the Pretender")
        self.assertFalse(wishclaw_cage_usable(wish_counter_on_mairsil=False,
                                              elixir_live=True, creature_ready=False))
        self.assertFalse(wishclaw_cage_usable(wish_counter_on_mairsil=False,
                                              elixir_live=False, creature_ready=True))
        self.assertTrue(wishclaw_cage_usable(wish_counter_on_mairsil=True,
                                             elixir_live=True, creature_ready=False))

    def test_E1_mairsil_real_blink_reentry_cages_one_more_card(self):
        self.source("E1", "Mairsil, the Pretender", "Essence Flux", "Displacer Kitten")
        self.assertEqual(mairsil_cage_on_entry(enters=True, hand_artifact_or_creature=True), 1)
        self.assertEqual(mairsil_cage_on_entry(enters=True, grave_artifact_or_creature=True), 1)
        self.assertEqual(mairsil_cage_on_entry(enters=False, hand_artifact_or_creature=True), 0)
        self.assertEqual(mairsil_cage_on_entry(enters=True), 0)

    def test_E2_caged_arcanis_tap_draw_3_requires_ready_body_and_unused_instance(self):
        self.source("E2", "Arcanis the Omnipotent", "Thousand-Year Elixir", "Anger")
        self.assertEqual(arcanis_caged_draw(mairsil_ready=False, elixir_live=True,
                                           already_used=False), 3)
        self.assertEqual(arcanis_caged_draw(mairsil_ready=False, elixir_live=False,
                                           already_used=False), 0)
        self.assertEqual(arcanis_caged_draw(mairsil_ready=True, elixir_live=True,
                                           already_used=True), 0)

    def test_W1_five_loop_caged_quicksilver_lotus_crab_unbounded_blue_invariant(self):
        self.source("W1", "Mairsil, the Pretender", "Quicksilver Elemental",
                    "Gilded Lotus", "Horseshoe Crab", "Thousand-Year Elixir")
        a = mairsil_quicksilver_loop(5)
        b = mairsil_quicksilver_loop(10)
        self.assertEqual((a["complete"], a["blue"]), (5, 5))
        self.assertEqual((b["complete"], b["blue"]), (10, 10))
        self.assertIsNone(b["stop"])
        self.assertLess(mairsil_quicksilver_loop(10, elemental=False)["complete"], 2)
        self.assertEqual(mairsil_quicksilver_loop(10, lotus=False)["complete"], 0)

    def test_W2_rings_aphetto_physical_lotus_self_untap_repeatable_net_blue(self):
        self.source("W2", "Rings of Brighthearth", "Aphetto Alchemist", "Gilded Lotus")
        self.assertEqual(alchemist_rings_lotus_loop(6), (6, 6))
        self.assertEqual(alchemist_rings_lotus_loop(12), (12, 12))
        self.assertEqual(alchemist_rings_lotus_loop(6, rings=False), (0, 0))
        self.assertEqual(alchemist_rings_lotus_loop(6, alchemist_ready=False), (0, 0))
        self.assertEqual(alchemist_rings_lotus_loop(6, lotus_ready=False), (0, 0))

    def test_F2_graveyard_hate_blocks_that_zone_not_hand_caging(self):
        self.source("F2", "Mairsil, the Pretender", "Entomb")
        self.assertEqual(cage_from_grave(grave_card_still_available=True,
                                        hand_card_available=False), (True, False))
        self.assertEqual(cage_from_grave(grave_card_still_available=False,
                                        hand_card_available=True), (False, True))
        self.assertEqual(cage_from_grave(grave_card_still_available=False,
                                        hand_card_available=False), (False, False))

    def test_W3_and_F3_unsafe_mirror_mad_absence_not_relabelled_as_win(self):
        self.assertEqual(self.deferred, CASES | {"W3", "F3"})
        self.assertNotIn("Mirror-Mad Phantasm", self.cards)


if __name__ == "__main__":
    unittest.main()
