"""Deck #31 Lynde M7 Rev1 one-approval canonical lock source-integrity tests."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SHA = "6e088891b3c92b632d95e4b6dbd83ffedb06834f812e6728cc5bfa7bdc13556e"
OLD = "05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166"
DECK = "Lynde__Cheerful_Tormentor"
NEW_PATH = "refinement/decklists/Lynde_Cheerful_Tormentor_M7_Rev1_Approved_2026-10-25.txt"
OLD_PATH = "refinement/decklists/Lynde_Cheerful_Tormentor_Approved_2026-10-14.txt"
ATTEST = "refinement/verification/m7_certification_transfer/Lynde__Cheerful_Tormentor_6e088891b3c92b63.json"


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def parse(path):
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    assert lines and lines[0] == "1x Lynde, Cheerful Tormentor [Commander]"
    d = {}
    for line in lines:
        q, name = line.split("x ", 1)
        name = name.removesuffix(" [Commander]")
        d[name] = int(q)
    return d


class LyndeRev1OwnerLock(unittest.TestCase):
    def test_100_and_raw_sha(self):
        self.assertEqual(sha(NEW_PATH), SHA)
        a = parse(NEW_PATH)
        self.assertEqual(sum(a.values()), 100)
        self.assertEqual(len(a), 96)
        self.assertEqual({k: v for k, v in a.items() if v > 1},
                         {"Island": 3, "Mountain": 2, "Swamp": 2})
        self.assertEqual(sha(OLD_PATH), OLD)

    def test_exact_eight_swaps_and_old_preserved(self):
        a, old = parse(NEW_PATH), parse(OLD_PATH)
        adds = Counter(a) - Counter(old)
        cuts = Counter(old) - Counter(a)
        self.assertEqual(set(adds), {"Court of Vantress", "Extravagant Replication",
            "Barrin, Master Wizard", "Into the Pit", "Staff of Compleation",
            "Urza's Saga", "Otawara, Soaring City", "Shizo, Death's Storehouse"})
        self.assertEqual(set(cuts), {"Cruel Reality", "Curse of Death's Hold",
            "Torment of Scarabs", "Curse of the Restless Dead", "Nightscape Familiar",
            "Island", "Mountain", "Swamp"})
        self.assertEqual(sum(adds.values()), sum(cuts.values()), 8)

    def test_only_this_approval_override(self):
        state = json.loads((ROOT / "state/current_deck_overrides.json").read_text())
        self.assertEqual(len(state["decks"]), 62)
        d = state["decks"][DECK]
        self.assertEqual((d["approval_status"], d["lock_status"]), ("APPROVED", "LOCKED"))
        self.assertEqual(d["approved_list_sha256"], SHA)
        self.assertEqual(d["previous_approved_list_sha256"], OLD)
        self.assertEqual(d["approved_list_artifact"], NEW_PATH)
        self.assertEqual(d["m7_m6_certification_transfer_artifact"], ATTEST)

    def test_tracker_and_owner_receipt(self):
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(newline="") as f:
            rec = next(row for row in csv.DictReader(f)
                       if row["deck_id"] == DECK)
        self.assertEqual(rec["final_list_hash"], SHA)
        self.assertEqual(rec["refinement_status"].split(" — ")[0], "APPROVED / LOCKED")
        self.assertIn(SHA, (ROOT / "refinement/approvals/Lynde_Cheerful_Tormentor_M7_Rev1_Approved_2026-10-25.md").read_text())

    def test_13_case_transfer_and_96_legal_oracles(self):
        t = json.loads((ROOT / ATTEST).read_text())
        self.assertEqual(t["approved_raw_sha256"], SHA)
        self.assertEqual({x["case_id"] for x in t["m6_transfer"]["P0"]},
                         {"C1", "K1", "K2", "K3", "F1"})
        self.assertEqual({x["case_id"] for x in t["m6_transfer"]["P1"]},
                         {"K4", "K5", "E1", "E2", "W1", "W2", "F2", "F3"})
        self.assertTrue(all(x["status"] == "PASSED" and x["tested_raw_sha256"] == SHA
                           for x in t["m6_transfer"]["P0"] + t["m6_transfer"]["P1"]))
        oracle = json.loads((ROOT / "refinement/verification/Lynde_Cheerful_Tormentor_M7_Rev1_Oracle_Identity_Index_2026-10-25.json").read_text())
        self.assertEqual({x["name"] for x in oracle["cards"]}, set(parse(NEW_PATH)))
        self.assertEqual(len(oracle["cards"]), 96)
        self.assertTrue(all(x["commander_legality"] == "legal" and
            set(x["color_identity"]) <= {"U", "B", "R"} for x in oracle["cards"]))


if __name__ == "__main__":
    unittest.main()
