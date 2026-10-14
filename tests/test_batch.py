import unittest
from grixis_pipeline.batch import run_many

class BatchTests(unittest.TestCase):
    def test_collects_successes_and_isolates_failures(self):
        def run(deck_id):
            if deck_id=="B": raise ValueError("bad")
            return deck_id.lower()
        out=run_many(["A","B","C"],run,max_workers=2)
        self.assertEqual(out["results"],{"A":"a","C":"c"})
        self.assertEqual(out["errors"]["B"]["type"],"ValueError")

    def test_rejects_duplicate_ids(self):
        with self.assertRaises(ValueError):
            run_many(["A","A"],lambda x:x)

if __name__=="__main__": unittest.main()
