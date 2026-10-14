from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

ALL_ANALYSES=frozenset({"STRUCTURE","ORACLE_IDENTITY","LEGALITY","COMMANDER_IDENTITY","SYNERGY","COMBOS","MANA_CURVE","ROLE_DENSITY","CANDIDATES","CONSISTENCY_TEST","MULTIPLAYER_TEST","FINAL_VERIFY"})
CARD_FACT_DEPENDENTS=frozenset({"ORACLE_IDENTITY","LEGALITY","COMMANDER_IDENTITY","SYNERGY","COMBOS","CANDIDATES","FINAL_VERIFY"})
DECKLIST_DEPENDENTS=frozenset({"STRUCTURE","ORACLE_IDENTITY","LEGALITY","COMMANDER_IDENTITY","SYNERGY","COMBOS","MANA_CURVE","ROLE_DENSITY","CANDIDATES","CONSISTENCY_TEST","MULTIPLAYER_TEST","FINAL_VERIFY"})
STRATEGY_DEPENDENTS=frozenset({"SYNERGY","COMBOS","ROLE_DENSITY","CANDIDATES","CONSISTENCY_TEST","MULTIPLAYER_TEST","FINAL_VERIFY"})
EXCEPTION_DEPENDENTS=frozenset({"LEGALITY","FINAL_VERIFY"})

@dataclass(frozen=True)
class Change:
    kind: str
    deck_ids: tuple[str,...]=()

def invalidated(change: Change, all_deck_ids: Iterable[str]):
    decks=tuple(all_deck_ids)
    if change.kind in {"ORACLE_SNAPSHOT","LEGALITY_SNAPSHOT"}:
        nodes=CARD_FACT_DEPENDENTS
        targets=decks
    elif change.kind=="DECKLIST":
        nodes=DECKLIST_DEPENDENTS
        targets=change.deck_ids
    elif change.kind=="COMMANDER_STRATEGY":
        nodes=STRATEGY_DEPENDENTS
        targets=change.deck_ids
    elif change.kind=="PROJECT_EXCEPTION":
        nodes=EXCEPTION_DEPENDENTS
        targets=change.deck_ids or decks
    else:
        raise ValueError(f"unknown change kind: {change.kind}")
    return {deck_id: sorted(nodes) for deck_id in targets}
