import unittest
from grixis_pipeline.dependencies import Change, invalidated

class DependencyInvalidationTests(unittest.TestCase):
    def test_one_deck_swap_does_not_invalidate_other_decks(self):
        result=invalidated(Change("DECKLIST",("Abaddon_the_Despoiler",)),["Abaddon_the_Despoiler","Anhelo__the_Painter"])
        self.assertEqual(set(result),{"Abaddon_the_Despoiler"})
        self.assertIn("COMBOS",result["Abaddon_the_Despoiler"]); self.assertIn("FINAL_VERIFY",result["Abaddon_the_Despoiler"])
    def test_oracle_snapshot_is_project_wide(self):
        result=invalidated(Change("ORACLE_SNAPSHOT"),["A","B"])
        self.assertEqual(set(result),{"A","B"}); self.assertIn("ORACLE_IDENTITY",result["A"]); self.assertIn("LEGALITY",result["B"])
    def test_strategy_change_preserves_structural_facts(self):
        nodes=set(invalidated(Change("COMMANDER_STRATEGY",("A",)),["A"])["A"])
        self.assertIn("SYNERGY",nodes); self.assertNotIn("STRUCTURE",nodes); self.assertNotIn("ORACLE_IDENTITY",nodes)
if __name__=="__main__": unittest.main()
