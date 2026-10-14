import tempfile, unittest
from pathlib import Path
from grixis_pipeline.core import stable_hash, run_cached_stage

class PipelineTests(unittest.TestCase):
    def test_hash_is_order_stable(self): self.assertEqual(stable_hash({"a":1,"b":2}),stable_hash({"b":2,"a":1}))
    def test_second_identical_run_hits_cache(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); calls=[]
            def work(): calls.append(1); return {"ok":True}
            run_cached_stage(deck_id="001",stage="VERIFY",inputs={"hash":"abc"},work=work,root=root)
            run_cached_stage(deck_id="001",stage="VERIFY",inputs={"hash":"abc"},work=work,root=root)
            self.assertEqual(len(calls),1)
    def test_changed_input_invalidates_cache(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); calls=[]
            def work(): calls.append(1); return {"ok":True}
            run_cached_stage(deck_id="001",stage="VERIFY",inputs={"hash":"a"},work=work,root=root)
            run_cached_stage(deck_id="001",stage="VERIFY",inputs={"hash":"b"},work=work,root=root)
            self.assertEqual(len(calls),2)
if __name__=="__main__": unittest.main()
