"""Exact-approved Madcap Jester five original remaining P1 finite cases.

These deliberately bounded tests do not claim official Commander legality for
two protected prerelease exceptions, an all-cards Magic engine, or game-win
by merely milling an opponent's library without a subsequent forced draw.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DECK = "The_Madcap_Jester"
SHA = "643eb1cc4827c1dd95485e9922506b514746e6bbc5b4b8a4cfff0f44b1007e43"
CASES = {"F2", "F3", "W1", "W2", "W3"}


def oracle_with_library_exile(*, oracle_trigger_resolves=True, devotion=2,
                              initial_library=88, consultation_resolves=False,
                              consultation_named_absent=False, pact_resolves=False,
                              all_remaining_names_unique=True):
    """Oracle's ETB trigger uses devotion and *current* library on resolution."""
    size = initial_library
    if consultation_resolves and consultation_named_absent:
        size = 0
    if pact_resolves and all_remaining_names_unique:
        size = 0
    return bool(oracle_trigger_resolves and devotion >= size)


def breach_led_freeze_table(*, our_library=90, opponents=(90, 90, 90),
                            grave_filler=9, breach=True, led=True,
                            freeze=True, interaction_before_copies=False,
                            turns=11):
    """One LED and one Freeze: all escape exiles and actual mill are charged.

    LED starts on battlefield and is known cast earlier this turn. Each next
    iteration escapes the ONE LED at zero mana while exiling three distinct
    other grave cards. Each Brain Freeze escape pays {1}{U}, exiles three
    other grave cards, and generates 1+prior-cast-count storm spell objects.
    First five Freeze casts mill 6,12,18,24,30 of our *actual* 90 cards.
    Next six casts distribute each copy across actual opponents' libraries.
    No instant loss from empty library is claimed for opponents.
    """
    opp = list(opponents)
    storm, mana, history = 1, 0, []
    for step in range(turns):
        if not all([breach, led, freeze]) or interaction_before_copies:
            break
        if step:
            if grave_filler < 3:
                break
            grave_filler -= 3  # escape real LED, not a phantom duplicate
            storm += 1
        mana += 3  # LED sacrifice adds three blue and puts LED in grave
        if grave_filler < 3 or mana < 2:
            break
        grave_filler -= 3  # pay Brain Freeze escape with three other objects
        mana -= 2  # pay printed {1}{U}, no commander discount assumed
        copies = storm + 1
        for _ in range(copies):
            if step < 5:
                mill = min(3, our_library)
                our_library -= mill
                grave_filler += mill
            else:
                victim = max(range(len(opp)), key=lambda i: opp[i])
                mill = min(3, opp[victim])
                opp[victim] -= mill
        storm += 1
        history.append({"freeze_cast": step + 1, "freeze_objects": copies,
                        "own_library": our_library, "opponents": tuple(opp),
                        "other_grave_cards": grave_filler, "blue": mana})
    return {"history": history, "self_library": our_library,
            "opponents": tuple(opp), "grave_filler": grave_filler, "blue": mana}


def controlled_exile_to_jester_cast(*, jester_present, controller_cast_extract,
                                    opponent_library_contains_card,
                                    cast_on_current_or_next_turn,
                                    sorcery_timing, mana_paid, mana_cost,
                                    opponent_card_is_land=False,
                                    unused_land_drop=False):
    """Extract's real target-library exile grants temporal permission, not mana.

    The victim's actual library holds one chosen hypothetical off-color card;
    its owner is not changed by Jester permission. Any mana *type* can be
    spent, but all generic/colored cost and ordinary timing still apply.
    """
    if not (jester_present and controller_cast_extract and opponent_library_contains_card):
        return False
    if not cast_on_current_or_next_turn or not sorcery_timing:
        return False
    if opponent_card_is_land:
        return unused_land_drop
    return mana_paid >= mana_cost


def extract_real_opponent_card(*, jester_present=True, colored_u=True,
                               spend_three_mana=True, stolen_sorcery_timing=True):
    """One opponent-owned spell physically traverses library/exile/stack/gy.

    The hypothetical opponent's exact library contents are an input, never
    implied to exist in a real matchup. The actual owner of the exiled spell
    remains the opponent, including when that spell goes to their graveyard.
    """
    spell = {"name": "Hypothetical non-Grixis sorcery", "cost": 3,
             "owner": "opponent", "zone": "opponent_library"}
    mana = Counter({"U": 1 if colored_u else 0, "B": 3 if spend_three_mana else 2})
    if not mana["U"]:
        return {"paid_extract": False, "resolved_spells": 0,
                "spell_zone": spell["zone"], "opponent_owns_spell": True}
    mana["U"] -= 1  # genuine {U} for the approved Extract sorcery
    spell["zone"] = "exile"  # one actual opponent-library card
    can_cast = controlled_exile_to_jester_cast(
        jester_present=jester_present, controller_cast_extract=True,
        opponent_library_contains_card=True,
        cast_on_current_or_next_turn=True, sorcery_timing=stolen_sorcery_timing,
        mana_paid=mana["B"], mana_cost=spell["cost"])
    if can_cast:
        mana["B"] -= 3  # any type of mana, but full total cost required
        spell["zone"] = "stack"
        spell["zone"] = "opponent_graveyard"  # spell finishes resolving
    return {"paid_extract": True, "resolved_spells": int(can_cast),
            "spell_zone": spell["zone"], "opponent_owns_spell": spell["owner"] == "opponent"}


class MadcapOriginalP1WinAndHate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        row = next(x for x in index["decks"] if x["deck_id"] == DECK)
        raw = (ROOT / row["source_file"]).read_bytes()
        assert sha256(raw).hexdigest() == row["source_sha256"] == SHA
        assert raw.decode().splitlines()[0] == "1x The Madcap Jester [Commander]"
        cls.cards = Counter()
        for line in raw.decode().splitlines():
            quantity, name = line.split("x ", 1)
            cls.cards[name.replace(" [Commander]", "")] += int(quantity)
        assert len(cls.cards) == sum(cls.cards.values()) == 100
        assert cls.cards["The Madcap Jester"] == cls.cards["Dragon's Smile"] == 1
        receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                              / f"{DECK}_{SHA[:16]}.json").read_text())
        assert receipt["approved_raw_sha256"] == SHA
        assert receipt["m6_transfer"]["plan_blob_sha"] == "3a065adefc6aebb3409810ed9d40b5e8b5a0b7a1"
        cls.deferred = {r["case_id"] for r in receipt["m6_transfer"]["P1"]
                        if r["status"] == "DEFERRED"}
        assert cls.deferred == CASES

    def source(self, case, *cards):
        self.assertIn(case, self.deferred)
        for card in cards:
            self.assertEqual(self.cards[card], 1, card)

    def test_W1_actual_oracle_consultation_pact_check_at_trigger_resolution(self):
        self.source("W1", "Thassa's Oracle", "Demonic Consultation", "Tainted Pact",
                    "Demonic Tutor", "Vampiric Tutor", "Imperial Seal", "Mystical Tutor")
        # Paid UU Oracle enters, ETB triggered; B-paid Consultation names an
        # absent card and exiles remaining library in response to that trigger.
        self.assertTrue(oracle_with_library_exile(consultation_resolves=True,
                                                  consultation_named_absent=True))
        # Paid 1B Pact, all 100 source names distinct, may elect to exile all.
        self.assertTrue(oracle_with_library_exile(pact_resolves=True))
        self.assertFalse(oracle_with_library_exile(consultation_named_absent=True,
                                                   consultation_resolves=False))
        self.assertFalse(oracle_with_library_exile(oracle_trigger_resolves=False,
                                                   consultation_resolves=True,
                                                   consultation_named_absent=True))
        self.assertFalse(oracle_with_library_exile(pact_resolves=True,
                                                   all_remaining_names_unique=False))

    def test_W2_breach_led_brain_freeze_mills_three_opponents_not_auto_loss(self):
        self.source("W2", "Underworld Breach", "Brain Freeze", "Lion's Eye Diamond",
                    "Lotus Petal", "Gamble", "Beseech the Mirror")
        trace = breach_led_freeze_table(turns=11)
        self.assertEqual(len(trace["history"]), 11)
        self.assertEqual([r["freeze_objects"] for r in trace["history"]],
                         [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])
        self.assertEqual(trace["history"][4]["own_library"], 0)
        self.assertEqual(trace["self_library"], 0)
        self.assertEqual(trace["opponents"], (0, 0, 0))
        self.assertEqual(trace["blue"], 11)
        self.assertEqual(trace["grave_filler"], 36)
        self.assertEqual(breach_led_freeze_table(breach=False)["history"], [])
        self.assertEqual(breach_led_freeze_table(led=False)["history"], [])
        self.assertEqual(breach_led_freeze_table(grave_filler=2)["history"], [])
        self.assertEqual(breach_led_freeze_table(interaction_before_copies=True)["history"], [])
        # Opponents have zero library cards; no forced *draw* has occurred in
        # this fixture, so milling alone has not yet made them lose the game.

    def test_W3_actual_opponent_exile_to_paid_jester_next_turn_value(self):
        self.source("W3", "The Madcap Jester", "Extract", "Sadistic Sacrament",
                    "Tasha's Hideous Laughter", "Dragon's Smile",
                    "Don Andres, the Renegade")
        self.assertNotIn("Bitter Ordeal", self.cards)
        self.assertNotIn("Gonti, Night Minister", self.cards)
        # Hypothetical opponent library physically includes a {2}{G} sorcery.
        # Source-paid U Extract exiles it while Jester is live; three black
        # mana can legally pay all three printed mana (any mana TYPE), on own
        # main phase before end of NEXT turn. Its owner stays the opponent.
        fixture = dict(jester_present=True, controller_cast_extract=True,
                       opponent_library_contains_card=True,
                       cast_on_current_or_next_turn=True, sorcery_timing=True,
                       mana_paid=3, mana_cost=3)
        self.assertTrue(controlled_exile_to_jester_cast(**fixture))
        resolved = extract_real_opponent_card()
        self.assertEqual(resolved, {"paid_extract": True, "resolved_spells": 1,
                                     "spell_zone": "opponent_graveyard", "opponent_owns_spell": True})
        self.assertEqual(extract_real_opponent_card(jester_present=False)["resolved_spells"], 0)
        self.assertEqual(extract_real_opponent_card(colored_u=False)["spell_zone"], "opponent_library")
        self.assertEqual(extract_real_opponent_card(spend_three_mana=False)["spell_zone"], "exile")
        self.assertEqual(extract_real_opponent_card(stolen_sorcery_timing=False)["resolved_spells"], 0)
        self.assertFalse(controlled_exile_to_jester_cast(**(fixture | {"jester_present": False})))
        self.assertFalse(controlled_exile_to_jester_cast(**(fixture | {"controller_cast_extract": False})))
        self.assertFalse(controlled_exile_to_jester_cast(**(fixture | {"opponent_library_contains_card": False})))
        self.assertFalse(controlled_exile_to_jester_cast(**(fixture | {"cast_on_current_or_next_turn": False})))
        self.assertFalse(controlled_exile_to_jester_cast(**(fixture | {"sorcery_timing": False})))
        self.assertFalse(controlled_exile_to_jester_cast(**(fixture | {"mana_paid": 2})))
        self.assertFalse(controlled_exile_to_jester_cast(**(fixture | {"opponent_card_is_land": True})))
        self.assertTrue(controlled_exile_to_jester_cast(**(fixture | {"opponent_card_is_land": True,
                                                            "unused_land_drop": True})))

    def test_F2_graveyard_hate_stops_this_breach_not_oracle(self):
        self.source("F2", "Underworld Breach", "Thassa's Oracle",
                    "Demonic Consultation", "Tainted Pact")
        live = breach_led_freeze_table(grave_filler=9, turns=2)
        emptied = breach_led_freeze_table(grave_filler=0, turns=2)
        self.assertEqual(len(live["history"]), 2)
        self.assertEqual(emptied["history"], [])
        self.assertTrue(oracle_with_library_exile(consultation_resolves=True,
                                                  consultation_named_absent=True))
        self.assertTrue(oracle_with_library_exile(pact_resolves=True))
        # The generic Oracle kill does not interact with a card in graveyard.

    def test_F3_etb_hate_or_countered_oracle_vs_nonrelevant_graveyard_hate(self):
        self.source("F3", "Thassa's Oracle", "Demonic Consultation", "Tainted Pact",
                    "Underworld Breach")
        self.assertFalse(oracle_with_library_exile(oracle_trigger_resolves=False,
                                                   consultation_resolves=True,
                                                   consultation_named_absent=True))
        self.assertFalse(oracle_with_library_exile(consultation_resolves=False,
                                                   consultation_named_absent=True))
        self.assertFalse(oracle_with_library_exile(pact_resolves=False))
        self.assertTrue(oracle_with_library_exile(consultation_resolves=True,
                                                  consultation_named_absent=True))


if __name__ == "__main__":
    unittest.main()
