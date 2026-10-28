"""Current-SHA M8 release must remain fail-closed until actual owner acceptance."""

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verify_m8_current_certification as gate


class CurrentSHAReleaseGate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads((ROOT / gate.EVIDENCE).read_text(encoding="utf-8"))
        cls.report = gate.inspect(cls.base)

    def test_snapshot_has_exact_canonical_sources_but_not_release_claim(self):
        self.assertEqual(self.report["approved_locked_exact_decks"], 62)
        self.assertEqual(self.report["playable_cards"], 6200)
        self.assertEqual(self.report["current_M7_transfer_receipts"], 38)
        self.assertEqual(self.report["historical_grandfathered_decks"], 24)
        self.assertEqual(self.report["original_deferred_P1"], 180)
        self.assertEqual(self.report["current_sha_case_dispositions"], 7)
        self.assertEqual(self.report["P1_pending_current_disposition"], 173)
        self.assertEqual(self.report["current_sha_commander_first_attestations"], 24)
        self.assertEqual(self.report["quality_attestations_pending"], 38)
        self.assertEqual(self.report["transferred_P0_passed"], 192)
        self.assertEqual(self.report["transferred_P1_passed"], 193)
        self.assertFalse(self.report["ready_for_final_release"])
        self.assertEqual(self.report["historical_M6_J_counted_as_current"], 0)
        self.assertEqual(len(self.report["release_fingerprint"]), 64)
        self.assertEqual(len(self.report["evidence_fingerprint"]), 64)

    def test_old_certificates_cannot_be_relabelled_as_current(self):
        invalid = copy.deepcopy(self.base)
        invalid["historical_m6_j_relabelled_as_current"] = True
        with self.assertRaisesRegex(gate.CertificationError, "may not relabel historical J"):
            gate.inspect(invalid, include_archive=False)

    def test_owner_acceptance_cannot_be_inferred_or_pre_signed(self):
        invalid = copy.deepcopy(self.base)
        invalid["m8_owner_acceptance"] = {"release_fingerprint": self.report["release_fingerprint"]}
        with self.assertRaisesRegex(gate.CertificationError, "cannot predate unresolved"):
            gate.inspect(invalid, include_archive=False)

    def test_no_duplicate_or_non_original_case_dispositions(self):
        original = ("Kefka__Court_Mage", "K4")
        deferred, _, _, _ = gate.current_case_index(gate.read_current())
        self.assertIn(original, deferred)
        for wrong in ({"deck_id": "Abaddon_the_Despoiler", "case_id": "BOGUS"},
                      {"deck_id": "Kefka__Court_Mage", "case_id": "K1"}):
            with self.subTest(case=wrong):
                with self.assertRaisesRegex(gate.CertificationError, "not a currently deferred"):
                    gate.validate_dispositions([wrong], deferred, gate.read_current())

    def test_current_sha_must_bind_each_case_and_retired_card_be_absent(self):
        decks = gate.read_current()
        deferred, _, _, _ = gate.current_case_index(decks)
        sha = next(x["sha256"] for x in decks if x["id"] == "Kefka__Court_Mage")
        entry = {
            "deck_id": "Kefka__Court_Mage", "case_id": "K4",
            "approved_raw_sha256": sha,
            "disposition": "SUPERSEDED_BY_APPROVED_REVISION",
            "reason": "Demonic Counsel was physically cut and its delirium-only line is no longer claimed in this build.",
            "evidence_path": "refinement/verification/m7_certification_transfer/Kefka__Court_Mage_14277f6e9774c5ef.json",
            "evidence_sha256": gate.sha(ROOT / "refinement/verification/m7_certification_transfer/Kefka__Court_Mage_14277f6e9774c5ef.json"),
            "removed_source_cards": ["Demonic Counsel"],
            "surviving_line_disposition": "No Counsel successor claim; remaining Breach loop reviewed separately.",
        }
        self.assertEqual(gate.validate_dispositions([entry], deferred, decks), {("Kefka__Court_Mage", "K4")})
        bad_sha = copy.deepcopy(entry)
        bad_sha["approved_raw_sha256"] = "0" * 64
        with self.assertRaisesRegex(gate.CertificationError, "Case SHA drift"):
            gate.validate_dispositions([bad_sha], deferred, decks)
        bad_removed = copy.deepcopy(entry)
        bad_removed["removed_source_cards"] = ["Underworld Breach"]
        with self.assertRaisesRegex(gate.CertificationError, "still in exact 100"):
            gate.validate_dispositions([bad_removed], deferred, decks)

        bad_provenance = copy.deepcopy(entry)
        bad_provenance["evidence_sha256"] = "0" * 64
        with self.assertRaisesRegex(gate.CertificationError, "Evidence SHA drift"):
            gate.validate_dispositions([bad_provenance], deferred, decks)

    def test_submitted_obsolete_case_cannot_be_recounted_twice(self):
        invalid = copy.deepcopy(self.base)
        invalid["case_dispositions"].append(copy.deepcopy(invalid["case_dispositions"][0]))
        with self.assertRaisesRegex(gate.CertificationError, "Duplicate case disposition"):
            gate.inspect(invalid, include_archive=False)

    def test_fake_quality_review_cannot_be_counted(self):
        invalid = copy.deepcopy(self.base)
        invalid["deck_quality_attestations"] = [{
            "deck_id": "RogSi",
            "approved_raw_sha256": "0" * 64,
            "outcome": "KEEP_EXACT_100",
        }]
        with self.assertRaisesRegex(gate.CertificationError, "Quality review not for current"):
            gate.inspect(invalid, include_archive=False)

    def test_grandfathered_quality_cannot_substitute_for_unexecuted_cases(self):
        approved = gate.read_current()
        target = next(x for x in approved if x["id"] == "Abaddon_the_Despoiler")
        attestation = {
            "deck_id": target["id"],
            "approved_raw_sha256": target["sha256"],
            "outcome": "KEEP_EXACT_100",
            "commander_first": "Cascade/life loss",
            "mana_and_protection": "Source-paid colored acceleration",
            "win_lines_and_counterplay": "Multiple real combo lines",
            "historical_M6_case_scope": "Historical P0/P1 review remains separate",
            "tested_pool_stop_reason": "Existing open-ended candidate challenge",
            "review_path": target["record"]["approval_record_artifact"],
            "review_sha256": gate.sha(ROOT / target["record"]["approval_record_artifact"]),
            "source_commit_sha": "a" * 40,
            "engineering_review_path": "data/grixis/m7/decision_reviews/Abaddon_the_Despoiler_rev3.json",
            "engineering_review_blob_sha": "b" * 40,
        }
        with self.assertRaisesRegex(gate.CertificationError, "Grandfathered M6 P0/P1 scope"):
            gate.validate_deck_attestations([attestation], approved)

    def test_prematurely_accepted_archive_manifest_is_rejected(self):
        with self.assertRaisesRegex(gate.CertificationError, "distinct final artifact"):
            gate.verify_final_archive("exports/Grixis_Commander_Encyclopedia_62_M8_CANDIDATE_2026-10-28.zip",
                                      "0" * 64, gate.read_current())

    def test_evidence_paths_cannot_escape_repository(self):
        for path in ("../sibling", "/tmp/whatever", ""):
            with self.subTest(path=path), self.assertRaises(gate.CertificationError):
                gate.repo_file(path)


if __name__ == "__main__":
    unittest.main()
