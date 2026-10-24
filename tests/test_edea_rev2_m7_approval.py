"""Edea M7 Rev2 exact owner-approved canonical lock and prior fifteen-lock regression.

Selected Oracle snapshot was live on 2026-10-23, not freshly queried on
2026-10-24; this suite does not claim multiplayer match simulations.
"""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVED = ROOT / "refinement/decklists/Edea_Possessed_Sorceress_M7_Rev2_Approved_2026-10-23.txt"
BASELINE = ROOT / "refinement/decklists/Edea_Possessed_Sorceress_Approved_2026-10-14.txt"
ORACLE = ROOT / "refinement/verification/Edea_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT = ROOT / "refinement/approvals/Edea_M7_Rev2_Approved_2026-10-23.md"
VERIFY = ROOT / "refinement/verification/Edea_M7_Rev2_Approved_2026-10-23_Verification.md"
REGISTRY = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
EXACT = "a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54"
OLD = "fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4"
DECK_ID = "Edea__Possessed_Sorceress"
COMMANDER = "Edea, Possessed Sorceress"
SWAPS = [
    ("Aggravated Assault", "Mass Mutiny"),
    ("Kaya's Ghostform", "Zara, Renegade Recruiter"),
    ("Hall of Echoes", "Shipwreck Marsh"),
    ("Geyadrone Dihada", "Village Rites"),
    ("Combat Celebrant", "Seize the Spotlight"),
]
BASICS = {"Island": 3, "Mountain": 3, "Swamp": 3}
ROCKS = {"Sol Ring", "Arcane Signet", "Fellwar Stone",
         "Talisman of Creativity", "Talisman of Dominance",
         "Talisman of Indulgence"}
GAME_CHANGERS = {"Ancient Tomb", "Demonic Tutor", "Fierce Guardianship"}
KEEP = {"Evereth, Viceroy of Plunder", "High Market",
        "Ayara, Widow of the Realm // Ayara, Furnace Queen",
        "Ashnod's Altar", "Phyrexian Altar", "Phyrexian Tower",
        "Goblin Bombardment", "Warren Soultrader", "Illuminor Szeras",
        "Viscera Seer", "Braids, Arisen Nightmare"}
PRIOR_15 = {
    "Abaddon_the_Despoiler": ("5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24", "refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt"),
    "Admiral_Beckett_Brass": ("ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000", "refinement/decklists/Admiral_Beckett_Brass_M7_Approved_2026-10-22.txt"),
    "Admiral_Brass__Unsinkable": ("dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7", "refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt"),
    "Anhelo_the_Painter": ("865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77", "refinement/decklists/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.txt"),
    "Ashad_the_Lone_Cyberman": ("352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267", "refinement/decklists/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.txt"),
    "Ashnod_the_Uncaring": ("a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761", "refinement/decklists/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23.txt"),
    "Be_lakor_the_Dark_Master": ("2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4", "refinement/decklists/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23.txt"),
    "Cecily__Bjorna__Lutri": ("e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d", "refinement/decklists/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23.txt"),
    "Cormela__Glamour_Thief": ("d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd", "refinement/decklists/Cormela_Glamour_Thief_M7_Rev2_Approved_2026-10-23.txt"),
    "Crosis__the_Purger": ("a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a", "refinement/decklists/Crosis_the_Purger_M7_Rev2_Approved_2026-10-23.txt"),
    "Cult_of_Skaro": ("e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d", "refinement/decklists/Cult_of_Skaro_M7_Rev2_Approved_2026-10-23.txt"),
    "Davros__Dalek_Creator": ("96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc", "refinement/decklists/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23.txt"),
    "Doctor_Doom__King_of_Latveria": ("7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20", "refinement/decklists/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23.txt"),
    "Don_Andres__the_Renegade": ("59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f", "refinement/decklists/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23.txt"),
    "Dr__Eggman": ("3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec", "refinement/decklists/Dr_Eggman_M7_Rev2_Approved_2026-10-23.txt"),
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    result = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        match = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        if match is None:
            raise AssertionError(f"Unparseable line {i + 1}: {line}")
        qty, name, command_marker = int(match[1]), match[2], match[3]
        if i == 0:
            assert (qty, name, bool(command_marker)) == (1, COMMANDER, True)
        else:
            assert command_marker is None
        result[name] += qty
    return result, lines

class EdeaM7Rev2ExactApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards, cls.lines = parse(APPROVED)
        cls.baseline, _ = parse(BASELINE)
        cls.oracle = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.oracle_by_name = {x["name"]: x for x in cls.oracle["cards"]}
        cls.state = json.loads(REGISTRY.read_text(encoding="utf-8"))
        with TRACKER.open(encoding="utf-8", newline="") as f:
            cls.tracker = list(csv.DictReader(f))

    def test_raw_bytes_and_historical_approved_source(self):
        self.assertEqual(digest(APPROVED), EXACT)
        self.assertEqual(digest(BASELINE), OLD)
        self.assertEqual(self.oracle["candidate_raw_sha256"], EXACT)
        self.assertEqual(self.oracle["baseline_raw_sha256"], OLD)
        self.assertEqual(self.oracle["as_of"], "2026-10-23")
        self.assertEqual(self.oracle["deck_id"], DECK_ID)
        self.assertIn(EXACT, RECEIPT.read_text(encoding="utf-8"))
        self.assertIn(EXACT, VERIFY.read_text(encoding="utf-8"))

    def test_exact_100_singleton_identity(self):
        self.assertEqual(sum(self.cards.values()), 100)
        self.assertEqual(len(self.cards), 94)
        self.assertEqual(len(self.lines), 94)
        self.assertEqual(self.cards[COMMANDER], 1)
        for name, quantity in self.cards.items():
            self.assertEqual(quantity, BASICS.get(name, 1), name)
        self.assertEqual(len(self.oracle_by_name), 94)

    def test_exact_five_swaps_and_protected_owner_keeps(self):
        additions = set(self.cards) - set(self.baseline)
        removals = set(self.baseline) - set(self.cards)
        self.assertEqual(additions, {x for x, _ in SWAPS})
        self.assertEqual(removals, {x for _, x in SWAPS})
        self.assertTrue(KEEP <= set(self.cards))
        for name in KEEP:
            self.assertEqual(self.cards[name], self.baseline[name])

    def test_oracle_identity_legality_lands_rocks(self):
        self.assertEqual(set(self.cards), set(self.oracle_by_name))
        self.assertEqual(sum(q for n, q in self.cards.items()
                             if "Land" in self.oracle_by_name[n]["type_line"]), 35)
        self.assertEqual(sum(self.cards[n] for n in ROCKS), 6)
        self.assertTrue(ROCKS <= self.cards.keys())
        self.assertEqual({n for n in self.cards
                          if self.oracle_by_name[n].get("game_changer")}, GAME_CHANGERS)
        for name, quantity in self.cards.items():
            evidence = self.oracle_by_name[name]
            self.assertEqual(evidence["name"], name)
            self.assertEqual(evidence["quantity"], quantity)
            self.assertEqual(evidence["commander_legality"], "legal", name)
            self.assertTrue(set(evidence["color_identity"]) <= set("UBR"), name)
            self.assertTrue(evidence.get("oracle_id"), name)
            self.assertIsInstance(evidence["oracle_text"], str)
        self.assertEqual(self.oracle["project_exceptions"], [])

    def test_actual_rules_for_theft_and_extra_combat(self):
        oracle = lambda name: self.oracle_by_name[name]["oracle_text"]
        self.assertIn("At the beginning of combat on your turn", oracle(COMMANDER))
        self.assertIn("you draw a card", oracle(COMMANDER))
        self.assertIn("additional combat phase", oracle("Aggravated Assault"))
        self.assertIn("Activate only as a sorcery", oracle("Aggravated Assault"))
        self.assertIn("exert it as it attacks", oracle("Combat Celebrant"))
        self.assertIn("additional combat phase", oracle("Combat Celebrant"))
        self.assertIn("under your control", oracle("Kaya's Ghostform"))
        self.assertIn("legend rule", oracle("Hall of Echoes"))
        self.assertIn("{5}", oracle("Hall of Echoes"))
        self.assertIn("Gain control of target creature or planeswalker",
                      oracle("Geyadrone Dihada"))

    def test_owner_registry_and_tracker(self):
        self.assertEqual(len(self.state["decks"]), 62)
        row = self.state["decks"][DECK_ID]
        self.assertEqual((row["approval_status"], row["lock_status"],
                          row["current_stage"]), ("APPROVED", "LOCKED", "LOCKED"))
        self.assertTrue(row["final_gate_passed"])
        self.assertEqual(row["approved_list_sha256"], EXACT)
        self.assertEqual(row["m7_final_candidate_sha256"], EXACT)
        self.assertEqual(row["user_approval_date"], "2026-10-23")
        self.assertEqual(row["previous_approved_source_raw_sha256"], OLD)
        self.assertEqual(row["previous_approved_list_artifact"], str(BASELINE.relative_to(ROOT)))
        self.assertEqual(row["approved_list_artifact"], str(APPROVED.relative_to(ROOT)))
        self.assertEqual(row["m7_archidekt_tags"], ["Theft", "Extra Combats", "Aristocrats"])
        self.assertEqual(row["m7_power_bracket"], "4 — Optimized")
        self.assertEqual(row["m7_project_exceptions"], [])
        self.assertEqual(len(self.tracker), 62)
        target = self.tracker[15]
        self.assertEqual(target["deck_id"], DECK_ID)
        self.assertEqual(target["final_list_hash"], EXACT)
        self.assertEqual(target["user_approval_date"], "2026-10-23")
        self.assertEqual(target["final_gate_passed"], "YES")
        self.assertIn("M7 Rev2", target["refinement_status"])

    def test_previous_fifteen_locks_untouched(self):
        for deck_id, (expected_sha, artifact) in PRIOR_15.items():
            row = self.state["decks"][deck_id]
            self.assertEqual(row["approved_list_sha256"], expected_sha, deck_id)
            self.assertEqual(row["approved_list_artifact"], artifact, deck_id)
            self.assertEqual(row["approval_status"], "APPROVED", deck_id)
            self.assertEqual(row["lock_status"], "LOCKED", deck_id)
            self.assertEqual(digest(ROOT / artifact), expected_sha, deck_id)

if __name__ == "__main__":
    unittest.main()
