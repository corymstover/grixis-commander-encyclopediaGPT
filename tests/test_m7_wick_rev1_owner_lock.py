#!/usr/bin/env python3
"""Deck #61: exact owner-approved M7 Wick bytes, registry, tracker and case scope."""
import csv
import hashlib
import json
import os
import subprocess
import unittest
from collections import Counter
from pathlib import Path

from scripts import verify_m7_certification_transfer as transfer

ROOT = Path(__file__).resolve().parents[1]
KEY = "Wick__the_Whorled_Mind"
OLD_SHA = "f4556840dc8f7a8e1d532b73652d0035592b52b86adbbad6ed8fbe4270341e98"
NEW_SHA = "1aea08a53b983ee9ce083c1e9c95b366a3abc478a43b75517714d6280b484c48"
ORIGINAL = ROOT / "refinement/decklists/Wick_the_Whorled_Mind_Approved_2026-10-15.txt"
NEW_REL = "refinement/decklists/Wick_the_Whorled_Mind_M7_Rev1_Approved_2026-10-27.txt"
NEW = ROOT / NEW_REL
RECEIPT = ROOT / "refinement/approvals/Wick_the_Whorled_Mind_M7_Rev1_Approved_2026-10-27.md"
CASES = ROOT / "refinement/verification/m7_certification_transfer/Wick__the_Whorled_Mind_1aea08a53b983ee9.json"
SWAPS = {
    "Rank Rat": "Tangled Colony",
    "Azure Beastbinder": "Persistent Marshstalker",
    "Yawgmoth, Thran Physician": "Totentanz, Swarm Piper",
    "Swarmyard Massacre": "Blasphemous Act",
    "Beseech the Mirror": "Plumb the Forbidden",
    "Malakir Rebirth // Malakir Mire": "Swarmyard",
    "Misty Rainforest": "Shipwreck Marsh",
    "Verdant Catacombs": "Haunted Ridge",
    "Wooded Foothills": "Stormcarved Coast",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def physical(path):
    rows=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        qty,name=line.split("x ",1)
        rows.append((int(qty),name.removesuffix(" [Commander]")))
    return Counter({name:qty for qty,name in rows}),rows


class WickM7OwnerApproval(unittest.TestCase):
    def test_01_source_sha_and_real_nine_changes(self):
        self.assertEqual(digest(ORIGINAL),OLD_SHA)
        self.assertEqual(digest(NEW),NEW_SHA)
        old,_=physical(ORIGINAL)
        new,rows=physical(NEW)
        self.assertEqual(rows[0],(1,"Wick, the Whorled Mind"))
        self.assertEqual(sum(q for q,_ in rows),100)
        self.assertEqual(len(new),99)
        self.assertEqual({k:v for k,v in new.items() if v>1},{"Island":2})
        self.assertEqual(new-old,Counter(SWAPS.keys()))
        self.assertEqual(old-new,Counter(SWAPS.values()))

    def test_02_current_authority_and_tracker(self):
        all_decks=json.loads((ROOT/"state/current_deck_overrides.json").read_text())["decks"]
        record=all_decks[KEY]
        self.assertEqual(len(all_decks),62)
        self.assertEqual(record["approved_list_sha256"],NEW_SHA)
        self.assertEqual(record["previous_approved_list_sha256"],OLD_SHA)
        self.assertEqual(record["approved_list_artifact"],NEW_REL)
        self.assertEqual(record["approval_status"],"APPROVED")
        self.assertEqual(record["lock_status"],"LOCKED")
        self.assertTrue(record["final_gate_passed"])
        with (ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(newline="",encoding="utf-8") as f:
            tracker={x["deck_id"]:x for x in csv.DictReader(f)}
        self.assertEqual(tracker[KEY]["final_list_hash"],NEW_SHA)
        self.assertEqual(tracker[KEY]["user_approval_date"],"2026-10-27")
        self.assertEqual(tracker[KEY]["final_gate_passed"],"YES")

    def test_03_owner_receipt_and_fourteen_cases(self):
        receipt=RECEIPT.read_text(encoding="utf-8")
        self.assertIn("> Approve",receipt)
        self.assertIn(NEW_SHA,receipt)
        self.assertIn(OLD_SHA,receipt)
        self.assertIn("40621910172",receipt)
        plan=json.loads((ROOT/transfer.PLANS).read_text())["decks"][KEY]
        proposed=json.loads(CASES.read_text())
        self.assertEqual(proposed["approved_raw_sha256"],NEW_SHA)
        self.assertEqual([x["case_id"] for x in proposed["m6_transfer"]["P0"]],plan["required_P0"])
        self.assertEqual([x["case_id"] for x in proposed["m6_transfer"]["P1"]],plan["required_P1"])
        authority=json.loads((ROOT/transfer.REGISTRY).read_text())["decks"][KEY]
        transfer.validate_attestation(ROOT,KEY,authority,plan,proposed)

    def test_04_other_61_authority_records_unchanged(self):
        baseline=os.environ.get("BASE_REF_SHA")
        if baseline is None:
            self.skipTest("Exact base comparison is enforced in the dedicated Wick PR workflow")
        from m7_approved_supersession import assert_other_decks_preserved
        assert_other_decks_preserved(self, ROOT, baseline, KEY)


if __name__=="__main__":
    unittest.main()
