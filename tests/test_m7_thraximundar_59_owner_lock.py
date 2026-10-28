"""Deck #59 exact Thraximundar M7 100, old owner lock, P0/P1 scope."""

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
KEY = "Thraximundar"
OLD = "d4fa3421752a4d666528c5218aa18b240465c817dd160642c103b2de8c3f9442"
NEW = "f3e71b71fc10fbe6d8a1afde29b5291e9e32d4e83db44c2dcb7aab0773f18da2"
BEFORE = ROOT / "refinement/decklists/Thraximundar_Approved_2026-10-15.txt"
AFTER = ROOT / "refinement/decklists/Thraximundar_M7_Rev1_Approved_2026-10-27.txt"
ADDS = {"Bontu's Monument", "Brotherhood Regalia", "Marionette Apprentice",
        "Marsh Flats", "Misty Rainforest", "Ophiomancer", "Plumb the Forbidden",
        "Priest of Forgotten Gods", "Roaming Throne", "Verdant Catacombs"}
CUTS = {"Archfiend of Depravity", "Diregraf Captain", "Dragonskull Summit",
        "Drowned Catacomb", "Grimgrin, Corpse-Born", "Liliana, Dreadhorde General",
        "Necrotic Hex", "Sheoldred, Whispering One", "Sulfur Falls", "Swiftfoot Boots"}


def inventory(path):
    cards = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for row in lines:
        n, card = row.split("x ", 1)
        cards[card.removesuffix(" [Commander]")] += int(n)
    return cards, lines


class Thraximundar59OwnerLock(unittest.TestCase):
    def test_01_exact_sources_100_and_ten_genuine_swaps(self):
        self.assertEqual(hashlib.sha256(BEFORE.read_bytes()).hexdigest(), OLD)
        self.assertEqual(hashlib.sha256(AFTER.read_bytes()).hexdigest(), NEW)
        old, _ = inventory(BEFORE)
        new, lines = inventory(AFTER)
        self.assertEqual(lines[0], "1x Thraximundar [Commander]")
        self.assertEqual(sum(new.values()), 100)
        self.assertEqual(len(new), 93)
        self.assertEqual({n: q for n,q in new.items() if q>1},
                         {"Island":3,"Mountain":2,"Swamp":5})
        self.assertEqual(set((new-old).elements()), ADDS)
        self.assertEqual(set((old-new).elements()), CUTS)
        self.assertEqual(sum((new-old).values()), 10)

    def test_02_state_tracker_owner_and_prior_hash(self):
        deck = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        for field, value in (("approved_list_sha256", NEW),
                             ("previous_approved_list_sha256", OLD),
                             ("m7_final_candidate_sha256", NEW),
                             ("user_approval_date", "2026-10-27"),
                             ("approval_status", "APPROVED"),
                             ("lock_status", "LOCKED")):
            self.assertEqual(deck[field], value, field)
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
                newline="", encoding="utf-8") as h:
            tracker = {r["deck_id"]: r for r in csv.DictReader(h)}
        self.assertEqual(tracker[KEY]["final_list_hash"], NEW)
        self.assertEqual(tracker[KEY]["user_approval_date"], "2026-10-27")
        self.assertEqual(tracker[KEY]["final_gate_passed"], "YES")
        self.assertIsNone(tracker[KEY].get(None), "Tracker must have no extra CSV columns")

    def test_03_source_bounded_five_p0_and_eight_honest_p1_deferrals(self):
        deck = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        receipt = (ROOT / deck["approval_record_artifact"]).read_text(encoding="utf-8")
        self.assertIn(NEW, receipt)
        self.assertIn(OLD, receipt)
        plan = json.loads((ROOT / transfer.PLANS).read_text())["decks"][KEY]
        attestation = json.loads((ROOT / transfer.ATTESTATIONS / f"{KEY}_{NEW[:16]}.json").read_text())
        for priority in ("P0", "P1"):
            self.assertEqual([x["case_id"] for x in attestation["m6_transfer"][priority]],
                             plan[f"required_{priority}"])
        self.assertEqual(sum(x["status"] == "PASSED" for x in attestation["m6_transfer"]["P0"]), 5)
        self.assertTrue(all(x["status"] == "DEFERRED" and x["owner_visible_unresolved"]
                            for x in attestation["m6_transfer"]["P1"]))
        transfer.validate_attestation(ROOT, KEY, deck, plan, attestation)

    def test_04_all_other_61_owner_locks_preserved(self):
        base = os.environ.get("BASE_REF_SHA")
        if not base:
            self.skipTest("PR-specific base comparison supplied by focused owner lock")
        assert_other_decks_preserved(self, ROOT, base, KEY, check_tracker=True)


if __name__ == "__main__":
    unittest.main()
