#!/usr/bin/env python3
"""Deck #62: exact Zevlor M7 Rev1 owner-approved SHA and immutable other 61."""
import csv
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import subprocess
import unittest

from scripts import verify_m7_certification_transfer as transfer

ROOT = Path(__file__).resolve().parents[1]
KEY = "Zevlor__Elturel_Exile"
OLD_SHA = "d2ea6ed8e42ec512b6a6ae7162da8c17b26494b45a9ff6d0c38882c202a42dc9"
NEW_SHA = "071e9a8b9eaa0f2cfad65f4e7ef05cc5cf0a8b5f74f2221c75d68e6c4dd1bb8f"
ORIGINAL = ROOT / "refinement/decklists/Zevlor_Elturel_Exile_Approved_2026-10-15.txt"
NEW_REL = "refinement/decklists/Zevlor_Elturel_Exile_M7_Rev1_Approved_2026-10-27.txt"
NEW = ROOT / NEW_REL
RECEIPT = ROOT / "refinement/approvals/Zevlor_Elturel_Exile_M7_Rev1_Approved_2026-10-27.md"
CASES = ROOT / "refinement/verification/m7_certification_transfer/Zevlor__Elturel_Exile_071e9a8b9eaa0f2c.json"
LEDGER = ROOT / "refinement/decisions/Zevlor_Elturel_Exile_M7_Rev1_Whole99_Audit_2026-10-27.csv"
SWAPS = {
    "End of the Hunt": "Abrade",
    "Strategic Betrayal": "Terminate",
    "Gifts Ungiven": "Gamble",
    "Rousing Refrain": "Dark Ritual",
    "Traumatic Critique": "Portent",
    "Cruelclaw's Heist": "Counterspell",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def physical(path: Path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        qty, name = line.split("x ", 1)
        rows.append((int(qty), name.removesuffix(" [Commander]")))
    return Counter({name: qty for qty, name in rows}), rows


class ZevlorM7Rev1OwnerLock(unittest.TestCase):
    def test_01_exact_raw_100_original_immutable_and_six_swaps(self):
        self.assertEqual(sha(ORIGINAL), OLD_SHA)
        self.assertEqual(sha(NEW), NEW_SHA)
        before, _ = physical(ORIGINAL)
        after, rows = physical(NEW)
        self.assertEqual(rows[0], (1, "Zevlor, Elturel Exile"))
        self.assertEqual(sum(q for q, _ in rows), 100)
        self.assertEqual(len(after), 97)
        self.assertEqual({n: q for n, q in after.items() if q > 1},
                         {"Island": 2, "Mountain": 2, "Swamp": 2})
        self.assertEqual(after - before, Counter(SWAPS.keys()))
        self.assertEqual(before - after, Counter(SWAPS.values()))

    def test_02_exact_registry_tracker_and_99_physical_slots(self):
        state = json.loads((ROOT / "state/current_deck_overrides.json").read_text())["decks"]
        self.assertEqual(len(state), 62)
        actual = state[KEY]
        self.assertEqual(actual["approved_list_sha256"], NEW_SHA)
        self.assertEqual(actual["previous_approved_list_sha256"], OLD_SHA)
        self.assertEqual(actual["approved_list_artifact"], NEW_REL)
        self.assertEqual(actual["approval_status"], "APPROVED")
        self.assertEqual(actual["lock_status"], "LOCKED")
        self.assertTrue(actual["final_gate_passed"])
        self.assertEqual(actual["user_approval_date"], "2026-10-27")
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
            newline="", encoding="utf-8"
        ) as handle:
            tracker = {row["deck_id"]: row for row in csv.DictReader(handle)}
        self.assertEqual(len(tracker), 62)
        self.assertEqual(tracker[KEY]["final_list_hash"], NEW_SHA)
        self.assertEqual(tracker[KEY]["user_approval_date"], "2026-10-27")
        self.assertEqual(tracker[KEY]["final_gate_passed"], "YES")
        with LEDGER.open(newline="", encoding="utf-8") as handle:
            ledger = list(csv.DictReader(handle))
        self.assertEqual(sum(int(row["quantity"]) for row in ledger), 99)
        self.assertEqual({row["baseline_name"] for row in ledger
                          if row["decision"] == "CUT CANDIDATE"}, set(SWAPS.values()))

    def test_03_owner_words_exact_ci_sixteen_source_bound_case_records(self):
        receipt = RECEIPT.read_text(encoding="utf-8")
        self.assertIn("Approve Deck #62 Zevlor M7 Rev1", receipt)
        self.assertIn(NEW_SHA, receipt)
        self.assertIn(OLD_SHA, receipt)
        self.assertIn("40629369955", receipt)
        plan = json.loads((ROOT / transfer.PLANS).read_text())["decks"][KEY]
        mapped = json.loads(CASES.read_text())
        self.assertEqual(mapped["approved_raw_sha256"], NEW_SHA)
        self.assertEqual([x["case_id"] for x in mapped["m6_transfer"]["P0"]],
                         plan["required_P0"])
        self.assertEqual([x["case_id"] for x in mapped["m6_transfer"]["P1"]],
                         plan["required_P1"])
        self.assertTrue(all(x["status"] == "PASSED" for tier in ("P0", "P1")
                            for x in mapped["m6_transfer"][tier]))
        source = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        transfer.validate_attestation(ROOT, KEY, source, plan, mapped)

    def test_04_all_other_61_registry_and_tracker_records_unchanged(self):
        base_sha = os.environ.get("BASE_REF_SHA")
        if base_sha is None:
            self.skipTest("Dedicated PR workflow supplies exact base comparison")
        self.assertRegex(base_sha, r"^[0-9a-f]{40}$")
        old = json.loads(subprocess.check_output(
            ["git", "show", f"{base_sha}:state/current_deck_overrides.json"], cwd=ROOT))["decks"]
        new = json.loads((ROOT / "state/current_deck_overrides.json").read_text())["decks"]
        self.assertEqual(set(old), set(new))
        for key in old:
            if key != KEY:
                self.assertEqual(old[key], new[key], key)
        def tracker(content):
            return {r["deck_id"]: r for r in csv.DictReader(content.splitlines())}
        old_tracker = tracker(subprocess.check_output(
            ["git", "show", f"{base_sha}:refinement/Deck_Refinement_Tracker_2026-10-12.csv"],
            cwd=ROOT, text=True))
        new_tracker = tracker(
            (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").read_text())
        self.assertEqual(set(old_tracker), set(new_tracker))
        for key in old_tracker:
            if key != KEY:
                self.assertEqual(old_tracker[key], new_tracker[key], key)


if __name__ == "__main__":
    unittest.main()
