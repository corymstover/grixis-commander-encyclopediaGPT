import unittest
from grixis_pipeline.state import load_cycle, load_deck_overrides, derive_current_rows

class CurrentCycleStateTests(unittest.TestCase):
    def test_global_restart_is_unapproved_unlocked(self):
        c=load_cycle(); d=c["global_defaults"]
        self.assertEqual(d["approval_status"],"UNAPPROVED"); self.assertEqual(d["lock_status"],"UNLOCKED")
        self.assertFalse(d["final_gate_passed"])

    def test_tracker_derives_exactly_62_current_rows(self):
        rows=derive_current_rows("refinement/Deck_Refinement_Tracker_2026-10-12.csv")
        self.assertEqual(len(rows),62)
        by_id={r["deck_id"]:r for r in rows}
        self.assertEqual(len(by_id),62)

        # Global restart defaults must not override subsequently explicit
        # owner-approved, SHA-locked records. The old regression assumed only
        # Abaddon was approved even after all 62 had acquired valid locks.
        authority=load_deck_overrides()
        self.assertEqual(set(authority),set(by_id))
        for deck_id,approved in authority.items():
            with self.subTest(deck_id=deck_id):
                current=by_id[deck_id]
                self.assertEqual(current["approval_status"],approved["approval_status"])
                self.assertEqual(current["lock_status"],approved["lock_status"])
                self.assertEqual(current["final_gate_passed"],approved["final_gate_passed"])
                self.assertEqual(current["approved_list_sha256"],approved["approved_list_sha256"])
                self.assertEqual(current["user_approval_date"],approved["user_approval_date"])
                self.assertEqual(current["current_stage"],approved["current_stage"])
                self.assertEqual(current["approval_status"],"APPROVED")
                self.assertEqual(current["lock_status"],"LOCKED")
                self.assertTrue(current["final_gate_passed"])

        abaddon=by_id["Abaddon_the_Despoiler"]
        self.assertEqual(abaddon["approved_list_sha256"],
            "0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790")
        self.assertEqual(abaddon["user_approval_date"],"2026-10-22")
        self.assertEqual(abaddon["approved_list_artifact"],
            "refinement/decklists/Abaddon_the_Despoiler_M7_Approved_2026-10-22.txt")

if __name__=="__main__":
    unittest.main()
