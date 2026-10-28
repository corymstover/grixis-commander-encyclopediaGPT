"""M8 release candidate must reproduce 62 locked sources and all 18 missing tags."""
import json
from hashlib import sha256
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_m8_release_export as release
from verify_m8_current_certification import inspect, read_current

class ExactM8MetadataRelease(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = release.payloads()
        cls.index = json.loads(cls.files["index.json"])
        cls.summary = json.loads(cls.files["M8_EVIDENCE_SUMMARY.json"])
        cls.ledger = json.loads(cls.files["M8_EVIDENCE_LEDGER.json"])

    def test_all_62_source_bytes_unchanged_and_import_hashes(self):
        sources = {d["id"]: d for d in read_current()}
        self.assertEqual(len(self.index["decks"]), 62)
        self.assertEqual(len(self.files), 129)
        for row in self.index["decks"]:
            self.assertEqual(sha256(self.files[row["archive_source"]]).hexdigest(),
                             sources[row["deck_id"]]["sha256"])
            self.assertEqual(sha256(self.files[row["archidekt_file"]]).hexdigest(),
                             row["archidekt_sha256"])
            self.assertTrue(row["power_bracket"])
            self.assertEqual(len(row["archidekt_tags"]), 3)

    def test_six_historically_missing_metadata_from_approved_records(self):
        known = release.metadata_map()
        rows = {r["commander"]: r for r in self.index["decks"]}
        self.assertEqual(len(known), 6)
        for name, entry in known.items():
            self.assertEqual(rows[name]["power_bracket"], "4 — Optimized")
            self.assertEqual(rows[name]["archidekt_tags"], entry["archidekt_tags"])
            self.assertEqual(rows[name]["metadata_provenance"], str(release.METADATA.relative_to(ROOT)))
        self.assertEqual(self.index["metadata_gaps"], [])
        self.assertEqual(self.summary["missing_bracket_or_tag_metadata"], [])

    def test_evidence_complete_release_not_presigned(self):
        report = inspect(self.ledger)
        self.assertEqual(report["current_sha_case_dispositions"], 180)
        self.assertEqual(report["P1_pending_current_disposition"], 0)
        self.assertEqual(report["current_sha_commander_first_attestations"], 62)
        self.assertEqual(self.index["release_fingerprint"], report["release_fingerprint"])
        self.assertEqual(self.index["evidence_fingerprint"], report["evidence_fingerprint"])
        self.assertIsNone(self.ledger["m8_owner_acceptance"])
        self.assertIsNone(self.index["m8_owner_acceptance"])
        self.assertFalse(report["ready_for_final_release"])
        self.assertFalse(self.index["official_commander_legality_certified"])
        self.assertEqual(self.index["status"], release.STATUS)

if __name__ == "__main__":
    unittest.main()
