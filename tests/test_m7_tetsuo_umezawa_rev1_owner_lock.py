#!/usr/bin/env python3
"""Exact owner lock for Deck #54 Tetsuo Umezawa M7 Rev1; no aggregate recertification."""
import csv
import hashlib
import json
import os
import subprocess
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEY = "Tetsuo_Umezawa"
OLD_SHA = "14ca66ceae4d634630a85aa1787731cfe840fd9fc2093bc37ad5dc17d1539ff6"
NEW_SHA = "e00196135931bde6e380e47d5ffe9e4360d4756f00ad083ee5ed0757919fddd7"
ORIGINAL = ROOT / "refinement/decklists/Tetsuo_Umezawa_Approved_2026-10-15.txt"
FINAL_REL = "refinement/decklists/Tetsuo_Umezawa_M7_Rev1_Approved_2026-10-27.txt"
FINAL = ROOT / FINAL_REL
SWAPS = [
    ("Rings of Brighthearth", "Battlemage's Bracers"),
    ("Mountain", "City of Brass"),
    ("Propaganda", "Deflecting Swat"),
    ("Dark Ritual", "Dramatic Reversal"),
    ("Counterspell", "Fierce Guardianship"),
    ("Sulfur Falls", "Forbidden Orchard"),
    ("Geode Rager", "Icy Manipulator"),
    ("Brainstorm", "Isochron Scepter"),
    ("Fumiko the Lowblood", "Life of the Party"),
    ("Mountain", "Mana Confluence"),
    ("Island", "Morphic Pool"),
    ("Island", "Otawara, Soaring City"),
    ("Sly Instigator", "Puppet Strings"),
    ("Xantcha, Sleeper Agent", "Rhystic Study"),
    ("Swamp", "Takenuma, Abandoned Mire"),
    ("Grenzo, Havoc Raiser", "Thornbite Staff"),
    ("Blasphemous Act", "Toxic Deluge"),
    ("Urabrask the Hidden", "Uphill Battle"),
    ("Swamp", "Urborg, Tomb of Yawgmoth"),
]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def physical(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        count, name = line.split("x ", 1)
        rows.append((int(count), name.removesuffix(" [Commander]")))
    return Counter({name: count for count, name in rows}), rows

class TetsuoM7OwnerLock(unittest.TestCase):
    def test_original_preserved_and_exact_new_hash(self):
        self.assertEqual(digest(ORIGINAL), OLD_SHA)
        self.assertEqual(digest(FINAL), NEW_SHA)

    def test_physical_100_and_exact_nineteen_swaps(self):
        before, previous_rows = physical(ORIGINAL)
        after, rows = physical(FINAL)
        self.assertEqual(rows[0], (1, "Tetsuo Umezawa"))
        self.assertEqual(sum(count for count, _ in rows), 100)
        self.assertEqual(len(after), 93)
        self.assertEqual({name: count for name, count in after.items() if count > 1},
                         {"Island": 3, "Mountain": 3, "Swamp": 4})
        self.assertEqual(before - after, Counter(x for x, _ in SWAPS))
        self.assertEqual(after - before, Counter(y for _, y in SWAPS))
        self.assertEqual(sum((before - after).values()), 19)
        self.assertEqual(sum((after - before).values()), 19)

    def test_authority_and_tracker_exact_match(self):
        state = json.loads((ROOT / "state/current_deck_overrides.json").read_text(encoding="utf-8"))
        record = state["decks"][KEY]
        self.assertEqual(record["approved_list_sha256"], NEW_SHA)
        self.assertEqual(record["previous_approved_list_sha256"], OLD_SHA)
        self.assertEqual(record["approval_status"], "APPROVED")
        self.assertEqual(record["lock_status"], "LOCKED")
        self.assertTrue(record["final_gate_passed"])
        self.assertEqual(record["approved_list_artifact"], FINAL_REL)
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(newline="", encoding="utf-8") as file:
            tracker = {r["deck_id"]: r for r in csv.DictReader(file)}
        self.assertEqual(tracker[KEY]["final_list_hash"], NEW_SHA)
        self.assertEqual(tracker[KEY]["user_approval_date"], "2026-10-27")
        self.assertEqual(tracker[KEY]["final_gate_passed"], "YES")

    def test_receipts_contain_exact_hashes_and_certification(self):
        state = json.loads((ROOT / "state/current_deck_overrides.json").read_text(encoding="utf-8"))
        record = state["decks"][KEY]
        for field in ("approval_record_artifact", "verification_artifact"):
            body = (ROOT / record[field]).read_text(encoding="utf-8")
            self.assertIn(NEW_SHA, body)
            self.assertIn(OLD_SHA, body)
            self.assertIn("40576836188", body)
            self.assertIn("40576836147", body)

    def test_other_61_authorities_preserved(self):
        base = os.environ.get("BASE_REF_SHA")
        if not base:
            self.skipTest("PR-base-only invariant: dedicated approval workflow supplies BASE_REF_SHA")
        self.assertTrue(base and len(base) == 40, "Exact PR base SHA required")
        historical = json.loads(subprocess.check_output(
            ["git", "show", f"{base}:state/current_deck_overrides.json"], cwd=ROOT))
        current = json.loads((ROOT / "state/current_deck_overrides.json").read_text(encoding="utf-8"))
        self.assertEqual(set(current["decks"]), set(historical["decks"]))
        for name, entry in historical["decks"].items():
            if name != KEY:
                now = current["decks"][name]
                if name == "Wick__the_Whorled_Mind":
                    # The separate owner-approved Deck #61 revision is a
                    # SHA-bound exception, not an unrestricted other-deck edit.
                    old = "f4556840dc8f7a8e1d532b73652d0035592b52b86adbbad6ed8fbe4270341e98"
                    new = "1aea08a53b983ee9ce083c1e9c95b366a3abc478a43b75517714d6280b484c48"
                    self.assertEqual(entry["approved_list_sha256"], old)
                    self.assertEqual(now["approved_list_sha256"], new)
                    self.assertEqual(now["previous_approved_list_sha256"], old)
                    self.assertEqual(now["m7_final_candidate_sha256"], new)
                    self.assertEqual(now["approval_status"], "APPROVED")
                    self.assertEqual(now["lock_status"], "LOCKED")
                    self.assertEqual(hashlib.sha256((ROOT / now["approved_list_artifact"]).read_bytes()).hexdigest(), new)
                    self.assertEqual(hashlib.sha256((ROOT / now["previous_approved_list_artifact"]).read_bytes()).hexdigest(), old)
                    receipt = (ROOT / now["approval_record_artifact"]).read_text(encoding="utf-8")
                    self.assertIn(new, receipt)
                    self.assertIn(old, receipt)
                    continue
                # Non-card certification repairs may adjust metadata. Preserve
                # exact owner approval, strategy basis, SHA and source bytes.
                for field in ("approved_list_sha256", "approval_status", "lock_status",
                              "approval_basis", "user_approval_date", "m7_final_candidate_sha256"):
                    self.assertEqual(now.get(field), entry.get(field), (name, field))
                source = ROOT / now["approved_list_artifact"]
                self.assertTrue(source.is_file(), name)
                self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),
                                 entry["approved_list_sha256"], name)

if __name__ == "__main__":
    unittest.main()
