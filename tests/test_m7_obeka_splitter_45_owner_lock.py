"""Deck #45 exact approved M7 Splitter source, swap and case provenance."""

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
KEY = "Obeka__Splitter_of_Seconds"
OLD = "c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63"
NEW = "f80d882944d5e39f3c6661da4dcdce3ec6eead577cd981dc54f7dc522be50859"
BEFORE = ROOT / "refinement/decklists/Obeka_Splitter_of_Seconds_Approval_Ready_2026-10-15.txt"
AFTER = ROOT / "refinement/decklists/Obeka_Splitter_of_Seconds_M7_Rev1_Approved_2026-10-27.txt"
SIX = {
    "Jeska, Thrice Reborn": "Rousing Refrain",
    "Blackblade Reforged": "Ring of Xathrid",
    "Academy Manufactor": "Jhoira of the Ghitu",
    "Rising of the Day": "Ring of Valkas",
    "Karlach, Fury of Avernus": "Paradox Haze",
    "Aggravated Assault": "Darksteel Reactor",
}


def inventory(path):
    cards = Counter()
    rows = path.read_text(encoding="utf-8").splitlines()
    for row in rows:
        qty, name = row.split("x ", 1)
        cards[name.removesuffix(" [Commander]")] += int(qty)
    return cards, rows


class ObekaSplitter45OwnerLock(unittest.TestCase):
    def test_01_exact_sources_and_six_swaps(self):
        self.assertEqual(hashlib.sha256(BEFORE.read_bytes()).hexdigest(), OLD)
        self.assertEqual(hashlib.sha256(AFTER.read_bytes()).hexdigest(), NEW)
        a, _ = inventory(BEFORE)
        b, rows = inventory(AFTER)
        self.assertEqual(rows[0], "1x Obeka, Splitter of Seconds [Commander]")
        self.assertEqual(sum(b.values()), 100)
        self.assertEqual(len(b), 96)
        self.assertEqual({n:q for n,q in b.items() if q>1},
                         {"Island":3,"Mountain":2,"Swamp":2})
        self.assertEqual(b - a, Counter(SIX.keys()))
        self.assertEqual(a - b, Counter(SIX.values()))

    def test_02_owner_state_and_tracker(self):
        deck = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        for field, value in (("approved_list_sha256", NEW),
                             ("previous_approved_list_sha256", OLD),
                             ("m7_final_candidate_sha256", NEW),
                             ("user_approval_date", "2026-10-27"),
                             ("approval_status", "APPROVED"),
                             ("lock_status", "LOCKED")):
            self.assertEqual(deck[field], value, field)
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
                newline="", encoding="utf-8") as handle:
            tracker = {r["deck_id"]: r for r in csv.DictReader(handle)}
        self.assertEqual(tracker[KEY]["final_list_hash"], NEW)
        self.assertEqual(tracker[KEY]["user_approval_date"], "2026-10-27")
        self.assertEqual(tracker[KEY]["final_gate_passed"], "YES")

    def test_03_original_five_p0_and_ten_visible_deferred_p1(self):
        deck = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        receipt = (ROOT / deck["approval_record_artifact"]).read_text(encoding="utf-8")
        self.assertIn(NEW, receipt)
        self.assertIn(OLD, receipt)
        plan = json.loads((ROOT / transfer.PLANS).read_text())["decks"][KEY]
        doc = json.loads((ROOT / transfer.ATTESTATIONS / f"{KEY}_{NEW[:16]}.json").read_text())
        for tier in ("P0", "P1"):
            self.assertEqual([c["case_id"] for c in doc["m6_transfer"][tier]],
                             plan[f"required_{tier}"])
        self.assertEqual(sum(c["status"] == "PASSED" for c in doc["m6_transfer"]["P0"]), 5)
        self.assertTrue(all(c["status"] == "DEFERRED" and c["owner_visible_unresolved"]
                            for c in doc["m6_transfer"]["P1"]))
        transfer.validate_attestation(ROOT, KEY, deck, plan, doc)

    def test_04_other_61_authorities_preserved(self):
        base = os.environ.get("BASE_REF_SHA")
        if not base:
            self.skipTest("Base SHA supplied by dedicated canonical PR workflow")
        assert_other_decks_preserved(self, ROOT, base, KEY, check_tracker=True)


if __name__ == "__main__":
    unittest.main()
