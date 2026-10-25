"""Fail-closed Deck #26 Kess owner-approved SHA and prior-61 preservation."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ID = "Kess__Dissident_Mage"
SHA = "11415352a453e52afe4b1cc6881061e0d255e8403f8d5af5a24f9803c004fde4"
OLD_SHA = "93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb"
NEW = ROOT / "refinement/decklists/Kess_Dissident_Mage_M7_Rev1_Approved_2026-10-24.txt"
OLD = ROOT / "refinement/decklists/Kess_Dissident_Mage_Approved_2026-10-14.txt"
RECEIPT = ROOT / "refinement/approvals/Kess_Dissident_Mage_M7_Rev1_Approved_2026-10-24.md"
VERIFY = ROOT / "refinement/verification/Kess_Dissident_Mage_M7_Rev1_Approved_2026-10-24_Verification.md"
INDEX = ROOT / "refinement/verification/Kess_Dissident_Mage_M7_Rev1_Oracle_Identity_Index_2026-10-24.json"
REG = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
SNAPSHOT = ROOT / "refinement/verification/m7_certification_transfer/frozen_approval_snapshot_2026-10-24.json"
ATTEST = ROOT / "refinement/verification/m7_certification_transfer/Kess__Dissident_Mage_11415352a453e52a.json"
ADD = Counter({"Mana Drain":1,"Grim Tutor":1,"Jeska's Will":1,"Cyclonic Rift":1,"Exotic Orchard":1})
CUT = Counter({"Personal Tutor":1,"Demonic Counsel":1,"Ledger Shredder":1,"Into the Flood Maw":1,"Fiery Islet":1})
CORE = {"Thassa's Oracle","Demonic Consultation","Tainted Pact","Intuition","Gifts Ungiven",
        "Displacer Kitten","Entomb","Reanimate","Underworld Breach","Lion's Eye Diamond",
        "Brain Freeze","Grinding Station"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class KessM7Rev1ExactOwnerLock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = NEW.read_bytes()
        cls.cards = cls.raw.decode("utf-8").splitlines()
        cls.old = OLD.read_text(encoding="utf-8").splitlines()
        cls.registry = json.loads(REG.read_text(encoding="utf-8"))["decks"]
        cls.snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))["approved_sha256_by_deck"]
        cls.index = json.loads(INDEX.read_text(encoding="utf-8"))
        cls.attestation = json.loads(ATTEST.read_text(encoding="utf-8"))
        with TRACKER.open(newline="", encoding="utf-8") as f:
            cls.tracker = list(csv.DictReader(f))

    def test_exact_100_raw_sha_singleton_commander_and_historical_baseline(self):
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), SHA)
        self.assertTrue(self.raw.endswith(b"\n"))
        self.assertFalse(self.raw.endswith(b"\n\n"))
        self.assertEqual(digest(OLD), OLD_SHA)
        self.assertEqual(len(self.cards), 100)
        self.assertEqual(len(set(self.cards)), 100)
        self.assertTrue(all(c.startswith("1x ") for c in self.cards))
        self.assertEqual(self.cards[0], "1x Kess, Dissident Mage [Commander]")

    def test_exact_five_swaps_and_kess_specific_engines(self):
        old = Counter(c.removeprefix("1x ") for c in self.old[1:])
        new = Counter(c.removeprefix("1x ") for c in self.cards[1:])
        self.assertEqual(new - old, ADD)
        self.assertEqual(old - new, CUT)
        self.assertTrue(CORE <= set(new))
        self.assertNotIn("Demonic Counsel", new)
        self.assertNotIn("Ledger Shredder", new)

    def test_all_100_archived_oracle_legal_and_grixis_with_27_lands(self):
        idx = self.index
        self.assertEqual(idx["candidate_raw_sha256"], SHA)
        self.assertEqual(idx["source_date"], "2026-10-23")
        self.assertEqual(idx["source_card_count"], 187)
        rows = idx["cards"]
        self.assertEqual(len(rows), 100)
        actual_names = {c.removeprefix("1x ").removesuffix(" [Commander]") for c in self.cards}
        self.assertEqual({c["name"] for c in rows}, actual_names)
        for card in rows:
            with self.subTest(name=card["name"]):
                self.assertEqual(card["commander_legality"], "legal")
                self.assertTrue(set(card["color_identity"]) <= {"B","R","U"})
                self.assertTrue(card["oracle_id"] and card["oracle_text"])
        self.assertEqual(sum("Land" in c["type_line"] for c in rows), 27)
        self.assertEqual(sum(bool(c["game_changer"]) for c in rows), 23)
        kess = next(c for c in rows if c["name"] == "Kess, Dissident Mage")
        self.assertIn("Once during each of your turns", kess["oracle_text"])
        self.assertIn("exile it instead", kess["oracle_text"])

    def test_explicit_owner_receipt_and_bounded_verification_disclosure(self):
        receipt = RECEIPT.read_text(encoding="utf-8")
        verified = VERIFY.read_text(encoding="utf-8")
        for body in (receipt, verified):
            self.assertIn(SHA, body)
            self.assertIn(OLD_SHA, body)
            self.assertIn("#704", body)
            self.assertIn("14", body)
            self.assertIn("100", body)
        self.assertIn("“Approve”", receipt)
        self.assertIn("five", receipt)
        self.assertIn("not full game", receipt.lower())

    def test_registry_tracker_exact_owner_target_and_only_one_new_hash(self):
        self.assertEqual(len(self.registry), 62)
        self.assertEqual(len(self.tracker), 62)
        e = self.registry[ID]
        self.assertEqual((e["approval_status"],e["lock_status"],e["current_stage"]),
                         ("APPROVED","LOCKED","LOCKED"))
        self.assertTrue(e["final_gate_passed"])
        self.assertEqual(e["approved_list_sha256"], SHA)
        self.assertEqual(e["m7_final_candidate_sha256"], SHA)
        self.assertEqual(e["previous_approved_list_sha256"], OLD_SHA)
        self.assertEqual(e["approved_list_artifact"], NEW.relative_to(ROOT).as_posix())
        self.assertEqual(e["previous_approved_list_artifact"], OLD.relative_to(ROOT).as_posix())
        self.assertEqual(e["m7_owner_approval_date"], "2026-10-24")
        self.assertEqual(e["m7_archidekt_tags"], ["cEDH","Spellslinger","Combo"])
        self.assertEqual(e["m7_power_bracket"], "5 — fringe cEDH")
        self.assertEqual(e["m7_project_exceptions"], [])
        self.assertEqual(sum(bool(v.get("m7_final_candidate_sha256")) for v in self.registry.values()),29)
        differences = {k for k,v in self.registry.items()
                       if v["approved_list_sha256"] != self.snapshot[k]}
        self.assertEqual(differences, {ID, "Grixistax___October_2026", "Loki__the_Deceiver", "Lord_of_Tresserhorn", "Lord_Xander__the_Collector"})
        # Deck #27 is a later, independent owner approval; its exact approval,
        # historical source, and other 61 locks have separate fail-closed tests.
        for k,e in self.registry.items():
            with self.subTest(deck=k):
                self.assertEqual(digest(ROOT / e["approved_list_artifact"]), e["approved_list_sha256"])
        row = next(r for r in self.tracker if r["deck_id"] == ID)
        self.assertEqual(row["index"], "25")
        self.assertEqual(row["final_list_hash"], SHA)
        self.assertEqual(row["user_approval_date"], "2026-10-24")
        self.assertEqual(row["final_gate_passed"], "YES")
        self.assertIn("APPROVED / LOCKED",row["refinement_status"])

    def test_required_m6_case_transfer_is_all_pass_on_exact_100(self):
        a = self.attestation
        self.assertEqual(a["approved_raw_sha256"],SHA)
        self.assertEqual(a["deck_id"],ID)
        self.assertEqual(a["engineering"]["head_sha"],"cd52815e58b540b400b25fdf6de2b3d5b291583d")
        self.assertIn("40141945074",a["engineering"]["m7_decision_gate_ci_run_url"])
        x = a["m6_transfer"]
        self.assertEqual(x["ij_scope"],"TRANSFERRED_WITH_CASE_MAPPING")
        self.assertEqual({r["case_id"] for r in x["P0"]},{"C1","K1","K2","K3","F1"})
        self.assertEqual({r["case_id"] for r in x["P1"]},
                         {"K4","K5","E1","E2","W1","W2","W3","F2","F3"})
        for record in x["P0"]+x["P1"]:
            with self.subTest(case=record["case_id"]):
                self.assertEqual(record["status"],"PASSED")
                self.assertEqual(record["scope"],"EXACT_APPROVED_100")
                self.assertEqual(record["tested_raw_sha256"],SHA)
                self.assertIn("40141945074",record["ci_run_url"])
                self.assertIn("test_m6_kess_rev1_case_transfer",record["test_ref"])
                self.assertTrue(record["payable_fixture"] and record["adversarial_assertion"])


if __name__ == "__main__":
    unittest.main()
