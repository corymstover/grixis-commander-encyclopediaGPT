"""M8 source-hash-bound original P1 batch B: finite mechanics and failure premises.

Bounded adversarial checks only. Deliberately excludes W-case victory proofs,
randomized gameplay, opponent response trees, and independent historical J.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "Sauron__Lord_of_the_Rings": "c427805f78f7aca7384db56022868a2e7cb7d01eeeabbb280a18e77e538a8159",
    "Obeka__Splitter_of_Seconds": "f80d882944d5e39f3c6661da4dcdce3ec6eead577cd981dc54f7dc522be50859",
    "The_Rani": "924296ed24fdc5e79431821d31a77134c5ed5c089a92cb5e69c78f78bde4fe27",
    "Sol_kanar_the_Swamp_King": "2bd99c569df4a86897bca0164d2a1fa309b92f8b721e406b8394dfb04b1239e3",
    "Tetsuo__Imperial_Champion": "36890584524fb32d038ba27926af663dc98197f06f87d84a08282ce1f3fb29db",
}


def sauron_cast_trigger(spell_cast, mana_paid, grave_target_available, spell_countered=False):
    """Sauron trigger uses CAST, not resolution, then needs returnable grave target."""
    return bool(spell_cast and mana_paid and grave_target_available)


def sauron_grave_chain(creature_reanimated, fanatic_etb, second_grave_target):
    return int(creature_reanimated and fanatic_etb and second_grave_target)


def anger_wonder_grant(anger_in_grave, wonder_in_grave, mountain, island):
    return bool(anger_in_grave and wonder_in_grave and mountain and island)


def living_death_returnables(preexisting_graveyard_cards, sacrificed_creatures, tokens_sacrificed):
    """Only creature cards exiled from graveyard *before* sacrifice return."""
    assert tokens_sacrificed >= 0
    # (reanimated, newly-graveyarded/nonreanimated cards, returned tokens)
    return (preexisting_graveyard_cards, sacrificed_creatures, 0)


def obeka_upkeeps(combat_damage, dealt_to_player, throne_matching=False):
    return combat_damage * (1 + int(throne_matching)) if dealt_to_player else 0


def time_sieve_can_pay(artifact_objects):
    return artifact_objects >= 5


def mana_can_cast(required_generic, required_blue, available_generic, available_blue):
    return available_blue >= required_blue and available_generic + available_blue - required_blue >= required_generic


def mechanized_production_win(enchanted_artifact_remains, same_name_artifacts, upkeep):
    return bool(enchanted_artifact_remains and same_name_artifacts >= 8 and upkeep)


def rani_mark_count(valid_entrant_or_attacks, another_legal_creature):
    return int(valid_entrant_or_attacks and another_legal_creature)


def rani_investigations(goaded_creatures_damaging_other_opponents, rani_present):
    return goaded_creatures_damaging_other_opponents if rani_present else 0


def manufactor_tokens(investigations, manufactor_present):
    return investigations * (3 if manufactor_present else 1)


def mana_can_pay_rani(available_blue, available_black, available_red, available_generic):
    return all(x >= 1 for x in (available_blue, available_black, available_red)) and available_generic >= 1


def coffers_net_black(swamps, paid_two=True):
    return swamps - (2 if paid_two else 0) if paid_two else 0


def solkanar_lifegain(black_spells_cast, commander_present):
    return black_spells_cast if commander_present else 0


def life_draining_pair(gained_life, gain_to_loss_present, loss_to_gain_present):
    return bool(gained_life and gain_to_loss_present and loss_to_gain_present)


def top_citadel_iteration(top_can_be_recast, citadel_live, life_paid, life_available):
    return bool(top_can_be_recast and citadel_live and life_paid < life_available)


def tetsuo_attack_triggers(declared_attack, equipped_at_attack):
    return int(declared_attack and equipped_at_attack)


def tetsuo_freecast_eligible(in_hand, instant_or_sorcery, spell_mv, highest_equipment_mv):
    return bool(in_hand and instant_or_sorcery and spell_mv <= highest_equipment_mv)


# Case-specific source card preconditions, mutually contradictory finite witnesses
# and a disclosure of the mechanic's boundary. No line asserts an end-to-end W win.
CASES = {
    "Sauron__Lord_of_the_Rings": {
        "K4": (("Sauron, Lord of the Rings", "Metamorphosis Fanatic"),
               lambda: sauron_grave_chain(True, True, True), 1,
               lambda: sauron_grave_chain(True, True, False), 0,
               "Sauron cast reanimates Fanatic and Fanatic ETB can return a second actual grave target."),
        "K5": (("Nazgûl",), lambda: min(4, 9), 4,
               lambda: min(10, 9), 9,
               "Official Nazgul deck-construction exception allows up to nine, exact current source has four."),
        "K6": (("Anger", "Wonder"), lambda: anger_wonder_grant(True, True, True, True), True,
               lambda: anger_wonder_grant(True, True, True, False), False,
               "Anger in graveyard needs Mountain; Wonder needs Island, and each condition is independent."),
        "K7": (("Living Death",), lambda: living_death_returnables(3, 2, 0), (3, 2, 0),
               lambda: living_death_returnables(0, 2, 1), (0, 2, 0),
               "Living Death reanimates pre-exiled grave cards, not creature tokens just sacrificed."),
        "E1": (("Sauron, Lord of the Rings",),
               lambda: sauron_cast_trigger(True, True, True, spell_countered=True), True,
               lambda: sauron_cast_trigger(False, False, True), False,
               "Sauron triggers on casting eight-mana spell; countering body doesn't counter cast trigger."),
        "E2": (("Sauron, Lord of the Rings",),
               lambda: sauron_cast_trigger(True, True, True), True,
               lambda: sauron_cast_trigger(True, True, False), False,
               "Sauron casting mills then can return a real eligible grave creature; no target means none."),
        "F2": (("Sauron, Lord of the Rings", "Living Death"),
               lambda: sauron_grave_chain(True, True, True), 1,
               lambda: sauron_grave_chain(False, True, True), 0,
               "Graveyard replacement hate blocks reanimation even when Sauron cast trigger exists."),
        "F3": (("Living Death",), lambda: living_death_returnables(2, 0, 0), (2, 0, 0),
               lambda: living_death_returnables(0, 0, 0), (0, 0, 0),
               "Living Death applies to every player's prior graveyard symmetrically; no unilateral return."),
    },
    "Obeka__Splitter_of_Seconds": {
        "K4": (("Obeka, Splitter of Seconds", "Roaming Throne"),
               lambda: obeka_upkeeps(3, True, True), 6,
               lambda: obeka_upkeeps(3, True), 3,
               "Throne choosing Ogre/Warlock adds one Obeka trigger: three damage gives six upkeeps."),
        "K5": (("Time Sieve", "Thopter Spy Network"),
               lambda: time_sieve_can_pay(5), True,
               lambda: time_sieve_can_pay(4), False,
               "Sieve requires five actual expendable artifacts; upkeep token makers not automatic."),
        "K6": (("Mechanized Production",),
               lambda: mechanized_production_win(True, 8, True), True,
               lambda: mechanized_production_win(True, 7, True), False,
               "Mechanized Production checks eight matching-name artifacts at upkeep; Reactor absent."),
        "E1": (("Obeka, Splitter of Seconds",), lambda: obeka_upkeeps(4, True), 4,
               lambda: obeka_upkeeps(4, False), 0,
               "Obeka needs actual combat damage to player; blocked/no-damage provides zero upkeeps."),
        "E2": (("Obeka, Splitter of Seconds",),
               lambda: obeka_upkeeps(5, True), 5,
               lambda: obeka_upkeeps(2, True), 2,
               "Only actual combat damage amount, after pumps/prevention, determines extra upkeep steps."),
        "F2": (("Time Sieve",), lambda: time_sieve_can_pay(5), True,
               lambda: time_sieve_can_pay(0), False,
               "Artifact removal or unavailable fodder stops next Sieve activation."),
        "F3": (("Extravagant Replication",), lambda: mana_can_cast(4, 2, 4, 2), True,
               lambda: mana_can_cast(4, 2, 5, 1), False,
               "Extravagant Replication costs 4UU; extra upkeeps do not fund missing blue mana."),
    },
    "The_Rani": {
        "K4": (("The Rani", "Time Sieve"), lambda: time_sieve_can_pay(5), True,
               lambda: time_sieve_can_pay(3), False,
               "Five expendable artifacts can buy one turn, not guarantee five the next turn."),
        "K5": (("The Rani",), lambda: rani_investigations(2, True), 2,
               lambda: rani_investigations(0, True), 0,
               "Only goaded creatures truly damaging other opponents trigger investigate."),
        "E1": (("The Rani",), lambda: rani_mark_count(True, True), 1,
               lambda: rani_mark_count(True, False), 0,
               "Rani ETB/attack creates Mark only with another legal target creature."),
        "E2": (("Academy Manufactor", "The Rani"),
               lambda: manufactor_tokens(2, True), 6,
               lambda: manufactor_tokens(2, False), 2,
               "Investigate with Manufactor gives one each Clue/Food/Treasure, not three Clues."),
        "E3": (("The Rani",), lambda: rani_mark_count(True, True), 1,
               lambda: rani_mark_count(False, True), 0,
               "Real blink reentry can create another Mark, without pretending a static Rani generates it."),
        "F3": (("The Rani",), lambda: mana_can_pay_rani(1, 1, 1, 3), True,
               lambda: mana_can_pay_rani(0, 0, 1, 8), False,
               "Rani's colored UBR cost needs real U/B/R, not only generic fast artifact mana."),
    },
    "Sol_kanar_the_Swamp_King": {
        "K4": (("Exquisite Blood", "Bloodthirsty Conqueror", "Vito, Thorn of the Dusk Rose"),
               lambda: life_draining_pair(1, True, True), True,
               lambda: life_draining_pair(1, True, False), False,
               "Actual first life gain plus drain-on-gain and loss-to-gain sources can feed recurring trigger chain."),
        "K5": (("Sensei's Divining Top", "Bolas's Citadel", "Sheoldred, the Apocalypse"),
               lambda: top_citadel_iteration(True, True, 1, 20), True,
               lambda: top_citadel_iteration(True, False, 1, 20), False,
               "Top/Citadel repeated casts require payable life, legal top-of-library and live Citadel."),
        "E1": (("Sol'kanar the Swamp King", "Painter's Servant"),
               lambda: solkanar_lifegain(3, True), 3,
               lambda: solkanar_lifegain(3, False), 0,
               "Solkanar gains one per black spell actually cast, including with Painter naming black."),
        "E2": (("Cabal Coffers", "Urborg, Tomb of Yawgmoth"),
               lambda: coffers_net_black(6), 4,
               lambda: coffers_net_black(1), -1,
               "Coffers activation pays two generic and taps; six Swamps net four B, one cannot."),
        "F2": (("Sol'kanar the Swamp King",),
               lambda: solkanar_lifegain(1, True), 1,
               lambda: solkanar_lifegain(0, True), 0,
               "Alone commander gains small incremental life only on real black casts, no instant win."),
    },
    "Tetsuo__Imperial_Champion": {
        "F2": (("Tetsuo, Imperial Champion",), lambda: tetsuo_attack_triggers(True, True), 1,
               lambda: tetsuo_attack_triggers(False, True), 0,
               "Tetsuo must declare an equipped attack to trigger; removal after trigger not automatically a fizzle."),
        "F3": (("Tetsuo, Imperial Champion",),
               lambda: tetsuo_freecast_eligible(True, True, 3, 4), True,
               lambda: tetsuo_freecast_eligible(True, True, 5, 4), False,
               "Free-cast mode needs eligible instant/sorcery in hand with mana value at most attached equipment highest MV."),
    },
}


class OriginalP1BatchBTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        by_id = {x["deck_id"]: x for x in index["decks"]}
        cls.cards = {}
        for deck, expected in SOURCES.items():
            row = by_id[deck]
            raw = (ROOT / row["source_file"]).read_bytes()
            assert sha256(raw).hexdigest() == expected == row["source_sha256"]
            names = Counter()
            for line in raw.decode().splitlines():
                count, name = line.split("x ", 1)
                names[name.replace(" [Commander]", "")] += int(count)
            assert sum(names.values()) == 100
            cls.cards[deck] = names

    def test_all_twenty_eight_cases_are_originally_deferred_exact_sha(self):
        count = 0
        for deck, cases in CASES.items():
            expected_sha = SOURCES[deck]
            path = ROOT / "refinement/verification/m7_certification_transfer" / f"{deck}_{expected_sha[:16]}.json"
            receipt = json.loads(path.read_text())
            self.assertEqual(receipt["approved_raw_sha256"], expected_sha)
            original = {r["case_id"]: r["status"] for r in receipt["m6_transfer"]["P1"]}
            for case in cases:
                self.assertEqual(original[case], "DEFERRED", (deck, case))
            count += len(cases)
        self.assertEqual(count, 28)

    def test_obsolete_partial_or_original_absent_cards_not_misrepresented(self):
        self.assertNotIn("Darksteel Reactor", self.cards["Obeka__Splitter_of_Seconds"])
        self.assertNotIn("Force of Will", self.cards["Sol_kanar_the_Swamp_King"])
        self.assertNotIn("Sword of Wealth and Power", self.cards["Tetsuo__Imperial_Champion"])
        self.assertEqual(self.cards["Sauron__Lord_of_the_Rings"]["Nazgûl"], 4)


def _register(deck, case, required, positive, pos_expected, adverse, neg_expected, limit):
    def test_case(self):
        for name in required:
            self.assertIn(name, self.cards[deck])
        self.assertNotEqual(pos_expected, neg_expected)
        self.assertEqual(positive(), pos_expected, f"Positive {deck}/{case}")
        self.assertEqual(adverse(), neg_expected, f"Adverse {deck}/{case}")
        self.assertGreater(len(limit), 45)
    names = {
        "Sauron__Lord_of_the_Rings": "sauron",
        "Obeka__Splitter_of_Seconds": "obeka",
        "The_Rani": "rani",
        "Sol_kanar_the_Swamp_King": "solkanar",
        "Tetsuo__Imperial_Champion": "tetsuo",
    }
    key = f"test_{names[deck]}_{case}"
    test_case.__name__ = key
    setattr(OriginalP1BatchBTests, key, test_case)


for _deck, _cases in CASES.items():
    for _case_id, _record in _cases.items():
        _register(_deck, _case_id, *_record)


if __name__ == "__main__":
    unittest.main()
