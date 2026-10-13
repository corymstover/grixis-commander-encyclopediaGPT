import unittest
from scripts.audit_abaddon_baseline_metadata import norm, first, BASIC_LANDS, NAME_FIELDS

class AbaddonMetadataAuditTests(unittest.TestCase):
    def test_name_normalization(self):
        self.assertEqual(norm("  ABADDON   the Despoiler "), "abaddon the despoiler")

    def test_first_nonempty_metadata_field(self):
        self.assertEqual(first({"oracle_id": "", "oracleId": "id-1"}, ("oracle_id", "oracleId")), "id-1")

    def test_basic_lands_are_the_only_duplicate_exception(self):
        self.assertIn("island", BASIC_LANDS)
        self.assertNotIn("sol ring", BASIC_LANDS)

    def test_known_overlay_name_field_candidates(self):
        self.assertIn("name", NAME_FIELDS)
        self.assertIn("card_name", NAME_FIELDS)

if __name__ == "__main__":
    unittest.main()
