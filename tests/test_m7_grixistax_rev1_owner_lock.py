"""Fail-closed exact owner-approval lock for Deck #27 Grixistax M7 Rev1."""
import csv
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DECK = "Grixistax___October_2026"
SHA = "70b48148409e849e38d7189bcda032d1c98d74329302563a005f86a86b81279e"
OLD_SHA = "f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c"
SOURCE = ROOT / "refinement/decklists/Grixistax_October_2026_M7_Rev1_Approved_2026-10-25.txt"
HISTORICAL = ROOT / "refinement/decklists/Grixistax_October_2026_Approved_2026-10-14.txt"
RECEIPT = ROOT / "refinement/approvals/Grixistax_October_2026_M7_Rev1_Approved_2026-10-25.md"
VERIFY = ROOT / "refinement/verification/Grixistax_October_2026_M7_Rev1_Approved_2026-10-25_Verification.md"
INDEX = ROOT / "refinement/verification/Grixistax_October_2026_M7_Rev1_Oracle_Identity_Index_2026-10-25.json"
ATTEST = ROOT / "refinement/verification/m7_certification_transfer/Grixistax___October_2026_70b48148409e849e.json"
REGISTRY = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
SNAPSHOT = ROOT / "refinement/verification/m7_certification_transfer/frozen_approval_snapshot_2026-10-24.json"

ADDS = {"Arcane Signet", "Bitterblossom", "Opposition", "Phyrexian Altar", "Ophiomancer"}
CUTS = {"Mox Amber", "Magus of the Moon", "Ashiok, Dream Render", "Damping Sphere", "Sheoldred, the Apocalypse"}
CORE = {"Contamination", "Skullclamp", "Winter Orb", "Static Orb", "Tangle Wire",
        "Blood Moon", "Back to Basics", "Trinisphere", "Chalice of the Void",
        "Cursed Totem", "Torpor Orb", "Overburden", "Karn, the Great Creator",
        "Helm of Obedience", "Leyline of the Void", "Dauthi Voidwalker",
        "Underworld Breach", "Lion's Eye Diamond", "Brain Freeze",
        "Wheel of Fortune", "Windfall", "Narset, Parter of Veils",
        "Notion Thief", "Ragavan, Nimble Pilferer"}
P0 = {"C1", "C2", "K1", "K2", "K3", "F1"}
P1 = {"K4", "K5", "E1", "E2", "W1", "W2", "W3", "F2", "F3"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def physical_names(path):
    cards = path.read_text(encoding="utf-8").splitlines()
    return cards, {line.removeprefix("1x ").removesuffix(" [Commander]") for line in cards}


class GrixistaxM7Rev1ExactOwnerLock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = SOURCE.read_bytes()
        cls.cards, cls.names = physical_names(SOURCE)
        cls.old_cards, cls.old_names = physical_names(HISTORICAL)
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))["decks"]
        cls.snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))["approved_sha256_by_deck"]
        cls.oracle = json.loads(INDEX.read_text(encoding="utf-8"))
        cls.attest = json.loads(ATTEST.read_text(encoding="utf-8"))
        with TRACKER.open(newline="", encoding="utf-8") as stream:
            cls.tracker = list(csv.DictReader(stream))

    def test_exact_raw_sha_two_partners_100_unique_and_historical_source_immutable(self):
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), SHA)
        self.assertTrue(self.raw.endswith(b"\n"))
        self.assertFalse(self.raw.endswith(b"\n\n"))
        self.assertEqual(digest(HISTORICAL), OLD_SHA)
        self.assertEqual(len(self.cards), 100)
        self.assertEqual(len(self.names), 100)
        self.assertTrue(all(line.startswith("1x ") for line in self.cards))
        self.assertEqual(self.cards[:2], [
            "1x Kraum, Ludevic's Opus [Commander]",
            "1x Tevesh Szat, Doom of Fools [Commander]",
        ])
        self.assertEqual(sum(line.endswith(" [Commander]") for line in self.cards), 2)

    def test_five_for_five_and_original_stax_combo_wheel_identity(self):
        self.assertEqual(self.names - self.old_names, ADDS)
        self.assertEqual(self.old_names - self.names, CUTS)
        self.assertTrue(CORE <= self.names)
        self.assertEqual(len(self.names & self.old_names), 95)
        self.assertFalse({"Thassa's Oracle", "Demonic Consultation", "Urza, Lord High Artificer"} & self.names)

    def test_selected_current_oracle_legal_ubr_26_land_22_game_changers(self):
        idx = self.oracle
        self.assertEqual(idx["candidate_raw_sha256"], SHA)
        self.assertEqual(idx["source_date"], "2026-10-25")
        self.assertEqual(idx["archived_selected_count"], 98)
        self.assertEqual(idx["new_scryfall_page_selected_count"], 2)
        self.assertEqual(len(idx["cards"]), 100)
        self.assertEqual({c["name"] for c in idx["cards"]}, self.names)
        for c in idx["cards"]:
            with self.subTest(name=c["name"]):
                self.assertEqual(c["commander_legality"], "legal")
                self.assertTrue(set(c["color_identity"]) <= {"B", "U", "R"})
                self.assertTrue(c["oracle_text"])
                # Ophiomancer and Phyrexian Altar pages are sources, not invented IDs.
                if c["name"] in {"Ophiomancer", "Phyrexian Altar"}:
                    self.assertIsNone(c["oracle_id"])
                    self.assertTrue(c["oracle_source_url"].startswith("https://scryfall.com/card/"))
        self.assertEqual(sum("Land" in c["type_line"] for c in idx["cards"]), 26)
        self.assertEqual(sum(bool(c["game_changer"]) for c in idx["cards"]), 22)

    def test_owner_receipt_verification_and_disclosed_damping_sheoldred_losses(self):
        receipt = RECEIPT.read_text(encoding="utf-8")
        verification = VERIFY.read_text(encoding="utf-8")
        for body in (receipt, verification):
            self.assertIn(SHA, body)
            self.assertIn(OLD_SHA, body)
            self.assertIn("#705", body)
            self.assertIn("100", body)
        self.assertIn("“Approve”", receipt)
        self.assertIn("Damping Sphere", receipt)
        self.assertIn("Sheoldred", receipt)
        self.assertIn("not", verification.lower())
        self.assertIn("establish empirical multiplayer win rates", receipt.lower())
        self.assertIn("15", verification)

    def test_only_target_registry_change_after_prior_kess_snapshot_and_tracker_reconciled(self):
        self.assertEqual(len(self.registry), 62)
        self.assertEqual(len(self.tracker), 62)
        entry = self.registry[DECK]
        self.assertEqual((entry["approval_status"], entry["lock_status"], entry["current_stage"]),
                         ("APPROVED", "LOCKED", "LOCKED"))
        self.assertTrue(entry["final_gate_passed"])
        self.assertEqual(entry["approved_list_sha256"], SHA)
        self.assertEqual(entry["m7_final_candidate_sha256"], SHA)
        self.assertEqual(entry["previous_approved_list_sha256"], OLD_SHA)
        self.assertEqual(entry["user_approval_date"], "2026-10-25")
        self.assertEqual(entry["m7_owner_approval_date"], "2026-10-25")
        self.assertEqual(entry["approved_list_artifact"], SOURCE.relative_to(ROOT).as_posix())
        self.assertEqual(entry["previous_approved_list_artifact"], HISTORICAL.relative_to(ROOT).as_posix())
        self.assertEqual(entry["m7_archidekt_tags"], ["Grixis Stax", "Thrull Sacrifice", "Helm–Breach Combo"])
        self.assertEqual(entry["m7_project_exceptions"], [])
        self.assertGreaterEqual(sum(bool(e.get("m7_final_candidate_sha256")) for e in self.registry.values()), 30)
        differences = {
            name for name, value in self.registry.items()
            if value["approved_list_sha256"] != self.snapshot[name]
        }
        required_prior = {"Kess__Dissident_Mage", DECK, "Loki__the_Deceiver", "Lord_of_Tresserhorn", "Lord_Xander__the_Collector", "Lynde__Cheerful_Tormentor"}
        self.assertTrue(required_prior.issubset(differences))
        for later in differences - required_prior:
            self.assertEqual(self.registry[later].get("previous_approved_list_sha256"), self.snapshot[later], later)
            self.assertTrue(self.registry[later].get("m7_owner_approval_date"), later)
        for name, e in self.registry.items():
            with self.subTest(deck=name):
                self.assertEqual(digest(ROOT / e["approved_list_artifact"]), e["approved_list_sha256"])
        row = next(r for r in self.tracker if r["deck_id"] == DECK)
        self.assertEqual(row["index"], "26")
        self.assertEqual(row["final_gate_passed"], "YES")
        self.assertEqual(row["final_list_hash"], SHA)
        self.assertEqual(row["user_approval_date"], "2026-10-25")
        self.assertIn("APPROVED / LOCKED", row["refinement_status"])

    def test_all_15_blueprint_p0_p1_cases_exact_source_and_ci_provenance(self):
        a = self.attest
        self.assertEqual(a["deck_id"], DECK)
        self.assertEqual(a["approved_raw_sha256"], SHA)
        self.assertEqual(a["approved_artifact"], SOURCE.relative_to(ROOT).as_posix())
        self.assertEqual(a["engineering"]["head_sha"], "dca07c0f58e751398ecc2d29753da4a65542bb14")
        self.assertIn("40175693250", a["engineering"]["m7_decision_gate_ci_run_url"])
        transfer = a["m6_transfer"]
        self.assertEqual(transfer["ij_scope"], "TRANSFERRED_WITH_CASE_MAPPING")
        self.assertEqual({c["case_id"] for c in transfer["P0"]}, P0)
        self.assertEqual({c["case_id"] for c in transfer["P1"]}, P1)
        for c in transfer["P0"] + transfer["P1"]:
            with self.subTest(case=c["case_id"]):
                self.assertEqual(c["status"], "PASSED")
                self.assertEqual(c["scope"], "EXACT_APPROVED_100")
                self.assertEqual(c["tested_raw_sha256"], SHA)
                self.assertIn("40175693250", c["ci_run_url"])
                self.assertIn("test_m6_grixistax_rev1_case_transfer", c["test_ref"])
                self.assertTrue(c["payable_fixture"])
                self.assertTrue(c["positive_assertion"])
                self.assertTrue(c["adversarial_assertion"])


if __name__ == "__main__":
    unittest.main()
