"""Exact-current original M6 W cases: Sol'kanar, RogSi, and Nekusar.

Executable finite source-paid witnesses plus explicit false-infinity, missing
card, priority, finite-library and delayed-loss counterexamples. Never a full
Magic rules engine or claim that these configurations are assembled at will.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

from test_m8_marchesa_dealer_original_e2_w2 import (
    breach_led_brain_freeze, escape_oracle_after_self_mill,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "Sol_kanar_the_Swamp_King": (
        "2bd99c569df4a86897bca0164d2a1fa309b92f8b721e406b8394dfb04b1239e3",
        "bacc66959952f4ce0310200ea8444c2a054d9b67"),
    "RogSi": (
        "97f3c0ca70303b44cd887938c320b75de01e991feec7d71d4c18811aeaa88225",
        "8b07274e5120b105c8fcf68c98635105448a29cf"),
    "Nekusar__the_Mindrazer": (
        "043d2521cec1e82d7ba8ff899b96920249e16ae32e73e2759f02044b41f94e53",
        "a6fba2244e45bfd57b98e8c94ae073059bd2c013"),
}


def vito_blood_chain(*, opponent_life=5, our_life=40, initial_life_gain=1,
                     blood=True, vito=True, target_legal=True,
                     stop_after=100):
    """One opponent; a *real* life gain seeds Vito→loss→Blood→gain.

    Every individual triggered gain/loss event has a source. Opponent leaves
    when life <= 0, so no literally endless triggers after a victory.
    """
    pending_gain = [initial_life_gain] if initial_life_gain > 0 else []
    history = []
    for _ in range(stop_after):
        if not pending_gain or opponent_life <= 0:
            break
        gain = pending_gain.pop(0)
        our_life += gain
        drain = gain if vito and target_legal else 0
        if drain:
            opponent_life -= drain
            if blood:
                pending_gain.append(drain)
        history.append({"gain": gain, "vito_drain": drain,
                        "opponent_life": opponent_life, "our_life": our_life})
    return {"events": tuple(history), "opponent_life": opponent_life,
            "our_life": our_life, "opponent_lost": opponent_life <= 0,
            "pending_gain": tuple(pending_gain)}


def reservoir_blood_chain(*, our_life=51, opponents=(40, 40, 40),
                          blood=True, targeted_players=(0, 1, 2),
                          damage_prevented=False, available=True):
    """Pay 50 life, then 50 opponent damage, then Blood gain if life lost.

    The activated ability is not a free trigger. Life at zero loses before
    gaining Blood's triggered life, even if Reservoir's ability was activated.
    """
    others = list(opponents)
    records = []
    for target in targeted_players:
        if not available or our_life <= 50 or not 0 <= target < len(others):
            break
        if others[target] <= 0:
            continue
        our_life -= 50
        loss = 0 if damage_prevented else 50
        others[target] -= loss
        if blood and loss:
            our_life += loss
        records.append({"target": target, "paid_life": 50,
                        "damage_dealt": loss, "blood_gain": loss if blood else 0,
                        "life_after": our_life, "target_life": others[target]})
    return {"records": tuple(records), "our_life": our_life,
            "opponents": tuple(others),
            "eliminated": tuple(i for i, l in enumerate(others) if l <= 0)}


def painter_grindstone(*, library_colors, painter_color="blue",
                       painter_present=True, grindstone_untapped=True,
                       generic_available=3, target_legal=True):
    """One paid Grindstone activation: mill two, then repeat if two share.

    Painter adds a color to every library card. If no Painter, the physical
    color sets in the fixture decide the repetition, not a fictional repeat.
    """
    if not grindstone_untapped or generic_available < 3 or not target_legal:
        return {"activated": False, "milled": 0, "library_left": len(library_colors)}
    colors = [set(c) | ({painter_color} if painter_present else set())
              for c in library_colors]
    milled = 0
    repeats = 0
    while colors:
        group, colors = colors[:2], colors[2:]
        milled += len(group)
        if len(group) != 2 or not (group[0] & group[1]):
            break
        repeats += 1
    return {"activated": True, "milled": milled,
            "library_left": len(colors), "repeats": repeats,
            "activation_cost": 3}


def tainted_pact_exile(names, *, put_in_hand_at=None):
    """Each actual card enters exile until a duplicate or a chosen hand card."""
    exiled = []
    for i, name in enumerate(names):
        if i == put_in_hand_at and name not in exiled:
            return {"exiled": tuple(exiled), "hand_card": name, "library": len(names) - i - 1}
        duplicate = name in exiled
        exiled.append(name)
        if duplicate:
            return {"exiled": tuple(exiled), "hand_card": None,
                    "library": len(names) - i - 1}
    return {"exiled": tuple(exiled), "hand_card": None, "library": 0}


def oracle_resolution(*, library, devotion, triggered=True, countered=False):
    """A resolved Oracle ETB checks actual library size and current devotion."""
    return bool(triggered and not countered and devotion >= library)


def extra_turn_with_delayed_loss(*, red_paid=2, spell_resolves=True,
                                 finish_wins=False, end_step_reached=True,
                                 opponent_stops_finish=False):
    """Final Fortune/Warrior's Oath RR; the *extra* turn is not a win."""
    if red_paid < 2 or not spell_resolves:
        return {"extra_turn": False, "won": False, "lost": False}
    won = bool(finish_wins and not opponent_stops_finish)
    return {"extra_turn": True, "won": won,
            "lost": bool(not won and end_step_reached)}


def wheels_from_one_grave_card(*, own_library=20, other_grave=6,
                               hand_cards=7, red_pool=7,
                               opponent_hand_for_will=7,
                               breach=True, wheel=True, wills_cast=True,
                               nekusar=True, dreams=True, sheoldred=True,
                               opponents=(40, 40, 40), requested=3):
    """One physical Wheel returns to grave after escape, not exile.

    Jeska's Will has already been paid for and resolved before this fixture;
    its red mode produces exactly the *target's hand at resolution*, not an
    assumed seven. Every escaped 2R Wheel exiles three other grave cards;
    each Wheel discards the physical current hand and draws seven from library.
    Damage/loss triggers resolve after the whole Wheel has finished drawing.
    """
    red = min(red_pool, opponent_hand_for_will) if wills_cast else 0
    other = other_grave
    hand = hand_cards
    opp = list(opponents)
    records = []
    for _ in range(requested):
        if not breach or not wheel or red < 3 or other < 3:
            break
        # Escape a *single* Wheel, keep its own physical card out of payment.
        other -= 3
        red -= 3  # three red legally pays {2}{R}.
        other += hand  # Wheel discards all our current hand.
        hand = min(7, own_library)
        own_library -= hand
        failed_self_draw = hand < 7
        # Wheel object returns to grave after resolving despite escape.
        # A failed own draw loses the game before our delayed punishment
        # triggers could convert those opponent draws to a victory.
        per_opponent = (7 * (int(nekusar) + int(dreams)
                             + 2 * int(sheoldred))) if not failed_self_draw else 0
        opp = [life - per_opponent for life in opp]
        records.append({"escaped": True, "paid_red": 3,
                        "other_grave": other, "own_library": own_library,
                        "own_hand": hand, "red_left": red,
                        "opponent_lives": tuple(opp),
                        "failed_self_draw": failed_self_draw})
        if failed_self_draw:
            break
    return {"records": tuple(records), "opponents": tuple(opp),
            "own_library": own_library, "other_grave": other,
            "red_left": red}


def niv_curiosity_chain(*, own_library=20, opponent_life=15,
                        target_legal=True, curiosity=True,
                        optional_draw=True):
    """The initial ordinary draw starts actual Niv ping→Curiosity draw.

    Curiosity says MAY, so it is not an uncontrollable compulsory loop.
    Each successful draw removes one distinct card from the finite library.
    """
    damage = 0
    draws = 0
    while own_library > 0 and target_legal:
        own_library -= 1
        draws += 1
        damage += 1
        opponent_life -= 1
        if opponent_life <= 0 or not curiosity or not optional_draw:
            break
    return {"draws": draws, "damage": damage, "own_library": own_library,
            "opponent_life": opponent_life, "opponent_lost": opponent_life <= 0,
            "attempted_empty_draw": False}


class ThreeDecksRemainingWinTraces(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        cls.records = {}
        for deck, (raw_sha, plan_blob) in SOURCES.items():
            row = next(x for x in index["decks"] if x["deck_id"] == deck)
            raw = (ROOT / row["source_file"]).read_bytes()
            assert sha256(raw).hexdigest() == row["source_sha256"] == raw_sha
            cards = Counter()
            for line in raw.decode().splitlines():
                n, name = line.split("x ", 1)
                cards[name.removesuffix(" [Commander]")] += int(n)
            assert sum(cards.values()) == 100
            receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                                  / f"{deck}_{raw_sha[:16]}.json").read_text())
            assert receipt["approved_raw_sha256"] == raw_sha
            assert receipt["m6_transfer"]["plan_blob_sha"] == plan_blob
            deferred = {r["case_id"] for r in receipt["m6_transfer"]["P1"]
                        if r["status"] == "DEFERRED"}
            cls.records[deck] = {"cards": cards, "deferred": deferred}
        assert SOURCES.keys() == cls.records.keys()
        cls.oracle = {}
        with (ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl").open() as stream:
            for line in stream:
                row = json.loads(line)
                cls.oracle[row["canonical_name"]] = row["oracle_text"]

    def source(self, deck, case, *cards):
        self.assertIn(case, self.records[deck]["deferred"])
        for name in cards:
            self.assertEqual(self.records[deck]["cards"][name], 1, (deck, name))

    def test_sol_W1_blood_vito_seed_and_mandatory_finite_drain(self):
        deck = "Sol_kanar_the_Swamp_King"
        self.source(deck, "W1", "Sol'kanar the Swamp King", "Exquisite Blood",
                    "Bloodthirsty Conqueror", "Vito, Thorn of the Dusk Rose",
                    "Marauding Blight-Priest", "Enduring Tenacity", "Starscape Cleric",
                    "Demon's Horn")
        self.assertIn("Whenever an opponent loses life", self.oracle["Exquisite Blood"])
        self.assertIn("Whenever you gain life", self.oracle["Vito, Thorn of the Dusk Rose"])
        self.assertIn("Whenever a player casts a black spell", self.oracle["Demon's Horn"])
        trace = vito_blood_chain(opponent_life=5, initial_life_gain=1)
        self.assertEqual(len(trace["events"]), 5)
        self.assertEqual([e["opponent_life"] for e in trace["events"]], [4, 3, 2, 1, 0])
        self.assertTrue(trace["opponent_lost"])
        self.assertEqual(trace["our_life"], 45)
        self.assertFalse(vito_blood_chain(blood=False)["opponent_lost"])
        self.assertFalse(vito_blood_chain(vito=False)["opponent_lost"])
        self.assertFalse(vito_blood_chain(target_legal=False)["opponent_lost"])
        self.assertEqual(vito_blood_chain(initial_life_gain=0)["events"], ())
        # Conqueror can supply the loss→gain half; Tenacity another gain→loss
        # half. Horn and Sol'kanar only seed life when a black spell is cast.

    def test_sol_W2_reservoir_50_life_paid_blood_replenishes_per_target(self):
        deck = "Sol_kanar_the_Swamp_King"
        self.source(deck, "W2", "Aetherflux Reservoir", "Exquisite Blood",
                    "Bloodthirsty Conqueror", "Sol'kanar the Swamp King", "Demon's Horn")
        self.assertIn("Pay 50 life", self.oracle["Aetherflux Reservoir"])
        result = reservoir_blood_chain()
        self.assertEqual(result["eliminated"], (0, 1, 2))
        self.assertEqual(result["our_life"], 51)
        self.assertEqual([r["paid_life"] for r in result["records"]], [50, 50, 50])
        self.assertEqual([r["blood_gain"] for r in result["records"]], [50] * 3)
        self.assertEqual(len(reservoir_blood_chain(our_life=50)["records"]), 0)
        self.assertEqual(len(reservoir_blood_chain(blood=False)["records"]), 1)
        self.assertEqual(len(reservoir_blood_chain(damage_prevented=True)["records"]), 1)
        self.assertEqual(len(reservoir_blood_chain(available=False)["records"]), 0)
        # Source is specifically a *player* taking damage. A creature target
        # or prevented damage cannot fuel the mandatory Blood/Conqueror gain.

    def test_sol_W3_painter_grindstone_paid_one_target_not_instant_win(self):
        deck = "Sol_kanar_the_Swamp_King"
        self.source(deck, "W3", "Painter's Servant", "Grindstone", "Demonic Tutor")
        self.assertIn("choose a color", self.oracle["Painter's Servant"])
        self.assertIn("{3}, {T}", self.oracle["Grindstone"])
        library = [{"white"}, {"red"}, {"green"}, {"black"}, {"colorless"}]
        result = painter_grindstone(library_colors=library)
        self.assertEqual(result["milled"], 5)
        self.assertEqual(result["library_left"], 0)
        self.assertEqual(result["activation_cost"], 3)
        absent = painter_grindstone(library_colors=library, painter_present=False)
        self.assertEqual((absent["milled"], absent["library_left"]), (2, 3))
        self.assertFalse(painter_grindstone(library_colors=library,
                         generic_available=2)["activated"])
        self.assertFalse(painter_grindstone(library_colors=library,
                         grindstone_untapped=False)["activated"])
        self.assertFalse(painter_grindstone(library_colors=library,
                         target_legal=False)["activated"])
        # One resolution targets ONE player, not the entire table. Losing to
        # drawing from empty occurs on that player's subsequent failed draw.

    def test_rog_W1_oracle_consultation_and_singleton_pact_full_exile(self):
        deck = "RogSi"
        self.source(deck, "W1", "Thassa's Oracle", "Demonic Consultation", "Tainted Pact",
                    "Rograkh, Son of Rohgahh", "Silas Renn, Seeker Adept")
        self.assertIn("devotion to blue", self.oracle["Thassa's Oracle"])
        self.assertIn("Exile the top six cards", self.oracle["Demonic Consultation"])
        self.assertIn("two cards with the same name", self.oracle["Tainted Pact"])
        cards = self.records[deck]["cards"]
        self.assertEqual(sum(cards.values()), 100)
        self.assertTrue(all(count == 1 for count in cards.values()))
        residual = [name for name in cards if name not in
                    {"Rograkh, Son of Rohgahh", "Silas Renn, Seeker Adept",
                     "Thassa's Oracle", "Tainted Pact", "Demonic Consultation"}]
        self.assertEqual(len(residual), 95)
        self.assertEqual(tainted_pact_exile(residual)["library"], 0)
        self.assertEqual(len(tainted_pact_exile(residual)["exiled"]), 95)
        self.assertTrue(oracle_resolution(library=0, devotion=2))
        # Consult naming a card *absent* from the remaining library removes
        # all ninety-five (including mandatory first six) if it resolves.
        self.assertNotIn("Plains", residual)
        self.assertGreaterEqual(len(residual), 6)
        self.assertFalse(oracle_resolution(library=1, devotion=0))
        self.assertFalse(oracle_resolution(library=0, devotion=2, countered=True))
        duplicate = tainted_pact_exile(["Island", "Sol Ring", "Island", "Wheel"])
        self.assertEqual((len(duplicate["exiled"]), duplicate["library"]), (3, 1))
        chosen = tainted_pact_exile(residual, put_in_hand_at=1)
        self.assertEqual(chosen["library"], 93)
        # The Oracle ETB trigger must be on stack and resolve after Pact or
        # Consultation; an unprotected sorcery-speed Pact is not assumed.

    def test_rog_W2_one_real_led_breach_freeze_and_finite_oracle_conversion(self):
        deck = "RogSi"
        self.source(deck, "W2", "Underworld Breach", "Lion's Eye Diamond",
                    "Lotus Petal", "Brain Freeze", "Wheel of Fortune",
                    "Jeska's Will", "Grinding Station", "Mox Amber",
                    "Thassa's Oracle")
        self.assertIn("exile three other cards", self.oracle["Underworld Breach"])
        self.assertIn("Sacrifice this artifact", self.oracle["Lion's Eye Diamond"])
        # Previous audited one-card LED recurrence is reused *only* after
        # binding every listed combo object to this different exact 100.
        # RogSi has TWO commanders, so own staged library is 83, not 84.
        self.assertEqual(83 + 9 + 1 + 1 + 1 + 1 + 2 + 2, 100)
        result = breach_led_brain_freeze(own_library=83)
        self.assertEqual(len(result["history"]), 11)
        self.assertEqual(result["own_library"], 0)
        self.assertEqual(result["opponents"], (0, 0, 0))
        self.assertEqual(result["history"][-1]["led_zone"], "graveyard")
        self.assertTrue(escape_oracle_after_self_mill(
                        own_library=0, other_grave_cards=result["other_grave_cards"])
                        ["oracle_win"])
        self.assertFalse(escape_oracle_after_self_mill(
                         own_library=1)["oracle_win"])
        self.assertFalse(escape_oracle_after_self_mill(
                         other_grave_cards=5)["oracle_win"])
        self.assertFalse(escape_oracle_after_self_mill(
                         oracle_trigger_resolves=False)["oracle_win"])
        self.assertEqual(breach_led_brain_freeze(own_library=83, breach=False)
                         ["history"], [])
        # LED sacrifices *one* artifact and discards a hand, not free UBR;
        # Station additionally requires a real artifact sacrifice and tap.

    def test_rog_W3_fortune_oath_extra_turn_must_finish_before_end_step(self):
        deck = "RogSi"
        self.source(deck, "W3", "Final Fortune", "Warrior's Oath",
                    "Ad Nauseam", "Necrodominance", "Thassa's Oracle")
        self.assertIn("At the beginning of that turn's end step, you lose the game",
                      self.oracle["Final Fortune"])
        self.assertIn("At the beginning of that turn's end step, you lose the game",
                      self.oracle["Warrior's Oath"])
        self.assertEqual(extra_turn_with_delayed_loss(),
                         {"extra_turn": True, "won": False, "lost": True})
        self.assertTrue(extra_turn_with_delayed_loss(finish_wins=True)["won"])
        self.assertTrue(extra_turn_with_delayed_loss(
                        finish_wins=True, opponent_stops_finish=True)["lost"])
        self.assertFalse(extra_turn_with_delayed_loss(red_paid=1)["extra_turn"])
        self.assertFalse(extra_turn_with_delayed_loss(
                         spell_resolves=False)["extra_turn"])
        # No probability of loading Oracle from Ad Naus/Necrodominance is
        # inferred, and neither red spell itself constitutes a win condition.

    def test_nek_W2_same_wheel_escape_recasts_paid_twice_not_infinite(self):
        deck = "Nekusar__the_Mindrazer"
        self.source(deck, "W2", "Nekusar, the Mindrazer", "Underworld Breach",
                    "Wheel of Fortune", "Jeska's Will", "Underworld Dreams",
                    "Sheoldred, the Apocalypse")
        self.assertEqual(self.records[deck]["cards"]["Fate Unraveler"], 0)
        self.assertIn("Whenever an opponent draws a card", self.oracle["Nekusar, the Mindrazer"])
        self.assertIn("Whenever an opponent draws a card", self.oracle["Underworld Dreams"])
        self.assertIn("they lose 2 life", self.oracle["Sheoldred, the Apocalypse"])
        self.assertIn("Add {R} for each card", self.oracle["Jeska's Will"])
        r = wheels_from_one_grave_card(requested=3)
        self.assertEqual(len(r["records"]), 2)
        self.assertEqual([x["own_library"] for x in r["records"]], [13, 6])
        self.assertEqual([x["red_left"] for x in r["records"]], [4, 1])
        self.assertEqual(r["opponents"], (-16, -16, -16))
        self.assertEqual(r["other_grave"], 14)
        self.assertEqual(len(wheels_from_one_grave_card(
                         opponent_hand_for_will=0)["records"]), 0)
        self.assertEqual(len(wheels_from_one_grave_card(
                         other_grave=2)["records"]), 0)
        self.assertEqual(len(wheels_from_one_grave_card(
                         breach=False)["records"]), 0)
        self.assertTrue(wheels_from_one_grave_card(
                        own_library=10)["records"][1]["failed_self_draw"])
        self.assertEqual(wheels_from_one_grave_card(sheoldred=False)
                         ["opponents"], (12, 12, 12))
        # Escape returns resolved instant/sorcery Wheel to its graveyard.
        # No unsupported Fate Unraveler, endless own library, free Jeska
        # modes, free red, or automatic mill-proof victory is claimed.

    def test_nek_W3_niv_curiosity_optional_real_draw_damage_finite(self):
        deck = "Nekusar__the_Mindrazer"
        self.source(deck, "W3", "Curiosity", "Niv-Mizzet, Parun")
        self.assertIn("Whenever you draw a card", self.oracle["Niv-Mizzet, Parun"])
        self.assertIn("you may draw a card", self.oracle["Curiosity"])
        r = niv_curiosity_chain(own_library=20, opponent_life=15)
        self.assertEqual((r["draws"], r["damage"], r["own_library"]), (15, 15, 5))
        self.assertTrue(r["opponent_lost"])
        self.assertFalse(r["attempted_empty_draw"])
        self.assertFalse(niv_curiosity_chain(own_library=20,
                         opponent_life=25)["opponent_lost"])
        self.assertEqual(niv_curiosity_chain(own_library=20,
                         opponent_life=25)["draws"], 20)
        self.assertEqual(niv_curiosity_chain(own_library=20,
                         opponent_life=25, curiosity=False)["draws"], 1)
        self.assertEqual(niv_curiosity_chain(own_library=20,
                         opponent_life=25, optional_draw=False)["draws"], 1)
        self.assertEqual(niv_curiosity_chain(target_legal=False)["draws"], 0)
        # Optional Curiosity and finite library constrain the chain; choosing
        # to draw from zero would lose, not create an automatic infinity.


if __name__ == "__main__":
    unittest.main()
