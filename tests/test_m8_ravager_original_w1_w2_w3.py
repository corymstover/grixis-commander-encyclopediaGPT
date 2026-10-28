"""Original deferred Ravager W1/W2/W3: exact-current bounded rules witnesses.

The fixture exposes requirements and counterexamples, not goldfish odds, a
whole-game simulator, or a claim that opponents permit an assembled board.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DECK = "Nicol_Bolas__the_Ravager"
SHA = "acfa7922e262805a15932b53b1399acdf6ddf5592c8a3793fafdeec720ad4693"
PLAN_BLOB = "15450a891569966fdec582e4a905ce21f739b3c8"
COMMANDER = "Nicol Bolas, the Ravager // Nicol Bolas, the Arisen"
CASES = {"W1", "W2", "W3"}


def veil_cycle(*, temporal_loyalty=5, master_loyalty=3, cycles=6,
               source_outputs=(2, 1, 1), temporal=True, master=True,
               gauntlet=True, rowan=True, veil=True, removed=False):
    """Real Veil {4}+tap, Teferi -1 and second Teferi's Gauntlet 0.

    Three *physical* repeatable sources (Sol Ring plus two painless lands)
    pay exactly four each iteration. Temporal -1 untaps Veil and all three;
    Master uses its own additional Veil loyalty allowance for Gauntlet [0].
    Rowan copies that proliferate effect without paying another loyalty cost
    and without adding a loyalty activation allowance. All actions happen
    sorcery speed with the stack empty between activations. Both Teferis are
    chosen in each proliferate and must still have a loyalty counter.
    """
    trace = []
    for n in range(cycles):
        if not veil or removed or not temporal or temporal_loyalty <= 1:
            break
        if not master or master_loyalty <= 0 or not gauntlet:
            break
        if len(source_outputs) != 3 or sum(source_outputs) < 4:
            break
        # One Veil activation gives precisely one *additional* allowance to
        # each of two separate planeswalkers (not two for either one).
        mana_generated = sum(source_outputs)
        mana_left = mana_generated - 4
        temporal_loyalty -= 1  # -1 as cost; Teferi must survive at >=1.
        # Ability resolves: Veil and the same three tapped sources untap.
        untapped = ("The Chain Veil", "Sol Ring", "Command Tower",
                    "Underground Sea")
        proliferates = 1 + int(rowan)  # 0 loyalty ability + Rowan effect copy.
        temporal_loyalty += proliferates
        master_loyalty += proliferates
        trace.append({"cycle": n + 1, "mana_paid": 4,
                      "mana_left": mana_left, "untapped": untapped,
                      "veil_resolutions": n + 1,
                      "temporal_activations": n + 1,
                      "master_activations": n + 1,
                      "rowan_copy_activations": 0,
                      "proliferates": proliferates,
                      "temporal_loyalty": temporal_loyalty,
                      "master_loyalty": master_loyalty})
    return trace


def lone_temporal_veil(*, loyalty=5, repetitions=10, has_mana=True):
    """No other loyalty-restoring effects: the fifth -1 kills Teferi."""
    activations = 0
    while has_mana and loyalty > 0 and activations < repetitions:
        loyalty -= 1
        activations += 1
    return {"activations": activations, "loyalty": loyalty}


def transform_arisen(*, colors=("U", "B", "R"), generic=4, main_phase=True,
                     empty_stack=True, creature_available=True):
    """Actual sorcery-speed 4UBR transformed commander activation."""
    paid = (all(color in colors for color in ("U", "B", "R"))
            and generic >= 4 and main_phase and empty_stack
            and creature_available)
    return {"transformed": paid, "arisen_loyalty": 7 if paid else None}


def deepglow_double(loyalties, *, targets=(), all_targets_legal=True):
    """A target without a counter or an illegal target never gains counters."""
    state = dict(loyalties)
    for target in targets:
        if all_targets_legal and state.get(target, 0) > 0:
            state[target] *= 2
    return state


def arise_ultimate(*, loyalty, libraries, target=0, rings=True,
                   rings_mana=2, copy_target=1, original_resolves=True,
                   rings_resolves=True):
    """Pay a single -12 cost; a paid Rings copy changes a second library.

    Activation/targeting is assumed legal at start. Rings copies the *ability*,
    not its loyalty cost or the act of activating a planeswalker. The copy
    resolves first, then the original; no player loses merely by being at one.
    """
    if loyalty < 12 or not 0 <= target < len(libraries):
        return {"activated": False, "loyalty": loyalty,
                "libraries": tuple(libraries), "copies": 0, "exiled": ()}
    remaining = list(libraries)
    exiled = []
    copied = int(bool(rings and rings_resolves and rings_mana >= 2
                      and 0 <= copy_target < len(libraries)))
    for dest, resolved in ((copy_target, bool(copied)),
                           (target, original_resolves)):
        if resolved:
            count = max(0, remaining[dest] - 1)
            remaining[dest] -= count
            exiled.append((dest, count))
    return {"activated": True, "loyalty": loyalty - 12,
            "libraries": tuple(remaining), "copies": copied,
            "exiled": tuple(exiled), "immediate_losers": ()}


def library_draws_after_ultimate(remaining, draws):
    """Lose only when an actual draw from empty library is attempted."""
    assert draws >= 0
    return {"drawn": min(remaining, draws),
            "failed_draw": draws > remaining,
            "library_left": max(remaining - draws, 0)}


def bastion_proliferate(*, available_generic=4, untapped=True, tekuthal=True):
    """Only a real {4}, tap of this Bastion pays for its one event."""
    paid = available_generic >= 4 and untapped
    return {"paid": paid, "spent_generic": 4 if paid else 0,
            "events": (2 if tekuthal else 1) if paid else 0}


def proliferate_sources(*, noncreature=True, second_spell=False,
                        flux=True, tide=True, whale=True, tekuthal=True,
                        gambit=False, spell_resolves=True):
    """Distinct cast triggers and on-resolution Tezzeret's Gambit.

    Dreamtide Whale needs the player's *second* spell this turn. Tekuthal
    replaces each proliferate instruction with two; it isn't a spell trigger.
    Gambit's draw-two and proliferate only happen when the spell resolves.
    """
    triggers = (int(bool(flux and noncreature)) + int(bool(tide))
                + int(bool(whale and second_spell)))
    resolution = int(bool(gambit and spell_resolves))
    multiplier = 2 if tekuthal else 1
    return {"cast_triggers": triggers, "proliferates": (triggers + resolution)
            * multiplier, "drawn": 2 if gambit and spell_resolves else 0}


def dragon_god_ultimate(*, loyalty, opponent_has_legendary,
                        ability_resolves=True):
    """Dragon-God -8 has an explicit legendary creature/PW exception."""
    if loyalty < 8:
        return {"activated": False, "loyalty": loyalty, "losers": ()}
    return {"activated": True, "loyalty": loyalty - 8,
            "losers": tuple(i for i, has_legend in enumerate(opponent_has_legendary)
                            if not has_legend and ability_resolves)}


def liliana_ultimate(*, loyalty, opponent_permanents):
    """Separate single-type objects; opponents pick a survivor per type."""
    if loyalty < 9:
        return {"activated": False, "loyalty": loyalty, "sacrificed": {}}
    return {"activated": True, "loyalty": loyalty - 9,
            "sacrificed": {card_type: max(0, count - 1)
                           for card_type, count in opponent_permanents.items()}}


def ripples_of_potential(*, loyalty=4, generic_available=1,
                         blue_available=1, resolves=True, choose=True,
                         tekuthal=True):
    """Paid 1U; choosing a counter-added PW phases it out until untap."""
    cast = generic_available >= 1 and blue_available >= 1
    added = (2 if tekuthal else 1) if cast and resolves else 0
    phased = bool(added and choose)
    return {"cast": cast, "loyalty": loyalty + added,
            "phased_out": phased, "may_activate_now": not phased}


class RavagerOriginalW1W2W3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        idx = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        row = next(r for r in idx["decks"] if r["deck_id"] == DECK)
        source = (ROOT / row["source_file"]).read_bytes()
        assert sha256(source).hexdigest() == row["source_sha256"] == SHA
        assert source.decode().splitlines()[0] == f"1x {COMMANDER} [Commander]"
        cls.cards = Counter()
        for line in source.decode().splitlines():
            n, card = line.split("x ", 1)
            cls.cards[card.removesuffix(" [Commander]")] += int(n)
        assert sum(cls.cards.values()) == 100 and cls.cards[COMMANDER] == 1
        receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                              / f"{DECK}_{SHA[:16]}.json").read_text())
        assert receipt["approved_raw_sha256"] == SHA
        assert receipt["m6_transfer"]["plan_blob_sha"] == PLAN_BLOB
        cls.deferred = {r["case_id"] for r in receipt["m6_transfer"]["P1"]
                        if r["status"] == "DEFERRED"}
        assert CASES.issubset(cls.deferred)
        cls.oracle = {}
        with (ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl").open() as rows:
            for row in rows:
                data = json.loads(row)
                cls.oracle[data["canonical_name"]] = data["oracle_text"]

    def source(self, case, *cards):
        self.assertIn(case, self.deferred)
        for card in cards:
            self.assertEqual(self.cards[card], 1, card)

    def test_W1_two_teferis_veil_paid_repeat_and_missing_replenishment(self):
        self.source("W1", "Teferi, Temporal Archmage", "Teferi, Master of Time",
                    "The Chain Veil", "Ichormoon Gauntlet", "Rowan's Talent",
                    "Sol Ring", "Command Tower", "Underground Sea")
        self.assertIn("Untap up to four target permanents", self.oracle["Teferi, Temporal Archmage"])
        self.assertIn("[0]: Proliferate", self.oracle["Ichormoon Gauntlet"])
        self.assertIn("copy that ability", self.oracle["Rowan's Talent"])
        self.assertIn("{4}, {T}", self.oracle["The Chain Veil"])
        self.assertIn("Add {C}{C}", self.oracle["Sol Ring"])
        self.assertIn("Add one mana", self.oracle["Command Tower"])
        self.assertIn("Add {U} or {B}", self.oracle["Underground Sea"])
        trace = veil_cycle(cycles=8)
        self.assertEqual(len(trace), 8)
        self.assertEqual([r["mana_paid"] for r in trace], [4] * 8)
        self.assertEqual([r["proliferates"] for r in trace], [2] * 8)
        self.assertEqual([r["temporal_loyalty"] for r in trace], list(range(6, 14)))
        self.assertEqual(trace[-1]["master_loyalty"], 19)
        self.assertTrue(all(r["rowan_copy_activations"] == 0 for r in trace))
        self.assertTrue(all(len(r["untapped"]) == 4 for r in trace))
        # End-of-cycle invariant: Veil and all sources untapped, the same
        # four generic available, and loyalty strictly increased. In this
        # *unopposed* fixed board, arbitrarily many further cycles repeat.
        self.assertEqual(veil_cycle(cycles=8, rowan=False)[-1]["temporal_loyalty"], 5)
        self.assertEqual(lone_temporal_veil(), {"activations": 5, "loyalty": 0})
        self.assertEqual(len(veil_cycle(cycles=8, gauntlet=False)), 0)
        self.assertEqual(len(veil_cycle(cycles=8, master=False)), 0)
        self.assertEqual(len(veil_cycle(cycles=8, veil=False)), 0)
        self.assertEqual(len(veil_cycle(cycles=8, removed=True)), 0)
        self.assertEqual(len(veil_cycle(cycles=8, source_outputs=(1, 1, 1))), 0)
        self.assertEqual(len(veil_cycle(cycles=8, temporal_loyalty=1)), 0)

    def test_W2_seven_to_twelve_paid_arisen_rings_and_draw_not_instant_loss(self):
        self.source("W2", COMMANDER, "Rings of Brighthearth", "Spark Double",
                    "Deepglow Skate", "Flux Channeler", "Tekuthal, Inquiry Dominus",
                    "Karn's Bastion")
        self.assertIn("−12:", self.oracle[COMMANDER])
        self.assertIn("copy that ability", self.oracle["Rings of Brighthearth"])
        self.assertIn("double the number", self.oracle["Deepglow Skate"])
        self.assertIn("additional loyalty counter", self.oracle["Spark Double"])
        transform = transform_arisen()
        self.assertEqual(transform, {"transformed": True, "arisen_loyalty": 7})
        self.assertFalse(transform_arisen(generic=3)["transformed"])
        self.assertFalse(transform_arisen(main_phase=False)["transformed"])
        self.assertFalse(transform_arisen(colors=("U", "B"))["transformed"])
        self.assertFalse(arise_ultimate(loyalty=7, libraries=(70, 60))["activated"])
        board = deepglow_double({"Arisen": 7, "Spark Double Arisen": 8},
                                targets=("Arisen", "Spark Double Arisen"))
        self.assertEqual(board, {"Arisen": 14, "Spark Double Arisen": 16})
        result = arise_ultimate(loyalty=board["Arisen"], libraries=(70, 60, 55),
                                target=0, copy_target=1)
        self.assertEqual((result["loyalty"], result["copies"]), (2, 1))
        self.assertEqual(result["libraries"], (1, 1, 55))
        self.assertEqual(result["exiled"], ((1, 59), (0, 69)))
        self.assertEqual(result["immediate_losers"], ())
        self.assertFalse(library_draws_after_ultimate(1, 1)["failed_draw"])
        self.assertTrue(library_draws_after_ultimate(1, 2)["failed_draw"])
        self.assertEqual(arise_ultimate(loyalty=14, libraries=(70, 60),
                                       rings_mana=1)["libraries"], (1, 60))
        self.assertEqual(arise_ultimate(loyalty=14, libraries=(70, 60),
                                       original_resolves=False)["libraries"], (70, 1))
        self.assertEqual(deepglow_double({"Arisen": 7}, targets=("Arisen",),
                                         all_targets_legal=False)["Arisen"], 7)
        # A *paid* {4},T Bastion creates a single event; Tekuthal doubles
        # that event, not the mana. Likewise one Flux trigger per cast.
        charged = proliferate_sources(noncreature=True, flux=True, tide=False,
                                      whale=False, tekuthal=True)
        self.assertEqual(charged["proliferates"], 2)
        bastion = bastion_proliferate()
        self.assertEqual(bastion, {"paid": True, "spent_generic": 4, "events": 2})
        self.assertFalse(bastion_proliferate(available_generic=3)["paid"])
        self.assertFalse(bastion_proliferate(untapped=False)["paid"])
        self.assertEqual(bastion_proliferate(tekuthal=False)["events"], 1)
        self.assertEqual(7 + charged["proliferates"] + bastion["events"], 11)
        self.assertEqual(7 + charged["proliferates"] + bastion["events"] + 2, 13)
        # +2 consumes this turn's ordinary loyalty activation; -12 is later,
        # unless a separately paid, resolved Veil activation enables it.

    def test_W3_superfriends_actual_ultimates_legendary_exception_and_triggers(self):
        self.source("W3", "Nicol Bolas, Dragon-God", "Nicol Bolas, God-Pharaoh",
                    "Nicol Bolas, Planeswalker", "Liliana, Dreadhorde General",
                    "Deepglow Skate", "Flux Channeler", "Tekuthal, Inquiry Dominus",
                    "Karn's Bastion", "Inexorable Tide", "Ripples of Potential",
                    "Dreamtide Whale", "Tezzeret's Gambit")
        self.assertIn("doesn't control a legendary creature or planeswalker loses the game",
                      self.oracle["Nicol Bolas, Dragon-God"])
        self.assertIn("chooses a permanent", self.oracle["Liliana, Dreadhorde General"])
        self.assertIn("their second spell each turn", self.oracle["Dreamtide Whale"])
        self.assertIn("phase out", self.oracle["Ripples of Potential"])
        board = deepglow_double({"Dragon-God": 4, "God-Pharaoh": 7,
                                 "Nicol Bolas PW": 5, "Liliana": 6},
                                targets=("Dragon-God", "God-Pharaoh",
                                         "Nicol Bolas PW", "Liliana"))
        self.assertEqual(board, {"Dragon-God": 8, "God-Pharaoh": 14,
                                 "Nicol Bolas PW": 10, "Liliana": 12})
        dragon = dragon_god_ultimate(loyalty=board["Dragon-God"],
                                     opponent_has_legendary=(False, False, False))
        self.assertEqual(dragon["losers"], (0, 1, 2))
        self.assertEqual(dragon["loyalty"], 0)  # PW leaves; ability may resolve.
        self.assertEqual(dragon_god_ultimate(loyalty=8,
                         opponent_has_legendary=(False, True, False))["losers"], (0, 2))
        self.assertEqual(dragon_god_ultimate(loyalty=8,
                         opponent_has_legendary=(False, False),
                         ability_resolves=False)["losers"], ())
        self.assertFalse(dragon_god_ultimate(loyalty=4,
                         opponent_has_legendary=(False,))["activated"])
        liliana = liliana_ultimate(loyalty=board["Liliana"],
                                  opponent_permanents={"creature": 3,
                                                       "artifact": 2, "land": 1})
        self.assertEqual(liliana["loyalty"], 3)
        self.assertEqual(liliana["sacrificed"], {"creature": 2,
                                                "artifact": 1, "land": 0})
        self.assertEqual(liliana_ultimate(loyalty=12,
                         opponent_permanents={"creature": 1})["sacrificed"],
                         {"creature": 0})
        # Two independent cast triggers (Flux/Tide) on the *first*
        # noncreature spell, three including Whale on the second. Each is
        # replaced by Tekuthal with two proliferate instructions.
        self.assertEqual(proliferate_sources()["proliferates"], 4)
        self.assertEqual(proliferate_sources(second_spell=True)["proliferates"], 6)
        gambit = proliferate_sources(second_spell=True, gambit=True)
        self.assertEqual((gambit["proliferates"], gambit["drawn"]), (8, 2))
        countered = proliferate_sources(second_spell=True, gambit=True,
                                        spell_resolves=False)
        self.assertEqual((countered["proliferates"], countered["drawn"]), (6, 0))
        self.assertEqual(proliferate_sources(noncreature=False,
                         second_spell=False)["proliferates"], 2)
        self.assertEqual(proliferate_sources(noncreature=True,
                         second_spell=True, whale=False)["proliferates"], 4)
        # A resolved Ripples may protect a proliferated PW by phasing it out,
        # but that PW is unavailable for later activations until it phases in.
        ripple = ripples_of_potential()
        self.assertEqual(ripple, {"cast": True, "loyalty": 6,
                                  "phased_out": True, "may_activate_now": False})
        self.assertEqual(ripples_of_potential(choose=False)["loyalty"], 6)
        self.assertTrue(ripples_of_potential(choose=False)["may_activate_now"])
        self.assertFalse(ripples_of_potential(generic_available=0)["cast"])
        self.assertEqual(ripples_of_potential(resolves=False)["loyalty"], 4)


if __name__ == "__main__":
    unittest.main()
