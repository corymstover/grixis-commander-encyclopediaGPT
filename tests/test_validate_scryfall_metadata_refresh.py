import unittest
from datetime import datetime, timedelta, timezone
from scripts.validate_scryfall_metadata_refresh import validate_summary

class ValidateScryfallRefreshTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 10, 13, 12, 0, tzinfo=timezone.utc)
        self.summary = {
            "generated_at_utc": self.now.isoformat(), "bulk_type": "default_cards",
            "bulk_updated_at": (self.now - timedelta(hours=6)).isoformat(),
            "deck_count": 62, "decklist_rows": 5964, "rows_written": 5964, "exact_matches": 5964,
            "name_variant_reviews": 0, "not_found": 0, "ambiguous": 0,
            "blank_oracle_text_rows": 0, "missing_oracle_id": 0,
            "color_identity_mismatches": [], "unresolved_printing_rows": [],
            "unresolved_project_exception_rows": [], "unexpected_official_illegal_rows": [],
            "decks_with_unresolved_commander_identity": [],
            "overall_result": "METADATA_REFRESH_PASS — registered exceptions remain separately labeled; rules-interaction review remains separate",
        }

    def test_clean_fresh_snapshot_passes(self):
        report = validate_summary(self.summary, now=self.now)
        self.assertEqual(report["validation"], "PASS")
        self.assertEqual(report["errors"], [])

    def test_dated_snapshot_fails_generation_freshness(self):
        old = dict(self.summary, generated_at_utc=(self.now - timedelta(days=2)).isoformat())
        report = validate_summary(old, now=self.now)
        self.assertTrue(any("snapshot is stale" in e for e in report["errors"]))


    def test_snapshot_from_previous_run_fails_even_if_recent(self):
        recent_old = dict(
            self.summary,
            generated_at_utc=(self.now - timedelta(minutes=10)).isoformat(),
        )
        run_started = (self.now - timedelta(minutes=5)).isoformat()
        report = validate_summary(recent_old, now=self.now, not_before_utc=run_started)
        self.assertTrue(any("snapshot predates this workflow run" in e for e in report["errors"]))

    def test_snapshot_created_after_run_start_passes_run_freshness(self):
        report = validate_summary(
            self.summary,
            now=self.now,
            not_before_utc=(self.now - timedelta(minutes=1)).isoformat(),
        )
        self.assertFalse(any("snapshot predates this workflow run" in e for e in report["errors"]))

    def test_stale_bulk_fails_even_if_generated_now(self):
        old = dict(self.summary, bulk_updated_at=(self.now - timedelta(days=5)).isoformat())
        report = validate_summary(old, now=self.now)
        self.assertTrue(any("bulk data is stale" in e for e in report["errors"]))

    def test_missing_card_rows_fail_closed(self):
        incomplete = dict(self.summary, exact_matches=5963, rows_written=5963)
        report = validate_summary(incomplete, now=self.now)
        self.assertTrue(any("exact_matches" in e for e in report["errors"]))

    def test_color_identity_mismatch_fails(self):
        wrong = dict(self.summary, color_identity_mismatches=[{"card_name": "Unexpected"}])
        report = validate_summary(wrong, now=self.now)
        self.assertTrue(any("color identity mismatches" in e for e in report["errors"]))

    def test_unexpected_legality_fails(self):
        illegal = dict(self.summary, unexpected_official_illegal_rows=[{"card_name": "Unexpected"}])
        report = validate_summary(illegal, now=self.now)
        self.assertTrue(any("unexpected official-illegal rows" in e for e in report["errors"]))

    def test_missing_timezone_fails(self):
        wrong = dict(self.summary, generated_at_utc="2026-10-13T12:00:00")
        report = validate_summary(wrong, now=self.now)
        self.assertTrue(any("has no timezone offset" in e for e in report["errors"]))

    def test_registered_project_exception_is_not_itself_a_failure(self):
        known = dict(self.summary, official_illegal_rows=[{"card_name": "registered exception"}])
        report = validate_summary(known, now=self.now)
        self.assertEqual(report["validation"], "PASS")

if __name__ == "__main__":
    unittest.main()
