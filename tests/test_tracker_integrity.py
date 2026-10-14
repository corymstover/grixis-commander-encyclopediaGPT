import unittest
from scripts.check_tracker_integrity import validate_tracker_text

HEADER = "index,deck_id,commander_names,final_gate_passed,final_list_hash,user_approval_date\n"

class TrackerIntegrityTests(unittest.TestCase):
    def test_valid_row_passes(self):
        content = HEADER + '0,Abaddon_the_Despoiler,Abaddon the Despoiler,NO,,\n'
        self.assertEqual(validate_tracker_text(content, expected_decks=1)["validation"], "PASS")

    def test_historical_mode_ignores_stale_approval_semantics(self):
        content = HEADER + '0,A,A,YES,,\n'
        self.assertEqual(validate_tracker_text(content, expected_decks=1, validate_approval_metadata=False)["validation"], "PASS")

    def test_malformed_extra_column_fails(self):
        content = HEADER + '0,Abaddon_the_Despoiler,Abaddon the Despoiler,NO,,,EXTRA\n'
        report = validate_tracker_text(content, expected_decks=1)
        self.assertEqual(report["validation"], "FAIL")
        self.assertTrue(any("malformed CSV field counts" in e for e in report["errors"]))

    def test_duplicate_deck_id_fails(self):
        content = HEADER + '0,A,A,NO,,\n1,A,A,NO,,\n'
        report = validate_tracker_text(content, expected_decks=2)
        self.assertTrue(any("duplicate deck_id" in e for e in report["errors"]))

    def test_yes_requires_hash_and_approval_date(self):
        content = HEADER + '0,A,A,YES,,\n'
        report = validate_tracker_text(content, expected_decks=1)
        self.assertTrue(any("YES requires" in e for e in report["errors"]))

    def test_no_cannot_have_approval_hash(self):
        content = HEADER + '0,A,A,NO,abc,2026-10-13\n'
        report = validate_tracker_text(content, expected_decks=1)
        self.assertTrue(any("gate must not carry approval hash/date" in e for e in report["errors"]))

if __name__ == "__main__":
    unittest.main()
