"""Current-SHA M8 release must remain fail-closed until actual owner acceptance."""

import copy
import json
import re
import sys
import unittest
from collections import Counter
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
        self.assertEqual(self.report["current_sha_case_dispositions"], 47)
        self.assertEqual(self.report["P1_pending_current_disposition"], 133)
        self.assertEqual(self.report["current_sha_commander_first_attestations"], 62)
        self.assertEqual(self.report["quality_attestations_pending"], 0)
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

    def test_m8_original_p1_batch_a_exact_head_thirty_five_bounded_not_w_cases(self):
        expected = {
            "Saruman__the_White_Hand": {"K4", "K5", "K6", "K7", "K8", "K9", "K10", "E1", "E2", "F2", "F3"},
            "Missy": {"K4", "K5", "K6", "K7", "E1", "E2", "F2", "F3"},
            "RogSi": {"K4", "K6", "K7", "E1", "E2", "F2", "F3"},
            "Nekusar__the_Mindrazer": {"K4", "K6", "E1", "E2", "F2", "F3"},
            "Parnesse__the_Subtle_Brush": {"K4", "E2", "F2"},
        }
        test_blob = "d7a5d78b0a12a0fa082fabaaa05b9628baf4d24a"
        test_head = "e2d02332739bf6a4562a89ce5ac32214f8456caf"
        test_run = "https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/40671465009"
        rows = [r for r in self.base["case_dispositions"] if r.get("test_blob_sha") == test_blob]
        self.assertEqual(len(rows), 35)
        for deck, cases in expected.items():
            actual = {r["case_id"] for r in rows if r["deck_id"] == deck}
            self.assertEqual(actual, cases, deck)
        for row in rows:
            self.assertEqual(row["disposition"], "CURRENT_SHA_TESTED")
            self.assertEqual(row["engineering_commit_sha"], test_head)
            self.assertEqual(row["ci_run_url"], test_run)
            self.assertNotIn(row["case_id"][0], {"W"})
            self.assertIn("test_" , row["test_ref"])
            self.assertIn("Finite Python model", row["limitations"])
        sources = gate.read_current()
        deferred, _, _, _ = gate.current_case_index(sources)
        self.assertEqual(gate.validate_dispositions(rows, deferred, sources),
                         {(r["deck_id"], r["case_id"]) for r in rows})

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

    def test_parnesse_exact_current_positive_and_adversarial_case_evidence_is_pinned(self):
        original = [row for row in self.base["case_dispositions"]
                    if row["deck_id"] == "Parnesse__the_Subtle_Brush"
                    and row["disposition"] == "CURRENT_SHA_TESTED"
                    and row["test_blob_sha"] == "d959ec8567046da38fdfd217b39efeec5e9b5c15"]
        self.assertEqual({x["case_id"] for x in original}, {"K5", "K6", "K7", "E1", "F3"})
        decks = gate.read_current()
        deferred, _, _, _ = gate.current_case_index(decks)
        self.assertEqual(gate.validate_dispositions(original, deferred, decks),
                         {(x["deck_id"], x["case_id"]) for x in original})
        for field, wrong, message in (
            ("approved_raw_sha256", "0" * 64, "Case SHA drift"),
            ("disposition", "FAKE_PASS", "Unknown disposition"),
            ("test_blob_sha", "not-a-blob", "Missing exact test blob"),
            ("ci_run_url", "https://example.com/unverifiable", "Missing exact-head test run"),
            ("adversarial_assertion", "", "Incomplete positive/adversarial"),
        ):
            with self.subTest(field=field):
                invalid = copy.deepcopy(original[0])
                invalid[field] = wrong
                with self.assertRaisesRegex(gate.CertificationError, message):
                    gate.validate_dispositions([invalid], deferred, decks)

    def test_parnesse_whole99_quality_is_distinct_from_unfinished_p1(self):
        decks = gate.read_current()
        row = next(row for row in self.base["deck_quality_attestations"]
                   if row["deck_id"] == "Parnesse__the_Subtle_Brush")
        self.assertEqual(gate.validate_deck_attestations([row], decks),
                         {"Parnesse__the_Subtle_Brush"})
        report = gate.repo_file(row["review_path"]).read_text(encoding="utf-8")
        self.assertIn(row["approved_raw_sha256"], report)
        self.assertIn("five still deferred", report)
        self.assertIn("35 lands", report)
        for field, bad, message in (
            ("approved_raw_sha256", "0" * 64, "not for current 100"),
            ("review_sha256", "0" * 64, "Evidence SHA drift"),
            ("engineering_review_blob_sha", "unverified", "Missing Git blob commitment"),
        ):
            with self.subTest(field=field):
                invalid = copy.deepcopy(row)
                invalid[field] = bad
                with self.assertRaisesRegex(gate.CertificationError, message):
                    gate.validate_deck_attestations([invalid], decks)

    def test_fake_quality_review_cannot_be_counted(self):
        invalid = copy.deepcopy(self.base)
        invalid["deck_quality_attestations"] = [{
            "deck_id": "RogSi",
            "approved_raw_sha256": "0" * 64,
            "outcome": "KEEP_EXACT_100",
        }]
        with self.assertRaisesRegex(gate.CertificationError, "Quality review not for current"):
            gate.inspect(invalid, include_archive=False)

    def test_markdown_whole_list_review_is_sha_and_path_bound(self):
        approved = gate.read_current()
        original = next(row for row in self.base["deck_quality_attestations"]
                        if row["deck_id"] == "RogSi")
        self.assertEqual(gate.validate_deck_attestations([original], approved), {"RogSi"})
        for unsafe in (
            "data/grixis/m7/unreviewed/claim.md",
            "data/grixis/m7/decision_reviews/../../claim.md",
            "data/grixis/m7/decision_reviews/claim.txt",
        ):
            with self.subTest(path=unsafe):
                invalid = copy.deepcopy(original)
                invalid["engineering_review_path"] = unsafe
                with self.assertRaisesRegex(gate.CertificationError, "Missing exact M7 whole-list decision source"):
                    gate.validate_deck_attestations([invalid], approved)
        invalid = copy.deepcopy(original)
        invalid["engineering_review_blob_sha"] = "not-a-git-blob"
        with self.assertRaisesRegex(gate.CertificationError, "Missing Git blob commitment"):
            gate.validate_deck_attestations([invalid], approved)

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

    def test_admiral_grandfathered_case_scope_is_exact_sha_and_report_hash_bound(self):
        approved = gate.read_current()
        original = next(row for row in self.base["deck_quality_attestations"]
                        if row["deck_id"] == "Admiral_Beckett_Brass")
        self.assertEqual(gate.validate_deck_attestations([original], approved),
                         {"Admiral_Beckett_Brass"})
        for field, value, message in (
            ("approved_raw_sha256", "0" * 64, "not for current 100"),
            ("grandfathered_case_scope_sha256", "0" * 64, "Evidence SHA drift"),
            ("grandfathered_case_scope_outcome", "INCOMPLETE", "scope remains unverified"),
        ):
            with self.subTest(field=field):
                invalid = copy.deepcopy(original)
                invalid[field] = value
                with self.assertRaisesRegex(gate.CertificationError, message):
                    gate.validate_deck_attestations([invalid], approved)

    def test_unsinkable_original_cases_and_99_ledger_are_distinct_from_beckett(self):
        approved = gate.read_current()
        original = next(row for row in self.base["deck_quality_attestations"]
                        if row["deck_id"] == "Admiral_Brass__Unsinkable")
        self.assertEqual(gate.validate_deck_attestations([original], approved),
                         {"Admiral_Brass__Unsinkable"})
        current = next(x for x in approved if x["id"] == "Admiral_Brass__Unsinkable")
        scoped = gate.repo_file(original["review_path"]).read_text(encoding="utf-8")
        self.assertIn(current["sha256"], scoped)
        self.assertIn("five original P0", scoped)
        self.assertIn("eight original P1", scoped)
        counted = Counter()
        for quantity, name in re.findall(r"^- (\d+)x (.+)$", scoped, re.MULTILINE):
            counted[name] += int(quantity)
        approved_pool = Counter({name: qty for qty, name, zone in current["cards"]
                                 if zone == "Main"})
        self.assertEqual(sum(counted.values()), 99)
        self.assertEqual(counted, approved_pool)
        self.assertNotIn("Admiral Brass, Unsinkable", counted)
        for field, bad, message in (
            ("approved_raw_sha256", "0" * 64, "not for current 100"),
            ("grandfathered_case_scope_sha256", "0" * 64, "Evidence SHA drift"),
            ("grandfathered_case_scope_outcome", "INCOMPLETE", "scope remains unverified"),
        ):
            with self.subTest(field=field):
                invalid = copy.deepcopy(original)
                invalid[field] = bad
                with self.assertRaisesRegex(gate.CertificationError, message):
                    gate.validate_deck_attestations([invalid], approved)

    def test_anhelo_current_fodder_case_scope_and_full_99_from_owner_approved_rev2(self):
        approved = gate.read_current()
        row = next(x for x in self.base["deck_quality_attestations"]
                   if x["deck_id"] == "Anhelo_the_Painter")
        self.assertEqual(gate.validate_deck_attestations([row], approved),
                         {"Anhelo_the_Painter"})
        current = next(x for x in approved if x["id"] == "Anhelo_the_Painter")
        report = gate.repo_file(row["review_path"]).read_text(encoding="utf-8")
        self.assertIn(current["sha256"], report)
        for marker in ("P0", "P1", "Maestros Ascendancy removed", "seven static rocks"):
            self.assertIn(marker, report)
        counted = Counter()
        for quantity, name in re.findall(r"^- (\d+)x (.+)$", report, re.MULTILINE):
            counted[name] += int(quantity)
        pool = Counter({name: quantity for quantity, name, zone in current["cards"]
                        if zone == "Main"})
        self.assertEqual(sum(counted.values()), 99)
        self.assertEqual(counted, pool)
        for field, wrong, message in (
            ("approved_raw_sha256", "0" * 64, "not for current 100"),
            ("grandfathered_case_scope_sha256", "0" * 64, "Evidence SHA drift"),
            ("grandfathered_case_scope_outcome", "INCOMPLETE", "scope remains unverified"),
        ):
            bad = copy.deepcopy(row)
            bad[field] = wrong
            with self.assertRaisesRegex(gate.CertificationError, message):
                gate.validate_deck_attestations([bad], approved)

    def test_ashad_rev3_current_99_and_oracle_corrections_have_scoped_evidence(self):
        approved = gate.read_current()
        row = next(x for x in self.base["deck_quality_attestations"]
                   if x["deck_id"] == "Ashad_the_Lone_Cyberman")
        self.assertEqual(gate.validate_deck_attestations([row], approved),
                         {"Ashad_the_Lone_Cyberman"})
        current = next(x for x in approved if x["id"] == "Ashad_the_Lone_Cyberman")
        report = gate.repo_file(row["review_path"]).read_text(encoding="utf-8")
        self.assertIn(current["sha256"], report)
        for marker in ("five P0", "nine P1", "Reckless Fireweaver", "Noxious Gearhulk",
                       "32 lands", "Twinning Staff"):
            self.assertIn(marker, report)
        counted = Counter()
        for quantity, name in re.findall(r"^- (\d+)x (.+)$", report, re.MULTILINE):
            counted[name] += int(quantity)
        pool = Counter({name: quantity for quantity, name, zone in current["cards"]
                        if zone == "Main"})
        self.assertEqual(sum(counted.values()), 99)
        self.assertEqual(counted, pool)
        for field, wrong, error in (
            ("approved_raw_sha256", "0" * 64, "not for current 100"),
            ("grandfathered_case_scope_sha256", "0" * 64, "Evidence SHA drift"),
            ("engineering_review_blob_sha", "not-a-blob", "Missing Git blob commitment"),
        ):
            with self.subTest(field=field):
                invalid = copy.deepcopy(row)
                invalid[field] = wrong
                with self.assertRaisesRegex(gate.CertificationError, error):
                    gate.validate_deck_attestations([invalid], approved)

    def test_original_nicol_bolas_current_99_copy_ledger_not_ravager(self):
        decks = gate.read_current()
        current = next(x for x in decks if x["id"] == "Nicol_Bolas")
        row = next(x for x in self.base["deck_quality_attestations"]
                   if x["deck_id"] == "Nicol_Bolas")
        self.assertEqual(gate.validate_deck_attestations([row], decks), {"Nicol_Bolas"})
        text = gate.repo_file(row["review_path"]).read_text(encoding="utf-8")
        self.assertIn(current["sha256"], text)
        roster = Counter({name: quantity for quantity, name, zone in current["cards"]
                          if zone == "Main"})
        ledger = Counter()
        for quantity, name in re.findall(r"^- (\d+)x (.+)$", text, re.MULTILINE):
            ledger[name] += int(quantity)
        self.assertEqual(sum(ledger.values()), 99)
        self.assertEqual(ledger, roster)
        self.assertNotIn("Nicol Bolas", ledger)
        self.assertIn("Nicol Bolas, the Ravager // Nicol Bolas, the Arisen", ledger)
        for field, invalid_value, error in (
            ("approved_raw_sha256", "0" * 64, "not for current 100"),
            ("review_sha256", "0" * 64, "Evidence SHA drift"),
            ("engineering_review_blob_sha", "invalid", "Missing Git blob commitment"),
        ):
            with self.subTest(field=field):
                tampered = copy.deepcopy(row)
                tampered[field] = invalid_value
                with self.assertRaisesRegex(gate.CertificationError, error):
                    gate.validate_deck_attestations([tampered], decks)

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
