from __future__ import annotations
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum
from itertools import combinations
from typing import Iterable, Mapping, Sequence

class Confidence(str, Enum):
    VERIFIED="VERIFIED"
    HIGH="HIGH_CONFIDENCE"
    PROVISIONAL="PROVISIONAL"
    TEST_REQUIRED="TEST_REQUIRED"
    BLOCKED="BLOCKED"

@dataclass(frozen=True)
class EvidenceDimension:
    name: str
    confidence: Confidence
    rationale: str
    evidence_refs: tuple[str, ...] = ()

@dataclass(frozen=True)
class CandidateDecision:
    card: str
    impact: str
    decision: str
    reason: str
    evidence_refs: tuple[str, ...] = ()

@dataclass(frozen=True)
class RedTeamFinding:
    category: str
    claim: str
    material: bool
    resolved: bool
    resolution: str = ""

@dataclass(frozen=True)
class HypothesisTest:
    hypothesis: str
    preregistered: bool
    controlled_comparison: bool
    integrity_preserved: bool
    result: str
    decision: str
    evidence_refs: tuple[str, ...] = ()

@dataclass(frozen=True)
class CommanderNecessity:
    thesis: str
    material_dependencies: tuple[str, ...]
    counterfactual_impact: str
    evidence_refs: tuple[str, ...] = ()

@dataclass(frozen=True)
class CrossDeckObservation:
    subject: str
    decks_observed: int
    accepted: int
    rejected: int
    note: str

def candidate_exhaustion(decisions: Sequence[CandidateDecision], *, discovery_passes: int,
                         new_material_candidates_last_pass: int) -> dict:
    allowed={"ACCEPT","REJECT","HOLD"}
    invalid=[d.card for d in decisions if d.decision not in allowed or d.impact not in {"HIGH","MEDIUM","LOW"}]
    unresolved_high=[d.card for d in decisions if d.impact=="HIGH" and d.decision=="HOLD"]
    unexplained=[d.card for d in decisions if not d.reason.strip()]
    passed=bool(decisions) and discovery_passes >= 1 and new_material_candidates_last_pass == 0 and not invalid and not unresolved_high and not unexplained
    return {"pass":passed,"reviewed":len(decisions),"invalid":invalid,"unresolved_high_impact":unresolved_high,
            "unexplained":unexplained,"discovery_passes":discovery_passes,
            "new_material_candidates_last_pass":new_material_candidates_last_pass}

def red_team_gate(findings: Sequence[RedTeamFinding]) -> dict:
    unresolved=[f for f in findings if f.material and not f.resolved]
    return {"pass":not unresolved,"material_findings":sum(f.material for f in findings),
            "unresolved_material":[{"category":f.category,"claim":f.claim} for f in unresolved]}

def hypothesis_testing_gate(tests: Sequence[HypothesisTest], *, required: bool) -> dict:
    if not required and not tests:
        return {"pass":True,"tests":0,"reason":"No material analytical tie required empirical resolution."}
    defects=[t.hypothesis for t in tests if not (t.preregistered and t.controlled_comparison and t.integrity_preserved and t.result.strip() and t.decision.strip())]
    return {"pass":bool(tests) and not defects,"tests":len(tests),"defects":defects}

def commander_necessity_gate(review: CommanderNecessity) -> dict:
    impact=review.counterfactual_impact.upper()
    passed=bool(review.thesis.strip()) and bool(review.material_dependencies) and impact in {"MATERIAL","HIGH","STRUCTURAL"}
    return {"pass":passed,"counterfactual_impact":impact,"material_dependencies":list(review.material_dependencies)}

def evidence_confidence_report(dimensions: Sequence[EvidenceDimension]) -> dict:
    if not dimensions:
        raise ValueError("at least one evidence dimension is required")
    blocked=[d.name for d in dimensions if d.confidence==Confidence.BLOCKED]
    test_required=[d.name for d in dimensions if d.confidence==Confidence.TEST_REQUIRED]
    provisional=[d.name for d in dimensions if d.confidence==Confidence.PROVISIONAL]
    strong=sum(d.confidence in {Confidence.VERIFIED,Confidence.HIGH} for d in dimensions)
    return {"pass":not blocked and not test_required,"dimensions":len(dimensions),"strong_dimensions":strong,
            "blocked":blocked,"test_required":test_required,"provisional":provisional,
            "overall":"HIGH" if strong==len(dimensions) else ("BLOCKED" if blocked else "MIXED")}

def final_quality_gate(*, hard_gates: Mapping[str,bool], candidate_gate: Mapping,
                       red_team: Mapping, testing: Mapping, necessity: Mapping,
                       evidence: Mapping) -> dict:
    failed_hard=sorted(k for k,v in hard_gates.items() if not v)
    failed_quality=[name for name,g in (("candidate_exhaustion",candidate_gate),("red_team",red_team),
                    ("hypothesis_testing",testing),("commander_necessity",necessity),("evidence_confidence",evidence))
                    if not bool(g.get("pass"))]
    passed=not failed_hard and not failed_quality
    return {"pass":passed,"failed_hard_gates":failed_hard,"failed_quality_gates":failed_quality,
            "approval_eligible":passed,"approval_status":"REQUIRES_EXPLICIT_USER_APPROVAL" if passed else "NOT_ELIGIBLE"}

def diversity_audit(deck_cards: Mapping[str, Iterable[str]], *, ignore_cards: Iterable[str]=(),
                    pair_overlap_warn: float=0.60, prevalence_warn: float=0.75) -> dict:
    ignored=set(ignore_cards)
    normalized={d:set(cards)-ignored for d,cards in deck_cards.items()}
    pair_warnings=[]
    for a,b in combinations(sorted(normalized),2):
        union=normalized[a]|normalized[b]
        overlap=len(normalized[a]&normalized[b])/len(union) if union else 0.0
        if overlap >= pair_overlap_warn:
            pair_warnings.append({"a":a,"b":b,"jaccard":round(overlap,4)})
    counts=Counter(card for cards in normalized.values() for card in cards)
    n=len(normalized)
    prevalent=[{"card":c,"deck_fraction":round(k/n,4)} for c,k in counts.most_common() if n and k/n >= prevalence_warn]
    return {"decks":n,"pair_overlap_warnings":pair_warnings,"prevalent_nonignored_cards":prevalent,
            "review_required":bool(pair_warnings or prevalent)}

def cross_deck_learning(decisions_by_deck: Mapping[str, Sequence[CandidateDecision]]) -> list[CrossDeckObservation]:
    by_card={}
    for deck,decisions in decisions_by_deck.items():
        for d in decisions:
            if d.decision not in {"ACCEPT","REJECT"}: continue
            x=by_card.setdefault(d.card,{"decks":set(),"accept":0,"reject":0})
            x["decks"].add(deck); x["accept"] += d.decision=="ACCEPT"; x["reject"] += d.decision=="REJECT"
    out=[]
    for card,x in by_card.items():
        if len(x["decks"]) < 2: continue
        out.append(CrossDeckObservation(card,len(x["decks"]),x["accept"],x["reject"],
            "Evidence lead only; never propagate a card choice automatically across commanders."))
    return sorted(out,key=lambda x:(-x.decks_observed,x.subject))
