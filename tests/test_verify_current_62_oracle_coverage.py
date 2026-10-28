"""Regression tests for exact-head Oracle coverage and exception controls."""
import json
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verify_current_62_oracle_coverage as verifier  # noqa: E402


class CurrentOracleCoverageTest(unittest.TestCase):
    def modified_cache_audit(self, records):
        with tempfile.TemporaryDirectory() as folder:
            cache = Path(folder) / "cache.jsonl"
            summary_path = Path(folder) / "summary.json"
            cache.write_text("".join(json.dumps(rec) + "\n" for rec in records))
            summary = json.loads(verifier.SUMMARY.read_text())
            summary["cache_sha256"] = hashlib.sha256(cache.read_bytes()).hexdigest()
            summary_path.write_text(json.dumps(summary))
            with patch.object(verifier, "CACHE", cache), patch.object(verifier, "SUMMARY", summary_path):
                return verifier.audit()

    def test_all_approved_lists_are_covered(self):
        result = verifier.audit()
        self.assertEqual(result["exact_locked_decks"], 62)
        self.assertEqual(result["playable_cards"], 6200)
        self.assertEqual(result["nonlegal_entries_with_explicit_project_exception"], 6)

    def test_missing_late_record_is_blocking(self):
        records = [json.loads(line) for line in verifier.CACHE.read_text().splitlines()]
        records = [rec for rec in records if rec["query_name"] != "The Meathook Massacre"]
        with self.assertRaisesRegex(ValueError, "missing late Tresserhorn"):
            self.modified_cache_audit(records)

    def test_unapproved_illegality_is_blocking(self):
        records = [json.loads(line) for line in verifier.CACHE.read_text().splitlines()]
        for rec in records:
            if rec["query_name"] == "Genesis Chamber":
                rec["commander_legality"] = "banned"
                break
        with self.assertRaisesRegex(ValueError, "unapproved official legality exception"):
            self.modified_cache_audit(records)


if __name__ == "__main__":
    unittest.main()
