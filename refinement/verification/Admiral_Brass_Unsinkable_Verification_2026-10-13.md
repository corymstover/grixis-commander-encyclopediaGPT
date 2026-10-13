# Admiral Brass, Unsinkable — New-Cycle Refinement & Verification Certificate

**Deck:** #3 of 62  
**Verification date:** 2026-10-13 (America/Chicago)  
**Baseline source:** `GrixisFINALTXT60--2026.zip` and `GrixisFINAL60--2026.zip` from the immutable 2026-10-12 snapshot  
**Baseline TXT SHA-256:** `2e3721984f38bd2a19c1377357f6e737e3588152014bed816e81ce2759392196`  
**Baseline CSV SHA-256:** `15432808436dbde87fddf6025ac8c2819b5bce9e31edaf3ca9f394e17ce26487`  
**Normalized baseline-list SHA-256:** `59dd38f44624572817cfb562a92debbb177a0ca4ddfe84405a1f2f3d41d0f570`  
**Revised-list SHA-256:** `c7ecef8a83351f34de3a8a8f5e17c1bcbaf4755e1f2bab77d34911dd6d140f7d`

## 1. Structural integrity

- Baseline CSV rows: 97; baseline quantity total: 100; baseline unique names: 97.
- Baseline TXT and CSV belong to the authoritative current archives; the raw TXT hash matches the preserved source package list.
- Revised deck copy list: 97 lines; total copies: 100; unique card names: 97.
- Commander marker: exactly one, first line.
- Singleton/copy compliance: **PASS**; no repeated nonbasic card names. Repeated basic lands remain Island x2, Mountain x2, Swamp x2.
- Land total: 34, unchanged. The land swap is Crumbling Necropolis → Nesting Grounds.
- CSV/TXT quantity reconciliation: **PASS**; revised CSV contains the same 100 copies as the revised TXT.

## 2. Card identity, Oracle and legality

- Commander: Admiral Brass, Unsinkable; current Oracle identity UBR. The commander’s Oracle text is verified at [mtg.wtf](https://www.mtg.wtf/card/lcc/121/Admiral-Brass-Unsinkable).
- Baseline metadata: the current project-wide Scryfall default-cards refresh generated `2026-10-13T07:03:26.694525Z` from data bulk-updated `2026-10-12T21:06:24.577Z`; project audit reports 5,964/5,964 exact printing/name joins and no unresolved Oracle IDs/text, identity mismatches or unexpected illegal statuses outside registered project exceptions. Deck-specific prior metadata has 97/97 names and UBR identity pass.
- Two pre-existing baseline cards that the source audit marked “not reverified in candidate-ranking table” were checked against current card references on 2026-10-13: **Enterprising Scallywag** and **Ghost of Ramirez DePietro**. Both references report Commander legal and current Oracle text. [Scallywag](https://www.mtg.wtf/card/lci/148/Enterprising-Scallywag); [Ghost of Ramirez DePietro](https://mtg.wtf/card/cmm/97/Ghost-of-Ramirez-DePietro).
- Additions: **Power Conduit** is colorless and current card reference says Commander legal; **Nesting Grounds** is colorless and Commander legal; **Kitesail Larcenist** is blue identity and Commander legal. Cut cards: Dire Fleet Daredevil (red), Crumbling Necropolis (UBR) and Amphin Mutineer (blue) all fit the commander identity and are listed as Commander legal by current references. No project-specific exception applies.
- Official Commander banned list checked on 2026-10-13. No revised-list card appears on it. The October 12, 2026 Wizards announcement changed Competitive Brawl, not tabletop Commander. Sources: [official Commander banned list](https://mtgcommander.net/index.php/banned-list/), [Wizards announcement](https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026).

## 3. Commander-first strategic review

Admiral Brass, Unsinkable self-mills four on entering and at each beginning of combat on your turn can return a Pirate creature from the graveyard with a finality counter, set its base power/toughness to 4/4, and grant haste. The revised list retains its dense Pirate/reanimation/treasure shell, six recursion spells or engines, tutors and combat-based payoffs. The three accepted changes focus on a limitation unique to this commander and the value of recurring ETB Pirates:

- **Power Conduit** can remove the finality counter as a cost. If the returned Pirate subsequently dies, it may go to the graveyard rather than being exiled, making future commander recursion possible. Selecting the +1/+1-counter mode also increases that returned Pirate to 5/5 while the commander’s base-4/4 effect applies.
- **Nesting Grounds** is a land-based backup counter-removal route after combat. Its ability is restricted to sorcery timing, so it cannot remove the finality counter during beginning of combat. If Roaming Throne doubles the commander trigger and two Pirates return, Power Conduit can be used in beginning of combat and Nesting Grounds can be used later in a main phase for a second surviving Pirate.
- **Kitesail Larcenist** supplies a lower-cost Pirate ETB that can temporarily convert up to one artifact/creature controlled by each player into a Treasure artifact and strip its other abilities. It is not permanent removal: the transformed permanents revert when Larcenist leaves and can be sacrificed for mana.

## 4. Candidate decision coverage

- Candidate-decision CSV contains 16 unique candidates: **3 accepted/implemented and 13 rejected** for this revision.
- Cumulative change ledger rows are six: three additions and their paired three cuts.
- EDHREC broad-cohort metadata in the 2026-10-12 source package is labelled historical snapshot only. A same-day/current Optimized page crawl (173 decks) displayed Power Conduit at 24% (41/173, Lift 89) and Nesting Grounds at 43% (74/173, Lift 52). These are corroborating inclusion signals, not proof of optimality.

## 5. Rules and interaction checks

- Finality counter is a counter that can be removed by Power Conduit; its removal occurs as the activation cost, not on resolution. The creature receives the chosen +1/+1 counter only if that mode resolves with a legal target.
- Nesting Grounds moves a counter between two targets, whose types do not have to match, but the ability is sorcery-only; counter transfer is only successful if both targets remain legal. [Wizards rules text](https://media.wizards.com/2025/downloads/EOE_Release_Notes_R8Z03VaANE/EN_MTGEOE_ReleaseNotes_20250718.pdf).
- Kitesail Larcenist’s chosen permanents become only Treasure artifacts and lose other types/subtypes and abilities while it remains on the battlefield; targets revert when Larcenist leaves. Its controller may select up to one other artifact/creature per player. [Wizards LCI release notes](https://media.wizards.com/2023/downloads/LCI_Release_Notes_kUj28nYwbydD/EN_MTGLCI_ReleaseNotes_20231107.pdf).
- No deterministic combo claim is introduced. Relevant timing, target constraints, finality-counter handling, replacement effects and target-leaves behavior were checked.

## 6. Consistency and performance evaluation

- Final main-deck card pool contains 26 Pirate creature cards among 99 cards, excluding the Commander.
- Exact hypergeometric probability that at least one of those 26 Pirates is among the four cards milled by Admiral’s ETB is **71.09%**, assuming 99-card library, Commander already on battlefield, and no prior Pirate already in graveyard.
- Descriptive 7-card hand density: chance to draw at least two Pirate cards is **59.32%**; at least three is **26.53%**. These figures do not account for a playable hand, mana/curve, mulligans, interaction, blockers, or actual successful combat.
- No qualified matched-start multiplayer or game-simulation comparison was available for these card changes. No win-rate or empirical superiority claim is made. A gameplay sample was not substituted for rules/role analysis.

## 7. Final gate results

| Gate | Result |
|---|---|
| Source integrity and baseline provenance | **PASS** |
| 100-card count; singleton; CSV/TXT reconciliation | **PASS** |
| Commander identity; current card metadata; new card legality; official ban list | **PASS** |
| Full commander-first strategic reassessment | **PASS** |
| Candidate review and add/cut ledger | **PASS** |
| Relevant rules interactions and finality-counter engine | **PASS** |
| Consistency/performance | **PASS WITH LIMITS** — exact hypergeometric calculations only; no gameplay superiority claim |
| Final list, hash, certificate and source traceability | **PASS** |

**Final status: `APPROVED / LOCKED — ALL TECHNICAL GATES PASSED`.** This approval applies only to the exact revised TXT bytes with SHA-256 `c7ecef8a83351f34de3a8a8f5e17c1bcbaf4755e1f2bab77d34911dd6d140f7d`. Any subsequent list change requires a new revision and verification. No separate user approval is required under the 2026-10-13 cycle protocol.