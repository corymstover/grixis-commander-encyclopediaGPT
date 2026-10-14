import json, tempfile, unittest
from pathlib import Path
from grixis_pipeline.metrics import summarize_telemetry, bottlenecks

class MetricsTests(unittest.TestCase):
    def test_summary_and_bottleneck_detection(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"telemetry.jsonl"
            rows=[
                {"stage":"VERIFY","duration_s":1.0,"cache_hit":False,"result":"PASS","retry_count":0},
                {"stage":"VERIFY","duration_s":2.0,"cache_hit":False,"result":"PASS","retry_count":1},
                {"stage":"VERIFY","duration_s":3.0,"cache_hit":False,"result":"BLOCKED","retry_count":2,"blocker_code":"TimeoutError"},
                {"stage":"VERIFY","duration_s":4.0,"cache_hit":False,"result":"PASS","retry_count":0},
                {"stage":"VERIFY","duration_s":5.0,"cache_hit":False,"result":"PASS","retry_count":0},
            ]
            p.write_text("\n".join(json.dumps(x) for x in rows)+"\n",encoding="utf-8")
            s=summarize_telemetry(p)
            self.assertEqual(s["runs"],5)
            self.assertEqual(s["blockers"]["TimeoutError"],1)
            kinds={x["kind"] for x in bottlenecks(s)}
            self.assertIn("BLOCKED_RATE",kinds)
            self.assertIn("LOW_CACHE_REUSE",kinds)
            self.assertIn("P95_HOTSPOT",kinds)

if __name__=="__main__":
    unittest.main()
