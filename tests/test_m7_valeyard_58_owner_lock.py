"""Deck #58 exact owner-approved ZIP 100 and scoped full P0/P1 transfer."""
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
KEY = "The_Valeyard"
OLD = "4bef619a33d85eafaf194997924fc8378dd490f62c59d76bafccc4fa07ef821c"
NEW = "1735629783fbea2c9b8782fe18835f6dc8b3b980715344249cdb0941fbd9887b"
BEFORE = ROOT / "refinement/decklists/The_Valeyard_Approved_2026-10-15.txt"
AFTER = ROOT / "refinement/decklists/The_Valeyard_M7_Rev1_Approved_2026-10-28.txt"
ADDS = {"Irenicus's Vile Duplication", "Double Vision", "Swan Song",
        "Toxic Deluge", "Chrome Mox", "Ancient Tomb"}
CUTS = {"Brainstorm", "Kess, Dissident Mage", "Arcane Denial",
        "Blasphemous Act", "Izzet Signet", "Haunted Ridge"}


def inventory(path):
    cards = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for row in lines:
        count, name = row.split("x ", 1)
        cards[name.removesuffix(" [Commander]")] += int(count)
    return cards, lines


class Valeyard58OwnerLock(unittest.TestCase):
    def test_01_exact_source_and_six_swaps(self):
        self.assertEqual(hashlib.sha256(BEFORE.read_bytes()).hexdigest(), OLD)
        self.assertEqual(hashlib.sha256(AFTER.read_bytes()).hexdigest(), NEW)
        original, _ = inventory(BEFORE)
        new, lines = inventory(AFTER)
        self.assertEqual(lines[0], "1x The Valeyard [Commander]")
        self.assertEqual(sum(new.values()), 100)
        self.assertEqual(len(new), 96)
        self.assertEqual({x for x, qty in new.items() if qty > 1} -
                         {"Island", "Mountain", "Swamp"}, set())
        self.assertEqual(set((new - original).elements()), ADDS)
        self.assertEqual(set((original - new).elements()), CUTS)
        self.assertEqual(sum((new - original).values()), 6)

    def test_02_receipt_registry_tracker(self):
        deck = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        for field, value in (("approved_list_sha256", NEW),
                             ("previous_approved_list_sha256", OLD),
                             ("m7_final_candidate_sha256", NEW),
                             ("user_approval_date", "2026-10-28"),
                             ("approval_status", "APPROVED"),
                             ("lock_status", "LOCKED")):
            self.assertEqual(deck[field], value, field)
        receipt = (ROOT / deck["approval_record_artifact"]).read_text()
        self.assertIn("Approve both exact ZIP lists", receipt)
        self.assertIn(NEW, receipt)
        self.assertIn(OLD, receipt)
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
                newline="", encoding="utf-8") as stream:
            tracker = {r["deck_id"]: r for r in csv.DictReader(stream)}
        self.assertEqual(tracker[KEY]["final_list_hash"], NEW)
        self.assertEqual(tracker[KEY]["user_approval_date"], "2026-10-28")
        self.assertEqual(tracker[KEY]["final_gate_passed"], "YES")
        self.assertIsNone(tracker[KEY].get(None))

    def test_03_all_original_m6_p0_p1_cases_bound_to_new_sha(self):
        deck = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        plan = json.loads((ROOT / transfer.PLANS).read_text())["decks"][KEY]
        att = json.loads((ROOT / transfer.ATTESTATIONS / f"{KEY}_{NEW[:16]}.json").read_text())
        for tier, count in (("P0", 5), ("P1", 9)):
            cases = att["m6_transfer"][tier]
            self.assertEqual([r["case_id"] for r in cases], plan[f"required_{tier}"])
            self.assertEqual(sum(r["status"] == "PASSED" for r in cases), count)
            self.assertTrue(all(r["tested_raw_sha256"] == NEW for r in cases))
        self.assertIn("Phase B", att["m6_transfer"]["revision_diff_and_validity_reason"])
        transfer.validate_attestation(ROOT, KEY, deck, plan, att)

    def test_04_other_61_owner_locks_preserved_from_pr_base(self):
        base = os.environ.get("BASE_REF_SHA")
        if not base:
            self.skipTest("PR-specific base SHA needed for other-61 exact comparison")
        assert_other_decks_preserved(self, ROOT, base, KEY, check_tracker=True)


if __name__ == "__main__":
    unittest.main()
