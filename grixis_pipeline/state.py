from __future__ import annotations
import csv, json
from pathlib import Path

VALID_STAGES={"UNREFINED","INTAKE","BLUEPRINT","CANDIDATE_TRIAGE","RULES_REVIEW","VERIFY","TEST","RED_TEAM","EVIDENCE_REVIEW","FINALIZE","LOCKED","BLOCKED"}

def load_cycle(path=Path("state/current_cycle.json")):
    data=json.loads(Path(path).read_text(encoding="utf-8"))
    if data["deck_count"] != 62: raise ValueError("canonical cycle must contain 62 decks")
    d=data["global_defaults"]
    if d["approval_status"]!="UNAPPROVED" or d["lock_status"]!="UNLOCKED": raise ValueError("global restart must default to unapproved/unlocked")
    if d["current_stage"] not in VALID_STAGES: raise ValueError("invalid stage")
    return data

def load_deck_overrides(path=Path("state/current_deck_overrides.json")):
    p=Path(path)
    if not p.exists(): return {}
    data=json.loads(p.read_text(encoding="utf-8"))
    return data.get("decks",{})

def derive_current_rows(tracker_path, cycle_path=Path("state/current_cycle.json"), overrides_path=Path("state/current_deck_overrides.json")):
    cycle=load_cycle(cycle_path); defaults=cycle["global_defaults"]; overrides=load_deck_overrides(overrides_path)
    with Path(tracker_path).open(newline="",encoding="utf-8-sig") as f: rows=list(csv.DictReader(f))
    if len(rows)!=cycle["deck_count"]: raise ValueError(f"expected {cycle['deck_count']} tracker rows, got {len(rows)}")
    seen=set(); out=[]
    for row in rows:
        deck_id=row["deck_id"]
        if deck_id in seen: raise ValueError(f"duplicate deck_id: {deck_id}")
        seen.add(deck_id)
        current={"index":int(row["index"]),"deck_id":deck_id,"commander_names":row["commander_names"],**defaults}
        current.update(overrides.get(deck_id,{}))
        if current["approval_status"]=="APPROVED" and (current["lock_status"]!="LOCKED" or not current["final_gate_passed"] or not current["user_approval_date"]): raise ValueError(f"invalid approved override: {deck_id}")
        out.append(current)
    return out
