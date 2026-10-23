"""Abaddon Rev3 exact owner-authorized canonical replacement and preservation guards."""
import collections
import csv
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
REV2 = ROOT / "refinement/decklists/Abaddon_the_Despoiler_M7_Approved_2026-10-22.txt"
REV3 = ROOT / "refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt"
STATE = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
OWNER = ROOT / "refinement/approvals/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.md"
VERIFY = ROOT / "refinement/verification/Abaddon_the_Despoiler_M7_Rev3_Approval_Verification_2026-10-23.md"
OLD_SHA = "0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790"
NEW_SHA = "5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24"
ADMIRAL_SHA = "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000"

def physical(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    self_copy = collections.Counter()
    for ln in lines:
        if not ln or not ln[0].isdigit() or "x " not in ln:
            raise AssertionError(f"Malformed source line: {ln!r}")
        n, name = ln.split("x ", 1)
        name = name.removesuffix(" [Commander]")
        self_copy[name] += int(n)
    return lines, self_copy

class AbaddonRev3CanonicalApprovalTests(unittest.TestCase):
    def test_hash_bytes_and_immutable_rev2(self):
        self.assertEqual(hashlib.sha256(REV3.read_bytes()).hexdigest(), NEW_SHA)
        self.assertEqual(hashlib.sha256(REV2.read_bytes()).hexdigest(), OLD_SHA)
        self.assertTrue(REV3.read_bytes().endswith(b"\\n"))
        self.assertFalse(b"\\r" in REV3.read_bytes())

    def test_one_commander_100_cards_95_names_and_singleton(self):
        lines, counts = physical(REV3)
        self.assertEqual(lines[0], "1x Abaddon the Despoiler [Commander]")
        self.assertEqual(sum(counts.values()), 100)
        self.assertEqual(len(counts), 95)
        self.assertEqual(counts["Abaddon the Despoiler"], 1)
        self.assertEqual({k: v for k, v in counts.items() if v > 1},
                         {"Island": 3, "Mountain": 2, "Swamp": 3})
        self.assertEqual(len([x for x in lines if "[Commander]" in x]), 1)

    def test_six_exact_authorized_deltas(self):
        _, old = physical(REV2)
        _, new = physical(REV3)
        self.assertEqual(new-old, collections.Counter({
            "Impact Tremors": 1, "Sanctum of Stone Fangs": 1,
            "Coruscation Mage": 1, "Sakashima of a Thousand Faces": 1,
            "Mount Doom": 1, "Sheoldred, the Apocalypse": 1
        }))
        self.assertEqual(old-new, collections.Counter({
            "Thermo-Alchemist": 1, "The Ruinous Powers": 1,
            "Kessig Flamebreather": 1, "Keeper of Secrets": 1,
            "Mountain": 1, "Ponder": 1
        }))
        for name in ("Noise Marine", "Nalfeshnee", "Call Forth the Tempest",
                     "The Lost and the Damned", "Aggravated Assault",
                     "Nightscape Familiar", "Grinning Ignus",
                     "Birgi, God of Storytelling // Harnfel, Horn of Bounty"):
            self.assertEqual(new[name], 1)

    def test_canonical_62_state_and_other_lock_preservation(self):
        registry = json.loads(STATE.read_text(encoding="utf-8"))
        self.assertEqual(len(registry["decks"]), 62)
        abaddon = registry["decks"]["Abaddon_the_Despoiler"]
        self.assertEqual(abaddon["approval_status"], "APPROVED")
        self.assertEqual(abaddon["lock_status"], "LOCKED")
        self.assertTrue(abaddon["final_gate_passed"])
        self.assertEqual(abaddon["approved_list_sha256"], NEW_SHA)
        self.assertEqual(abaddon["m7_final_candidate_sha256"], NEW_SHA)
        self.assertEqual(abaddon["user_approval_date"], "2026-10-23")
        self.assertEqual(abaddon["previous_approved_list_sha256"], OLD_SHA)
        self.assertEqual(abaddon["approved_list_artifact"], str(REV3.relative_to(ROOT)))
        admiral = registry["decks"]["Admiral_Beckett_Brass"]
        self.assertEqual(admiral["approved_list_sha256"], ADMIRAL_SHA)
        self.assertEqual(admiral["approval_status"], "APPROVED")
        self.assertEqual(admiral["lock_status"], "LOCKED")

    def test_tracker_matches_authority_and_61_decks_unrevised(self):
        with TRACKER.open(encoding="utf-8", newline="") as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(len(rows), 62)
        self.assertEqual(rows[0]["deck_id"], "Abaddon_the_Despoiler")
        self.assertEqual(rows[0]["final_list_hash"], NEW_SHA)
        self.assertEqual(rows[0]["user_approval_date"], "2026-10-23")
        self.assertIn("Rev3", rows[0]["refinement_status"])
        self.assertEqual(rows[1]["deck_id"], "Admiral_Beckett_Brass")
        self.assertEqual(rows[1]["final_list_hash"], ADMIRAL_SHA)

    def test_owner_receipt_and_source_scoped_milestone_boundary(self):
        approval = OWNER.read_text(encoding="utf-8")
        verification = VERIFY.read_text(encoding="utf-8")
        for document in (approval, verification):
            self.assertIn(NEW_SHA, document)
            self.assertIn(OLD_SHA, document)
            self.assertIn("2026-10-23", document)
            self.assertIn("Cascade", document)
            self.assertIn("Exile Cast", document)
        self.assertIn("explicitly", approval)
        self.assertIn("61", approval)
        self.assertIn("M6.10", approval)
        self.assertIn("M8", verification)

if __name__ == "__main__":
    unittest.main()
