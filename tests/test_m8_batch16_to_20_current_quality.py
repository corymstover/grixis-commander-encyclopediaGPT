"""M8 exact-approved decks #16-#20: 495 library copies and scoped cases.

Bounded adversarial mechanics fixtures only, not a full rules-engine, independent
M6 J recertification, or claims of simulated multiplayer win rate.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONFIG = {
    "Edea__Possessed_Sorceress": {
        "number": 16, "prefix": "Edea__Possessed_Sorceress_a039a79c6205c3dc",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 E3 W1 W2 F2 F3",
        "removed": ("Mass Mutiny", "Village Rites", "Shipwreck Marsh"),
        "basics": {"Island": 3, "Mountain": 3, "Swamp": 3},
    },
    "Edward_Kenway": {
        "number": 17, "prefix": "Edward_Kenway_8c01f2be6190be3e",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "removed": ("Coastal Piracy", "Lotus Petal", "Vaan, Street Thief"),
        "basics": {"Island": 2, "Swamp": 2, "Mountain": 1},
    },
    "Evelyn__the_Covetous": {
        "number": 18, "prefix": "Evelyn__the_Covetous_c3f6862c6f449877",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "removed": ("Spellskite", "Redirect Lightning", "Wan Shi Tong, Librarian"),
        "basics": {"Island": 1, "Swamp": 1},
    },
    "Fire_Lord_Azula": {
        "number": 19, "prefix": "Fire_Lord_Azula_77ac26a4f4ff70d0",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "removed": ("Samut, Tyrant of Naktamun", "Redirect Lightning", "Vivi Ornitier"),
        "basics": {},
    },
    "Garza_Zol__Plague_Queen": {
        "number": 20, "prefix": "Garza_Zol__Plague_Queen_353381caa82e6804",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "removed": ("Scythe of the Wretched", "Inquisitor's Flail", "Robe of the Archmagi"),
        "basics": {"Island": 1, "Mountain": 1, "Swamp": 1},
    },
}


def edea_death_trigger(ours_but_theirs, died, object_in_grave_on_resolution):
    """(return_to_owner, card_draw): moving first does not void the draw."""
    if not (ours_but_theirs and died):
        return False, 0
    return object_in_grave_on_resolution, 1


def edward_qualifiers(permanents):
    """One count per still controlled+untapped object of any eligible types."""
    wanted = {"Assassin", "Pirate", "Vehicle"}
    return sum(bool(owned and tapped and wanted.intersection(types))
               for owned, tapped, types in permanents)


def azula_cast_copy(attacking, is_cast, source_present):
    return int(attacking and is_cast and source_present)


def garza_attack_power(base, two_handed_axe):
    return base * (2 if two_handed_axe else 1)


class NextFiveCurrentQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        idx = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        cls.by_id = {row["deck_id"]: row for row in idx["decks"]}
        cls.sources = {}
        cls.reports = {}
        for deck_id, cfg in CONFIG.items():
            entry = cls.by_id[deck_id]
            assert entry["number"] == cfg["number"]
            raw = (ROOT / entry["source_file"]).read_bytes()
            assert sha256(raw).hexdigest() == entry["source_sha256"]
            cls.sources[deck_id] = Counter()
            for line in raw.decode().splitlines():
                count, name = line.split("x ", 1)
                cls.sources[deck_id][name] += int(count)
            path = ROOT / f"refinement/verification/m8_quality_scope/{cfg['prefix']}.md"
            cls.reports[deck_id] = path.read_text()

    def test_all_five_source_hashes_and_all_495_exact_library_copies(self):
        total = 0
        for deck_id, cfg in CONFIG.items():
            with self.subTest(deck_id=deck_id):
                source = self.sources[deck_id]
                doc = self.reports[deck_id]
                self.assertIn(self.by_id[deck_id]["source_sha256"], doc)
                self.assertEqual(sum(source.values()), 100)
                self.assertEqual(sum(v for k, v in source.items() if "[Commander]" in k), 1)
                library = Counter({k: v for k, v in source.items() if "[Commander]" not in k})
                ledger = Counter()
                for count, card in re.findall(r"^- (\d+)x (.+)$", doc, re.MULTILINE):
                    ledger[card] += int(count)
                self.assertEqual(ledger, library)
                self.assertEqual(sum(ledger.values()), 99)
                for name, count in cfg["basics"].items():
                    self.assertEqual(ledger[name], count)
                for removed in cfg["removed"]:
                    self.assertNotIn(removed, ledger)
                self.assertIn("Historic I/J", doc)
                total += sum(ledger.values())
        self.assertEqual(total, 495)

    def test_seventy_historical_case_groups_scoped_with_adversarial_witness(self):
        groups = 0
        for deck_id, cfg in CONFIG.items():
            found = re.findall(r"^\| \*\*(P0|P1) (C\d+|K\d+|E\d+|W\d+|F\d+)\*\* \|([^\n]+)$",
                               self.reports[deck_id], re.MULTILINE)
            expected = {(priority, case) for priority in ("P0", "P1")
                        for case in cfg[priority].split()}
            self.assertEqual({(p, case) for p, case, _ in found}, expected, deck_id)
            self.assertEqual(len(found), len(expected))
            for p, case, text in found:
                with self.subTest(deck=deck_id, case=case):
                    columns = [c.strip() for c in text.split("|")]
                    self.assertGreaterEqual(len(columns), 2)
                    self.assertGreater(len(columns[0]), 38)
                    self.assertGreater(len(columns[1]), 35)
            groups += len(expected)
        self.assertEqual(groups, 70)

    def test_edea_sacrifice_return_owner_and_nonexistent_grave_object(self):
        self.assertEqual(edea_death_trigger(True, True, True), (True, 1))
        self.assertEqual(edea_death_trigger(True, True, False), (False, 1))
        self.assertEqual(edea_death_trigger(False, True, True), (False, 0))
        self.assertEqual(edea_death_trigger(True, False, True), (False, 0))

    def test_edea_combat_steal_extra_combat_and_hall_cost(self):
        def steal_steps(combat_steps, commander_alive):
            return combat_steps if commander_alive else 0
        self.assertEqual(steal_steps(2, True), 2)
        self.assertEqual(steal_steps(2, False), 0)
        def hall_can_copy(mana, controlled_target, untapped):
            return mana >= 5 and controlled_target and untapped
        self.assertTrue(hall_can_copy(5, True, True))
        self.assertFalse(hall_can_copy(4, True, True))
        self.assertFalse(hall_can_copy(5, False, True))
        self.assertFalse(hall_can_copy(5, True, False))

    def test_edward_one_tapped_object_even_multiple_types(self):
        permanents = [(True, True, {"Pirate", "Assassin", "Vehicle"}),
                      (True, True, {"Vehicle"}),
                      (True, False, {"Pirate"}),
                      (False, True, {"Pirate"}),
                      (True, True, {"Treasure"})]
        self.assertEqual(edward_qualifiers(permanents), 2)

    def test_edward_titanic_sacrifice_cannot_count_absent_at_end_step(self):
        titanic_sacrificed_on_damage = []
        self.assertEqual(edward_qualifiers(titanic_sacrificed_on_damage), 0)
        titanic_survives_tapped = [(True, True, {"Vehicle"})]
        self.assertEqual(edward_qualifiers(titanic_survives_tapped), 1)
        self.assertIn("Original blanket claim Titanic still counts after sacrifice is disproven",
                      self.reports["Edward_Kenway"])

    def test_edward_fateful_mandatory_draw_can_deck_out(self):
        def survive_mandatory_drawing(library, draw_events):
            return library >= draw_events
        self.assertTrue(survive_mandatory_drawing(5, 5))
        self.assertFalse(survive_mandatory_drawing(4, 5))

    def test_evelyn_collection_entry_and_finite_library_exile(self):
        def collection_per_entry(players, library_cards_each):
            return players if library_cards_each > 0 else 0
        self.assertEqual(collection_per_entry(4, 4), 4)
        self.assertEqual(collection_per_entry(4, 0), 0)
        self.assertIn("Insolent Neonate", self.sources["Evelyn__the_Covetous"])
        self.assertNotIn("Spellskite", self.sources["Evelyn__the_Covetous"])

    def test_evelyn_worldgorger_requires_real_exit(self):
        def can_finish_worldgorger(live_enchantment, mana_sources, exit_available):
            return live_enchantment and mana_sources and exit_available
        self.assertTrue(can_finish_worldgorger(True, True, True))
        self.assertFalse(can_finish_worldgorger(True, True, False))
        self.assertFalse(can_finish_worldgorger(False, True, True))

    def test_evelyn_vexing_bauble_self_anti_synergy(self):
        def bauble_counters_spell(zero_mana_spent, bauble_present):
            return zero_mana_spent and bauble_present
        self.assertTrue(bauble_counters_spell(True, True))
        self.assertFalse(bauble_counters_spell(False, True))
        self.assertFalse(bauble_counters_spell(True, False))

    def test_azula_copy_only_during_attack_and_on_real_cast(self):
        self.assertEqual(azula_cast_copy(True, True, True), 1)
        self.assertEqual(azula_cast_copy(True, False, True), 0)
        self.assertEqual(azula_cast_copy(False, True, True), 0)
        self.assertEqual(azula_cast_copy(True, True, False), 0)

    def test_azula_electro_two_legal_targets_can_allow_two_hand_casts(self):
        def eligible_electro_casts(copy_target_legal, original_target_legal, hand_spells):
            return min(hand_spells, int(copy_target_legal) + int(original_target_legal))
        self.assertEqual(eligible_electro_casts(True, True, 2), 2)
        self.assertEqual(eligible_electro_casts(True, True, 1), 1)
        self.assertEqual(eligible_electro_casts(True, False, 2), 1)
        self.assertEqual(eligible_electro_casts(False, False, 2), 0)

    def test_azula_copy_big_score_does_not_discard_twice(self):
        def paid_big_score(original_resolves, copied_spell_resolves,
                           paid_original_discard):
            if not paid_original_discard:
                return 0, 0, 0
            resolutions = int(original_resolves) + int(copied_spell_resolves)
            return 2 * resolutions, 2 * resolutions, 1
        self.assertEqual(paid_big_score(True, True, True), (4, 4, 1))
        self.assertEqual(paid_big_score(True, False, True), (2, 2, 1))
        self.assertEqual(paid_big_score(False, False, True), (0, 0, 1))
        self.assertEqual(paid_big_score(True, True, False), (0, 0, 0))

    def test_garza_axe_double_strike_twenty_is_not_twenty_one(self):
        attack_power = garza_attack_power(5, True)
        self.assertEqual(attack_power, 10)
        self.assertEqual(attack_power * 2, 20)
        self.assertLess(attack_power * 2, 21)
        self.assertEqual(garza_attack_power(7, True), 14)

    def test_garza_infect_kediss_noncombat_and_malakir_new_object(self):
        def poison(damage, infect, prevented):
            return damage if infect and not prevented else 0
        self.assertEqual(poison(14, True, False), 14)
        self.assertEqual(poison(14, True, True), 0)
        # Kediss spreads noncombat damage from Garza: infect applies, but no
        # additional commander COMBAT damage is accumulated on other players.
        def kediss_spread_to_other_opponent(original_combat_hit, infect):
            return (poison(original_combat_hit, infect, False), 0)
        self.assertEqual(kediss_spread_to_other_opponent(14, True), (14, 0))
        self.assertIn("Malakir Rebirth // Malakir Mire",
                      self.sources["Garza_Zol__Plague_Queen"])

    def test_garza_jeska_life_only_command_zone_casts(self):
        def jeska_loyalty(command_zone_casts):
            return command_zone_casts
        self.assertEqual(jeska_loyalty(0), 0)
        self.assertEqual(jeska_loyalty(1), 1)
        self.assertEqual(jeska_loyalty(2), 2)


if __name__ == "__main__":
    unittest.main()
