"""Kefka exact-approved original M6 W2 finite Breach and Wheel variants.

Reuses the already CI-proven physical one-LED/one-Freeze cost ledger while
separately testing Wheel/Jeska's Will stack, hand and opponent choices.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

from test_m8_marchesa_dealer_original_e2_w2 import (
    breach_led_brain_freeze,
    escape_oracle_after_self_mill,
    petal_only_can_pay_brain_freeze,
)


ROOT = Path(__file__).resolve().parents[1]
DECK = "Kefka__Court_Mage"
SHA = "14277f6e9774c5ef02b4f92332b52684794367007abf81bc2d84ef7ad7bcaa7d"
PLAN_BLOB = "07efd24960263757e3dbc9177127554ce3539f14"


def paid_wheel_led_response(*, wheel_in_hand=True, wheel_paid_2r=True,
                            led_in_play=True, led_sacrificed_before_cast=False,
                            prior_hand_cards=3, our_library=70,
                            opponent_libraries=(70, 70, 70),
                            wheel_countered=False):
    """Wheel in hand is cast with real external 2R, then LED responds.

    Sacrificing LED *before* casting Wheel from hand discards that Wheel.
    The three fresh mana cannot retroactively pay a spell already cast.
    """
    result = {"wheel_cast": False, "led_mana": 0, "own_draws": 0,
              "opp_draws": (), "own_new_hand": 0, "grave_discarded": 0}
    if not wheel_in_hand or not wheel_paid_2r or led_sacrificed_before_cast:
        return result
    result["wheel_cast"] = True
    if led_in_play:
        result["led_mana"] = 3  # all one color, AFTER Wheel has been cast.
        result["grave_discarded"] = prior_hand_cards
    if wheel_countered:
        return result
    # Wheel actually resolves. Drawing is bounded by physical libraries.
    result["own_draws"] = min(7, our_library)
    result["opp_draws"] = tuple(min(7, n) for n in opponent_libraries)
    result["own_new_hand"] = result["own_draws"]
    result["all_draw_seven"] = (our_library >= 7 and
                                all(n >= 7 for n in opponent_libraries))
    return result


def paid_jeskas_will_then_wheel(*, cost_2r_paid=True,
                                opponent_hand_at_resolution=7,
                                commander_controlled_on_cast=False,
                                wheel_still_in_hand=True, our_library=60):
    """Jeska's Will uses the stack; R output is opponent hand on resolution.

    If chosen, the three exiled cards are permission to *play* through end
    of turn (with real costs), not free card draws or immediate mana.
    """
    if not cost_2r_paid:
        return {"will_cast": False, "red_generated": 0,
                "wheel_paid": False, "exiled": 0}
    red = opponent_hand_at_resolution
    exiled = min(3, our_library) if commander_controlled_on_cast else 0
    wheel_payable = red >= 3 and wheel_still_in_hand
    return {"will_cast": True, "red_generated": red,
            "wheel_paid": wheel_payable,
            "red_remaining": red - 3 if wheel_payable else red,
            "exiled": exiled, "cards_drawn_from_exile": 0}


class KefkaOriginalW2BreachWheel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        row = next(x for x in index["decks"] if x["deck_id"] == DECK)
        raw = (ROOT / row["source_file"]).read_bytes()
        assert sha256(raw).hexdigest() == row["source_sha256"] == SHA
        assert raw.decode().splitlines()[0].endswith("Kefka, Ruler of Ruin [Commander]")
        cls.cards = Counter()
        for line in raw.decode().splitlines():
            count, name = line.split("x ", 1)
            cls.cards[name.removesuffix(" [Commander]")] += int(count)
        assert sum(cls.cards.values()) == 100
        receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                              / f"{DECK}_{SHA[:16]}.json").read_text())
        assert receipt["approved_raw_sha256"] == SHA
        assert receipt["m6_transfer"]["plan_blob_sha"] == PLAN_BLOB
        cls.deferred = {r["case_id"] for r in receipt["m6_transfer"]["P1"]
                        if r["status"] == "DEFERRED"}
        assert cls.deferred == {"K4", "W2", "F3"}
        # M8 has already retired old Demonic Counsel K4/F3 claims; this
        # original-plan test concerns only the remaining W2 live cards.
        cls.oracle = {}
        with (ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl").open() as stream:
            for line in stream:
                entry = json.loads(line)
                cls.oracle[entry["canonical_name"]] = entry["oracle_text"]

    def source(self, *cards):
        self.assertIn("W2", self.deferred)
        for card in cards:
            self.assertEqual(self.cards[card], 1, card)

    def test_W2_breach_and_wheel_paid_finite_positives_and_adverse_states(self):
        self.source("Underworld Breach", "Lion's Eye Diamond", "Lotus Petal",
                    "Brain Freeze", "Wheel of Fortune", "Jeska's Will",
                    "Thassa's Oracle", "Kefka, Court Mage // Kefka, Ruler of Ruin")
        self.assertIn("exile three other cards", self.oracle["Underworld Breach"])
        self.assertIn("Storm", self.oracle["Brain Freeze"])
        self.assertIn("Discard your hand, Sacrifice", self.oracle["Lion's Eye Diamond"])
        self.assertIn("Each player discards their hand", self.oracle["Wheel of Fortune"])
        self.assertIn("target opponent's hand", self.oracle["Jeska's Will"])

        # The already proven one-LED/one-Freeze finite resource engine is
        # valid only after re-binding every named card to THIS approved 100.
        trace = breach_led_brain_freeze()
        self.assertEqual([x["storm_objects"] for x in trace["history"]],
                         [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])
        self.assertEqual(trace["own_library"], 0)
        self.assertEqual(trace["opponents"], (0, 0, 0))
        self.assertTrue(escape_oracle_after_self_mill(
            own_library=0, other_grave_cards=trace["other_grave_cards"])["oracle_win"])
        self.assertFalse(escape_oracle_after_self_mill(
            own_library=0, oracle_trigger_resolves=False)["oracle_win"])
        self.assertEqual(breach_led_brain_freeze(other_grave_cards=2)["history"], [])
        self.assertEqual(breach_led_brain_freeze(opponent_removes_breach=True)["history"], [])
        self.assertFalse(petal_only_can_pay_brain_freeze())

        # After actually paying Wheel's 2R and placing it on the stack,
        # sacrificing LED can discard our remaining hand and add three mana;
        # it cannot pay the spell retroactively or be used first from hand.
        wheel = paid_wheel_led_response()
        self.assertTrue(wheel["wheel_cast"])
        self.assertEqual((wheel["led_mana"], wheel["grave_discarded"]), (3, 3))
        self.assertEqual(wheel["own_new_hand"], 7)
        self.assertEqual(wheel["opp_draws"], (7, 7, 7))
        self.assertTrue(wheel["all_draw_seven"])
        self.assertFalse(paid_wheel_led_response(led_sacrificed_before_cast=True)
                         ["wheel_cast"])
        self.assertFalse(paid_wheel_led_response(wheel_paid_2r=False)["wheel_cast"])
        self.assertEqual(paid_wheel_led_response(wheel_countered=True)["own_draws"], 0)
        self.assertFalse(paid_wheel_led_response(our_library=3)["all_draw_seven"])

        # Pay a separate 2R to cast Jeska's Will *before* Wheel. It can
        # yield R x7 from a seven-card opponent hand at resolution, then
        # 2R pays Wheel and leaves R x4; hand-size changes can give zero.
        will = paid_jeskas_will_then_wheel(commander_controlled_on_cast=True)
        self.assertEqual(will["red_generated"], 7)
        self.assertTrue(will["wheel_paid"])
        self.assertEqual(will["red_remaining"], 4)
        self.assertEqual((will["exiled"], will["cards_drawn_from_exile"]), (3, 0))
        self.assertFalse(paid_jeskas_will_then_wheel(
            opponent_hand_at_resolution=0)["wheel_paid"])
        self.assertFalse(paid_jeskas_will_then_wheel(cost_2r_paid=False)["will_cast"])
        self.assertEqual(paid_jeskas_will_then_wheel(
            commander_controlled_on_cast=False)["exiled"], 0)
        self.assertFalse(paid_jeskas_will_then_wheel(
            wheel_still_in_hand=False)["wheel_paid"])
        # Kefka's own card-type draws require a Kefka ETB/attack trigger;
        # casting Wheel alone does not trigger that distinct commander ability.


if __name__ == "__main__":
    unittest.main()
