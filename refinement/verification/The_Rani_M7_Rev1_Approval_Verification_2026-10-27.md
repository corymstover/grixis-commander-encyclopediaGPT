# Deck #57 The Rani M7 Rev1 — exact-source verification and certification boundaries

**Owner-approved raw SHA-256:** `924296ed24fdc5e79431821d31a77134c5ed5c089a92cb5e69c78f78bde4fe27`.

## Exact hundred and legality

- The Rani `[Commander]` is first in the 100-card UTF-8 LF-terminated source.
- 100 physical cards; 94 unique names; basic Island ×3, Mountain ×3, Swamp ×3 are the only non-singleton entries; 33 lands.
- Every name is resolved in the source-pinned 104-card 2026-10-27 Scryfall snapshot, with official Commander-legal flag and color identity contained in `{U,B,R}`; no unresolved identity or exception.
- Eight exact additions and eight exact removals reconcile cleanly against the preserved October 15 approved predecessor. 9- and 10-swap alternatives were evaluated and rejected from approval, not silently substituted.
- Full independent M7 candidate review, 99-slot keep/cut ledger, independent decision packet, and exact-head CI are archived with engineering PR [#741](https://github.com/corymstover/GrokBotMTGCompanion/pull/741).

## Commander-first interactions

1. Rani triggers upon entering or attacking, creating a Mark Aura on **another legal target creature**; if there is none, that trigger cannot produce a Mark. The Mark adds +2/+2 and goads its enchanted creature.
2. Rani investigates only when a goaded creature deals **combat damage to one of Rani's controller's opponents**. Mere attacks, noncombat damage, and damage to nonopponents do not satisfy this condition.
3. Erdwal Illuminator doubles the **first** investigate in a turn; with Academy Manufactor, two investigations each produce one Clue, Food, and Treasure, six artifact tokens total. Further investigations that turn do not get another Illuminator bonus.
4. Thassa can exile and return a controlled Rani at end step for another ETB; the new Mark still requires a legal target. Mark on Baeloth Barrityl raises its base 2/5 to 4/7, broadening its strict **less-than** goad threshold to opposing creatures with power 0–3.
5. Time Sieve spends five artifacts and taps for one extra turn; it is **not automatically infinite**. Roaming Throne, naming Time Lord, can double Rani's triggered abilities but cannot erase costs, targeting restrictions, or damage conditions.

## Executed checks and restrictions

- Original exact-head [M7 list-and-Oracle run #40602646406](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40602646406) and [M7 decision contract #40602646407](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40602646407) both passed.
- [Engineering P0 follow-up PR #742](https://github.com/corymstover/GrokBotMTGCompanion/pull/742) contains five finite, positive-and-adversarial executable cases, source-mapped exactly to immutable M6 plan C1/K1/K2/K3/F1, each pinned to the approved raw 100 and Oracle snapshot. Refer to the per-case attestation for exact CI run and fixture.
- These are **bounded unit-level assertions**, not a complete rules engine, goldfish win-rate estimate, exact paid-turn simulation, or executed M6 I/J Phase B.
- Nine original P1 cases remain **DEFERRED** rather than mislabeled as certified.
- The canonical approval receipt and proposed registry pointers must pass the **global whole-registry M7 transfer gate** before any merge. Existing unrelated historical evidence gaps are not waived by a Deck #57 focused success.
