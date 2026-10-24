# Crosis, the Purger — M7 Rev2 nine-swap owner approval and canonical lock

Date: **2026-10-23** (America/Chicago)  
Cycle: `global-restart-2026-10-13`  
Owner: **Cory Stover**  
Decision: **APPROVED / LOCKED**, Deck #10 (tracker index 9), raw SHA-256 `a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a`.

## Explicit owner decision and exact byte binding

After the complete ChatGPT independent nine-swap M7 Rev2 list, exact raw SHA and [engineering PR #685](https://github.com/corymstover/GrokBotMTGCompanion/pull/685) were presented, Cory replied:

> Approve

This expressly approves **only** the exact 100-card candidate, UTF-8 text with trailing LF, raw `a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a`. It is **not a blanket approval** of other decks or a waiver of future owner approvals. The approved list is `refinement/decklists/Crosis_the_Purger_M7_Rev2_Approved_2026-10-23.txt`.

The prior approved October14 list `refinement/decklists/Crosis_the_Purger_Approval_Candidate_2026-10-14.txt` (despite its misleading "candidate" filename) remains immutable at raw `a59150c323aa1e21cbda65291a3b172d08ecc3b83266b708768f4e14f0b07ec1`. The historical tracker says "Brotherhood Regalia → Blizzard Specter" though both are in that bound baseline. Do not silently correct old evidence. The nine approved swaps below are computed from actual approved baseline bytes.

## Nine expressly approved one-for-one changes

| Add | Cut | Why |
|---|---|---|
| Megrim | Jet Medallion | Two damage per discarded card; trades away discount on black spells including Crosis generic mana. |
| Rankle, Master of Pranks | Blizzard Specter | Hasty flying discard pressure; modes affect each player, sometimes self. |
| Aggravated Assault | Dream Salvage | More Crosis combat triggers; with Sword of Feast and Famine can repeat conditional combat. |
| Raiders' Wake | Oppression | Asymmetric opponent discard punishment and raid. |
| Deadly Rollick | Fell Specter | Commander-conditional free exile while preserving Izzet Signet acceleration instead of cutting two rocks. |
| Bloodchief Ascension | Bottomless Pit | One-mana conditional graveyard life drain/gain after three quest counters; removes symmetrical hand depletion. |
| Otawara, Soaring City | 1 Island | Untapped U + channel bounce, legendary reduction. |
| Takenuma, Abandoned Mire | 1 Swamp | Untapped B + channel recursion, legendary reduction. |
| Sokenzan, Crucible of Defiance | 1 Mountain | Untapped R + hasty Spirit attackers for raid; nonbasic-risk tradeoff acknowledged. |

**Owner-approved configuration:** 100 physical, 95 names; 1 commander; 36 lands (Island 3, Swamp 3, Mountain 2 plus 28 nonbasic); 12 acceleration artifacts, 14 Game Changers; Grixis; all officially Commander legal; no project exceptions. Power Bracket **4 — Optimized**, Archidekt tags **Discard / Dragons / Extra Combats**.

## Exact tests, scope, and provenance

- Independently recalculated raw SHA `a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a` from the engineering candidate and refetched source.
- [PR #685](https://github.com/corymstover/GrokBotMTGCompanion/pull/685), exact engineering head `6bc6ff135e90db1237c0dd9881017aaf36e249fe`. Four exact-head workflows SUCCESS: `40054286052`, `40054286088`, `40054286009`, `40054286063`.
- All 95 distinct card names independently resolved and legality/Oracle/identity checked using Crosis Oct23 archived live Scryfall and three canonical Cecily/Bjorna Oct23 selected live Scryfall channel-land records. Full selected record included with canonical receipt.
- Bounded interactions: Crosis trigger cost {2}{B}; Painter's Servant color changes; Megrim/Caress/Raiders' Wake per discarded card; Bloodchief **not active** until three quest counters; Sword of Feast and Famine + Aggravated Assault **not unconditional** and needs ongoing combat damage, {3}{R}{R} and optional additional {2}{B}. Existing Notion Thief + Teferi's Puzzle Box remains.
- The formal M6 I/J Grok first-pass five-swap certificate and sealed CI workflow were **not** re-sealed for Rev2. Review packet records the abandoned temporary sealed-workflow change and exact restoration. New Rev2 CI was additive. This approval does not assert independent third-model Pass C or measured gameplay win rate.
- No other roster, M7 approval SHA, historical source or project exception is modified. Canonical approval PR and its own exact-head CI and post-merge verification complete the lock.

## Governance

This is a **specific owner approval** for nine changes and the exact decklist. No next deck is approved implicitly; proceed to tracker Deck #11 **Cult of Skaro** only after canonical merge and post-merge raw SHA match. Once locked, do not reopen Crosis without Cory's explicit instruction.
