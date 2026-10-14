from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class DeckQuality:
    commander_identity: float
    synergy: float
    interaction: float
    consistency: float
    resilience: float
    mana: float
    combo_integrity: float
    legality_integrity: float

WEIGHTS={
    "commander_identity":0.24,
    "synergy":0.18,
    "interaction":0.10,
    "consistency":0.14,
    "resilience":0.10,
    "mana":0.08,
    "combo_integrity":0.10,
    "legality_integrity":0.06,
}

def quality_score(q: DeckQuality)->float:
    vals=q.__dict__
    if any(not 0 <= float(v) <= 100 for v in vals.values()):
        raise ValueError("quality dimensions must be in [0,100]")
    return sum(float(vals[k])*w for k,w in WEIGHTS.items())

def compare_variant(baseline: DeckQuality, variant: DeckQuality, *, min_gain=0.25,
                    identity_floor_drop=0.0, integrity_floor=100.0):
    b=quality_score(baseline); v=quality_score(variant)
    hard_fail = (
        variant.commander_identity < baseline.commander_identity - identity_floor_drop or
        variant.legality_integrity < integrity_floor or
        variant.combo_integrity < min(integrity_floor, baseline.combo_integrity)
    )
    gain=v-b
    return {
        "baseline_score":round(b,4),
        "variant_score":round(v,4),
        "gain":round(gain,4),
        "accept":bool(not hard_fail and gain >= min_gain),
        "hard_gate_failure":bool(hard_fail),
    }
