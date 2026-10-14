#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from grixis_pipeline.metrics import summarize_telemetry, bottlenecks

def main():
    p=argparse.ArgumentParser(description="Summarize adaptive pipeline telemetry and identify measured bottlenecks.")
    p.add_argument("--telemetry",default=".grixis/telemetry.jsonl")
    p.add_argument("--output")
    a=p.parse_args()
    summary=summarize_telemetry(a.telemetry)
    report={"summary":summary,"bottlenecks":bottlenecks(summary)}
    encoded=json.dumps(report,indent=2,sort_keys=True)+"\n"
    print(encoded,end="")
    if a.output:
        Path(a.output).write_text(encoded,encoding="utf-8")
if __name__=="__main__":
    main()
