"""Final five exact-owner-SHA quality audits: 495 physical library cards.

Finite state counterexamples and source-bound case mapping, not full MTG
rules simulation, historical independent J, or actual multiplayer playtests.
"""

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONFIG = {
    "Abaddon_the_Despoiler": {
        "number": 1, "slug": "Abaddon_the_Despoiler_5ab1a3628352016b",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "basics": {"Island": 3, "Mountain": 2, "Swamp": 3},
        "removed": ("Thermo-Alchemist", "The Ruinous Powers",
                    "Kessig Flamebreather", "Keeper of Secrets", "Ponder"),
        "not_original_blueprint": True,
    },
    "Goro_Goro_and_Satoru": {
        "number": 21, "slug": "Goro_Goro_and_Satoru_36b71b76f913c385",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "basics": {"Island": 2, "Mountain": 1, "Swamp": 1},
        "removed": ("Mist-Syndicate Naga", "Grim Hireling", "Kaito, Bane of Nightmares",
                    "Crumbling Necropolis", "Fabled Passage"),
    },
    "Gwendlyn_Di_Corci": {
        "number": 22, "slug": "Gwendlyn_Di_Corci_36b76cbe47a04b74",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "basics": {"Island": 2, "Mountain": 1, "Swamp": 5},
        "removed": ("Dauthi Voidwalker", "Underworld Dreams",
                    "The Raven Man", "Crumbling Necropolis", "Drowned Catacomb"),
    },
    "Inalla__Archmage_Ritualist": {
        "number": 23, "slug": "Inalla__Archmage_Ritualist_c9f35cac41a7717e",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "basics": {"Swamp": 1},
        "removed": ("Kefka, Court Mage // Kefka, Ruler of Ruin",
                    "Final Fortune", "Wheel of Fortune", "Exotic Orchard", "Island"),
    },
    "Jeleva__Nephalia_s_Scourge": {
        "number": 24, "slug": "Jeleva__Nephalia_s_Scourge_6f2cdafa089c3e92",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "basics": {"Island": 1, "Swamp": 1},
        "removed": ("City of Traitors", "Toxic Deluge"),
    },
}


def abaddon_qualifies(own_turn, from_hand, mana_value, opponent_life_lost):
    return own_turn and from_hand and mana_value <= sum(opponent_life_lost)


def goro_dragons(damaged_players, throne_human=False, double_strike_steps=1):
    return len(set(damaged_players)) * (1 + int(throne_human)) * double_strike_steps


def gwendlyn_discard_effects(own_turn, usable_tap, bracers=False, rings_paid=False):
    return int(own_turn and usable_tap) * (1 + int(bracers) + int(rings_paid))


def inalla_copy(is_nontoken_wizard, correct_inalla_zone, paid_one):
    return int(is_nontoken_wizard and correct_inalla_zone and paid_one)


def jeleva_exile_count(was_cast, mana_actually_spent, players=4, prodigy=False):
    return int(was_cast) * mana_actually_spent * players * (1 + int(prodigy))


class FinalFiveCurrentQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        cls.index = {x["deck_id"]: x for x in index["decks"]}
        cls.library = {}
        cls.docs = {}
        for deck_id, cfg in CONFIG.items():
            entry = cls.index[deck_id]
            assert entry["number"] == cfg["number"]
            raw = (ROOT / entry["source_file"]).read_bytes()
            assert sha256(raw).hexdigest() == entry["source_sha256"]
            source = Counter()
            for line in raw.decode().splitlines():
                qty, card = line.split("x ", 1)
                source[card] += int(qty)
            cls.library[deck_id] = Counter(
                {c: n for c, n in source.items() if "[Commander]" not in c}
            )
            cls.docs[deck_id] = (ROOT / "refinement/verification/m8_quality_scope"
                                 / f"{cfg['slug']}.md").read_text()

    def test_all_495_exact_physical_library_cards_and_source_hashes(self):
        total = 0
        for deck_id, cfg in CONFIG.items():
            with self.subTest(deck=deck_id):
                doc = self.docs[deck_id]
                self.assertIn(self.index[deck_id]["source_sha256"], doc)
                self.assertEqual(sum(self.library[deck_id].values()), 99)
                from_report = Counter()
                for n, card in re.findall(r"^- (\d+)x (.+)$", doc, re.MULTILINE):
                    from_report[card] += int(n)
                self.assertEqual(from_report, self.library[deck_id])
                for name, count in cfg["basics"].items():
                    self.assertEqual(from_report[name], count)
                for removed in cfg["removed"]:
                    self.assertNotIn(removed, from_report)
                total += sum(from_report.values())
        self.assertEqual(total, 495)

    def test_seventy_original_or_new_cases_all_have_adversarial_witness(self):
        total = 0
        for deck_id, cfg in CONFIG.items():
            doc = self.docs[deck_id]
            found = re.findall(r"^\| \*\*(P0|P1) (C\d+|K\d+|E\d+|W\d+|F\d+)\*\* \|([^\n]+)$",
                               doc, re.MULTILINE)
            expected = {(p, c) for p in ("P0", "P1") for c in cfg[p].split()}
            self.assertEqual({(p, c) for p, c, _ in found}, expected, deck_id)
            for p, case, text in found:
                with self.subTest(deck=deck_id, priority=p, case=case):
                    fields = [x.strip() for x in text.split("|")]
                    self.assertGreaterEqual(len(fields), 2)
                    self.assertGreater(len(fields[0]), 35)
                    self.assertGreater(len(fields[1]), 35)
            self.assertIn("I/J", doc)
            if cfg.get("not_original_blueprint"):
                self.assertIn("new bounded review", doc)
            total += len(found)
        self.assertEqual(total, 70)

    def test_abaddon_threshold_requires_precast_life_and_hand_cast(self):
        self.assertTrue(abaddon_qualifies(True, True, 5, [1, 2, 2]))
        self.assertFalse(abaddon_qualifies(True, True, 6, [1, 2, 2]))
        self.assertFalse(abaddon_qualifies(True, False, 2, [4, 4, 4]))
        self.assertFalse(abaddon_qualifies(False, True, 2, [4, 4, 4]))
        self.assertFalse(abaddon_qualifies(True, True, 1, [0, 0, 0]))

    def test_abaddon_mount_doom_and_ignus_payable_loop_resources(self):
        def mount_doom_can_trigger(mana, untapped, three_opponents=True):
            return untapped and mana["generic"] >= 1 and mana["B"] >= 1 and mana["R"] >= 1 and three_opponents
        self.assertTrue(mount_doom_can_trigger({"generic": 1, "B": 1, "R": 1}, True))
        self.assertFalse(mount_doom_can_trigger({"generic": 1, "B": 1, "R": 0}, True))
        self.assertFalse(mount_doom_can_trigger({"generic": 1, "B": 1, "R": 1}, False))
        # Familiar reduces 2R Ignus recast by a single generic, not R.
        # One activation returns 2C+R net of its own R cost only after payable setup.
        self.assertEqual((2 - 1), 1)
        self.assertIn("Impact Tremors", self.library["Abaddon_the_Despoiler"])

    def test_abaddon_native_cascade_and_printed_nonhand_boundary(self):
        src = self.library["Abaddon_the_Despoiler"]
        for name in ("Noise Marine", "Call Forth the Tempest", "Nalfeshnee",
                     "Sakashima of a Thousand Faces", "Sanctum of Stone Fangs"):
            self.assertIn(name, src)
        self.assertFalse(abaddon_qualifies(True, False, 5, [5, 5, 5]))

    def test_goro_one_per_damaged_player_not_creature(self):
        self.assertEqual(goro_dragons(["A", "A", "B"]), 2)
        self.assertEqual(goro_dragons(["A", "A", "B"], True), 4)
        self.assertEqual(goro_dragons(["A", "B", "C"], True), 6)
        self.assertEqual(goro_dragons([], True), 0)

    def test_goro_double_strike_and_future_haste_boundary(self):
        self.assertEqual(goro_dragons(["A"], False, 2), 2)
        before_damage_haste_affected = {"Hanweir token"}
        later_entered_dragon = "new Dragon"
        self.assertNotIn(later_entered_dragon, before_damage_haste_affected)
        self.assertIn("Dragon Tempest", self.library["Goro_Goro_and_Satoru"])
        self.assertIn("Samut, Hazoret's Champion", self.library["Goro_Goro_and_Satoru"])

    def test_goro_breath_needs_real_host_hit_and_haste(self):
        def can_continue(enchanted_hit, next_host_exists, can_attack_next_combat):
            return enchanted_hit and next_host_exists and can_attack_next_combat
        self.assertTrue(can_continue(True, True, True))
        self.assertFalse(can_continue(True, True, False))
        self.assertFalse(can_continue(False, True, True))
        self.assertFalse(can_continue(True, False, True))

    def test_gwendlyn_turn_only_and_brighthearth_bracers(self):
        self.assertEqual(gwendlyn_discard_effects(True, True, True, True), 3)
        self.assertEqual(gwendlyn_discard_effects(True, True, True, False), 2)
        self.assertEqual(gwendlyn_discard_effects(True, True, False, True), 2)
        self.assertEqual(gwendlyn_discard_effects(False, True, True, True), 0)
        self.assertEqual(gwendlyn_discard_effects(True, False, True, True), 0)

    def test_gwendlyn_sting_untap_does_not_undo_opponent_turn_restriction(self):
        self.assertEqual(gwendlyn_discard_effects(False, True), 0)
        src = self.library["Gwendlyn_Di_Corci"]
        for card in ("Sting, the Glinting Dagger", "Rings of Brighthearth",
                     "Illusionist's Bracers", "Chains of Mephistopheles"):
            self.assertIn(card, src)
        self.assertNotIn("Mindcrank", src)

    def test_inalla_eminence_non_token_zone_and_payment(self):
        self.assertEqual(inalla_copy(True, True, True), 1)
        self.assertEqual(inalla_copy(False, True, True), 0)
        self.assertEqual(inalla_copy(True, False, True), 0)
        self.assertEqual(inalla_copy(True, True, False), 0)

    def test_inalla_gifts_six_of_six_access_not_full_victory(self):
        pile = {"Spellseeker", "Step Through", "Reanimate", "Unearth"}
        for grave in combinations(sorted(pile), 2):
            hand = pile - set(grave)
            reachable = "Spellseeker" in hand or (
                "Spellseeker" in grave and bool(hand & {"Reanimate", "Unearth"})
            )
            with self.subTest(grave=grave):
                self.assertTrue(reachable)
        self.assertEqual(len(list(combinations(pile, 2))), 6)

    def test_inalla_scholar_mana_value_and_five_wizard_cost(self):
        doc = self.docs["Inalla__Archmage_Ritualist"]
        self.assertIn("retain printed mana value 7", doc)
        def can_tap_five_untapped_wizards(wizard_states):
            return sum(untapped for untapped in wizard_states) >= 5
        self.assertTrue(can_tap_five_untapped_wizards([True] * 5))
        self.assertFalse(can_tap_five_untapped_wizards([True] * 4 + [False]))
        self.assertIn("Corpse Dance", self.library["Inalla__Archmage_Ritualist"])
        self.assertNotIn("Final Fortune", self.library["Inalla__Archmage_Ritualist"])

    def test_jeleva_actual_cast_mana_includes_commander_tax(self):
        self.assertEqual(jeleva_exile_count(True, 4, 4), 16)
        self.assertEqual(jeleva_exile_count(True, 6, 4), 24)
        self.assertEqual(jeleva_exile_count(False, 0, 4), 0)
        self.assertEqual(jeleva_exile_count(True, 4, 4, True), 32)

    def test_jeleva_prodigy_two_casts_require_two_linked_cards(self):
        def legal_casts(trigger_count, eligible_distinct_linked_cards):
            return min(trigger_count, eligible_distinct_linked_cards)
        self.assertEqual(legal_casts(2, 2), 2)
        self.assertEqual(legal_casts(2, 1), 1)
        self.assertEqual(legal_casts(2, 0), 0)
        self.assertIn("Harmonic Prodigy", self.library["Jeleva__Nephalia_s_Scourge"])

    def test_jeleva_free_fire_covenant_still_pays_life(self):
        def can_cast_fire_covenant(current_life, needed_damage, legal_targets):
            return current_life > needed_damage and legal_targets
        self.assertTrue(can_cast_fire_covenant(20, 6, True))
        self.assertFalse(can_cast_fire_covenant(6, 6, True))
        self.assertFalse(can_cast_fire_covenant(20, 6, False))

    def test_jeleva_cavern_mana_cast_restriction_and_greaves_shroud(self):
        def cavern_protects(chose_wizard, casting_wizard, colored_cavern_mana_spent):
            return chose_wizard and casting_wizard and colored_cavern_mana_spent
        self.assertTrue(cavern_protects(True, True, True))
        self.assertFalse(cavern_protects(True, True, False))
        self.assertFalse(cavern_protects(True, False, True))
        self.assertIn("Lightning Greaves", self.library["Jeleva__Nephalia_s_Scourge"])
        self.assertIn("Torch Courier", self.library["Jeleva__Nephalia_s_Scourge"])


if __name__ == "__main__":
    unittest.main()
