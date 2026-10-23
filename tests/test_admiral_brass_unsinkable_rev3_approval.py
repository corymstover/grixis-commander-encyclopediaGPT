"""Pin exact owner-approved Admiral Brass, Unsinkable M7 Rev3 canonical bytes and predecessor."""
import csv
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = "Admiral_Brass__Unsinkable"
NEW = ROOT / "refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt"
OLD = ROOT / "refinement/decklists/Admiral_Brass_Unsinkable_Whole_List_Approval_Candidate_2026-10-13.txt"
EXPECTED = "dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7"
OLD_RAW = "056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc"
OLD_REGISTRY = "e66e3a59719401f41830e9938997a87a45a1b0dcaa0663b0ec7b44e10077dd39"
ADDS = {"Kitesail Larcenist", "Timestream Navigator", "Warkite Marauder",
        "Jhoira, Weatherlight Corsair", "Siren's Ruse", "Ripples of Undeath",
        "Thassa, Deep-Dwelling", "City of Brass"}
CUTS = {"Enterprising Scallywag", "Francisco, Fowl Marauder", "Fathom Fleet Captain",
        "Pitiless Plunderer", "Crumbling Necropolis", "Forerunner of the Coalition",
        "Wonder", "Path of Ancestry"}
LANDS = {"Ancient Tomb", "Badlands", "Blood Crypt", "Bloodstained Mire",
         "Cavern of Souls", "City of Brass", "Command Tower", "Drowned Catacomb",
         "Exotic Orchard", "Island", "Luxury Suite", "Mana Confluence",
         "Morphic Pool", "Mountain", "Otawara, Soaring City", "Polluted Delta",
         "Scalding Tarn", "Secluded Courtyard", "Shipwreck Marsh",
         "Smoldering Marsh", "Steam Vents", "Stormcarved Coast", "Sulfur Falls",
         "Swamp", "Training Center", "Underground River", "Underground Sea",
         "Volcanic Island", "Watery Grave", "Xander's Lounge"}
BASICS = {"Island", "Mountain", "Swamp"}

def normalized(name):
    return name.replace("Brass's Tunnel-Grinder // Tecutlan, the Searing Rift",
                        "Brass's Tunnel-Grinder")

def physical(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    counts = Counter()
    for line in lines:
        quantity, name = line.split("x ", 1)
        assert quantity.isdecimal() and int(quantity) > 0, line
        counts[normalized(name.removesuffix(" [Commander]"))] += int(quantity)
    return lines, counts

class AdmiralBrassUnsinkableRev3ApprovalTests(unittest.TestCase):
    def test_exact_source_and_singleton_mana_commander(self):
        self.assertEqual(hashlib.sha256(NEW.read_bytes()).hexdigest(), EXPECTED)
        lines, counts = physical(NEW)
        self.assertEqual(lines[0], "1x Admiral Brass, Unsinkable [Commander]")
        self.assertEqual(len(lines), 97)
        self.assertEqual(len(counts), 97)
        self.assertEqual(sum(counts.values()), 100)
        self.assertEqual(counts["Admiral Brass, Unsinkable"], 1)
        self.assertEqual(sum("[Commander]" in line for line in lines), 1)
        self.assertEqual({n:q for n,q in counts.items() if q > 1},
                         {"Island":2, "Mountain":2, "Swamp":2})
        self.assertTrue(all(q == 1 or n in BASICS for n,q in counts.items()))
        self.assertEqual(sum(counts[n] for n in LANDS), 33)
        self.assertIn("1x Faithless Looting", lines)
        self.assertIn("1x Changeling Outcast", lines)
        self.assertIn("1x Mary Read and Anne Bonny", lines)
        self.assertIn("1x Power Conduit", lines)

    def test_eight_real_swaps_and_historical_provenance_exception(self):
        self.assertEqual(hashlib.sha256(OLD.read_bytes()).hexdigest(), OLD_RAW)
        _, before = physical(OLD)
        _, after = physical(NEW)
        self.assertEqual(set((after-before).elements()), ADDS)
        self.assertEqual(set((before-after).elements()), CUTS)
        self.assertEqual(sum((after-before).values()), 8)
        self.assertEqual(sum((before-after).values()), 8)
        self.assertIn("Brass's Tunnel-Grinder", before)
        self.assertIn("Brass's Tunnel-Grinder", after)

    def test_registry_tracker_match_explicit_owner_approval(self):
        state = json.loads((ROOT/"state/current_deck_overrides.json").read_text(encoding="utf-8"))
        self.assertEqual(len(state["decks"]), 62)
        x = state["decks"][DECK]
        for key, value in (("approved_list_sha256",EXPECTED),
                           ("m7_final_candidate_sha256",EXPECTED),
                           ("user_approval_date","2026-10-23"),
                           ("previous_approved_list_sha256",OLD_REGISTRY),
                           ("previous_approved_source_raw_sha256",OLD_RAW),
                           ("approved_list_artifact",str(NEW.relative_to(ROOT)))):
            self.assertEqual(x[key], value, key)
        self.assertEqual((x["approval_status"],x["lock_status"]),("APPROVED","LOCKED"))
        self.assertTrue(x["final_gate_passed"])
        self.assertEqual(sum(z["approval_status"]=="APPROVED" and z["lock_status"]=="LOCKED"
                             for z in state["decks"].values()),62)
        with (ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
            encoding="utf-8",newline=""
        ) as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),62)
        self.assertEqual(rows[2]["deck_id"],DECK)
        self.assertEqual(rows[2]["final_list_hash"],EXPECTED)
        self.assertEqual(rows[2]["user_approval_date"],"2026-10-23")
        self.assertIn("APPROVED / LOCKED",rows[2]["refinement_status"])
        self.assertEqual(state["decks"]["Abaddon_the_Despoiler"]["approved_list_sha256"],
                         "5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24")
        self.assertEqual(state["decks"]["Admiral_Beckett_Brass"]["approved_list_sha256"],
                         "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000")

    def test_receipts_owner_quote_and_scope(self):
        approval = (ROOT/"refinement/approvals/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.md").read_text(encoding="utf-8")
        verify = (ROOT/"refinement/verification/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23_Verification.md").read_text(encoding="utf-8")
        for content in (approval,verify):
            self.assertIn(EXPECTED,content)
            self.assertIn(OLD_REGISTRY,content)
            self.assertIn(OLD_RAW,content)
            self.assertIn("M6.10",content)
        self.assertIn("I explicitly approve and authorize canonical locking",approval)
        for name in ADDS:
            self.assertIn(name,approval)

if __name__ == "__main__":
    unittest.main()
