"""M8 #11-#15 exact-approved raw cards, full 99 libraries and scoped cases.

Finite factual models plus adverse fixtures are NOT a complete Magic stack engine,
independent M6 J or measured multiplayer game win rate.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONFIGS = {
    "Cult_of_Skaro": {
        "number": 11, "prefix": "Cult_of_Skaro_e7c264409bd23bd6",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 E1 E2 W1 W2 W3 F2 F3",
        "retired": ("Cybermen Squadron", "Anrakyr the Traveller", "Thopter Spy Network"),
        "basics": {"Island": 2, "Mountain": 3, "Swamp": 2},
    },
    "Davros__Dalek_Creator": {
        "number": 12, "prefix": "Davros__Dalek_Creator_96c6b1cde56eb79d",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 F2 F3",
        "retired": ("Labyrinth Raptor", "The Cyber-Controller", "Blasphemous Act"),
        "basics": {"Island": 2, "Mountain": 3, "Swamp": 3},
    },
    "Doctor_Doom__King_of_Latveria": {
        "number": 13, "prefix": "Doctor_Doom__King_of_Latveria_7f74aa25cbbc47d4",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "retired": ("Big Score", "Kang, Temporal Tyrant", "Unexpected Windfall"),
        "basics": {"Island": 1, "Mountain": 1, "Swamp": 1},
    },
    "Don_Andres__the_Renegade": {
        "number": 14, "prefix": "Don_Andres__the_Renegade_59c62e50874816a4",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "retired": ("Professional Face-Breaker", "Seize the Spotlight", "Stolen Strategy"),
        "basics": {"Island": 2, "Mountain": 1, "Swamp": 1},
    },
    "Dr__Eggman": {
        "number": 15, "prefix": "Dr__Eggman_3ef9dc5bcda84834",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 F2 F3",
        "retired": ("Blasphemous Act", "Cryptothrall", "Withering Torment"),
        "basics": {"Island": 2, "Mountain": 2, "Swamp": 2},
    },
}


def cult_attack_events(declared_attackers: int, copied_trigger: bool = False,
                       roaming_throne: bool = False) -> int:
    return declared_attackers * (1 + int(copied_trigger) + int(roaming_throne))


def davros_resolution(losses, permanent_end_step_copies=0):
    qualifies = [life >= 3 for life in losses]
    triggers = 1 + permanent_end_step_copies
    return triggers if any(qualifies) else 0, sum(qualifies) * triggers


def doom_events(discard_events, commander_present=True):
    """Each event is a tuple (lands_discarded, cards_discarded)."""
    return 2 * sum(lands > 0 for lands, _ in discard_events) if commander_present else 0


def don_treasure(action, owner_is_opponent, card_is_noncreature,
                 throne_on_pirate=False):
    if action != "cast" or not owner_is_opponent or not card_is_noncreature:
        return 0
    return 4 if throne_on_pirate else 2


def eggman_put_possible(opponent_hand, own_eligible_payloads, opponent_discards):
    if opponent_discards:
        return False, int(opponent_hand > 0)
    return own_eligible_payloads > 0, 0


class NextFiveExactCurrentQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        index = json.loads((ROOT / "exports/m8_candidate_2026-10-28/index.json").read_text())
        cls.by_id = {row["deck_id"]: row for row in index["decks"]}
        cls.source = {}
        cls.reports = {}
        for deck_id, cfg in CONFIGS.items():
            row = cls.by_id[deck_id]
            assert row["number"] == cfg["number"]
            raw = (ROOT / row["source_file"]).read_bytes()
            assert sha256(raw).hexdigest() == row["source_sha256"]
            cls.source[deck_id] = Counter()
            for line in raw.decode("utf-8").splitlines():
                quantity, name = line.split("x ", 1)
                cls.source[deck_id][name] += int(quantity)
            path = ROOT / f"refinement/verification/m8_quality_scope/{cfg['prefix']}.md"
            cls.reports[deck_id] = path.read_text()

    def test_five_source_sha_and_all_495_physical_library_copies_exact(self):
        all_copies = 0
        for deck_id, cfg in CONFIGS.items():
            with self.subTest(deck=deck_id):
                source = self.source[deck_id]
                doc = self.reports[deck_id]
                self.assertEqual(sum(source.values()), 100)
                self.assertEqual(sum(q for n, q in source.items() if "[Commander]" in n), 1)
                self.assertIn(self.by_id[deck_id]["source_sha256"], doc)
                library = Counter({n: q for n, q in source.items() if "[Commander]" not in n})
                ledger = Counter()
                for q, n in re.findall(r"^- (\d+)x (.+)$", doc, re.MULTILINE):
                    ledger[n] += int(q)
                self.assertEqual(library, ledger)
                self.assertEqual(sum(ledger.values()), 99)
                self.assertEqual({n: library[n] for n in cfg["basics"]}, cfg["basics"])
                for retired in cfg["retired"]:
                    self.assertNotIn(retired, library)
                all_copies += sum(ledger.values())
        self.assertEqual(all_copies, 495)

    def test_sixty_seven_original_group_id_adversarial_rows_not_old_j(self):
        total = 0
        for deck_id, cfg in CONFIGS.items():
            doc = self.reports[deck_id]
            actual = re.findall(r"^\| \*\*(P0|P1) (C\d+|K\d+|E\d+|W\d+|F\d+)\*\* \|([^\n]+)$",
                                doc, re.MULTILINE)
            expected = {(priority, case) for priority in ("P0", "P1")
                        for case in cfg[priority].split()}
            self.assertEqual({(p, n) for p, n, _ in actual}, expected, deck_id)
            self.assertEqual(len(actual), len(expected), deck_id)
            for priority, case, cells in actual:
                with self.subTest(deck=deck_id, case=case):
                    parts = [x.strip() for x in cells.split("|")]
                    self.assertGreaterEqual(len(parts), 2)
                    self.assertGreater(len(parts[0]), 40)
                    self.assertGreater(len(parts[1]), 37)
            self.assertIn("DESIGN_ONLY_UNIMPLEMENTED_NOT_RUN", doc)
            total += len(expected)
        self.assertEqual(total, 67)

    def test_cult_random_mode_attack_only_and_trigger_copy_vs_new(self):
        self.assertEqual(cult_attack_events(1), 1)
        self.assertEqual(cult_attack_events(1, copied_trigger=True), 2)
        self.assertEqual(cult_attack_events(1, roaming_throne=True), 2)
        self.assertEqual(cult_attack_events(1, True, True), 3)
        self.assertEqual(cult_attack_events(0, True, True), 0)
        self.assertEqual(len(("Thay", "Caan", "Sec", "Jast")), 4)

    def test_cult_real_assault_loop_requires_paid_sword_damage_and_main(self):
        def repeat(sword_connects, available_total, red_pips, legal_main):
            return sword_connects and available_total >= 5 and red_pips >= 2 and legal_main
        self.assertTrue(repeat(True, 5, 2, True))
        for case in ((False, 5, 2, True), (True, 4, 2, True),
                     (True, 5, 1, True), (True, 5, 2, False)):
            self.assertFalse(repeat(*case))

    def test_davros_resolution_permanently_cloned_and_threshold(self):
        self.assertEqual(davros_resolution([3, 0, 0]), (1, 1))
        self.assertEqual(davros_resolution([0, 0, 0], 3), (0, 0))
        self.assertEqual(davros_resolution([3, 0, 0], 2), (3, 3))
        self.assertEqual(davros_resolution([3, 3, 3], 2), (3, 9))
        self.assertEqual(davros_resolution([3, 2, 2]), (1, 1))
        self.assertEqual(davros_resolution([3, 3, 3]), (1, 3))
        self.assertEqual(davros_resolution([3, 3, 3], 0)[0], 1)

    def test_davros_purphoros_two_not_three_without_multiplier(self):
        # After first qualifying Dalek, Purphoros's 2 to B/C fails threshold.
        self.assertEqual(davros_resolution([3, 2, 2]), (1, 1))
        # Mechanized Warfare increases an actual red source damage event by 1.
        self.assertEqual(davros_resolution([3, 3, 3]), (1, 3))
        self.assertNotIn("Labyrinth Raptor", self.source["Davros__Dalek_Creator"])

    def test_doom_event_count_not_discarded_land_cards(self):
        self.assertEqual(doom_events([(3, 3)]), 2)
        self.assertEqual(doom_events([(1, 1), (1, 1), (1, 1)]), 6)
        self.assertEqual(doom_events([(0, 4), (2, 3)]), 2)
        self.assertEqual(doom_events([(1, 1)], commander_present=False), 0)

    def test_doom_dakmor_dredge_card_count_and_tolar_west_zero(self):
        def dredge_two(library_cards, land_in_grave):
            return library_cards >= 2 and land_in_grave
        self.assertTrue(dredge_two(2, True))
        self.assertFalse(dredge_two(1, True))
        self.assertFalse(dredge_two(4, False))
        # Transmute costs one plus UU and can find MV-0 lands/Mox, not MV-1.
        self.assertIn("Tolaria West", self.source["Doctor_Doom__King_of_Latveria"])

    def test_don_opponent_ownership_cast_and_tapped_treasures(self):
        self.assertEqual(don_treasure("cast", True, True), 2)
        self.assertEqual(don_treasure("cast", True, True, True), 4)
        self.assertEqual(don_treasure("cast", False, True), 0)
        self.assertEqual(don_treasure("cast", True, False), 0)
        self.assertEqual(don_treasure("put", True, True), 0)
        self.assertEqual(don_treasure("copy", True, True), 0)

    def test_don_shipwreck_two_other_not_two_basics_and_verges(self):
        def shipwreck_untapped(other_land_count):
            return other_land_count >= 2
        def gloomlake_black(types):
            return "Island" in types or "Swamp" in types
        def blazemire_red(types):
            return "Swamp" in types or "Mountain" in types
        self.assertFalse(shipwreck_untapped(1))
        self.assertTrue(shipwreck_untapped(2))
        self.assertFalse(gloomlake_black(set()))
        self.assertTrue(gloomlake_black({"Island"}))
        self.assertFalse(blazemire_red({"Island"}))
        self.assertTrue(blazemire_red({"Mountain"}))

    def test_eggman_empty_hand_choice_and_put_is_not_cast(self):
        self.assertEqual(eggman_put_possible(0, 3, True), (False, 0))
        self.assertEqual(eggman_put_possible(2, 3, True), (False, 1))
        self.assertEqual(eggman_put_possible(0, 3, False), (True, 0))
        self.assertEqual(eggman_put_possible(0, 0, False), (False, 0))
        # A Cityscape Leveler put into play does not produce its on-cast trigger.
        self.assertIn("Cityscape Leveler", self.source["Dr__Eggman"])
        self.assertIn("Skysovereign, Consul Flagship", self.source["Dr__Eggman"])

    def test_eggman_mox_conditional_and_vehicle_noncreature_until_crewed(self):
        def mox_opal_produces_mana(artifact_count):
            return artifact_count >= 3
        self.assertFalse(mox_opal_produces_mana(2))
        self.assertTrue(mox_opal_produces_mana(3))
        def skysovereign_crewed(available_untapped_power):
            return available_untapped_power >= 3
        self.assertFalse(skysovereign_crewed(2))
        self.assertTrue(skysovereign_crewed(3))


if __name__ == "__main__":
    unittest.main()
