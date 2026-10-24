"""Exact owner-approved Edward Kenway M7 Rev2 canonical lock; sixteen prior locks.

Selected Oracle was live on October 23; this is not fresh 24th Scryfall query
and no gameplay simulation or third-model independence is claimed.
"""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVED = ROOT / "refinement/decklists/Edward_Kenway_M7_Rev2_Approved_2026-10-23.txt"
BASELINE = ROOT / "refinement/decklists/Edward_Kenway_Approved_2026-10-14.txt"
ORACLE = ROOT / "refinement/verification/Edward_Kenway_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT = ROOT / "refinement/approvals/Edward_Kenway_M7_Rev2_Approved_2026-10-23.md"
VERIFY = ROOT / "refinement/verification/Edward_Kenway_M7_Rev2_Approved_2026-10-23_Verification.md"
REGISTRY = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
EXPECTED = "8c01f2be6190be3e3af0fc5ba45eca16faa1b9346981f840811e4b63822c5ee1"
OLD = "a08d3bc9c283415f1579c493eccb3febd7d10dea3777bf3dc50cfbc0dbed4019"
DECK_ID = "Edward_Kenway"
COMMANDER = "Edward Kenway"
SWAPS = [
    ("Mu Yanling, Wind Rider", "Breeches, Brazen Plunderer"),
    ("Brotherhood Vertibird", "Imposter Mech"),
    ("Mirkwood Bats", "Coastal Piracy"),
    ("Spectral Sailor", "Lotus Petal"),
    ("Malcolm, the Eyes", "Vaan, Street Thief"),
]
KEEP = {"Fellwar Stone", "Captain Lannery Storm", "Fateful Discovery",
        "Imperial Seal", "Time Sieve", "Academy Manufactor", "The Indomitable",
        "Luxurious Locomotive", "Glint-Horn Buccaneer",
        "Malcolm, Keen-Eyed Navigator", "Roaming Throne"}
ROCKS = {"Sol Ring", "Arcane Signet", "Fellwar Stone", "Mana Vault",
         "Talisman of Creativity", "Talisman of Dominance",
         "Talisman of Indulgence"}
GAME_CHANGERS = {"Ancient Tomb", "Chrome Mox", "Cyclonic Rift",
                 "Fierce Guardianship", "Force of Will", "Imperial Seal",
                 "Jeska's Will", "Mana Vault", "Mox Diamond",
                 "Vampiric Tutor"}
PRIOR_16 = {
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
    "Edea__Possessed_Sorceress": ("a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54", "refinement/decklists/Edea_Possessed_Sorceress_M7_Rev2_Approved_2026-10-23.txt"),
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    result = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        if m is None:
            raise AssertionError(f"Unparseable deck line {i+1}: {line}")
        qty, name, marker = int(m[1]), m[2], m[3]
        if i == 0:
            assert (qty, name, bool(marker)) == (1, COMMANDER, True)
        else:
            assert marker is None
        result[name] += qty
    return result, lines

class EdwardM7Rev2ExactApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards, cls.lines = parse(APPROVED)
        cls.baseline, _ = parse(BASELINE)
        cls.oracle = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.ev = {x["name"]: x for x in cls.oracle["cards"]}
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        with TRACKER.open(newline="", encoding="utf-8") as f:
            cls.tracker = list(csv.DictReader(f))

    def test_raw_hash_immutability(self):
        self.assertEqual(digest(APPROVED), EXPECTED)
        self.assertEqual(digest(BASELINE), OLD)
        self.assertEqual(self.oracle["candidate_raw_sha256"], EXPECTED)
        self.assertEqual(self.oracle["baseline_raw_sha256"], OLD)
        self.assertEqual(self.oracle["as_of"], "2026-10-23")
        self.assertIn(EXPECTED, RECEIPT.read_text(encoding="utf-8"))
        self.assertIn(EXPECTED, VERIFY.read_text(encoding="utf-8"))

    def test_100_singleton_and_owner_changes(self):
        self.assertEqual(sum(self.cards.values()), 100)
        self.assertEqual(len(self.cards), 98)
        self.assertEqual(len(self.lines), 98)
        for name, qty in self.cards.items():
            self.assertEqual(qty, 2 if name in {"Island", "Swamp"} else 1, name)
        self.assertEqual(set(self.cards) - set(self.baseline), {x for x,_ in SWAPS})
        self.assertEqual(set(self.baseline) - set(self.cards), {y for _,y in SWAPS})
        self.assertTrue(KEEP <= self.cards.keys())
        for name in KEEP:
            self.assertEqual(self.cards[name], self.baseline[name])

    def test_archived_scryfall_identity_and_resources(self):
        self.assertEqual(set(self.cards), set(self.ev))
        self.assertEqual(sum(qty for name, qty in self.cards.items()
                             if "Land" in self.ev[name]["type_line"]), 35)
        self.assertEqual({name for name in self.cards
                          if self.ev[name].get("game_changer")}, GAME_CHANGERS)
        self.assertTrue(ROCKS <= self.cards.keys())
        self.assertEqual(len(ROCKS), 7)
        self.assertEqual(len([name for name in self.cards
                              if "Vehicle" in self.ev[name]["type_line"]]), 13)
        self.assertEqual(len([name for name in self.cards
                              if "Creature" in self.ev[name]["type_line"]
                              and ("Pirate" in self.ev[name]["type_line"]
                                   or "Assassin" in self.ev[name]["type_line"])]), 22)
        for name, qty in self.cards.items():
            ev = self.ev[name]
            self.assertEqual(ev["quantity"], qty)
            self.assertEqual(ev["commander_legality"], "legal", name)
            self.assertTrue(set(ev["color_identity"]) <= set("UBR"), name)
            self.assertTrue(ev.get("oracle_id"), name)
        self.assertEqual(self.oracle["project_exceptions"], [])

    def test_commander_mechanics_as_actual_oracle(self):
        txt = lambda n: self.ev[n]["oracle_text"]
        self.assertIn("At the beginning of your end step", txt(COMMANDER))
        self.assertIn("Whenever a Vehicle you control deals combat damage", txt(COMMANDER))
        self.assertIn("Vehicles you control have flying", txt("Mu Yanling, Wind Rider"))
        self.assertIn("Brotherhood Vertibird's power is equal", txt("Brotherhood Vertibird"))
        self.assertIn("Whenever you create or sacrifice a token", txt("Mirkwood Bats"))
        self.assertIn("cast your second spell each turn", txt("Malcolm, the Eyes"))
        self.assertIn("Whenever Captain Lannery Storm attacks", txt("Captain Lannery Storm"))
        self.assertIn("Whenever an artifact you control enters, draw a card",
                      txt("Fateful Discovery"))

    def test_canonical_authority_and_tracker(self):
        self.assertEqual(len(self.registry["decks"]), 62)
        state = self.registry["decks"][DECK_ID]
        self.assertEqual((state["approval_status"], state["lock_status"],
                          state["current_stage"]), ("APPROVED", "LOCKED", "LOCKED"))
        self.assertTrue(state["final_gate_passed"])
        self.assertEqual(state["approved_list_sha256"], EXPECTED)
        self.assertEqual(state["m7_final_candidate_sha256"], EXPECTED)
        self.assertEqual(state["previous_approved_source_raw_sha256"], OLD)
        self.assertEqual(state["previous_approved_list_artifact"], str(BASELINE.relative_to(ROOT)))
        self.assertEqual(state["approved_list_artifact"], str(APPROVED.relative_to(ROOT)))
        self.assertEqual(state["user_approval_date"], "2026-10-23")
        self.assertEqual(state["m7_power_bracket"], "4 — Optimized")
        self.assertEqual(state["m7_archidekt_tags"], ["Vehicles", "Pirates", "Treasure"])
        self.assertEqual(state["m7_project_exceptions"], [])
        self.assertEqual(len(self.tracker), 62)
        entry = self.tracker[16]
        self.assertEqual(entry["deck_id"], DECK_ID)
        self.assertEqual(entry["final_list_hash"], EXPECTED)
        self.assertEqual(entry["user_approval_date"], "2026-10-23")
        self.assertEqual(entry["final_gate_passed"], "YES")
        self.assertIn("M7 Rev2", entry["refinement_status"])

    def test_sixteen_earlier_owner_locks_untouched(self):
        for deck_id, (expected_sha, path) in PRIOR_16.items():
            entry = self.registry["decks"][deck_id]
            self.assertEqual(entry["approved_list_sha256"], expected_sha, deck_id)
            self.assertEqual(entry["approved_list_artifact"], path, deck_id)
            self.assertEqual(entry["approval_status"], "APPROVED", deck_id)
            self.assertEqual(entry["lock_status"], "LOCKED", deck_id)
            self.assertEqual(digest(ROOT / path), expected_sha, deck_id)

if __name__ == "__main__":
    unittest.main()
