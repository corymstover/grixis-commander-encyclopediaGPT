import unittest

from scripts.audit_abaddon_baseline_metadata import norm, get_value, REGISTERED_EXCEPTIONS


class AbaddonMetadataAuditTests(unittest.TestCase):
    def test_name_normalization_is_case_and_space_insensitive(self):
        self.assertEqual(norm("  ABADDON   the Despoiler "), "abaddon the despoiler")

    def test_missing_optional_field_is_empty(self):
        self.assertEqual(get_value({"oracle_id": ""}, ("oracle_id",)), "")

    def test_project_exceptions_are_explicitly_separate(self):
        self.assertIn("lutri, the spellchaser", REGISTERED_EXCEPTIONS)
        self.assertIn("trade secrets", REGISTERED_EXCEPTIONS)


if __name__ == "__main__":
    unittest.main()
