"""Fail-closed owner-approved canonical SHA lock for Deck #28 Loki M7 Rev1.

Mechanical CI is finite source-bound evidence, not a full gameplay simulation.
"""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = "Loki__the_Deceiver"
NEW_SHA = "919734ad1f60e56a636561815d319ec1eb0fbd0c233265ad5e85064f589c7185"
OLD_SHA = "5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062"
NEW = ROOT / "refinement/decklists/Loki_the_Deceiver_M7_Rev1_Approved_2026-10-25.txt"
OLD = ROOT / "refinement/decklists/Loki_the_Deceiver_Approved_2026-10-14.txt"
RECEIPT = ROOT / "refinement/approvals/Loki_the_Deceiver_M7_Rev1_Approved_2026-10-25.md"
VERIFY = ROOT / "refinement/verification/Loki_the_Deceiver_M7_Rev1_Approved_2026-10-25_Verification.md"
ORACLE = ROOT / "refinement/verification/Loki_the_Deceiver_M7_Rev1_Oracle_Identity_Index_2026-10-25.json"
ATTEST = ROOT / "refinement/verification/m7_certification_transfer/Loki__the_Deceiver_919734ad1f60e56a.json"
REVIEW = ROOT / "refinement/decisions/Loki_the_Deceiver_M7_Rev1_Whole99_Review_2026-10-25.md"
STATE = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
SNAPSHOT = ROOT / "refinement/verification/m7_certification_transfer/frozen_approval_snapshot_2026-10-24.json"
ADDS = {"Sakashima of a Thousand Faces", "Elektra, Daughter of the Hand",
        "Ultimo, Civilization's End", "M.O.D.O.K., Evil Intellect",
        "Living Lies of Loki", "Kid Loki", "City of Brass"}
CUTS = {"Thunderbolts Conspiracy", "Kang Prime", "Doctor Octopus, Master Planner",
        "Venom, Eddie Brock", "Kang, Temporal Tyrant", "Dark Ritual", "Path of Ancestry"}
P0 = {"C1", "K1", "K2", "K3", "F1"}
P1 = {"K4", "K5", "E1", "E2", "W1", "W2", "F2", "F3"}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_deck(path):
    rows = path.read_text(encoding="utf-8").splitlines()
    cards = Counter()
    for row in rows:
        m = re.fullmatch(r"(\d+)x (.+?)(?: \[Commander\])?", row)
        if not m:
            raise AssertionError(f"Invalid row: {row!r}")
        cards[m.group(2)] += int(m.group(1))
    return cards, rows


class LokiRev1OwnerLock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current, cls.rows = parse_deck(NEW)
        cls.original, cls.old_rows = parse_deck(OLD)
        cls.index = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.oracle = {x["name"]: x for x in cls.index["cards"]}
        cls.registry = json.loads(STATE.read_text(encoding="utf-8"))["decks"]
        cls.snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))["approved_sha256_by_deck"]
        cls.attest = json.loads(ATTEST.read_text(encoding="utf-8"))
        with TRACKER.open(encoding="utf-8", newline="") as f:
            cls.tracker = list(csv.DictReader(f))

    def test_exact_bytes_100_physical_basic_multiplicity_historical_lock(self):
        self.assertEqual(sha(NEW), NEW_SHA)
        self.assertEqual(sha(OLD), OLD_SHA)
        self.assertTrue(NEW.read_bytes().endswith(b"\n"))
        self.assertFalse(NEW.read_bytes().endswith(b"\n\n"))
        self.assertEqual(self.rows[0], "1x Loki, the Deceiver [Commander]")
        self.assertEqual(len(self.rows), 95)
        self.assertEqual(sum(self.current.values()), 100)
        self.assertEqual(len(self.current), 95)
        self.assertEqual(self.current["Loki, the Deceiver"], 1)
        self.assertEqual(sum(line.endswith(" [Commander]") for line in self.rows), 1)
        self.assertEqual({n: q for n, q in self.current.items() if q > 1},
                         {"Island": 3, "Mountain": 2, "Swamp": 3})
        self.assertEqual(sum(self.original.values()), 100)

    def test_exact_seven_paired_swaps_commander_first_and_not_combo_shell(self):
        self.assertEqual(set(self.current - self.original), ADDS)
        self.assertEqual(set(self.original - self.current), CUTS)
        self.assertTrue(all(v == 1 for v in (self.current - self.original).values()))
        self.assertTrue(all(v == 1 for v in (self.original - self.current).values()))
        for core in ("Crimson Cowl, Master of Evil", "Killmonger, Ruthless Usurper",
                     "The Master, Multiplied", "Sundial of the Infinite", "Roaming Throne",
                     "Kindred Discovery", "Loki's Scepter", "The Squadron Sinister"):
            self.assertEqual(self.current[core], 1)
        self.assertFalse({"Thassa's Oracle", "Demonic Consultation", "Dockside Extortionist",
                          "Jeweled Lotus", "Underworld Breach"} & set(self.current))

    def test_selected_scryfall_oracle_legality_land_cheap_targets_game_changers(self):
        idx = self.index
        self.assertEqual(idx["candidate_raw_sha256"], NEW_SHA)
        self.assertEqual(idx["source_date"], "2026-10-23")
        self.assertEqual(idx["selected_names_count"], 95)
        self.assertEqual(idx["physical_count"], 100)
        self.assertEqual(set(self.oracle), set(self.current))
        self.assertEqual(len(self.oracle), 95)
        for name, card in self.oracle.items():
            with self.subTest(card=name):
                self.assertEqual(card["commander_legality"], "legal")
                self.assertTrue(set(card["color_identity"]) <= {"U", "B", "R"})
                self.assertTrue(card["oracle_text"] or "Basic Land" in card["type_line"])
        self.assertEqual(sum(q for n, q in self.current.items() if "Land" in self.oracle[n]["type_line"]), 34)
        cheap = sum(q for n, q in self.current.items()
                    if n != "Loki, the Deceiver" and "Creature" in self.oracle[n]["type_line"]
                    and "Villain" in self.oracle[n]["type_line"] and self.oracle[n]["cmc"] <= 3)
        self.assertEqual(cheap, 12)
        gcs = {c["name"] for c in self.index["cards"] if c["game_changer"]}
        self.assertEqual(gcs, {"Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship",
                               "Jeska's Will", "Rhystic Study"})
        for name in ADDS:
            self.assertLessEqual(self.oracle[name]["released_at"], "2026-10-25")

    def test_commander_and_all_seven_additions_exact_oracle_rules(self):
        o = self.oracle
        self.assertIn("tapped and attacking token", o["Loki, the Deceiver"]["oracle_text"])
        self.assertIn("another target Villain", o["Loki, the Deceiver"]["oracle_text"])
        self.assertIn("legend rule", o["Sakashima of a Thousand Faces"]["oracle_text"])
        self.assertIn("When Elektra enters, destroy target creature", o["Elektra, Daughter of the Hand"]["oracle_text"])
        self.assertIn("When Ultimo enters, each opponent sacrifices", o["Ultimo, Civilization's End"]["oracle_text"])
        self.assertIn("Whenever you draw your second card each turn", o["M.O.D.O.K., Evil Intellect"]["oracle_text"])
        self.assertIn("When this creature dies, draw a card", o["Living Lies of Loki"]["oracle_text"])
        self.assertIn("put one or more +1/+1 counters on this turn has hexproof", o["Kid Loki"]["oracle_text"])
        self.assertIn("Add one mana of any color", o["City of Brass"]["oracle_text"])
        self.assertNotIn("This land enters tapped", o["City of Brass"]["oracle_text"])

    def test_explicit_approval_review_receipt_limitations_and_eng_success(self):
        a, v, r = [p.read_text(encoding="utf-8") for p in (RECEIPT, VERIFY, REVIEW)]
        for body in (a, v, r):
            self.assertIn(NEW_SHA, body)
            self.assertIn(OLD_SHA, body)
            self.assertIn("100", body)
        self.assertIn("“Approve”", a)
        self.assertIn("#706", a)
        self.assertIn("40178847336", a)
        self.assertIn("40178847260", v)
        self.assertIn("empirical multiplayer win rates", a)
        self.assertIn("13-case", v)

    def test_registry_tracker_62_locks_27_m7_records_and_pinned_historical_snap(self):
        self.assertEqual(len(self.registry), 62)
        self.assertEqual(len(self.tracker), 62)
        entry = self.registry[DECK]
        self.assertEqual((entry["approval_status"], entry["lock_status"], entry["current_stage"]),
                         ("APPROVED", "LOCKED", "LOCKED"))
        self.assertTrue(entry["final_gate_passed"])
        self.assertEqual(entry["approved_list_sha256"], NEW_SHA)
        self.assertEqual(entry["m7_final_candidate_sha256"], NEW_SHA)
        self.assertEqual(entry["previous_approved_list_sha256"], OLD_SHA)
        self.assertEqual(entry["approved_list_artifact"], NEW.relative_to(ROOT).as_posix())
        self.assertEqual(entry["previous_approved_list_artifact"], OLD.relative_to(ROOT).as_posix())
        self.assertEqual(entry["user_approval_date"], "2026-10-25")
        self.assertEqual(entry["m7_power_bracket"], "4 — Optimized")
        self.assertEqual(entry["m7_archidekt_tags"], ["Villain Copies", "Combat Value", "Connive"])
        self.assertEqual(entry["m7_project_exceptions"], [])
        self.assertEqual(sum(bool(d.get("m7_final_candidate_sha256")) for d in self.registry.values()), 28)
        changed_since_snapshot = {n for n, d in self.registry.items()
                                  if d["approved_list_sha256"] != self.snapshot[n]}
        self.assertEqual(changed_since_snapshot,
                         {"Kess__Dissident_Mage", "Grixistax___October_2026", DECK, "Lord_of_Tresserhorn"})
        for n, d in self.registry.items():
            with self.subTest(locked=n):
                self.assertEqual(sha(ROOT / d["approved_list_artifact"]), d["approved_list_sha256"])
        row = next(r for r in self.tracker if r["deck_id"] == DECK)
        self.assertEqual(row["index"], "27")
        self.assertEqual(row["final_gate_passed"], "YES")
        self.assertEqual(row["final_list_hash"], NEW_SHA)
        self.assertEqual(row["user_approval_date"], "2026-10-25")
        self.assertIn("APPROVED / LOCKED", row["refinement_status"])

    def test_all_13_p0_p1_execution_evidence_exact_new_sha(self):
        a = self.attest
        self.assertEqual(a["approved_raw_sha256"], NEW_SHA)
        self.assertEqual(a["approved_artifact"], NEW.relative_to(ROOT).as_posix())
        self.assertEqual(a["owner_approval_receipt"], RECEIPT.relative_to(ROOT).as_posix())
        self.assertEqual(a["engineering"]["head_sha"], "b316ce65c6355523c32169454ed51d4211d07ea0")
        self.assertIn("40178847336", a["engineering"]["m7_decision_gate_ci_run_url"])
        transfer = a["m6_transfer"]
        self.assertEqual(transfer["ij_scope"], "TRANSFERRED_WITH_CASE_MAPPING")
        self.assertEqual({c["case_id"] for c in transfer["P0"]}, P0)
        self.assertEqual({c["case_id"] for c in transfer["P1"]}, P1)
        for item in transfer["P0"] + transfer["P1"]:
            with self.subTest(case=item["case_id"]):
                self.assertEqual(item["status"], "PASSED")
                self.assertEqual(item["scope"], "EXACT_APPROVED_100")
                self.assertEqual(item["tested_raw_sha256"], NEW_SHA)
                self.assertIn("40178847336", item["ci_run_url"])
                self.assertIn("test_m6_loki_rev1_case_transfer.py", item["test_ref"])
                self.assertTrue(item["payable_fixture"])
                self.assertTrue(item["positive_assertion"])
                self.assertTrue(item["adversarial_assertion"])


if __name__ == "__main__":
    unittest.main()
