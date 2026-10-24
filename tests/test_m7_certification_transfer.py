"""Mandatory exact-SHA M6/IJ provenance transfer regression tests."""
import copy
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from scripts.verify_m7_certification_transfer import (
    ATTESTATIONS, FROZEN, PLANS, REGISTRY, ROOT,
    EvidenceError, validate_attestation, validate_case_records, validate_live_state,
)


class TransferEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        raw = b"1x Kefka, Court Mage // Kefka, Ruler of Ruin [Commander]\n"
        self.sha = hashlib.sha256(raw).hexdigest()
        self.approved = {
            "approved_list_sha256": self.sha,
            "approved_list_artifact": "refinement/decklists/Kefka_Test.txt",
            "approval_status": "APPROVED",
            "lock_status": "LOCKED",
        }
        self.write(self.approved["approved_list_artifact"], raw)
        self.write("refinement/approvals/Kefka_Test.md", f"Approved exact {self.sha}\n".encode())
        self.required = {
            "source_path": "data/grixis/m6/test_blueprints/Kefka__Court_Mage.json",
            "plan_blob_sha": "a" * 40,
            "required_P0": ["C1", "K1"],
            "required_P1": ["F2"],
        }
        self.doc = {
            "schema_version": 1,
            "deck_id": "Kefka__Court_Mage",
            "approved_raw_sha256": self.sha,
            "approved_artifact": self.approved["approved_list_artifact"],
            "owner_approval_receipt": "refinement/approvals/Kefka_Test.md",
            "engineering": {
                "pr_url": "https://github.com/corymstover/GrokBotMTGCompanion/pull/701",
                "head_sha": "b" * 40,
                "grok_first_pass_ref": "PR #673",
                "independent_review_ref": "data/grixis/m7/independent_reviews/Kefka.md",
                "m7_decision_packet_ref": "data/grixis/m7/decision_reviews/Kefka__Court_Mage.json",
                "m7_decision_gate_command": "python scripts/grixis_m7_decision_gate.py --check",
                "m7_decision_gate_ci_run_url": "https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/123",
                "oracle_legality_ref": "data/grixis/m6/oracle_snapshots/Kefka.json",
            },
            "m6_transfer": {
                "plan_source_path": self.required["source_path"],
                "plan_blob_sha": self.required["plan_blob_sha"],
                "ij_receipt_ref": "data/grixis/m6/ij/certificates/kefka-court-mage-m7.json",
                "ij_scope": "TRANSFERRED_WITH_CASE_MAPPING",
                "revision_diff_and_validity_reason": "Compare Grok's prior tested candidate with the exact newly approved deck.",
                "P0": [self.passed_case("C1"), self.passed_case("K1")],
                "P1": [self.passed_case("F2")],
            },
        }

    def write(self, rel, value):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(value)

    def passed_case(self, case_id):
        return {
            "case_id": case_id,
            "status": "PASSED",
            "test_ref": "tests/test_m6_kefka_court_mage_m7_mechanics.py::test_case",
            "execution_command": "python -m unittest tests.test_m6_kefka_court_mage_m7_mechanics",
            "oracle_source": "data/grixis/m6/oracle_snapshots/Kefka.json",
            "payable_fixture": "Pay exact UBR and generic costs in a defined four-player state.",
            "positive_assertion": "Legal Kefka trigger resolves exactly once.",
            "adversarial_assertion": "Trigger cannot resolve when named precondition is absent.",
            "ci_run_url": "https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/123",
            "scope": "EXACT_APPROVED_100",
            "tested_raw_sha256": self.sha,
        }

    def validate(self, doc=None, approved=None, required=None):
        validate_attestation(
            self.root, "Kefka__Court_Mage", approved or self.approved,
            required or self.required, doc or self.doc,
        )

    def test_proper_exact_sha_transfer_is_accepted(self):
        self.validate()

    def test_missing_required_p0_fails_closed(self):
        changed = copy.deepcopy(self.doc)
        changed["m6_transfer"]["P0"].pop()
        with self.assertRaisesRegex(EvidenceError, "inventory mismatch"):
            self.validate(changed)

    def test_unrun_p0_cannot_be_papered_over(self):
        changed = copy.deepcopy(self.doc)
        changed["m6_transfer"]["P0"][0]["status"] = "DEFERRED"
        with self.assertRaisesRegex(EvidenceError, "P0 may not be deferred"):
            self.validate(changed)

    def test_unclear_prior_candidate_scope_fails_closed(self):
        changed = copy.deepcopy(self.doc)
        case = changed["m6_transfer"]["P0"][0]
        case["scope"] = "REUSED_UNCHANGED"
        case.pop("tested_raw_sha256")
        case["prior_candidate_sha256"] = "c" * 64
        with self.assertRaisesRegex(EvidenceError, "explain why"):
            self.validate(changed)

    def test_documented_valid_reuse_is_accepted(self):
        changed = copy.deepcopy(self.doc)
        case = changed["m6_transfer"]["P0"][0]
        case["scope"] = "REUSED_UNCHANGED"
        case.pop("tested_raw_sha256")
        case["prior_candidate_sha256"] = "c" * 64
        case["transfer_rationale"] = (
            "The effect, source cards, triggers and payments are unchanged "
            "in the selected add/cut package; unchanged assertions were rerun."
        )
        self.validate(changed)

    def test_p1_deferral_requires_visible_consequence(self):
        changed = copy.deepcopy(self.doc)
        changed["m6_transfer"]["P1"] = [{"case_id": "F2", "status": "DEFERRED",
                                              "specific_reason": "Off-plan line"}]
        with self.assertRaisesRegex(EvidenceError, "coverage_consequence"):
            self.validate(changed)

    def test_documented_p1_deferral_is_not_falsely_passed(self):
        changed = copy.deepcopy(self.doc)
        changed["m6_transfer"]["P1"] = [{
            "case_id": "F2", "status": "DEFERRED", "specific_reason": "Off-plan line",
            "coverage_consequence": "No conclusion about this interaction",
            "owner_visible_unresolved": True,
        }]
        self.validate(changed)

    def test_wrong_approved_file_bytes_fail(self):
        self.write(self.approved["approved_list_artifact"], b"changed without SHA\n")
        with self.assertRaisesRegex(EvidenceError, "raw bytes disagree"):
            self.validate()

    def test_original_ij_cannot_be_called_same_exact_100_without_scope(self):
        changed = copy.deepcopy(self.doc)
        changed["m6_transfer"].pop("ij_scope")
        with self.assertRaisesRegex(EvidenceError, "distinguish original I/J"):
            self.validate(changed)

    def test_approval_receipt_must_name_approved_sha(self):
        self.write("refinement/approvals/Kefka_Test.md", b"Approve something else\n")
        with self.assertRaisesRegex(EvidenceError, "does not name exact"):
            self.validate()

    def test_duplicate_case_claims_fail(self):
        records = [self.passed_case("C1"), self.passed_case("C1")]
        with self.assertRaisesRegex(EvidenceError, "duplicate P0"):
            validate_case_records("P0", records, ["C1"], "Kefka", self.sha)


class CompleteRegistryGateTests(unittest.TestCase):
    def test_frozen_actual_24_new_m7_locks_remain_unchanged(self):
        result = validate_live_state(ROOT)
        self.assertEqual(61, result["source_plans"])
        self.assertEqual([], result["new_or_revised_approvals_with_case_evidence"])

    def test_new_kefka_approval_without_evidence_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for rel in (FROZEN, PLANS):
                target = root / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / rel, target)
            reg = json.loads((ROOT / REGISTRY).read_text(encoding="utf-8"))
            reg["decks"]["Kefka__Court_Mage"]["approved_list_sha256"] = "f" * 64
            target = root / REGISTRY
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(reg), encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "Missing evidence file"):
                validate_live_state(root)


if __name__ == "__main__":
    unittest.main()
