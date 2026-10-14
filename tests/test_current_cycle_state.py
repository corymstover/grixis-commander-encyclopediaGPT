import unittest
from grixis_pipeline.state import load_cycle, derive_current_rows

class CurrentCycleStateTests(unittest.TestCase):
    def test_global_restart_is_unapproved_unlocked(self):
        c=load_cycle(); d=c["global_defaults"]
        self.assertEqual(d["approval_status"],"UNAPPROVED"); self.assertEqual(d["lock_status"],"UNLOCKED")
        self.assertFalse(d["final_gate_passed"])
    def test_tracker_derives_exactly_62_current_rows(self):
        rows=derive_current_rows("refinement/Deck_Refinement_Tracker_2026-10-12.csv")
        self.assertEqual(len(rows),62); self.assertEqual(len({r["deck_id"] for r in rows}),62)
        self.assertTrue(all(r["approval_status"]=="UNAPPROVED" and r["lock_status"]=="UNLOCKED" for r in rows))
if __name__=="__main__": unittest.main()
