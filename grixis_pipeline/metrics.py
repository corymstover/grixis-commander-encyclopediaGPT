from __future__ import annotations
import json, statistics
from collections import Counter, defaultdict
from pathlib import Path

def summarize_telemetry(path):
    path=Path(path)
    rows=[]
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    by_stage=defaultdict(list)
    for r in rows:
        by_stage[r["stage"]].append(r)
    stages={}
    for stage,items in sorted(by_stage.items()):
        durations=sorted(float(x.get("duration_s",0)) for x in items)
        hits=sum(bool(x.get("cache_hit")) for x in items)
        blocked=sum(x.get("result")=="BLOCKED" for x in items)
        retries=sum(int(x.get("retry_count",0)) for x in items)
        p95=durations[min(len(durations)-1,max(0,int(len(durations)*0.95)-1))] if durations else 0
        stages[stage]={
            "runs":len(items),
            "cache_hit_rate":hits/len(items),
            "blocked_rate":blocked/len(items),
            "retry_count":retries,
            "median_duration_s":statistics.median(durations) if durations else 0,
            "p95_duration_s":p95,
        }
    blockers=Counter(r.get("blocker_code") for r in rows if r.get("blocker_code"))
    return {"runs":len(rows),"stages":stages,"blockers":dict(blockers)}

def bottlenecks(summary, *, min_runs=3):
    findings=[]
    stages=summary.get("stages",{})
    for stage,m in stages.items():
        if m["runs"]<min_runs: continue
        if m["blocked_rate"]>0.10:
            findings.append({"stage":stage,"kind":"BLOCKED_RATE","value":m["blocked_rate"]})
        if m["cache_hit_rate"]<0.25 and m["runs"]>=5:
            findings.append({"stage":stage,"kind":"LOW_CACHE_REUSE","value":m["cache_hit_rate"]})
    if stages:
        eligible=[(s,m["p95_duration_s"]) for s,m in stages.items() if m["runs"]>=min_runs]
        if eligible:
            slow=max(eligible,key=lambda x:x[1])
            if slow[1]>0:
                findings.append({"stage":slow[0],"kind":"P95_HOTSPOT","value":slow[1]})
    return findings
