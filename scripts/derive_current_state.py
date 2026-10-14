#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from grixis_pipeline.state import derive_current_rows

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--tracker",default="refinement/Deck_Refinement_Tracker_2026-10-12.csv")
    p.add_argument("--output",default="state/current_decks.json")
    a=p.parse_args(); rows=derive_current_rows(a.tracker)
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps({"schema_version":1,"decks":rows},indent=2)+"\n",encoding="utf-8")
    print(f"Wrote {len(rows)} canonical current-cycle deck states to {out}")
if __name__=="__main__": main()
