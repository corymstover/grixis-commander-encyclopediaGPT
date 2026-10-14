import unittest
from grixis_pipeline.epistemic import (
    Confidence, EvidenceDimension, CandidateDecision, RedTeamFinding, HypothesisTest,
    CommanderNecessity, candidate_exhaustion, red_team_gate, hypothesis_testing_gate,
    commander_necessity_gate, evidence_confidence_report, final_quality_gate,
    diversity_audit, cross_deck_learning,
)

class EpistemicGateTests(unittest.TestCase):
    def test_candidate_exhaustion_rejects_high_impact_hold(self):
        ds=[CandidateDecision("A","HIGH","HOLD","Need rules evidence")]
        self.assertFalse(candidate_exhaustion(ds,discovery_passes=2,new_material_candidates_last_pass=0)["pass"])

    def test_candidate_exhaustion_passes_closed_material_search(self):
        ds=[CandidateDecision("A","HIGH","ACCEPT","Improves commander engine"),
            CandidateDecision("B","MEDIUM","REJECT","Redundant at current density")]
        self.assertTrue(candidate_exhaustion(ds,discovery_passes=2,new_material_candidates_last_pass=0)["pass"])

    def test_red_team_blocks_unresolved_material_objection(self):
        x=red_team_gate([RedTeamFinding("mana","Curve cannot support 32 lands",True,False)])
        self.assertFalse(x["pass"])

    def test_testing_is_hypothesis_driven(self):
        bad=HypothesisTest("A beats B",False,True,True,"A +4%","Use A")
        self.assertFalse(hypothesis_testing_gate([bad],required=True)["pass"])
        good=HypothesisTest("A beats B",True,True,True,"A +4%","Use A")
        self.assertTrue(hypothesis_testing_gate([good],required=True)["pass"])

    def test_commander_necessity_requires_material_counterfactual(self):
        weak=CommanderNecessity("Generic shell",("draw",),"LOW")
        strong=CommanderNecessity("Commander converts damage into cascade",("cascade threshold","sequencing"),"STRUCTURAL")
        self.assertFalse(commander_necessity_gate(weak)["pass"])
        self.assertTrue(commander_necessity_gate(strong)["pass"])

    def test_evidence_report_exposes_uncertainty(self):
        dims=[EvidenceDimension("rules",Confidence.VERIFIED,"Oracle checked"),
              EvidenceDimension("testing",Confidence.TEST_REQUIRED,"Close variant")]
        r=evidence_confidence_report(dims)
        self.assertFalse(r["pass"]); self.assertEqual(r["test_required"],["testing"])

    def test_final_gate_never_auto_approves(self):
        ok={"pass":True}
        r=final_quality_gate(hard_gates={"count":True,"legality":True},candidate_gate=ok,red_team=ok,testing=ok,necessity=ok,evidence=ok)
        self.assertTrue(r["approval_eligible"])
        self.assertEqual(r["approval_status"],"REQUIRES_EXPLICIT_USER_APPROVAL")

    def test_diversity_audit_flags_collection_homogenization(self):
        r=diversity_audit({"A":{"X","Y","Z"},"B":{"X","Y","Z"}},pair_overlap_warn=.8,prevalence_warn=1.0)
        self.assertTrue(r["review_required"]); self.assertEqual(len(r["pair_overlap_warnings"]),1)

    def test_cross_deck_learning_is_non_prescriptive(self):
        ds={"A":[CandidateDecision("X","HIGH","ACCEPT","fit")],
            "B":[CandidateDecision("X","HIGH","REJECT","wrong identity")]}
        obs=cross_deck_learning(ds)
        self.assertEqual(len(obs),1); self.assertIn("never propagate",obs[0].note)

if __name__=="__main__": unittest.main()
