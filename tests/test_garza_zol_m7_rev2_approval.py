"""Cory's exact Garza M7 Rev2 approved source, 7 swaps and all prior 19 locks.
97 card records are from archived Oct23 Scryfall; 3 are published manual references.
This test does not simulate multiplayer games, assert win rates or make a new live API call.
"""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVED = ROOT / "refinement/decklists/Garza_Zol_Plague_Queen_M7_Rev2_Approved_2026-10-24.txt"
BASELINE = ROOT / "refinement/decklists/Garza_Zol_Plague_Queen_Approved_2026-10-14.txt"
ORACLE = ROOT / "refinement/verification/Garza_Zol_Plague_Queen_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT = ROOT / "refinement/approvals/Garza_Zol_Plague_Queen_M7_Rev2_Approved_2026-10-24.md"
VERIFICATION = ROOT / "refinement/verification/Garza_Zol_Plague_Queen_M7_Rev2_Approved_2026-10-24_Verification.md"
REGISTRY = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
SHA = "353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244"
OLD = "32c0e8049a9c8a5d238048b4f774f0457908d724f23d4597b7da93a6cba0c16f"
DECK_ID = "Garza_Zol__Plague_Queen"
SWAPS = {
    "Lizard Blades": "Scythe of the Wretched",
    "Two-Handed Axe // Sweeping Cleave": "Inquisitor's Flail",
    "Conqueror's Flail": "Robe of the Archmagi",
    "Giantfall": "Rapid Hybridization",
    "Seize the Day": "Sheoldred's Edict",
    "Temur Battle Rage": "Psychotic Fury",
    "Malakir Rebirth // Malakir Mire": "Takenuma, Abandoned Mire",
}
MANUALLY_CHECKED = {
    "Conqueror's Flail", "Seize the Day", "Two-Handed Axe // Sweeping Cleave"
}
ROCKS = {
    "Arcane Signet", "Sol Ring", "Mana Vault", "Grim Monolith", "Fellwar Stone",
    "Dimir Signet", "Izzet Signet", "Rakdos Signet",
    "Talisman of Creativity", "Talisman of Dominance", "Talisman of Indulgence",
}
PRIOR_19 = {
  "Abaddon_the_Despoiler": [
    "5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
    "refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt"
  ],
  "Admiral_Beckett_Brass": [
    "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
    "refinement/decklists/Admiral_Beckett_Brass_M7_Approved_2026-10-22.txt"
  ],
  "Admiral_Brass__Unsinkable": [
    "dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
    "refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt"
  ],
  "Anhelo_the_Painter": [
    "865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77",
    "refinement/decklists/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Ashad_the_Lone_Cyberman": [
    "352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267",
    "refinement/decklists/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.txt"
  ],
  "Ashnod_the_Uncaring": [
    "a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761",
    "refinement/decklists/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Be_lakor_the_Dark_Master": [
    "2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4",
    "refinement/decklists/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Cecily__Bjorna__Lutri": [
    "e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d",
    "refinement/decklists/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Cormela__Glamour_Thief": [
    "d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd",
    "refinement/decklists/Cormela_Glamour_Thief_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Crosis__the_Purger": [
    "a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a",
    "refinement/decklists/Crosis_the_Purger_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Cult_of_Skaro": [
    "e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d",
    "refinement/decklists/Cult_of_Skaro_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Davros__Dalek_Creator": [
    "96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc",
    "refinement/decklists/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Doctor_Doom__King_of_Latveria": [
    "7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20",
    "refinement/decklists/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Don_Andres__the_Renegade": [
    "59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f",
    "refinement/decklists/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Dr__Eggman": [
    "3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec",
    "refinement/decklists/Dr_Eggman_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Edea__Possessed_Sorceress": [
    "a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54",
    "refinement/decklists/Edea_Possessed_Sorceress_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Edward_Kenway": [
    "8c01f2be6190be3e3af0fc5ba45eca16faa1b9346981f840811e4b63822c5ee1",
    "refinement/decklists/Edward_Kenway_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Evelyn__the_Covetous": [
    "c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac",
    "refinement/decklists/Evelyn_the_Covetous_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Fire_Lord_Azula": [
    "77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273",
    "refinement/decklists/Fire_Lord_Azula_M7_Rev2_Approved_2026-10-24.txt"
  ]
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cards(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    counted = Counter()
    for i, line in enumerate(lines):
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        assert m, (i, line)
        n, name, tag = int(m[1]), m[2], m[3]
        assert n == 1
        assert (bool(tag) if i == 0 else not bool(tag))
        if i == 0:
            assert name == "Garza Zol, Plague Queen"
        counted[name] += n
    assert len(lines) == 100 and sum(counted.values()) == 100
    return lines, counted


class GarzaZolM7Rev2CanonicalApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lines, cls.deck = cards(APPROVED)
        _, cls.original = cards(BASELINE)
        cls.archive = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.oracle = {row["name"]: row for row in cls.archive["cards"]}
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        with TRACKER.open(newline="", encoding="utf-8") as stream:
            cls.tracker = list(csv.DictReader(stream))

    def test_exact_hash_and_original_preserved(self):
        self.assertEqual(digest(APPROVED), SHA)
        self.assertTrue(APPROVED.read_bytes().endswith(b"\n"))
        self.assertEqual(digest(BASELINE), OLD)
        self.assertEqual(self.archive["candidate_raw_sha256"], SHA)
        self.assertEqual(self.archive["baseline_raw_sha256"], OLD)
        self.assertIn(SHA, RECEIPT.read_text(encoding="utf-8"))
        self.assertIn(SHA, VERIFICATION.read_text(encoding="utf-8"))

    def test_structural_singleton_seven_exact_swaps(self):
        self.assertEqual((len(self.lines), sum(self.deck.values()), len(self.deck)), (100,100,100))
        self.assertEqual(self.lines[0], "1x Garza Zol, Plague Queen [Commander]")
        self.assertTrue(all(q == 1 for q in self.deck.values()))
        self.assertEqual(set(self.deck)-set(self.original), set(SWAPS))
        self.assertEqual(set(self.original)-set(self.deck), set(SWAPS.values()))
        self.assertEqual(self.lines[1:], sorted(self.lines[1:], key=str.casefold))
        for important in ROCKS | {"Exotic Orchard", "Kediss, Emberclaw Familiar", "Grafted Exoskeleton",
                                  "Aggravated Assault", "Quietus Spike", "Thornbite Staff"}:
            self.assertIn(important, self.deck)

    def test_selected_source_legality_oracle_and_game_changers(self):
        self.assertEqual(self.archive["status"], "CORY_APPROVED_GARZA_ZOL_M7_REV2_CANONICAL_SOURCE_BOUND")
        self.assertEqual(self.archive["physical_cards"], 100)
        self.assertEqual(self.archive["distinct_names"], 100)
        self.assertEqual(set(self.oracle), set(self.deck))
        self.assertEqual(len(self.archive["cards"]), 100)
        self.assertEqual(len(self.archive["project_exceptions"]), 0)
        self.assertEqual(sum("Land" in c["type_line"] for c in self.oracle.values()), 38)
        self.assertEqual(sum("Equipment" in c["type_line"] for c in self.oracle.values()), 20)
        self.assertEqual(sum(bool(c["game_changer"]) for c in self.oracle.values()), 9)
        count_published = 0
        for name, c in self.oracle.items():
            self.assertEqual(c["quantity"], 1, name)
            self.assertEqual(c["commander_legality"], "legal", name)
            self.assertTrue(set(c["color_identity"]) <= set("UBR"), name)
            if name in MANUALLY_CHECKED:
                count_published += 1
                self.assertTrue(c["source_url"].startswith("https://scryfall.com/"))
                self.assertIsNone(c["oracle_id"]) # Do NOT fabricate Scryfall API metadata
                self.assertIn("published", c["source_kind"].lower())
            else:
                self.assertTrue(c["oracle_id"], name)
                self.assertIn("snapshot", c["source_kind"].lower())
        self.assertEqual(count_published, 3)

    def test_key_rules_and_mana_costs_not_games(self):
        text = lambda n: self.oracle[n]["oracle_text"]
        self.assertIn("Whenever a creature dealt damage by Garza Zol this turn dies", text("Garza Zol, Plague Queen"))
        self.assertIn("Whenever Garza Zol deals combat damage to a player", text("Garza Zol, Plague Queen"))
        self.assertIn("Equipped creature has double strike", text("Lizard Blades"))
        self.assertIn("double its power until end of turn", text("Two-Handed Axe // Sweeping Cleave"))
        self.assertIn("double strike", text("Two-Handed Axe // Sweeping Cleave"))
        self.assertIn("can't cast spells during your turn", text("Conqueror's Flail"))
        self.assertIn("deals damage equal to its power", text("Giantfall"))
        self.assertIn("Flashback {2}{R}", text("Seize the Day"))
        self.assertIn("trample", text("Temur Battle Rage"))
        self.assertIn("return it to the battlefield tapped", text("Malakir Rebirth // Malakir Mire"))
        self.assertIn("enters tapped", text("Malakir Rebirth // Malakir Mire"))
        self.assertIn("Scythe of the Wretched", RECEIPT.read_text(encoding="utf-8"))
        self.assertNotIn("Scythe of the Wretched", self.deck)
        self.assertEqual(len(set(self.deck)&ROCKS), 11)
        self.assertEqual(5*2*2, 20) # Axe-doubled 5 power in Lizard two damage steps
        self.assertEqual(5*2 + 5*4, 30) # Axe two separate attack triggers on Seize extra combat

    def test_approval_registry_tracker_only_this_new_row(self):
        self.assertEqual(len(self.registry["decks"]), 62)
        e = self.registry["decks"][DECK_ID]
        self.assertEqual((e["approval_status"],e["lock_status"],e["current_stage"]), ("APPROVED","LOCKED","LOCKED"))
        self.assertTrue(e["final_gate_passed"])
        self.assertEqual(e["approved_list_sha256"], SHA)
        self.assertEqual(e["m7_final_candidate_sha256"], SHA)
        self.assertEqual(e["previous_approved_list_sha256"], OLD)
        self.assertEqual(e["previous_approved_list_artifact"], str(BASELINE.relative_to(ROOT)))
        self.assertEqual(e["approved_list_artifact"], str(APPROVED.relative_to(ROOT)))
        self.assertEqual(e["m7_archidekt_tags"], ["Voltron","Commander Damage","Deathtouch-Control"])
        self.assertEqual(e["m7_power_bracket"], "4 — Optimized")
        self.assertEqual(e["m7_project_exceptions"], [])
        self.assertEqual(e["user_approval_date"], "2026-10-24")
        self.assertEqual(len(self.tracker), 62)
        t = self.tracker[19]
        self.assertEqual(t["deck_id"], DECK_ID)
        self.assertEqual(t["final_list_hash"], SHA)
        self.assertEqual(t["user_approval_date"], "2026-10-24")
        self.assertEqual(t["final_gate_passed"], "YES")
        self.assertIn("M7 Rev2",t["refinement_status"])

    def test_all_nineteen_previous_m7_locks_preserved_byte_for_byte(self):
        self.assertEqual(len(PRIOR_19), 19)
        for deck_id, (expected, path) in PRIOR_19.items():
            with self.subTest(deck_id=deck_id):
                e = self.registry["decks"][deck_id]
                self.assertEqual((e["approval_status"],e["lock_status"]),("APPROVED","LOCKED"))
                self.assertEqual(e["approved_list_sha256"],expected)
                self.assertEqual(e["approved_list_artifact"],path)
                self.assertEqual(digest(ROOT/path),expected)


if __name__ == "__main__":
    unittest.main()
