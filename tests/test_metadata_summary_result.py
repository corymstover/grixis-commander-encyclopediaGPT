import unittest
from scripts.refresh_scryfall_metadata import compute_overall_result


def clean_summary():
    return {
        "deck_count": 62,
        "decklist_rows": 5964,
        "rows_written": 5964,
        "exact_matches": 5964,
        "not_found": 0,
        "ambiguous": 0,
        "name_variant_reviews": 0,
        "blank_oracle_text_rows": 0,
        "missing_oracle_id": 0,
        "color_identity_mismatches": [],
        "unresolved_printing_rows": [],
        "unresolved_project_exception_rows": [],
        "unexpected_official_illegal_rows": [],
        "unknown_commander_legality_rows": [],
        "decks_with_unresolved_commander_identity": [],
    }


class RefreshOverallResultTests(unittest.TestCase):
    def test_clean_snapshot_passes(self):
        self.assertTrue(compute_overall_result(clean_summary()).startswith("METADATA_REFRESH_PASS"))

    def test_blank_oracle_text_means_review_required(self):
        summary = clean_summary()
        summary["blank_oracle_text_rows"] = 1
        self.assertEqual(compute_overall_result(summary), "REVIEW_REQUIRED")

    def test_unknown_legality_means_review_required(self):
        summary = clean_summary()
        summary["unknown_commander_legality_rows"] = [{"deck_id": "X", "card_name": "Y"}]
        self.assertEqual(compute_overall_result(summary), "REVIEW_REQUIRED")

    def test_missing_rows_mean_review_required(self):
        summary = clean_summary()
        summary["rows_written"] = 5963
        self.assertEqual(compute_overall_result(summary), "REVIEW_REQUIRED")

    def test_unresolved_commander_identity_means_review_required(self):
        summary = clean_summary()
        summary["decks_with_unresolved_commander_identity"] = ["TestDeck"]
        self.assertEqual(compute_overall_result(summary), "REVIEW_REQUIRED")


if __name__ == "__main__":
    unittest.main()
