"""Owner-exact #60 M7 100; project-only future release; all 15 bounded M6 cases."""
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
KEY = "Tresserhorn_s_Lord__Returned"
OLD = "8c802586a4742156fb96246f4f23331eb51d1a77d6717da63ceed2446e98adf8"
NEW = "9a9d2f7a344e2491444c0a0e4c48525dfe8faa37032eaf8e22a94082f6fbf60e"
BEFORE = ROOT / "refinement/decklists/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.txt"
AFTER = ROOT / "refinement/decklists/Tresserhorn_s_Lord_Returned_M7_Rev1_Approved_2026-10-27.txt"
ADDS = {"Genesis Chamber", "Sengir Autocrat", "Deflecting Swat",
        "Fierce Guardianship", "Song of Totentanz", "The Meathook Massacre",
        "Agadeem's Awakening // Agadeem, the Undercrypt"}
CUTS = {"Dark Ritual", "Endrek Sahr, Master Breeder", "Village Rites",
        "Stubborn Denial", "Tempt with Vengeance", "Blasphemous Edict", "Swamp"}


def inventory(path):
    cards = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for row in lines:
        n, card = row.split("x ", 1)
        cards[card.removesuffix(" [Commander]")] += int(n)
    return cards, lines


class Tresserhorn60OwnerLock(unittest.TestCase):
    def test_01_exact_100_and_real_seven_swaps(self):
        self.assertEqual(hashlib.sha256(BEFORE.read_bytes()).hexdigest(), OLD)
        self.assertEqual(hashlib.sha256(AFTER.read_bytes()).hexdigest(), NEW)
        prior, _ = inventory(BEFORE)
        current, lines = inventory(AFTER)
        self.assertEqual(lines[0], "1x Tresserhorn's Lord, Returned [Commander]")
        self.assertEqual(sum(current.values()), 100)
        self.assertEqual(len(current), 94)
        self.assertEqual({n: q for n,q in current.items() if q > 1},
                         {"Island":3, "Mountain":3, "Swamp":3})
        self.assertEqual(set((current-prior).elements()), ADDS)
        self.assertEqual(set((prior-current).elements()), CUTS)
        self.assertEqual(sum((current-prior).values()), 7)

    def test_02_owner_state_tracker_and_project_exception(self):
        deck = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        for field, value in (("approved_list_sha256", NEW),
                             ("previous_approved_list_sha256", OLD),
                             ("m7_final_candidate_sha256", NEW),
                             ("user_approval_date", "2026-10-27"),
                             ("approval_status", "APPROVED"),
                             ("lock_status", "LOCKED")):
            self.assertEqual(deck[field], value, field)
        self.assertIn("not_legal", deck["project_future_release_exception"])
        self.assertIn("2026-11-13", deck["project_future_release_exception"])
        receipt = (ROOT / deck["approval_record_artifact"]).read_text()
        self.assertIn("Approve. And be quick about it.", receipt)
        self.assertIn(NEW, receipt)
        self.assertIn(OLD, receipt)
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
                newline="", encoding="utf-8") as f:
            tracker = {r["deck_id"]:r for r in csv.DictReader(f)}
        self.assertEqual(tracker[KEY]["final_list_hash"], NEW)
        self.assertEqual(tracker[KEY]["user_approval_date"], "2026-10-27")
        self.assertEqual(tracker[KEY]["final_gate_passed"], "YES")
        self.assertIsNone(tracker[KEY].get(None))

    def test_03_all_original_p0_p1_case_ids_and_honest_ij_limit(self):
        deck = json.loads((ROOT / transfer.REGISTRY).read_text())["decks"][KEY]
        plan = json.loads((ROOT / transfer.PLANS).read_text())["decks"][KEY]
        attestation = json.loads((ROOT / transfer.ATTESTATIONS /
                                  f"{KEY}_{NEW[:16]}.json").read_text())
        for priority, count in (("P0",5), ("P1",10)):
            cases = attestation["m6_transfer"][priority]
            self.assertEqual([r["case_id"] for r in cases], plan[f"required_{priority}"])
            self.assertEqual(sum(r["status"] == "PASSED" for r in cases), count)
            self.assertTrue(all(r["tested_raw_sha256"] == NEW for r in cases))
        scope = attestation["m6_transfer"]["revision_diff_and_validity_reason"]
        self.assertIn("Phase B", scope)
        self.assertIn("future-release", scope.lower())
        transfer.validate_attestation(ROOT, KEY, deck, plan, attestation)

    def test_04_other_61_owner_locks_unchanged_from_exact_base(self):
        base = os.environ.get("BASE_REF_SHA")
        if not base:
            self.skipTest("PR-specific exact base SHA needed for other-61 comparison")
        assert_other_decks_preserved(self, ROOT, base, KEY, check_tracker=True)


if __name__ == "__main__":
    unittest.main()
