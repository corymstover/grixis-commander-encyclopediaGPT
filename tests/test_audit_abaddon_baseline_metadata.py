import unittest

from scripts.audit_abaddon_baseline_metadata import (
    BASIC_LANDS,
    NAME_FIELDS,
    first,
    norm,
    validate_bulk_summary,
)


def valid_summary():
    return {
        "bulk_type": "default_cards",
        "deck_count": 62,
        "decklist_rows": 5964,
        "exact_matches": 5964,
        "name_variant_reviews": 0,
        "not_found": 0,
        "ambiguous": 0,
        "blank_oracle_text_rows": 0,
        "missing_oracle_id": 0,
        "generated_at_utc": "2026-10-13T04:36:45.235158+00:00",
        "bulk_updated_at": "2026-10-12T21:06:24.577+00:00",
        "color_identity_mismatches": [],
        "unresolved_printing_rows": [],
        "decks_with_unresolved_commander_identity": [],
        "unresolved_project_exception_rows": [],
        "unexpected_official_illegal_rows": [],
        "overall_result": "METADATA_REFRESH_PASS — registered exceptions remain separately labeled; rules-interaction review remains separate",
    }


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

    def test_current_bulk_summary_accepts_clean_refresh(self):
        summary = valid_summary()
        self.assertIs(validate_bulk_summary(summary), summary)

    def test_current_bulk_summary_rejects_missing_or_unmatched_rows(self):
        summary = valid_summary()
        summary["not_found"] = 1
        with self.assertRaises(ValueError):
            validate_bulk_summary(summary)

    def test_current_bulk_summary_rejects_unexpected_illegality(self):
        summary = valid_summary()
        summary["unexpected_official_illegal_rows"] = [{"card_name": "Unexpected Test"}]
        with self.assertRaises(ValueError):
            validate_bulk_summary(summary)


if __name__ == "__main__":
    unittest.main()
