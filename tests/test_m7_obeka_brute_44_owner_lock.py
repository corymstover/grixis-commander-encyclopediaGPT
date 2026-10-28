"""Deck #44 owner-approved M7 100, exact prior 100 and source-bound case inventory."""

from collections import Counter
import csv
import hashlib
import json
import os
from pathlib import Path
import unittest

from scripts import verify_m7_certification_transfer as transfer
from m7_approved_supersession import assert_other_decks_preserved

ROOT = Path(__file__).resolve().parents[1]
KEY = "Obeka__Brute_Chronologist"
OLD = "31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8"
NEW = "43f1249c9a1da82bc1e74254a44613a0ab5763c91295a56ffae3b75a889029f2"
BEFORE = ROOT / "refinement/decklists/Obeka_Brute_Chronologist_Approval_Ready_2026-10-15.txt"
AFTER = ROOT / "refinement/decklists/Obeka_Brute_Chronologist_M7_Rev1_Approved_2026-10-27.txt"
SIX = {
    "Footsteps of the Goryo": "Delina, Wild Mage",
    "Entomb": "Windfall",
    "Mimic Vat": "Purphoros, Bronze-Blooded",
    "Zealous Conscripts": "Ilharg, the Raze-Boar",
    "Splinter Twin": "Hate Mirage",
    "Spellseeker": "Avaricious Dragon",
}


def count(path):
    items = Counter()
    rows = path.read_text(encoding="utf-8").splitlines()
    for row in rows:
        quantity, name = row.split("x ", 1)
        items[name.removesuffix(" [Commander]")] += int(quantity)
    return items, rows


class Obeka44M7OwnerLock(unittest.TestCase):
    def test_01_exact_sources_100_34_lands_six_swaps(self):
        self.assertEqual(hashlib.sha256(BEFORE.read_bytes()).hexdigest(), OLD)
        self.assertEqual(hashlib.sha256(AFTER.read_bytes()).hexdigest(), NEW)
        a, old_rows = count(BEFORE)
        b, rows = count(AFTER)
        self.assertEqual(rows[0], "1x Obeka, Brute Chronologist [Commander]")
        self.assertEqual(sum(b.values()), 100)
        self.assertEqual(len(b), 100)
        self.assertEqual(b - a, Counter(SIX.keys()))
        self.assertEqual(a - b, Counter(SIX.values()))

    def test_02_registry_tracker_owner_approval_match(self):
        d = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        self.assertEqual(d["approved_list_sha256"], NEW)
        self.assertEqual(d["previous_approved_list_sha256"], OLD)
        self.assertEqual(d["m7_final_candidate_sha256"], NEW)
        self.assertEqual(d["approval_status"], "APPROVED")
        self.assertEqual(d["lock_status"], "LOCKED")
        self.assertEqual(d["user_approval_date"], "2026-10-27")
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
                newline="", encoding="utf-8") as handle:
            tracker = {r["deck_id"]: r for r in csv.DictReader(handle)}
        self.assertEqual(tracker[KEY]["final_list_hash"], NEW)
        self.assertEqual(tracker[KEY]["user_approval_date"], "2026-10-27")
        self.assertEqual(tracker[KEY]["final_gate_passed"], "YES")

    def test_03_receipt_case_mapping_and_provenance(self):
        d = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        receipt = (ROOT / d["approval_record_artifact"]).read_text(encoding="utf-8")
        self.assertIn(NEW, receipt)
        self.assertIn(OLD, receipt)
        p = json.loads((ROOT / transfer.PLANS).read_text())["decks"][KEY]
        doc = json.loads((ROOT / transfer.ATTESTATIONS / f"{KEY}_{NEW[:16]}.json").read_text())
        self.assertEqual([x["case_id"] for x in doc["m6_transfer"]["P0"]], p["required_P0"])
        self.assertEqual([x["case_id"] for x in doc["m6_transfer"]["P1"]], p["required_P1"])
        transfer.validate_attestation(ROOT, KEY, d, p, doc)

    def test_04_all_other_owner_authorities_preserved(self):
        base = os.environ.get("BASE_REF_SHA")
        if not base:
            self.skipTest("PR-specific base comparison provided by workflow")
        assert_other_decks_preserved(self, ROOT, base, KEY, check_tracker=True)


if __name__ == "__main__":
    unittest.main()
