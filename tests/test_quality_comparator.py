import unittest
from grixis_pipeline.quality import DeckQuality, compare_variant

def q(**kw):
    base=dict(commander_identity=90,synergy=85,interaction=80,consistency=80,resilience=80,mana=80,combo_integrity=100,legality_integrity=100)
    base.update(kw); return DeckQuality(**base)

class QualityComparatorTests(unittest.TestCase):
    def test_rejects_generic_power_gain_that_loses_identity(self):
        result=compare_variant(q(),q(commander_identity=88,interaction=100,consistency=90))
        self.assertFalse(result["accept"]); self.assertTrue(result["hard_gate_failure"])

    def test_rejects_legality_regression(self):
        result=compare_variant(q(),q(synergy=100,legality_integrity=99))
        self.assertFalse(result["accept"]); self.assertTrue(result["hard_gate_failure"])

    def test_accepts_material_identity_preserving_gain(self):
        result=compare_variant(q(),q(synergy=90,consistency=85))
        self.assertTrue(result["accept"]); self.assertGreater(result["gain"],0)

if __name__=="__main__": unittest.main()
