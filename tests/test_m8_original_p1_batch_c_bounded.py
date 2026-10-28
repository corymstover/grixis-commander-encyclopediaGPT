"""Exact-source P1 batch C: 17 finite interaction and adverse boundary witnesses.

No W-case loop, multiplayer win rate, opponent strategy, or absence-of-combos
proof is inferred. Source SHA, original DEFERRED status and required card are
checked for every witness.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "Nicol_Bolas": "a6079935a50b9469ca487e58e6bac159f8b777348b31585256b967f92c5d0df6",
    "Nicol_Bolas__the_Ravager": "acfa7922e262805a15932b53b1399acdf6ddf5592c8a3793fafdeec720ad4693",
    "Thraximundar": "f3e71b71fc10fbe6d8a1afde29b5291e9e32d4e83db44c2dcb7aab0773f18da2",
}


def upkeep_keeps_bolas(paid_blue, paid_black, paid_red):
    return all((paid_blue, paid_black, paid_red))


def ignition_result(power, other_own_creature_toughness, opponent_creatures_toughness):
    return (power >= other_own_creature_toughness,
            sum(power >= toughness for toughness in opponent_creatures_toughness),
            power)  # opponent takes that much noncombat damage from Bolas source


def bolas_discard_on_damage(damage_dealt, creature_is_bolas_source, opponent_hand):
    return opponent_hand if damage_dealt > 0 and creature_is_bolas_source else 0


def bolas_enter_or_connect(commander_present, opponent_was_damaged, upkeep_paid):
    return bool(commander_present and opponent_was_damaged and upkeep_paid)


def discard_payoffs(cards_discarded_by_opponent, effects_present):
    return cards_discarded_by_opponent * effects_present


def repeat_upkeep_tax(initial_ubr_paid, later_ubr_paid):
    return int(initial_ubr_paid) + int(initial_ubr_paid and later_ubr_paid)


def kitten_flickers_planeswalker(noncreature_cast, nonland_target_controlled):
    return bool(noncreature_cast and nonland_target_controlled)


def bolas_spell_clauses(bolas_walker_on_battlefield, bolas_walker_spell_cast):
    """Deliver condition checks control; Dark Intimations bonus needs casting a walker."""
    return bool(bolas_walker_on_battlefield), bool(bolas_walker_spell_cast)


def spark_double_copies_bolas(copy_target_is_walker, target_valid, source_loyalty):
    return (source_loyalty + 1, True) if copy_target_is_walker and target_valid else None


def ravager_transform(total_generic, blue, black, red, sorcery_speed, training_grounds):
    generic_needed = 2 if training_grounds else 4
    return bool(sorcery_speed and total_generic >= generic_needed and blue and black and red)


def walker_ability_resolutions(base_activation, veil_grants_second_use, rings_copy_paid):
    """Rings copies a loyalty ability, but never grants another activation."""
    return base_activation + int(veil_grants_second_use) + int(rings_copy_paid)


def walker_survives_combat(current_loyalty, damage):
    return current_loyalty > damage


def veil_extra_activation(veil_live, enough_mana):
    return bool(veil_live and enough_mana)


def gravecrawler_can_cast(another_zombie_controlled, black_available, in_graveyard):
    return bool(another_zombie_controlled and black_available and in_graveyard)


def thrax_growth(creatures_sacrificed_while_present, commander_present):
    return creatures_sacrificed_while_present if commander_present else 0


def pact_sacrifice_count(own_creatures_sacrificed, opponents_with_creatures, pact_effects):
    """Each Pact orders opponents to sacrifice; no player can sac more creatures than available."""
    forced = sum(min(creatures, own_creatures_sacrificed * pact_effects)
                 for creatures in opponents_with_creatures)
    return own_creatures_sacrificed + forced


def exiled_gravecrawler_returnable(in_graveyard, another_zombie):
    return bool(in_graveyard and another_zombie)


# Required source cards; favorable/adverse witness; exact result; explicit scope.
CASES = {
    "Nicol_Bolas": {
        "K4": (("Nicol Bolas",), lambda: upkeep_keeps_bolas(True, True, True), True,
               lambda: upkeep_keeps_bolas(True, False, True), False,
               "Every upkeep requires actual UBR payment, else Nicol Bolas is sacrificed."),
        "K5": (("Chandra's Ignition", "Ingris Stingerquill", "Kediss, Emberclaw Familiar"),
               lambda: ignition_result(7, 4, [3, 8]), (True, 1, 7),
               lambda: ignition_result(7, 8, [8]), (False, 0, 7),
               "Ignition damages other friendly creatures too; no automatic immunity to the self-sweep."),
        "K6": (("Nicol Bolas", "Chandra's Ignition", "Curiosity"),
               lambda: bolas_discard_on_damage(7, True, 5), 5,
               lambda: bolas_discard_on_damage(7, False, 5), 0,
               "Bolas must be the damage source to cause opponent hand discard; noncombat damage can work."),
        "E1": (("Nicol Bolas", "Dragon Tempest"),
               lambda: bolas_enter_or_connect(True, True, True), True,
               lambda: bolas_enter_or_connect(True, False, True), False,
               "A real player-damage event plus paid upkeep matters; mere on-board Bolas does not discard."),
        "E2": (("Waste Not", "Geth's Grimoire"),
               lambda: discard_payoffs(4, 2), 8,
               lambda: discard_payoffs(0, 2), 0,
               "Discard-trigger payoffs require actual opponent card discards; unrelated shuffling is not one."),
        "F2": (("Nicol Bolas",), lambda: repeat_upkeep_tax(True, True), 2,
               lambda: repeat_upkeep_tax(True, False), 1,
               "Keeping eight-mana Nicol Bolas across multiple upkeeps requires separate recurring UBR taxes."),
    },
    "Nicol_Bolas__the_Ravager": {
        "K4": (("Displacer Kitten", "Nicol Bolas, the Ravager // Nicol Bolas, the Arisen"),
               lambda: kitten_flickers_planeswalker(True, True), True,
               lambda: kitten_flickers_planeswalker(False, True), False,
               "Kitten needs actual noncreature cast and eligible controlled nonland target; flickered DFC returns front."),
        "K5": (("Deliver Unto Evil", "Dark Intimations"),
               lambda: bolas_spell_clauses(True, False), (True, False),
               lambda: bolas_spell_clauses(False, False), (False, False),
               "Deliver checks Bolas planeswalker on field; transforming Ravager is not casting a Bolas walker spell."),
        "K6": (("Spark Double", "Nicol Bolas, Dragon-God"),
               lambda: spark_double_copies_bolas(True, True, 4), (5, True),
               lambda: spark_double_copies_bolas(True, False, 4), None,
               "Spark Double may copy a live planeswalker with extra loyalty and no legendary supertype."),
        "E1": (("Nicol Bolas, the Ravager // Nicol Bolas, the Arisen", "Training Grounds"),
               lambda: ravager_transform(2, True, True, True, True, True), True,
               lambda: ravager_transform(2, True, True, True, False, True), False,
               "Ravager transforms only at sorcery speed for payable 4UBR or reduced 2UBR with Grounds."),
        "E2": (("The Chain Veil", "Rings of Brighthearth"),
               lambda: walker_ability_resolutions(1, True, True), 3,
               lambda: walker_ability_resolutions(1, False, False), 1,
               "A paid Chain Veil grants extra loyalty use; paid Rings copies ability but not its activation."),
        "F2": (("Nicol Bolas, Dragon-God",),
               lambda: walker_survives_combat(5, 4), True,
               lambda: walker_survives_combat(5, 5), False,
               "Five-loyalty planeswalker survives four combat damage but dies to five unprevented damage."),
        "F3": (("The Chain Veil",), lambda: veil_extra_activation(True, True), True,
               lambda: veil_extra_activation(False, True), False,
               "Artifact hate that removes Chain Veil stops future activations from that specific artifact."),
    },
    "Thraximundar": {
        "K4": (("Gravecrawler", "Thraximundar"),
               lambda: gravecrawler_can_cast(True, True, True), True,
               lambda: gravecrawler_can_cast(False, True, True), False,
               "Casting Gravecrawler from grave needs another Zombie and actual B payment."),
        "E1": (("Thraximundar", "Fleshbag Marauder"),
               lambda: thrax_growth(3, True), 3,
               lambda: thrax_growth(3, False), 0,
               "Every actually sacrificed creature on either side grows present Thraximundar by one counter."),
        "E2": (("Grave Pact", "Dictate of Erebos", "Mayhem Devil"),
               lambda: pact_sacrifice_count(1, [2, 2], 2), 5,
               lambda: pact_sacrifice_count(1, [0, 0], 2), 1,
               "Our own creature sacrifice with two Pact effects makes other players sacrifice only what exists."),
        "F3": (("Gravecrawler",),
               lambda: exiled_gravecrawler_returnable(True, True), True,
               lambda: exiled_gravecrawler_returnable(False, True), False,
               "If graveyard hate exiles Gravecrawler, controlling a Zombie cannot cast it from grave."),
    },
}


class OriginalP1BatchCTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        by_id = {d["deck_id"]: d for d in index["decks"]}
        cls.cards = {}
        for deck, digest in SOURCES.items():
            row = by_id[deck]
            raw = (ROOT / row["source_file"]).read_bytes()
            assert sha256(raw).hexdigest() == row["source_sha256"] == digest
            names = Counter()
            for line in raw.decode().splitlines():
                count, name = line.split("x ", 1)
                names[name.replace(" [Commander]", "")] += int(count)
            assert sum(names.values()) == 100
            cls.cards[deck] = names

    def test_all_seventeen_cases_originally_deferred_on_exact_approved_sha(self):
        total = 0
        for deck, cases in CASES.items():
            sha = SOURCES[deck]
            receipt = json.loads((ROOT / "refinement/verification/m7_certification_transfer"
                                  / f"{deck}_{sha[:16]}.json").read_text())
            self.assertEqual(receipt["approved_raw_sha256"], sha)
            current = {r["case_id"]: r["status"] for r in receipt["m6_transfer"]["P1"]}
            for case in cases:
                self.assertEqual(current[case], "DEFERRED", (deck, case))
            total += len(cases)
        self.assertEqual(total, 17)

    def test_removed_prior_premises_are_not_current_source_cards(self):
        self.assertNotIn("No Mercy", self.cards["Nicol_Bolas"])
        self.assertNotIn("Force of Will", self.cards["Thraximundar"])
        self.assertIn("Mana Vault", self.cards["Thraximundar"])


def _register(deck, case, names, good, good_expected, bad, bad_expected, scope):
    def test(self):
        for name in names:
            self.assertIn(name, self.cards[deck])
        self.assertNotEqual(good_expected, bad_expected)
        self.assertEqual(good(), good_expected)
        self.assertEqual(bad(), bad_expected)
        self.assertGreater(len(scope), 45)
    aliases = {"Nicol_Bolas": "bolas", "Nicol_Bolas__the_Ravager": "ravager", "Thraximundar": "thraxi"}
    key = f"test_{aliases[deck]}_{case}"
    test.__name__ = key
    setattr(OriginalP1BatchCTests, key, test)


for _deck, _cases in CASES.items():
    for _case, _info in _cases.items():
        _register(_deck, _case, *_info)


if __name__ == "__main__":
    unittest.main()
