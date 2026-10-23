import re
import unittest
from grixis_pipeline.state import load_cycle, load_deck_overrides, derive_current_rows

def normalized_id(deck_id):
    # Three historical tracker spellings use doubled underscores; the
    # canonical state authority stores their equivalent single-underscore IDs.
    return re.sub(r"_+", "_", deck_id)

class CurrentCycleStateTests(unittest.TestCase):
    def test_global_restart_is_unapproved_unlocked(self):
        c=load_cycle(); d=c["global_defaults"]
        self.assertEqual(d["approval_status"],"UNAPPROVED"); self.assertEqual(d["lock_status"],"UNLOCKED")
        self.assertFalse(d["final_gate_passed"])

    def test_tracker_derives_exactly_62_current_rows(self):
        rows=derive_current_rows("refinement/Deck_Refinement_Tracker_2026-10-12.csv")
        self.assertEqual(len(rows),62)
        by_id={normalized_id(r["deck_id"]):r for r in rows}
        self.assertEqual(len(by_id),62)

        # Global restart defaults do not override 62 explicit current-cycle
        # approvals. Reconcile the original three legacy underscore aliases.
        authority=load_deck_overrides()
        authority_by_id={normalized_id(k):v for k,v in authority.items()}
        self.assertEqual(len(authority_by_id),62)
        self.assertEqual(set(authority_by_id),set(by_id))
        for deck_id,approved in authority_by_id.items():
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
            "5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24")
        self.assertEqual(abaddon["user_approval_date"],"2026-10-23")
        self.assertEqual(abaddon["approved_list_artifact"],
            "refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt")

        admiral=by_id["Admiral_Beckett_Brass"]
        self.assertEqual(admiral["approved_list_sha256"],
            "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000")
        self.assertEqual(admiral["user_approval_date"],"2026-10-22")
        self.assertEqual(admiral["approved_list_artifact"],
            "refinement/decklists/Admiral_Beckett_Brass_M7_Approved_2026-10-22.txt")

if __name__=="__main__":
    unittest.main()
