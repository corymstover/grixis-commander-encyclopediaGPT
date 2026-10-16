# The Valeyard — approval-ready verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #58 of 62

## Result

**APPROVAL_READY — NOT APPROVED / NOT LOCKED.**

- Exact candidate SHA-256: `4bef619a33d85eafaf194997924fc8378dd490f62c59d76bafccc4fa07ef821c`
- Cards: **100**
- Distinct names: **96**
- Lands: **36**
- Repeats: **Island x2 / Mountain x2 / Swamp x3 only**
- Singleton: **PASS**
- Commander color identity: **U/B/R — PASS**
- Current Oracle / color-identity verification: **PASS**
- Official Commander legality: **PASS**
- Project exceptions: **none**
- Rules-interaction attestation: **PASS**
- Force of Will blue-pitch pool: **26 other blue cards**
- Whole-list audit: **99/99 noncommander copies adjudicated; 90 KEEP / 9 CUT**
- Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS**
- Natural ceiling: **Power Bracket 4 — Optimized**
- Proposed Archidekt tags: **Villainous Choice / Voting / Political Control**

## Final proposed delta

1. Counterspell -> Force of Will
2. The Toymaker's Trap -> Messenger Jays
3. Paradox Haze -> Spark Double
4. Prisoner's Dilemma -> Quantum Misalignment
5. Dalek Drone -> Sakashima of a Thousand Faces
6. Seize the Spotlight -> Auton Soldier
7. Windswept Heath -> Arid Mesa
8. Dragonskull Summit -> City of Brass
9. Drowned Catacomb -> Mana Confluence

## Critical rules and mana findings

- **Prisoner's Dilemma does not currently interact with The Valeyard's extra-vote ability.** Its current Oracle text has each opponent *choose* silence or snitch and does not use the word "vote." Comprehensive Rule 701.38c says references to "voting" apply only to an actual vote, not choices or decisions that do not use "vote." The original 2024 release notes used secret-vote terminology in explanatory bullets, but the current Oracle wording and current Comprehensive Rules govern the interaction.
- **Messenger Jays is a real voting card.** Its Council's dilemma ability explicitly has each player vote for feather or quill, so The Valeyard can cast an additional vote.
- **Windswept Heath has zero fetchable lands in the authoritative current list.** It searches only for a Forest or Plains. **Arid Mesa** searches for a Mountain or Plains and has five Mountain-typed targets in this list: Badlands, Blood Crypt, Steam Vents, Volcanic Island, and Xander's Lounge.
- **The accepted copy package directly multiplies the commander's text without immediately losing copies to the legend rule.** Spark Double is nonlegendary when copying The Valeyard; Quantum Misalignment creates a nonlegendary copy; Sakashima of a Thousand Faces lets the legend rule stop applying while it remains; and Auton Soldier enters as a nonlegendary copy and its myriad tokens copy its listed exceptions.
- Multiple Valeyard effects stack additively: each replacement effect causes an additional villainous choice, performed one at a time under rule 701.55c, and each Valeyard permits an additional vote when its controller votes.

## Strategic preservation

All **13 noncommander Villainous Choice sources** from the authoritative baseline remain intact. The changes remove generic/off-axis choice cards and narrow upkeep support in favor of actual voting plus repeatable/temporary Valeyard-copy effects. The deck remains a Villainous Choice / Voting political-control deck rather than becoming generic Grixis control or combo.

The mana base remains at **36 lands** while replacing a dead fetchland and two conditional checklands with three unconditional/fetch-compatible upgrades. The deck's protection improves through Force of Will without reducing its commander-specific engine density.

## Source-of-truth handling

The authoritative October 12 FINAL CSV/TXT export was used as the baseline. The inherited `deck_card_audit.csv` contains stale membership for several Valeyard slots, so it was used only as supporting metadata where applicable and was **not** allowed to overwrite current FINAL membership.

Current public verification references used for this gate:
- Wizards Commander banned/restricted list
- Current Magic Comprehensive Rules, especially 701.38 (Vote) and 701.55 (Face a Villainous Choice)
- Wizards Doctor Who release notes for Auton Soldier / myriad-copy behavior
- Current Oracle/legalities for The Valeyard, Messenger Jays, Prisoner's Dilemma, Force of Will, Arid Mesa, Spark Double, Sakashima of a Thousand Faces, and Quantum Misalignment

## Approval boundary

This artifact is **not** an approval record and does **not** lock the deck. Lock only after explicit user approval of exact SHA-256 `4bef619a33d85eafaf194997924fc8378dd490f62c59d76bafccc4fa07ef821c`.
