"""Deck #25 exact owner-approved ZIP M7 lock, two swaps, scoped M6 transfer."""
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
KEY = "Kefka__Court_Mage"
OLD = "cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03"
NEW = "14277f6e9774c5ef02b4f92332b52684794367007abf81bc2d84ef7ad7bcaa7d"
BEFORE = ROOT / "refinement/decklists/Kefka_Court_Mage_Approved_2026-10-14.txt"
AFTER = ROOT / "refinement/decklists/Kefka_Court_Mage_M7_Rev1_Approved_2026-10-28.txt"
ADDS = {"Step Through", "Sakashima of a Thousand Faces"}
CUTS = {"Demonic Counsel", "Phyrexian Metamorph"}


def inventory(path):
    cards = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for row in lines:
        count, name = row.split("x ", 1)
        cards[name.removesuffix(" [Commander]")] += int(count)
    return cards, lines


class Kefka25OwnerLock(unittest.TestCase):
    def test_01_exact_source_and_two_swaps(self):
        self.assertEqual(hashlib.sha256(BEFORE.read_bytes()).hexdigest(), OLD)
        self.assertEqual(hashlib.sha256(AFTER.read_bytes()).hexdigest(), NEW)
        self.assertFalse(AFTER.read_bytes().endswith(b"\n"))
        old, _ = inventory(BEFORE)
        new, lines = inventory(AFTER)
        self.assertEqual(lines[0], "1x Kefka, Court Mage // Kefka, Ruler of Ruin [Commander]")
        self.assertEqual(sum(new.values()), 100)
        self.assertEqual(len(new), 100)
        self.assertEqual(set((new - old).elements()), ADDS)
        self.assertEqual(set((old - new).elements()), CUTS)
        self.assertEqual(sum((new - old).values()), 2)

    def test_02_owner_receipt_registry_tracker(self):
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
        self.assertIn("Kefka", deck["m7_swap_floor_waiver"])
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
                newline="", encoding="utf-8") as stream:
            tracker = {r["deck_id"]: r for r in csv.DictReader(stream)}
        self.assertEqual(tracker[KEY]["final_list_hash"], NEW)
        self.assertEqual(tracker[KEY]["user_approval_date"], "2026-10-28")
        self.assertEqual(tracker[KEY]["final_gate_passed"], "YES")
        self.assertIsNone(tracker[KEY].get(None))

    def test_03_original_m6_case_ids_and_honest_deferrals(self):
        deck = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        plan = json.loads((ROOT / transfer.PLANS).read_text())["decks"][KEY]
        att = json.loads((ROOT / transfer.ATTESTATIONS / f"{KEY}_{NEW[:16]}.json").read_text())
        for tier in ("P0", "P1"):
            self.assertEqual([r["case_id"] for r in att["m6_transfer"][tier]], plan[f"required_{tier}"])
        self.assertEqual(sum(r["status"] == "PASSED" for r in att["m6_transfer"]["P0"]), 5)
        self.assertEqual(sum(r["status"] == "PASSED" for r in att["m6_transfer"]["P1"]), 6)
        self.assertEqual({r["case_id"] for r in att["m6_transfer"]["P1"]
                          if r["status"] == "DEFERRED"}, {"K4", "W2", "F3"})
        self.assertTrue(all(r["tested_raw_sha256"] == NEW for tier in ("P0", "P1")
                            for r in att["m6_transfer"][tier] if r["status"] == "PASSED"))
        self.assertIn("Phase B", att["m6_transfer"]["revision_diff_and_validity_reason"])
        transfer.validate_attestation(ROOT, KEY, deck, plan, att)

    def test_04_other_61_locks_preserved_from_pr_base(self):
        base = os.environ.get("BASE_REF_SHA")
        if not base:
            self.skipTest("PR-specific base SHA needed for other-61 exact comparison")
        assert_other_decks_preserved(self, ROOT, base, KEY, check_tracker=True)


if __name__ == "__main__":
    unittest.main()
