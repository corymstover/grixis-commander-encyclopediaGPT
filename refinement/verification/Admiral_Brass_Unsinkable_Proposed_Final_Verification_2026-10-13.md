# Admiral Brass, Unsinkable — Proposed Final Verification

**Date:** 2026-10-13  
**Status:** TECHNICAL VERIFICATION PASS — awaiting explicit approval of this exact revised list  
**Frozen baseline:** 2026-10-12 FINAL TXT export; preserved unchanged  
**Approved swap:** cut 1x Revel in Riches; add 1x Power Conduit  
**Card delta:** one-for-one replacement only

## 1. Exact revised list and hashes

- Copy/paste list: `refinement/decklists/Admiral_Brass_Unsinkable_Proposed_Final_2026-10-13.txt`
- Clean-list SHA-256 (UTF-8, LF, trailing newline): `3857cf322615957d799b29d4fa753fa6f80086700c1053145675b345056b6dae`
- Source-format TXT: `refinement/decklists/Admiral_Brass_Unsinkable_Proposed_Source_Format_2026-10-13.txt`
- Source-format SHA-256: `f98685fc6fb89bd72448ae63b0ba412e4031b06a8764a0737b655b7d15d270ca`
- Original frozen baseline TXT SHA-256: `2e3721984f38bd2a19c1377357f6e737e3588152014bed816e81ce2759392196`

The frozen source export is not overwritten.

## 2. Structural integrity

- Card quantity total: **100**.
- Source rows / distinct card names: **97 / 97**.
- Commander: exactly one, Admiral Brass, Unsinkable, first in the copy/paste list.
- Singleton: **PASS**; repeated basic land quantities are represented as quantities on their own rows.
- Revel in Riches: removed.
- Power Conduit: added exactly once.
- No other card name or quantity changed.

## 3. New card Oracle text, identity, and legality

**Power Conduit — Mirrodin (MRD #229)**  
Mana cost: `{2}`; type: Artifact; color identity: colorless. Oracle text: `{T}, Remove a counter from a permanent you control: Choose one — put a charge counter on target artifact, or put a +1/+1 counter on target creature.` Commander legality: legal.

The outgoing Revel in Riches is also Commander-legal. Its current Oracle text creates a Treasure whenever an opponent's creature dies and wins the game at upkeep if its controller has ten or more Treasures.

## 4. Commander-specific interaction

Admiral Brass, Unsinkable returns a Pirate creature card at the beginning of combat with a finality counter on it. If that permanent would be put into a graveyard from the battlefield while it still has a finality counter, it is exiled instead. Power Conduit can remove that counter as part of its activation cost. If the counter is removed before the Pirate would die, the finality-counter replacement effect no longer applies; if it later dies normally, it can be a graveyard target for Admiral Brass again.

Power Conduit is an artifact rather than a creature, so summoning sickness does not prevent using its tap ability on the turn it enters. The commander trigger must resolve and return the Pirate before Power Conduit can remove its newly placed finality counter.

References:
- https://mtg.wtf/card/mrd/229/Power-Conduit
- https://mtg.wtf/card/lcc/17/Admiral-Brass-Unsinkable
- https://mtg.wtf/card/xln/117/Revel-in-Riches

## 5. Strategic assessment

The swap removes a five-mana Treasure engine and alternate-win condition in favor of a two-mana, commander-specific counter-management artifact. Power Conduit does not itself provide a Pirate or card advantage, and its activation is once per untap cycle, but it can turn the commander's otherwise one-shot reanimation into a repeatable value line for selected Pirates. This is a focused identity upgrade, not a claim that the deck's independent Revel in Riches win condition was weak in every game state.

No gameplay win-rate or representative multiplayer testing claim is made.

## 6. Final approval gate

- 100-card count and structural integrity: **PASS**.
- Singleton compliance: **PASS**.
- New card Oracle text, color identity, and Commander legality: **PASS**.
- Relevant finality-counter interaction: **PASS**.
- Frozen baseline preserved: **PASS**.
- User approval of the swap: **PASS**.
- Exact revised list approved for final lock: **PENDING**.
- Tracker `final_gate_passed`: remains **NO** until the user approves this exact revised list.
