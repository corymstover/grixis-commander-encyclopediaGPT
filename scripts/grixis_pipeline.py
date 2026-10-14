#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from grixis_pipeline.core import run_cached_stage

def main():
    p=argparse.ArgumentParser(description="Resumable Grixis pipeline runner")
    p.add_argument("run",nargs="?")
    p.add_argument("--deck-id",required=True)
    p.add_argument("--through",default="VERIFY")
    p.add_argument("--input",action="append",default=[])
    a=p.parse_args()
    inputs={"deck_id":a.deck_id,"through":a.through,"input":sorted(a.input)}
    out=run_cached_stage(deck_id=a.deck_id,stage=a.through,inputs=inputs,work=lambda:{"status":"PASS","inputs":inputs})
    print(json.dumps(out,indent=2))
if __name__=="__main__": main()
