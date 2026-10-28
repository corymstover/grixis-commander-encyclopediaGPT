"""Regression tests for exact-head Oracle coverage and exception controls."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verify_current_62_oracle_coverage as verifier  # noqa: E402


class CurrentOracleCoverageTest(unittest.TestCase):
    def test_all_approved_lists_are_covered(self):
        result = verifier.audit()
        self.assertEqual(result["exact_locked_decks"], 62)
        self.assertEqual(result["playable_cards"], 6200)
        self.assertEqual(result["nonlegal_entries_with_explicit_project_exception"], 6)

    def test_missing_late_record_is_blocking(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "supplement.jsonl"
            lines = verifier.SUPPLEMENT.read_text().splitlines()
            path.write_text("\n".join(lines[:-1]) + "\n")
            with patch.object(verifier, "SUPPLEMENT", path):
                with self.assertRaisesRegex(ValueError, "Oracle cache gap"):
                    verifier.audit()

    def test_unapproved_illegality_is_blocking(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "supplement.jsonl"
            lines = [json.loads(line) for line in verifier.SUPPLEMENT.read_text().splitlines()]
            lines[0]["commander_legality"] = "banned"
            path.write_text("".join(json.dumps(rec) + "\n" for rec in lines))
            with patch.object(verifier, "SUPPLEMENT", path):
                with self.assertRaisesRegex(ValueError, "unapproved official legality exception"):
                    verifier.audit()


if __name__ == "__main__":
    unittest.main()
