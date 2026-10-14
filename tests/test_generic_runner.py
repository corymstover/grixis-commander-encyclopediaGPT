import tempfile, unittest
from pathlib import Path
from grixis_pipeline.runner import run_deck

class GenericRunnerTests(unittest.TestCase):
    def test_runs_in_order_and_reuses_cache(self):
        with tempfile.TemporaryDirectory() as d:
            calls=[]
            def work(stage,inputs): calls.append(stage); return {"stage":stage}
            a=run_deck(deck_id="A",target="VERIFY",base_inputs={"deck_hash":"x"},stage_work=work,root=Path(d))
            b=run_deck(deck_id="A",target="VERIFY",base_inputs={"deck_hash":"x"},stage_work=work,root=Path(d))
            self.assertEqual(list(a),["INTAKE","BLUEPRINT","CANDIDATE_TRIAGE","RULES_REVIEW","VERIFY"])
            self.assertEqual(len(calls),5); self.assertEqual(a,b)
    def test_changed_input_recomputes_chain(self):
        with tempfile.TemporaryDirectory() as d:
            calls=[]
            def work(stage,inputs): calls.append(stage); return {"stage":stage}
            run_deck(deck_id="A",target="BLUEPRINT",base_inputs={"deck_hash":"x"},stage_work=work,root=Path(d))
            run_deck(deck_id="A",target="BLUEPRINT",base_inputs={"deck_hash":"y"},stage_work=work,root=Path(d))
            self.assertEqual(len(calls),4)
if __name__=="__main__": unittest.main()
