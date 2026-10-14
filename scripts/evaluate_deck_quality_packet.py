#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from grixis_pipeline.epistemic import (
    Confidence, EvidenceDimension, CandidateDecision, RedTeamFinding, HypothesisTest,
    CommanderNecessity, candidate_exhaustion, red_team_gate, hypothesis_testing_gate,
    commander_necessity_gate, evidence_confidence_report, final_quality_gate,
)

def evaluate(packet):
    candidates=[CandidateDecision(**x) for x in packet.get("candidates",[])]
    findings=[RedTeamFinding(**x) for x in packet.get("red_team_findings",[])]
    tests=[HypothesisTest(**x) for x in packet.get("hypothesis_tests",[])]
    n=packet["commander_necessity"]
    necessity=CommanderNecessity(n["thesis"],tuple(n.get("material_dependencies",[])),n["counterfactual_impact"],tuple(n.get("evidence_refs",[])))
    dims=[EvidenceDimension(x["name"],Confidence(x["confidence"]),x["rationale"],tuple(x.get("evidence_refs",[]))) for x in packet.get("evidence_dimensions",[])]
    cg=candidate_exhaustion(candidates,discovery_passes=int(packet.get("discovery_passes",0)),
                            new_material_candidates_last_pass=int(packet.get("new_material_candidates_last_pass",-1)))
    rg=red_team_gate(findings)
    tg=hypothesis_testing_gate(tests,required=bool(packet.get("testing_required",False)))
    ng=commander_necessity_gate(necessity)
    eg=evidence_confidence_report(dims)
    final=final_quality_gate(hard_gates=packet.get("hard_gates",{}),candidate_gate=cg,red_team=rg,testing=tg,necessity=ng,evidence=eg)
    return {"candidate_exhaustion":cg,"red_team":rg,"hypothesis_testing":tg,
            "commander_necessity":ng,"evidence_confidence":eg,"quality_gate":final}

def main():
    ap=argparse.ArgumentParser(description="Evaluate a Deck Quality Gates v3 evidence packet.")
    ap.add_argument("packet",type=Path)
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    report=evaluate(json.loads(args.packet.read_text(encoding="utf-8")))
    encoded=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(encoded,encoding="utf-8")
    print(encoded,end="")
    raise SystemExit(0 if report["quality_gate"]["pass"] else 2)

if __name__=="__main__": main()
