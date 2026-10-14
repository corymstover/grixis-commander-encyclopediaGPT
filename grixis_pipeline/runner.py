from __future__ import annotations
from pathlib import Path
from .core import STAGES, run_cached_stage

EXECUTABLE_STAGES=STAGES[1:-1]

def stages_through(target):
    if target not in EXECUTABLE_STAGES: raise ValueError(f"target must be one of {EXECUTABLE_STAGES}")
    return EXECUTABLE_STAGES[:EXECUTABLE_STAGES.index(target)+1]

def run_deck(*,deck_id,target,base_inputs,stage_work,root=Path(".grixis")):
    results={}
    upstream={}
    for stage in stages_through(target):
        inputs={"base":base_inputs,"upstream":upstream}
        payload=run_cached_stage(deck_id=deck_id,stage=stage,inputs=inputs,work=lambda s=stage: stage_work(s,inputs),root=root)
        results[stage]=payload
        upstream[stage]=payload
    return results
