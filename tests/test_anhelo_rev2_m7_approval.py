"""Pin exact owner-authorized Anhelo M7 Rev2 source, state, tracker and predecessor bytes."""
import csv
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW = ROOT / "refinement/decklists/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.txt"
OLD = ROOT / "refinement/decklists/Anhelo_the_Painter_Approval_Ready_2026-10-13.txt"
EXPECTED = "865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77"
OLD_RAW = "8d5f8a9bd4fcdcd164aab63150c14dc69a814a4d9fd764876de3214d3adf9972"
OLD_REG = "d19d94b8a96fb27a760c7b7d9181221f74bd61642d1d1dd7644fc1c59c09839e"
ADDS = ["Forsaken Miner","Skyclave Shade","Sinister Concierge","Case of the Stashed Skeleton","Fable of the Mirror-Breaker // Reflection of Kiki-Jiki","City of Brass","Misty Rainforest"]
CUTS = ["Primal Amulet // Primal Wellspring","Talisman of Indulgence","Fellwar Stone","Maestros Ascendancy","Lagomos, Hand of Hatred","Haunted Ridge","Shipwreck Marsh"]
BASICS = {"Island", "Mountain", "Swamp"}
LANDS = {
    "Badlands", "Blood Crypt", "Bloodstained Mire", "Cascade Bluffs", "City of Brass",
    "Command Tower", "Exotic Orchard", "Island", "Luxury Suite", "Mana Confluence",
    "Misty Rainforest", "Morphic Pool", "Mountain", "Otawara, Soaring City",
    "Polluted Delta", "Scalding Tarn", "Shivan Reef", "Steam Vents", "Stormcarved Coast",
    "Sulfur Falls", "Swamp", "Training Center", "Undercity Sewers", "Underground Sea",
    "Urborg, Tomb of Yawgmoth", "Volcanic Island", "Watery Grave", "Xander's Lounge",
}
ROCKS = {"Arcane Signet", "Dimir Signet", "Izzet Signet", "Rakdos Signet", "Sol Ring",
         "Talisman of Creativity", "Talisman of Dominance"}

def counts(path):
    out = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        count, name = line.split("x ", 1)
        assert count.isdecimal() and int(count) > 0, line
        out[name.removesuffix(" [Commander]")] += int(count)
    return lines, out

class AnheloRev2M7ApprovalTests(unittest.TestCase):
    def test_source_bytes_physical_singleton_and_mana(self):
        self.assertEqual(hashlib.sha256(NEW.read_bytes()).hexdigest(), EXPECTED)
        lines, ct = counts(NEW)
        self.assertEqual(lines[0], "1x Anhelo, the Painter [Commander]")
        self.assertEqual((len(lines), len(ct), sum(ct.values())), (94, 94, 100))
        self.assertEqual(sum("[Commander]" in line for line in lines), 1)
        self.assertEqual(ct["Anhelo, the Painter"], 1)
        self.assertEqual({n:q for n,q in ct.items() if q > 1},
                         {"Island": 3, "Mountain": 3, "Swamp": 3})
        self.assertTrue(all(q == 1 or n in BASICS for n, q in ct.items()))
        self.assertEqual(sum(ct[n] for n in LANDS), 34)
        self.assertEqual(sum(ct[n] for n in ROCKS), 7)
        self.assertIn("Feed the Swarm", ct)
        self.assertIn("Forsaken Miner", ct)
        self.assertIn("Fable of the Mirror-Breaker // Reflection of Kiki-Jiki", ct)

    def test_seven_exact_one_for_one_changes_and_untouched_old_bytes(self):
        self.assertEqual(hashlib.sha256(OLD.read_bytes()).hexdigest(), OLD_RAW)
        _, before = counts(OLD)
        _, after = counts(NEW)
        self.assertEqual(set((after-before).elements()), set(ADDS))
        self.assertEqual(set((before-after).elements()), set(CUTS))
        self.assertEqual(sum((after-before).values()), 7)
        self.assertEqual(sum((before-after).values()), 7)

    def test_registry_and_tracker_scoped_owner_authority(self):
        state = json.loads((ROOT/"state/current_deck_overrides.json").read_text(encoding="utf-8"))
        self.assertEqual(len(state["decks"]), 62)
        x = state["decks"]["Anhelo_the_Painter"]
        for k,v in (("approved_list_sha256", EXPECTED), ("m7_final_candidate_sha256", EXPECTED),
                    ("user_approval_date","2026-10-23"), ("approved_list_artifact",str(NEW.relative_to(ROOT))),
                    ("previous_approved_list_sha256",OLD_REG), ("previous_approved_source_raw_sha256",OLD_RAW)):
            self.assertEqual(x[k],v,k)
        self.assertEqual((x["approval_status"],x["lock_status"],x["current_stage"]),
                         ("APPROVED","LOCKED","LOCKED"))
        self.assertTrue(x["final_gate_passed"])
        with (ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
            encoding="utf-8", newline=""
        ) as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows),62)
        self.assertEqual(rows[3]["deck_id"],"Anhelo__the_Painter")
        self.assertEqual(rows[3]["final_list_hash"],EXPECTED)
        self.assertEqual(rows[3]["user_approval_date"],"2026-10-23")
        self.assertIn("APPROVED / LOCKED",rows[3]["refinement_status"])
        previous = {
            "Abaddon_the_Despoiler":"5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
            "Admiral_Beckett_Brass":"ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
            "Admiral_Brass__Unsinkable":"dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
        }
        for key,locked in previous.items():
            self.assertEqual(state["decks"][key]["approved_list_sha256"],locked,key)

    def test_receipts_provenance_and_scope(self):
        a=(ROOT/"refinement/approvals/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.md").read_text(encoding="utf-8")
        v=(ROOT/"refinement/verification/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23_Verification.md").read_text(encoding="utf-8")
        for body in (a,v):
            for digest in (EXPECTED, OLD_RAW, OLD_REG):
                self.assertIn(digest,body)
            self.assertIn("M6.10",body)
        self.assertIn("I explicitly approve and authorize canonical locking",a)
        for name in ADDS: self.assertIn(name,a)

if __name__ == "__main__":
    unittest.main()
