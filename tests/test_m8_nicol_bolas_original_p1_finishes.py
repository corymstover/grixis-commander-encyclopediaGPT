"""Finite exact-approved Nicol Bolas original M6 P1 W1/W2/F3 witnesses.

This is intentionally a bounded state trace, not a complete rules engine, a
matchup win-rate claim, or proof that an opponent will allow these lines.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DECK = "Nicol_Bolas"
SHA = "a6079935a50b9469ca487e58e6bac159f8b777348b31585256b967f92c5d0df6"
PLAN_BLOB = "fb8641de923796d2b3b4b9de1eb76cd02367bc9d"
CASES = {"W1", "W2", "F3"}


def assault_land_payment(lands, tapped):
    """Select and tap exactly five real available lands, including two red."""
    reds = [i for i, color in enumerate(lands) if color == "R" and not tapped[i]]
    if len(reds) < 2:
        return ()
    paid = reds[:2]
    generics = [i for i in range(len(lands)) if i not in paid and not tapped[i]]
    if len(generics) < 3:
        return ()
    return tuple(paid + generics[:3])


def sword_assault_combats(*, lands=("R", "R", "U", "B", "C"),
                          sword_equipped=True, assault_present=True,
                          bolas_present=True, combat_hits=(True,) * 5,
                          bolas_upkeep_paid=True, assault_resolves=True):
    """Physical combat/land-payment ledger within one turn.

    The first hit may untap all lands, then postcombat-main Assault pays five
    from those lands. Every additional successful Sword hit repeats that
    untap/payment in the ensuing main. No free extra combat or phantom land.
    """
    commander_damage = 0
    # Model setup having tapped the physical lands before the first combat.
    # A Sword hit, not a phantom untap, must refill the pool here.
    tapped = [True] * len(lands)
    records = []
    if not bolas_present or not bolas_upkeep_paid:
        return records
    for n, hit in enumerate(combat_hits):
        # An unblocked 7/7 Nicol Bolas with Sword attached deals nine combat.
        combat_damage = (7 + (2 if sword_equipped else 0)) if hit else 0
        commander_damage += combat_damage
        sword_untapped_lands = bool(hit and sword_equipped)
        if sword_untapped_lands:
            tapped = [False] * len(lands)
        payment = (assault_land_payment(lands, tapped)
                   if (commander_damage < 21 and assault_present and assault_resolves)
                   else ())
        for i in payment:
            tapped[i] = True
        may_continue = bool(payment)
        records.append({"combat": n + 1, "hit": hit,
                        "damage": combat_damage, "commander_damage": commander_damage,
                        "lands_untapped_by_sword": sword_untapped_lands,
                        "assault_paid": may_continue, "paid_lands": payment,
                        "lands_tapped_after": tuple(tapped),
                        "commander_loss": commander_damage >= 21})
        if not may_continue or commander_damage >= 21:
            break
    return records


def bolas_damage(*, opponents, target, amount, combat=False, caress=False,
                 curiosity=False):
    """One real Nicol Bolas damage event; only target discards their hand.

    Noncombat damage triggers Bolas just as combat damage does, but noncombat
    damage is NOT commander damage under official Commander rules.
    """
    state = [dict(row) for row in opponents]
    victim = state[target]
    victim["life"] -= amount
    discarded = victim["hand"]
    victim["hand"] = 0
    victim["life"] -= 2 * discarded if caress else 0
    victim["commander_damage"] += amount if combat else 0
    return {"players": state, "discarded": discarded,
            "curiosity_optional_draws": int(bool(curiosity and amount > 0)),
            "dead_by_commander": victim["commander_damage"] >= 21}


def kediss_followup(*, initial_hands=(5, 4, 6), caress=True,
                    blockers=False, kediss_present=True):
    """Bolas hits player zero in combat; Kediss makes Bolas deal others damage.

    Bolas's damage trigger empties each *damaged* opponent's hand. Kediss
    additional damage is noncombat; it never increments commander damage.
    """
    players = [{"life": 40, "hand": hand, "commander_damage": 0}
               for hand in initial_hands]
    if blockers:
        return {"players": players, "discards": [], "events": 0}
    discards = []
    first = bolas_damage(opponents=players, target=0, amount=7,
                         combat=True, caress=caress)
    players = first["players"]
    discards.append(first["discarded"])
    if kediss_present:
        for n in range(1, len(players)):
            event = bolas_damage(opponents=players, target=n, amount=7,
                                 combat=False, caress=caress)
            players = event["players"]
            discards.append(event["discarded"])
    return {"players": players, "discards": discards, "events": len(discards)}


def torment_of_hailfire(*, x, life=40, hand=3, nonland_permanents=3,
                        opponent_prefers_sacrifice=True):
    """One opponent's actual decisions on X successive Torment instructions."""
    history = []
    for _ in range(x):
        if opponent_prefers_sacrifice and nonland_permanents:
            nonland_permanents -= 1
            action = "sacrifice"
        elif hand:
            hand -= 1
            action = "discard"
        else:
            life -= 3
            action = "lose_3"
        history.append(action)
    return {"life": life, "hand": hand,
            "nonland_permanents": nonland_permanents,
            "history": history}


def fast_combo_before_bolas(*, opponent_turn=3, bolas_ready_turn=4,
                            counter_available=False, blue_pitch=False,
                            force_of_will=True, life=40,
                            opponent_spell_counterable=True):
    """A specifically declared pre-Bolas opposing combo, not measured odds."""
    can_force = (force_of_will and counter_available and blue_pitch
                 and life > 1 and opponent_spell_counterable)
    return {"bolas_in_play": opponent_turn >= bolas_ready_turn,
            "countered": can_force,
            "opponent_wins_in_fixture": opponent_turn < bolas_ready_turn
                                        and not can_force}


class NicolBolasOriginalP1Finishes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        row = next(x for x in index["decks"] if x["deck_id"] == DECK)
        source = (ROOT / row["source_file"]).read_bytes()
        assert sha256(source).hexdigest() == row["source_sha256"] == SHA
        assert source.decode().splitlines()[0] == "1x Nicol Bolas [Commander]"
        cls.cards = Counter()
        for line in source.decode().splitlines():
            quantity, name = line.split("x ", 1)
            cls.cards[name.removesuffix(" [Commander]")] += int(quantity)
        assert sum(cls.cards.values()) == 100 and cls.cards["Nicol Bolas"] == 1
        receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                              / f"{DECK}_{SHA[:16]}.json").read_text())
        assert receipt["approved_raw_sha256"] == SHA
        assert receipt["m6_transfer"]["plan_blob_sha"] == PLAN_BLOB
        cls.deferred = {r["case_id"] for r in receipt["m6_transfer"]["P1"]
                        if r["status"] == "DEFERRED"}
        assert CASES.issubset(cls.deferred)
        cls.oracle = {}
        with (ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl").open() as stream:
            for line in stream:
                oracle_row = json.loads(line)
                cls.oracle[oracle_row["canonical_name"]] = oracle_row["oracle_text"]

    def source(self, case, *cards):
        self.assertIn(case, self.deferred)
        for card in cards:
            self.assertEqual(self.cards[card], 1, card)

    def test_W1_sword_assault_actual_five_mana_and_three_hits(self):
        self.source("W1", "Nicol Bolas", "Sword of Feast and Famine",
                    "Aggravated Assault")
        self.assertIn("untap all lands you control", self.oracle["Sword of Feast and Famine"])
        self.assertIn("Activate only as a sorcery", self.oracle["Aggravated Assault"])
        trace = sword_assault_combats()
        self.assertEqual([r["commander_damage"] for r in trace], [9, 18, 27])
        self.assertEqual([r["assault_paid"] for r in trace], [True, True, False])
        self.assertEqual([len(r["paid_lands"]) for r in trace], [5, 5, 0])
        self.assertEqual(trace[0]["lands_tapped_after"], (True,) * 5)
        self.assertTrue(trace[-1]["commander_loss"])
        # A hit is not an automatically free combat. RR and total five are
        # actually required in the main phase after each Sword untap.
        self.assertEqual(len(sword_assault_combats(lands=("R", "U", "U", "B", "C"))), 1)
        self.assertEqual(len(sword_assault_combats(lands=("R", "R", "U", "B"))), 1)
        self.assertEqual(len(sword_assault_combats(combat_hits=(True, False, True))), 2)
        self.assertEqual(len(sword_assault_combats(sword_equipped=False)), 1)
        self.assertEqual(len(sword_assault_combats(assault_present=False)), 1)
        self.assertEqual(len(sword_assault_combats(assault_resolves=False)), 1)
        self.assertEqual(sword_assault_combats(bolas_upkeep_paid=False), [])
        # Three uninterrupted hits are only one possible finite witness;
        # removal, blockers, tax and initial setup are not waived.

    def test_W2_real_damage_discard_copies_and_nonlethal_torment(self):
        self.source("W2", "Nicol Bolas", "Liliana's Caress", "Torment of Hailfire",
                    "Kediss, Emberclaw Familiar", "Ingris Stingerquill",
                    "Chandra's Ignition", "Quicksilver Dagger", "Pain for All",
                    "Dragon Tempest", "Curiosity")
        # Original M6 plan named these, but neither is in the approved Rev1.
        self.assertEqual(self.cards["Raiders' Wake"], 0)
        self.assertEqual(self.cards["Viridian Longbow"], 0)
        self.assertIn("that player discards their hand", self.oracle["Nicol Bolas"])
        self.assertIn("each other opponent", self.oracle["Kediss, Emberclaw Familiar"])
        out = kediss_followup(initial_hands=(5, 4, 6))
        self.assertEqual(out["discards"], [5, 4, 6])
        self.assertEqual([p["life"] for p in out["players"]], [23, 25, 21])
        self.assertEqual([p["commander_damage"] for p in out["players"]], [7, 0, 0])
        # If damage is blocked, the combat-only Kediss chain never starts.
        self.assertEqual(kediss_followup(blockers=True)["events"], 0)
        self.assertEqual(kediss_followup(kediss_present=False)["discards"], [5])
        # One paid Chandra's Ignition, Ingris attack, or Dagger tap can cause
        # an independent noncombat Bolas damage trigger, not commander damage.
        players = [{"life": 40, "hand": 4, "commander_damage": 0}]
        direct = bolas_damage(opponents=players, target=0, amount=7,
                              combat=False, caress=True, curiosity=True)
        self.assertEqual(direct["players"][0],
                         {"life": 25, "hand": 0, "commander_damage": 0})
        self.assertEqual(direct["curiosity_optional_draws"], 1)
        # Torment is NOT unconditional life loss: opponent may sac/discard.
        paid = torment_of_hailfire(x=4, hand=2, nonland_permanents=2)
        self.assertEqual(paid["life"], 40)
        self.assertEqual(paid["history"], ["sacrifice", "sacrifice", "discard", "discard"])
        exhausted = torment_of_hailfire(x=4, hand=0, nonland_permanents=0)
        self.assertEqual(exhausted["life"], 28)

    def test_F3_fast_combo_precommander_counterplay_is_conditional(self):
        self.source("F3", "Nicol Bolas", "Force of Will", "Fierce Guardianship",
                    "Deflecting Swat", "Counterspell", "Mana Drain")
        self.assertIn("pay {U}{B}{R}", self.oracle["Nicol Bolas"])
        lost = fast_combo_before_bolas()
        self.assertTrue(lost["opponent_wins_in_fixture"])
        self.assertFalse(lost["bolas_in_play"])
        defended = fast_combo_before_bolas(counter_available=True, blue_pitch=True)
        self.assertTrue(defended["countered"])
        self.assertFalse(defended["opponent_wins_in_fixture"])
        self.assertTrue(fast_combo_before_bolas(counter_available=True,
                                                blue_pitch=False)["opponent_wins_in_fixture"])
        self.assertTrue(fast_combo_before_bolas(counter_available=True,
                                                blue_pitch=True, life=1)["opponent_wins_in_fixture"])
        self.assertTrue(fast_combo_before_bolas(counter_available=True,
                                                blue_pitch=True,
                                                opponent_spell_counterable=False)
                        ["opponent_wins_in_fixture"])
        # Fixture does not measure prevalence of fast decks or imply Force
        # was drawn, or that other in-deck protection resolves every stack.


if __name__ == "__main__":
    unittest.main()
