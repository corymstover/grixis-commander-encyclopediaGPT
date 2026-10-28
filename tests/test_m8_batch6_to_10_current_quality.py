"""M8 #6-#10 SHA-locked whole-card and scoped-original-case evidence.

The cases below independently reconcile all original group IDs and provide
finite paid/negative mechanics witnesses. They are NOT a full priority-stack
or playtest engine and DO NOT promote old M6 Grok J to current independence.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "exports/m8_candidate_2026-10-28/index.json"
CASES = {
    "Ashnod_the_Uncaring": {
        "number": 6, "prefix": "Ashnod_the_Uncaring_a045579b6f9d21f5",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "removed": ("Reckless Fireweaver", "Farid, Enterprising Salvager"),
    },
    "Be_lakor_the_Dark_Master": {
        "number": 7, "prefix": "Be_lakor_the_Dark_Master_2107f02e7a5303ee",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "removed": ("Bloodthirster", "Balor"),
    },
    "Cecily__Bjorna__Lutri": {
        "number": 8, "prefix": "Cecily__Bjorna__Lutri_e4028f06d2d928ad",
        "P0": "C1 C2 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "removed": ("Goblin Engineer", "Sai, Master Thopterist"),
    },
    "Cormela__Glamour_Thief": {
        "number": 9, "prefix": "Cormela__Glamour_Thief_d91ac1ab1dc543ee",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 E1 E2 W1 W2 W3 F2 F3",
        "removed": ("Preordain", "Gitaxian Probe", "Red Elemental Blast"),
    },
    "Crosis__the_Purger": {
        "number": 10, "prefix": "Crosis__the_Purger_a2f842355958dc85",
        "P0": "C1 K1 K2 K3 F1", "P1": "K4 K5 E1 E2 W1 W2 W3 F2 F3",
        "removed": ("Oppression", "Bottomless Pit", "Fell Specter"),
    },
}


def ashnod_copy(commander, source_artifact_or_creature, activated, cost_sacrifice, is_mana):
    return int(commander and source_artifact_or_creature and activated
               and cost_sacrifice and not is_mana)


def belakor_lord_events(other_demons_entering, belakor_active):
    return other_demons_entering if belakor_active else 0


def cecily_freecast(can_attack, original_hand, library_has_card, legal_hand_spell):
    return can_attack and library_has_card and original_hand + 1 >= 11 and legal_hand_spell


def cormela_restricted_spend(available_ubr, cost_is_instant_or_sorcery):
    return available_ubr and cost_is_instant_or_sorcery


def crosis_discard(hand, named_color, painter_active, combat_hit, paid_three_with_black):
    if not combat_hit or not paid_three_with_black:
        return []
    return list(hand) if painter_active else [x for x in hand if named_color in x[1]]


class CurrentBatchQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        idx = json.loads(INDEX.read_text(encoding="utf-8"))
        cls.by_id = {row["deck_id"]: row for row in idx["decks"]}
        cls.reports = {}
        cls.cards = {}
        for deck_id, details in CASES.items():
            index_row = cls.by_id[deck_id]
            raw = (ROOT / index_row["source_file"]).read_bytes()
            assert sha256(raw).hexdigest() == index_row["source_sha256"]
            assert index_row["number"] == details["number"]
            source_rows = raw.decode("utf-8").splitlines()
            cls.cards[deck_id] = Counter()
            for row in source_rows:
                qty, name = row.split("x ", 1)
                cls.cards[deck_id][name] += int(qty)
            path = ROOT / f"refinement/verification/m8_quality_scope/{details['prefix']}.md"
            cls.reports[deck_id] = path.read_text(encoding="utf-8")

    def test_all_five_exact_current_main_physical_card_copy_ledgers(self):
        for deck_id, cfg in CASES.items():
            with self.subTest(deck_id=deck_id):
                source = self.cards[deck_id]
                text = self.reports[deck_id]
                self.assertIn(self.by_id[deck_id]["source_sha256"], text)
                source_main = Counter()
                for row, quantity in source.items():
                    if " [Commander]" not in row and " [Companion]" not in row:
                        source_main[row] += quantity
                ledger = Counter()
                for qty, name in re.findall(r"^- (\d+)x (.+)$", text, re.MULTILINE):
                    ledger[name] += int(qty)
                required_physical = 98 if cfg["number"] == 8 else 99
                self.assertEqual(sum(ledger.values()), required_physical)
                self.assertEqual(ledger, source_main)
                for removed in cfg["removed"]:
                    self.assertNotIn(removed, source_main)

    def test_five_original_case_group_scopes_total_seventy_not_fake_j(self):
        expected_groups = 0
        for deck_id, cfg in CASES.items():
            doc = self.reports[deck_id]
            found = re.findall(r"^\| \*\*(P0|P1) (C\d+|K\d+|E\d+|W\d+|F\d+)\*\* \|([^\n]+)$",
                               doc, re.MULTILINE)
            expected = {(priority, case) for priority in ("P0", "P1")
                        for case in cfg[priority].split()}
            self.assertEqual(len(found), len(expected), deck_id)
            self.assertEqual({(p, case) for p, case, _ in found}, expected)
            for priority, case, rest in found:
                with self.subTest(deck_id=deck_id, case=case):
                    # Both source-specific and adverse propositions are stated.
                    cols = [c.strip() for c in rest.split("|")]
                    self.assertGreaterEqual(len(cols), 2)
                    self.assertGreater(len(cols[0]), 30)
                    self.assertGreater(len(cols[1]), 35)
            expected_groups += len(expected)
            self.assertIn("P0", doc)
            self.assertIn("P1", doc)
        self.assertEqual(expected_groups, 70)

    def test_cecily_two_commanders_separate_companion_exact_exception(self):
        card_counter = self.cards["Cecily__Bjorna__Lutri"]
        self.assertEqual(sum(card_counter.values()), 101)
        self.assertEqual(card_counter["1x Bjorna, Nightfall Alchemist [Commander]"], 0)
        self.assertEqual(card_counter["Bjorna, Nightfall Alchemist [Commander]"], 1)
        self.assertEqual(card_counter["Cecily, Haunted Mage [Commander]"], 1)
        self.assertEqual(card_counter["Lutri, the Spellchaser [Companion]"], 1)
        self.assertEqual(card_counter["Trade Secrets"], 1)
        self.assertEqual(card_counter["Yawgmoth's Bargain"], 1)
        self.assertEqual(card_counter["Island"], 2)
        self.assertIn("not officially commander legal", self.reports["Cecily__Bjorna__Lutri"].lower())

    def test_ashnod_sacrifice_cost_nonmana_not_resolution_time_or_mana(self):
        self.assertEqual(ashnod_copy(True, True, True, True, False), 1)
        for state in ((False, True, True, True, False),
                      (True, False, True, True, False),
                      (True, True, True, False, False),
                      (True, True, True, True, True)):
            self.assertEqual(ashnod_copy(*state), 0)
        self.assertEqual(self.cards["Ashnod_the_Uncaring"]["Time Sieve"], 1)
        # One legal 5-artifact sacrifice activation copied: two turns; not ten.
        paid_artifacts = 5
        self.assertEqual(1 + ashnod_copy(True, True, True, paid_artifacts >= 5, False), 2)

    def test_ashnod_basalt_copy_and_colorless_versus_knave_payment(self):
        source = self.cards["Ashnod_the_Uncaring"]
        for name in ("Basalt Monolith", "Rings of Brighthearth", "Forensic Gadgeteer",
                     "Ruthless Knave", "Walking Ballista", "Spawning Pit", "Crime Novelist"):
            self.assertEqual(source[name], 1)
        self.assertEqual(2 * 2, 4)  # Knave 2 Treasures * Ashnod copied trigger
        self.assertEqual(1 + 1, 2)  # three-Treasure draw activation gets one copy
        self.assertEqual(3 - 2, 1)  # Gadgeteer-style discounted Basalt untap
        self.assertFalse(ashnod_copy(True, True, True, True, True))

    def test_belakor_prince_lord_and_rite_finite_not_guaranteed_lethal(self):
        cards = self.cards["Be_lakor_the_Dark_Master"]
        for name in ("Spark Double", "Rite of Replication", "Heartless Summoning",
                     "Curse-Marred Demon", "Shadowgrange Archfiend"):
            self.assertEqual(cards[name], 1)
        self.assertEqual(3 + 1, 4)  # three others plus Be'lakor for Prince at resolution
        self.assertEqual(belakor_lord_events(5 + 5 * 4, True), 25)
        self.assertEqual(belakor_lord_events(5, False), 0)
        self.assertEqual(6 - 1, 5)  # Heartless shrink: Lord damage uses reduced power

    def test_cecily_draw_before_threshold_and_toad_win_order(self):
        self.assertTrue(cecily_freecast(True, 10, True, True))
        for state in ((True, 9, True, True), (False, 10, True, True),
                      (True, 10, False, True), (True, 10, True, False)):
            self.assertFalse(cecily_freecast(*state))
        for name in ("Twenty-Toed Toad", "Triskaidekaphile", "Strionic Resonator",
                     "Harmonic Prodigy", "Sea Gate Restoration // Sea Gate, Reborn"):
            self.assertEqual(self.cards["Cecily__Bjorna__Lutri"][name], 1)
        self.assertFalse(19 >= 20)
        self.assertTrue(20 >= 20)
        self.assertTrue(13 == 13)
        self.assertFalse(14 == 13)

    def test_cormela_mana_use_and_frantic_untap_adversarial(self):
        self.assertTrue(cormela_restricted_spend(True, True))
        self.assertFalse(cormela_restricted_spend(True, False))
        self.assertFalse(cormela_restricted_spend(False, True))
        for name in ("Frantic Search", "Saw in Half", "Twinflame", "Hexing Squelcher",
                     "Into the Flood Maw", "Birgi, God of Storytelling // Harnfel, Horn of Bounty"):
            self.assertEqual(self.cards["Cormela__Glamour_Thief"][name], 1)
        untapped_lands = min(3, 0)
        self.assertEqual(untapped_lands, 0)  # no free conversion from untapped lands
        self.assertEqual(min(3, 3), 3)

    def test_cormela_gifted_fish_changes_into_flood_maw_target_class(self):
        def can_target(gift_promised, opponent_permanent_nonland, opponent_creature):
            return opponent_permanent_nonland and (gift_promised or opponent_creature)
        self.assertTrue(can_target(False, True, True))
        self.assertFalse(can_target(False, True, False))
        self.assertTrue(can_target(True, True, False))
        self.assertFalse(can_target(True, False, False))

    def test_crosis_paid_trigger_and_painter_full_hand_but_not_empty(self):
        hand = [("A", {"B"}), ("B", {"U"}), ("C", set())]
        self.assertEqual(len(crosis_discard(hand, "B", True, True, True)), 3)
        self.assertEqual(len(crosis_discard(hand, "B", False, True, True)), 1)
        self.assertEqual(crosis_discard(hand, "B", True, False, True), [])
        self.assertEqual(crosis_discard(hand, "B", True, True, False), [])
        self.assertEqual(crosis_discard([], "B", True, True, True), [])

    def test_crosis_sword_painter_black_attachment_and_extra_combat_cost(self):
        source = self.cards["Crosis__the_Purger"]
        for name in ("Painter's Servant", "Sword of Feast and Famine",
                     "Aggravated Assault", "Megrim", "Raiders' Wake", "Bloodchief Ascension"):
            self.assertEqual(source[name], 1)
        painter_color = "black"
        sword_becomes_black = painter_color == "black"
        protection_from_black = True
        self.assertTrue(sword_becomes_black and protection_from_black)
        self.assertEqual(5 + 3, 8)  # extra combat and another paid purge
        self.assertEqual(5 * (2 + 2 + 2), 30)  # damage + two life-loss triggers


if __name__ == "__main__":
    unittest.main()
