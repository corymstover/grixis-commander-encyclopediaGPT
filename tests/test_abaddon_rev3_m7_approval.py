"""Bind owner-authorized Abaddon Rev3 canonical approval to one physical immutable source."""
import csv
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = "Abaddon_the_Despoiler"
NEW = ROOT / "refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt"
REV2 = ROOT / "refinement/decklists/Abaddon_the_Despoiler_M7_Approved_2026-10-22.txt"
OCT13 = ROOT / "refinement/decklists/Abaddon_the_Despoiler_Approved_2026-10-13.txt"
EXPECTED = "5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24"
REV2_HASH = "0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790"
OCT13_HASH = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
ADDS = {"Impact Tremors", "Sanctum of Stone Fangs", "Coruscation Mage",
        "Sakashima of a Thousand Faces", "Mount Doom", "Sheoldred, the Apocalypse"}
CUTS = {"Thermo-Alchemist", "The Ruinous Powers", "Kessig Flamebreather",
        "Keeper of Secrets", "Mountain", "Ponder"}
BASICS = {"Island", "Mountain", "Swamp"}
LANDS = {
    "Ancient Tomb", "Badlands", "Blood Crypt", "Bloodstained Mire",
    "City of Brass", "Command Tower", "Exotic Orchard", "Flooded Strand",
    "Island", "Luxury Suite", "Mana Confluence", "Marsh Flats",
    "Misty Rainforest", "Morphic Pool", "Mountain", "Mount Doom",
    "Otawara, Soaring City", "Polluted Delta", "Scalding Tarn",
    "Steam Vents", "Swamp", "Takenuma, Abandoned Mire", "Training Center",
    "Underground Sea", "Urborg, Tomb of Yawgmoth", "Verdant Catacombs",
    "Volcanic Island", "Watery Grave", "Xander's Lounge",
}

def physical(path):
    counter = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        amount, name = line.split("x ", 1)
        assert amount.isdecimal() and int(amount) > 0, line
        name = name.removesuffix(" [Commander]")
        counter[name] += int(amount)
    return lines, counter

class AbaddonRev3ApprovalTests(unittest.TestCase):
    def test_exact_approved_source_100_singleton_lands_commander(self):
        self.assertEqual(hashlib.sha256(NEW.read_bytes()).hexdigest(), EXPECTED)
        lines, counts = physical(NEW)
        self.assertEqual(lines[0], "1x Abaddon the Despoiler [Commander]")
        self.assertEqual(sum(counts.values()), 100)
        self.assertEqual(len(counts), 95)
        self.assertEqual(counts["Abaddon the Despoiler"], 1)
        self.assertEqual(sum(counts[n] for n in LANDS), 34)
        self.assertEqual({n: q for n, q in counts.items() if q > 1},
                         {"Island": 3, "Mountain": 2, "Swamp": 3})
        self.assertTrue(all(q == 1 or n in BASICS for n, q in counts.items()))
        self.assertEqual(sum("[Commander]" in line for line in lines), 1)

    def test_exactly_six_replacements_and_immutable_predecessors(self):
        self.assertEqual(hashlib.sha256(REV2.read_bytes()).hexdigest(), REV2_HASH)
        self.assertEqual(hashlib.sha256(OCT13.read_bytes()).hexdigest(), OCT13_HASH)
        _, current = physical(NEW)
        _, previous = physical(REV2)
        self.assertEqual(set((current - previous).elements()), ADDS)
        self.assertEqual(set((previous - current).elements()), CUTS)
        self.assertEqual(sum((current - previous).values()), 6)
        self.assertEqual(sum((previous - current).values()), 6)

    def test_canonical_62_state_and_tracker_only_abaddon_supersession(self):
        state = json.loads((ROOT / "state/current_deck_overrides.json").read_text(encoding="utf-8"))
        self.assertEqual(len(state["decks"]), 62)
        entry = state["decks"][DECK]
        self.assertEqual(entry["approval_status"], "APPROVED")
        self.assertEqual(entry["lock_status"], "LOCKED")
        self.assertTrue(entry["final_gate_passed"])
        self.assertEqual(entry["approved_list_sha256"], EXPECTED)
        self.assertEqual(entry["m7_final_candidate_sha256"], EXPECTED)
        self.assertEqual(entry["user_approval_date"], "2026-10-23")
        self.assertEqual(entry["previous_approved_list_sha256"], REV2_HASH)
        self.assertEqual(entry["previous_approved_list_artifact"], str(REV2.relative_to(ROOT)))
        self.assertEqual(entry["approved_list_artifact"], str(NEW.relative_to(ROOT)))
        self.assertEqual(entry["approval_record_artifact"],
                         "refinement/approvals/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.md")
        self.assertEqual(sum(v["approval_status"] == "APPROVED" and v["lock_status"] == "LOCKED"
                             for v in state["decks"].values()), 62)
        self.assertEqual(state["decks"]["Admiral_Beckett_Brass"]["approved_list_sha256"],
                         "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000")
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 62)
        self.assertEqual(rows[0]["deck_id"], DECK)
        self.assertEqual(rows[0]["final_list_hash"], EXPECTED)
        self.assertEqual(rows[0]["user_approval_date"], "2026-10-23")
        self.assertIn("APPROVED / LOCKED", rows[0]["refinement_status"])
        self.assertEqual(rows[1]["deck_id"], "Admiral_Beckett_Brass")
        self.assertEqual(rows[1]["final_list_hash"],
                         "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000")

    def test_explicit_owner_scope_and_source_evidence(self):
        approval = (ROOT / "refinement/approvals/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.md").read_text(encoding="utf-8")
        verification = (ROOT / "refinement/verification/Abaddon_the_Despoiler_M7_Rev3_Approval_Verification_2026-10-23.md").read_text(encoding="utf-8")
        self.assertIn("I explicitly approve and authorize locking Abaddon the Despoiler Rev3", approval)
        for text in (approval, verification):
            self.assertIn(EXPECTED, text)
            self.assertIn(REV2_HASH, text)
            self.assertIn("M6.10", text)
        for card in ADDS:
            self.assertIn(card, approval)
        self.assertIn("M7", verification)
        self.assertIn("95", verification)

if __name__ == "__main__":
    unittest.main()
