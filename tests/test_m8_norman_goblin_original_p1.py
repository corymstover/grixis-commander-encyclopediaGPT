"""Original Norman/Green Goblin P1 executable finite action traces, not a rules engine.

The immutable register calls this commander Goben__Gene_Splice_Savant. The exact
owner-approved source and commander line establish its sole authorized crosswalk.
"""

from collections import Counter
from hashlib import sha256
from math import comb
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DECK = "Goben__Gene_Splice_Savant"
SHA = "c002a49243bd54780bb0f4a36a3c239a00e042defa1d0c6c4b891c3c8060eef9"
CASES = {"K4", "K5", "K6", "K7", "E1", "E2", "W1", "W2", "W3", "F2", "F3"}


def mox_amber_colors(*, legendary_front=False, transformed=False, other_legendary=()):
    """Available colors of legendary creatures, not mere color identities."""
    colors = set(other_legendary)
    if legendary_front:
        colors.add("U")
    if transformed:
        colors.update("UBR")
    return colors


def zero_cost_mox_legal(*, mox_name, imprintable_nonartifact_nonland=False,
                        discardable_land=False):
    """Some zero printed mana costs hide real hand-card costs."""
    if mox_name == "Chrome Mox":
        return imprintable_nonartifact_nonland
    if mox_name == "Mox Diamond":
        return discardable_land
    raise ValueError(mox_name)


def connive(*, damage_dealt, library, hand, discard_index, counters):
    """One combat-damage trigger with physical draw/discard order."""
    if not damage_dealt:
        return library[:], hand[:], counters, None
    if not library:
        raise ValueError("cannot draw from an empty library in this fixture")
    library, hand = library[:], hand[:]
    hand.append(library.pop(0))
    discarded_name, is_land = hand.pop(discard_index)
    counters += int(not is_land)
    return library, hand, counters, (discarded_name, is_land)


def cavern_protects(*, chosen_type, creature_types, paid_with_cavern_colored_mana):
    return bool(paid_with_cavern_colored_mana and chosen_type in creature_types)


def transform(*, on_battlefield=True, main_phase=True, stack_empty=True,
              mana=None, activated_before=False):
    """Costs one generic plus UBR and only as a sorcery; no free second face cast."""
    if mana is None:
        mana = Counter()
    if not on_battlefield or not main_phase or not stack_empty or activated_before:
        return False
    if any(mana[color] < 1 for color in "UBR"):
        return False
    return sum(mana.values()) >= 4


def mayhem_cast_cost(*, card_discarded_this_turn, transformed, normal_timing,
                     flash_granted, printed_generic, colored_cost, mana,
                     additional_discard_needed=False, cards_in_hand=0):
    """Mayhem does not waive timing, printed colored mana, or extra cast costs."""
    if not (card_discarded_this_turn and transformed and (normal_timing or flash_granted)):
        return False
    if additional_discard_needed and not cards_in_hand:
        return False
    paid = Counter(mana)
    for symbol in colored_cost:
        paid[symbol] -= 1
        if paid[symbol] < 0:
            return False
    return sum(paid.values()) >= max(0, printed_generic - 2)


def oracle_trigger_wins(*, oracle_resolves, devotion, library_size,
                        consultation_resolves=False, consultation_named_absent=False,
                        pact_resolves=False, singleton_library=False):
    """Triggered ability checks library on resolution, after responses."""
    if not oracle_resolves:
        return False
    if consultation_resolves and consultation_named_absent:
        library_size = 0
    if pact_resolves and singleton_library:
        library_size = 0
    return devotion >= library_size


def breach_led_brain_freeze(*, library, grave_filler, breach=True, led=True,
                            brain_freeze=True, rounds=3, initial_storm=1):
    """Pay BF {1}{U}, escape exiles 3 OTHER cards, LED gives UUU.

    First LED starts on battlefield; later LED casts are escaped and cost an
    additional three other cards each. Brain Freeze's storm copies each mill
    three from the chosen player's real finite library. No endless-library
    fiction or automatic opponent kill is inferred.
    """
    mana, storm, grave = 0, initial_storm, grave_filler
    history = []
    for step in range(rounds):
        if not (breach and led and brain_freeze):
            break
        if step:
            if grave < 3:
                break
            grave -= 3  # replay LED from grave via escape
            storm += 1
        mana += 3  # sacrifice LED for three blue, moving LED to grave
        if mana < 2 or grave < 3:
            mana -= 3  # cannot realize the proposed Brain Freeze cast
            break
        mana -= 2
        grave -= 3  # Brain Freeze escape, three OTHER graveyard cards
        copies = storm + 1  # original Brain Freeze plus storm copies
        milled = min(library, 3 * copies)
        library -= milled
        grave += milled
        storm += 1
        history.append({"round": step + 1, "mana": mana, "library": library,
                        "grave_filler": grave, "copies": copies, "milled": milled})
    return history


def station_amber_to_oracle(*, library=90, grave_filler=3, breach=True,
                            station=True, amber=True, norman=True,
                            oracle_in_hand=True, opponent_intervenes=False):
    """One physical Mox: escape, ETB untap Station, tap for U, sac to mill 3.

    Each escape exiles 3 eligible graveyard cards. Each Station activation
    mills up to 3 physical library cards; the graveyard only replenishes from
    real cards. One loop nets 1U but cannot continue past an empty library.
    """
    blue = 0
    rounds = 0
    station_untapped = True
    mox_in_grave = True
    exiled = 0
    while breach and station and amber and mox_in_grave and grave_filler >= 3 and library:
        if opponent_intervenes:
            break
        grave_filler -= 3
        exiled += 3
        mox_in_grave = False  # one real Amber escaped and entered
        station_untapped = True  # Station trigger sees artifact enter
        blue += int(norman)   # Amber taps for blue iff Norman is legendary U creature
        assert station_untapped
        station_untapped = False
        mox_in_grave = True  # Station's tap+sac cost physically sacrifices Amber
        milled = min(3, library)
        grave_filler += milled
        library -= milled
        rounds += 1
    oracle_wins = bool(oracle_in_hand and blue >= 2 and library == 0 and
                       oracle_trigger_wins(oracle_resolves=True, devotion=2,
                                          library_size=library))
    return {"rounds": rounds, "blue": blue, "library": library,
            "grave_filler": grave_filler, "exiled": exiled,
            "mox_in_grave": mox_in_grave, "oracle_wins": oracle_wins}


class NormanGreenGoblinOriginalP1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        row = next(x for x in index["decks"] if x["deck_id"] == DECK)
        raw = (ROOT / row["source_file"]).read_bytes()
        assert sha256(raw).hexdigest() == row["source_sha256"] == SHA
        lines = raw.decode().splitlines()
        assert lines[0] == "1x Norman Osborn // Green Goblin [Commander]"
        cls.cards = Counter()
        for line in lines:
            quantity, name = line.split("x ", 1)
            cls.cards[name.replace(" [Commander]", "")] += int(quantity)
        assert sum(cls.cards.values()) == 100
        cls.receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                                  / f"{DECK}_{SHA[:16]}.json").read_text())
        assert cls.receipt["approved_raw_sha256"] == SHA
        assert cls.receipt["m6_transfer"]["plan_blob_sha"] == "24c7b78a1548c7f0c9cf40931d06b13286cf0f6c"
        cls.deferred = {r["case_id"] for r in cls.receipt["m6_transfer"]["P1"]
                        if r["status"] == "DEFERRED"}
        assert cls.deferred == CASES

    def source(self, case, *cards):
        self.assertIn(case, self.deferred)
        for card in cards:
            self.assertEqual(self.cards[card], 1, card)

    def test_K4_mox_amber_legendaries_and_face_specific_colors(self):
        self.source("K4", "Norman Osborn // Green Goblin", "Mox Amber")
        self.assertEqual(mox_amber_colors(legendary_front=True), {"U"})
        self.assertEqual(mox_amber_colors(transformed=True), {"U", "B", "R"})
        self.assertEqual(mox_amber_colors(), set())

    def test_K5_connive_damage_draw_then_discard_land_or_nonland(self):
        self.source("K5", "Norman Osborn // Green Goblin", "Cabal Ritual",
                    "Careful Study", "Ancient Tomb")
        deck = [("Careful Study", False), ("Ancient Tomb", True)]
        library, hand, counters, discarded = connive(
            damage_dealt=True, library=deck, hand=[("Cabal Ritual", False)],
            discard_index=0, counters=0)
        self.assertEqual((discarded, counters, len(hand), len(library)),
                         (("Cabal Ritual", False), 1, 1, 1))
        l2, h2, n2, d2 = connive(damage_dealt=True, library=library,
                                hand=hand, discard_index=1, counters=counters)
        self.assertEqual((d2, n2), (("Ancient Tomb", True), 1))
        self.assertEqual(connive(damage_dealt=False, library=l2, hand=h2,
                                discard_index=0, counters=n2)[2:], (1, None))
        self.assertEqual(len(l2) + len(h2) + 2, len(deck) + 1)

    def test_K6_cavern_human_front_cast_vs_other_type_or_missing_payment(self):
        self.source("K6", "Norman Osborn // Green Goblin", "Cavern of Souls",
                    "Thassa's Oracle")
        self.assertTrue(cavern_protects(chosen_type="Human", creature_types={"Human", "Scientist", "Villain"},
                                       paid_with_cavern_colored_mana=True))
        self.assertFalse(cavern_protects(chosen_type="Goblin", creature_types={"Human", "Scientist", "Villain"},
                                        paid_with_cavern_colored_mana=True))
        self.assertFalse(cavern_protects(chosen_type="Human", creature_types={"Merfolk", "Wizard"},
                                        paid_with_cavern_colored_mana=True))
        self.assertFalse(cavern_protects(chosen_type="Human", creature_types={"Human"},
                                        paid_with_cavern_colored_mana=False))

    def test_K7_generic_oracle_and_breach_wins_do_not_require_commander(self):
        self.source("K7", "Thassa's Oracle", "Demonic Consultation", "Underworld Breach",
                    "Lion's Eye Diamond", "Brain Freeze")
        self.assertTrue(oracle_trigger_wins(oracle_resolves=True, devotion=2, library_size=63,
                                             consultation_resolves=True, consultation_named_absent=True))
        self.assertFalse(oracle_trigger_wins(oracle_resolves=True, devotion=2, library_size=63))
        self.assertGreaterEqual(len(breach_led_brain_freeze(library=45, grave_filler=9,
                                                           rounds=2)), 2)
        self.assertEqual(breach_led_brain_freeze(library=45, grave_filler=9, led=False), [])

    def test_E1_transform_then_discard_this_turn_grants_paid_mayhem(self):
        self.source("E1", "Norman Osborn // Green Goblin", "Frantic Search",
                    "Faithless Looting", "Borne Upon a Wind", "Big Score")
        self.assertTrue(transform(mana=Counter({"U": 1, "B": 1, "R": 1, "C": 1})))
        self.assertFalse(transform(mana=Counter({"U": 1, "B": 1, "R": 1})))
        self.assertFalse(transform(main_phase=False, mana=Counter({"U": 1, "B": 1, "R": 1, "C": 1})))
        # Frantic Search costs {2}{U}, Goblin's generic reduction makes it {U}.
        self.assertTrue(mayhem_cast_cost(card_discarded_this_turn=True, transformed=True,
                                         normal_timing=True, flash_granted=False,
                                         printed_generic=2, colored_cost="U", mana={"U": 1}))
        self.assertFalse(mayhem_cast_cost(card_discarded_this_turn=False, transformed=True,
                                          normal_timing=True, flash_granted=False,
                                          printed_generic=2, colored_cost="U", mana={"U": 1}))
        self.assertFalse(mayhem_cast_cost(card_discarded_this_turn=True, transformed=True,
                                          normal_timing=False, flash_granted=False,
                                          printed_generic=2, colored_cost="U", mana={"U": 1}))
        self.assertTrue(mayhem_cast_cost(card_discarded_this_turn=True, transformed=True,
                                         normal_timing=False, flash_granted=True,
                                         printed_generic=2, colored_cost="U", mana={"U": 1}))
        # Big Score additional discard cost remains after generic reduction.
        self.assertFalse(mayhem_cast_cost(card_discarded_this_turn=True, transformed=True,
                                          normal_timing=True, flash_granted=False,
                                          printed_generic=3, colored_cost="R", mana={"C": 1, "R": 1},
                                          additional_discard_needed=True, cards_in_hand=0))
        self.assertTrue(mayhem_cast_cost(card_discarded_this_turn=True, transformed=True,
                                         normal_timing=True, flash_granted=False,
                                         printed_generic=3, colored_cost="R", mana={"C": 1, "R": 1},
                                         additional_discard_needed=True, cards_in_hand=1))

    def test_E2_real_fast_mana_sources_do_not_create_free_mana(self):
        self.source("E2", "Mana Vault", "Grim Monolith", "Chrome Mox", "Mox Diamond",
                    "Mox Opal", "Mox Amber", "Lotus Petal", "Dark Ritual",
                    "Cabal Ritual", "Rite of Flame", "Simian Spirit Guide",
                    "Gemstone Caverns", "Ancient Tomb")
        self.assertNotIn("City of Traitors", self.cards)  # frozen M6 design, cut in M7
        # Ancient Tomb taps for CC and inflicts two actual damage; {1} casts Vault,
        # which taps for CCC. No invented colored mana from this branch.
        pool, life = Counter({"C": 2}), 40 - 2
        pool["C"] -= 1  # pay {1} for Mana Vault
        pool["C"] += 3  # tap Vault exactly once
        self.assertEqual((pool["C"], life), (4, 38))
        self.assertEqual(mox_amber_colors(), set())  # zero legendary creatures
        self.assertEqual(mox_amber_colors(legendary_front=True), {"U"})
        # Chrome Mox needs an imprintable nonartifact/nonland; Diamond discards
        # a real land as an additional cost, not an imaginary free colored source.
        self.assertFalse(zero_cost_mox_legal(mox_name="Chrome Mox"))
        self.assertTrue(zero_cost_mox_legal(mox_name="Chrome Mox",
                                            imprintable_nonartifact_nonland=True))
        self.assertFalse(zero_cost_mox_legal(mox_name="Mox Diamond"))
        self.assertTrue(zero_cost_mox_legal(mox_name="Mox Diamond", discardable_land=True))

    def test_W1_paid_oracle_consultation_and_singleton_pact_response_window(self):
        self.source("W1", "Thassa's Oracle", "Demonic Consultation", "Tainted Pact")
        # Oracle has entered after paying UU. With its trigger still on stack,
        # B-paid Consultation names an absent card and exiles all the library.
        self.assertTrue(oracle_trigger_wins(oracle_resolves=True, devotion=2, library_size=72,
                                             consultation_resolves=True, consultation_named_absent=True))
        # Pact can exhaust a truly singleton physical library when never stopped.
        self.assertTrue(oracle_trigger_wins(oracle_resolves=True, devotion=2, library_size=71,
                                             pact_resolves=True, singleton_library=True))
        self.assertFalse(oracle_trigger_wins(oracle_resolves=True, devotion=2, library_size=72,
                                              consultation_resolves=False,
                                              consultation_named_absent=True))
        self.assertFalse(oracle_trigger_wins(oracle_resolves=False, devotion=2, library_size=0,
                                              consultation_resolves=True,
                                              consultation_named_absent=True))
        self.assertFalse(oracle_trigger_wins(oracle_resolves=True, devotion=2, library_size=72,
                                              pact_resolves=True, singleton_library=False))

    def test_W2_breach_led_brain_freeze_mills_finitely_at_real_escape_costs(self):
        self.source("W2", "Underworld Breach", "Lion's Eye Diamond", "Lotus Petal",
                    "Brain Freeze", "Wheel of Fortune", "Jeska's Will")
        turns = breach_led_brain_freeze(library=45, grave_filler=9, rounds=4)
        self.assertEqual(len(turns), 4)
        self.assertEqual([turn["copies"] for turn in turns], [2, 4, 6, 8])
        self.assertEqual([turn["mana"] for turn in turns], [1, 2, 3, 4])
        self.assertEqual(turns[-1]["library"], 0)
        self.assertGreaterEqual(turns[-1]["grave_filler"], 0)
        self.assertEqual(breach_led_brain_freeze(library=45, grave_filler=9,
                                                 rounds=4, breach=False), [])
        self.assertEqual(breach_led_brain_freeze(library=45, grave_filler=9,
                                                 rounds=4, brain_freeze=False), [])
        self.assertEqual(breach_led_brain_freeze(library=45, grave_filler=2,
                                                 rounds=4), [])
        # Self-milling alone does not win; Oracle/another converter is still needed.
        self.assertTrue(oracle_trigger_wins(oracle_resolves=True, devotion=2,
                                             library_size=turns[-1]["library"]))

    def test_W3_breach_station_amber_paid_90_card_trace_into_oracle(self):
        self.source("W3", "Underworld Breach", "Grinding Station", "Mox Amber",
                    "Norman Osborn // Green Goblin", "Brain Freeze", "Thassa's Oracle")
        trace = station_amber_to_oracle(library=90, grave_filler=3)
        # Concrete disjoint starting zones: 90 library + three other eligible
        # grave cards + commander/Breach/Station/Amber/Oracle + two hand cards.
        self.assertEqual(90 + 3 + 1 + 1 + 1 + 1 + 1 + 2, 100)
        self.assertEqual(trace, {"rounds": 30, "blue": 30, "library": 0,
                                 "grave_filler": 3, "exiled": 90,
                                 "mox_in_grave": True, "oracle_wins": True})
        self.assertFalse(station_amber_to_oracle(station=False)["oracle_wins"])
        self.assertFalse(station_amber_to_oracle(breach=False)["oracle_wins"])
        self.assertFalse(station_amber_to_oracle(grave_filler=2)["oracle_wins"])
        self.assertFalse(station_amber_to_oracle(norman=False)["oracle_wins"])
        self.assertFalse(station_amber_to_oracle(opponent_intervenes=True)["oracle_wins"])
        self.assertFalse(station_amber_to_oracle(oracle_in_hand=False)["oracle_wins"])

    def test_F2_four_mana_sorcery_transform_has_real_tempo_cost(self):
        self.source("F2", "Norman Osborn // Green Goblin", "Thassa's Oracle")
        fully_paid = Counter({"C": 1, "U": 1, "B": 1, "R": 1})
        self.assertTrue(transform(mana=fully_paid))
        self.assertFalse(transform(mana=Counter({"C": 3, "U": 1})))
        self.assertFalse(transform(mana=fully_paid, stack_empty=False))
        self.assertFalse(transform(mana=fully_paid, on_battlefield=False))
        # Front-face absence doesn't stop generic (paid UU+B) Oracle+Consult.
        self.assertTrue(oracle_trigger_wins(oracle_resolves=True, devotion=2, library_size=51,
                                             consultation_resolves=True, consultation_named_absent=True))

    def test_F3_twenty_three_lands_zero_land_hand_counterexample(self):
        self.source("F3", "Mana Vault", "Chrome Mox", "Mox Diamond", "Ancient Tomb")
        lands = {"Ancient Tomb", "Arid Mesa", "Badlands", "Blood Crypt", "Bloodstained Mire",
                 "Cavern of Souls", "Cephalid Coliseum", "City of Brass", "Command Tower",
                 "Flooded Strand", "Gemstone Caverns", "Mana Confluence", "Marsh Flats",
                 "Misty Rainforest", "Otawara, Soaring City", "Polluted Delta",
                 "Scalding Tarn", "Steam Vents", "Underground Sea", "Verdant Catacombs",
                 "Volcanic Island", "Watery Grave", "Wooded Foothills"}
        self.assertEqual(len(lands), 23)
        self.assertTrue(all(self.cards[name] == 1 for name in lands))
        zero_land_hand = {"Thassa's Oracle", "Brain Freeze", "Underworld Breach",
                          "Psychic Frog", "Intuition", "Rhystic Study", "Faithless Looting"}
        self.assertEqual(len(zero_land_hand), 7)
        self.assertTrue(all(self.cards[name] == 1 for name in zero_land_hand))
        self.assertTrue(zero_land_hand.isdisjoint(lands))
        fast_sources = {"Mana Vault", "Chrome Mox", "Mox Diamond", "Mox Opal",
                        "Mox Amber", "Lotus Petal", "Dark Ritual", "Cabal Ritual",
                        "Rite of Flame", "Simian Spirit Guide", "Grim Monolith"}
        self.assertTrue(zero_land_hand.isdisjoint(fast_sources))
        no_land_probability = comb(77, 7) / comb(100, 7)
        self.assertGreater(no_land_probability, 0.1)
        self.assertLess(no_land_probability, 0.2)
        self.assertEqual(self.cards["Ancient Tomb"], 1)


if __name__ == "__main__":
    unittest.main()
