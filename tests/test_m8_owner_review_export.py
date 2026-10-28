"""The unsigned M8 owner-review package is reproducible and cannot presign."""

import json
from hashlib import sha256
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_m8_owner_review_export as review


class M8OwnerReviewUnsignedArchive(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from pathlib import Path
        import json
        live = json.loads((ROOT / "refinement/verification/m8_current_release_evidence_v1.json").read_text(encoding="utf-8"))
        if live.get("m8_owner_acceptance") is not None:
            raise unittest.SkipTest("Unsigned preview builder correctly stops after exact-M8 owner acceptance")
        cls.files = review.files_for_review()
        cls.index = json.loads(cls.files["index.json"])
        cls.summary = json.loads(cls.files["M8_EVIDENCE_SUMMARY.json"])
        cls.register = json.loads(cls.files["M8_EVIDENCE_LEDGER.json"])

    def test_exact_sixty_two_canonical_sources_and_archidekt_exports(self):
        self.assertEqual(len(self.files), 129)
        self.assertEqual(len(self.index["decks"]), 62)
        self.assertEqual(len([n for n in self.files if n.startswith("canonical_sources/")]), 62)
        self.assertEqual(len([n for n in self.files if n.startswith("decks/")]), 62)
        for deck in self.index["decks"]:
            self.assertEqual(sha256(self.files[deck["archive_source"]]).hexdigest(),
                             deck["source_sha256"])
            self.assertEqual(sha256(self.files[deck["archidekt_file"]]).hexdigest(),
                             deck["archidekt_sha256"])

    def test_evidence_180_quality_62_and_unsigned_fingerprints(self):
        self.assertEqual(len(self.register["case_dispositions"]), 180)
        self.assertEqual(len(self.register["deck_quality_attestations"]), 62)
        self.assertEqual(self.summary["original_unresolved"], 0)
        self.assertEqual(self.summary["original_dispositions_retired"], 12)
        self.assertEqual(self.summary["original_dispositions_current"], 180)
        self.assertEqual(self.index["release_fingerprint"], self.summary["release_fingerprint"])
        self.assertEqual(self.index["evidence_fingerprint"], self.summary["evidence_fingerprint"])
        self.assertIsNone(self.register["m8_owner_acceptance"])
        self.assertIsNone(self.summary["m8_owner_acceptance"])
        self.assertIsNone(self.index["m8_owner_acceptance"])
        self.assertEqual(self.index["status"], review.STATUS)
        self.assertFalse(self.index["official_commander_legality_certified"])
        self.assertIn("UNSIGNED", self.files["README.txt"].decode())

    def test_project_exceptions_and_missing_optional_metadata_exposed(self):
        exceptions = {d["deck_id"]: d["project_exceptions"] for d in self.index["decks"]
                      if d["project_exceptions"]}
        self.assertIn("Cecily__Bjorna__Lutri", exceptions)
        self.assertIn("The_Madcap_Jester", exceptions)
        self.assertEqual(self.summary["project_only_nonlegal_entries"], 6)
        self.assertEqual(len(self.index["metadata_gaps"]), 6)
        self.assertIn("Parnesse__the_Subtle_Brush", self.index["metadata_gaps"])
        self.assertTrue(all("acceptance" in s.lower() or "nonofficial" in s.lower()
                            or "metadata" in s.lower()
                            for s in self.index["release_blockers"]))


if __name__ == "__main__":
    unittest.main()
