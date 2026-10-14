import tempfile, unittest
from pathlib import Path
from grixis_pipeline.core import run_cached_stage

class RetryResumeTests(unittest.TestCase):
    def test_transient_failure_retries_then_caches(self):
        with tempfile.TemporaryDirectory() as d:
            calls=[]
            def work():
                calls.append(1)
                if len(calls)<3:
                    raise TimeoutError("temporary")
                return {"ok":True}
            sleeps=[]
            out=run_cached_stage(deck_id="A",stage="VERIFY",inputs={"x":1},work=work,
                                 root=Path(d),max_retries=2,retry_delay_s=0.01,sleep=sleeps.append)
            self.assertEqual(out,{"ok":True})
            self.assertEqual(len(calls),3)
            self.assertEqual(sleeps,[0.01,0.02])
            run_cached_stage(deck_id="A",stage="VERIFY",inputs={"x":1},work=work,
                             root=Path(d),sleep=sleeps.append)
            self.assertEqual(len(calls),3)

    def test_permanent_error_fails_without_retry(self):
        with tempfile.TemporaryDirectory() as d:
            calls=[]
            def work():
                calls.append(1)
                raise ValueError("bad input")
            with self.assertRaises(ValueError):
                run_cached_stage(deck_id="A",stage="VERIFY",inputs={"x":1},work=work,
                                 root=Path(d),max_retries=5,sleep=lambda _:None)
            self.assertEqual(len(calls),1)

    def test_exhausted_transient_retry_records_blocked_checkpoint(self):
        with tempfile.TemporaryDirectory() as d:
            def work(): raise ConnectionError("down")
            root=Path(d)
            with self.assertRaises(ConnectionError):
                run_cached_stage(deck_id="A",stage="VERIFY",inputs={"x":1},work=work,
                                 root=root,max_retries=1,sleep=lambda _:None)
            checkpoint=(root/"checkpoints"/"A.json").read_text()
            self.assertIn('"result": "BLOCKED"',checkpoint)
            self.assertIn('"retry_count": 1',checkpoint)

if __name__=="__main__":
    unittest.main()
