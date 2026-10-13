# Abaddon Interaction Audit — Step 1 Results and Remaining Card-Level Coverage

**Snapshot:** frozen list dated 2026-10-12  
**Baseline TXT SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`  
**Decklist changes:** none  
**Finalization status:** NOT APPROVED / final gate NO

## Purpose

This is a bounded coverage control for completing the final remaining Abaddon rules/interaction audit. It is intentionally narrower than another deck-research or candidate-ranking pass. Already documented interactions remain closed unless a current rules/text change or a specific contradiction is found.

## Already documented and treated as provisionally closed

The existing Abaddon interaction review contains sourced discussion of:
- Abaddon mana value 5, hand-cast condition, and same-turn aggregate opponent life-loss threshold.
- Cascade rules, multiple cascade instances, and why Aurora Phoenix's return ability can trigger from an Abaddon-granted cascade spell.
- Why Aurora Phoenix vs Mind's Desire remains performance-inconclusive under the available Forge AI pilot; Mind's Desire stays in the baseline.
- Bloodletter of Aclazotz and Solphim, Mayhem Dominus: the difference between damage replacement and life-loss replacement, with turns/opponents caveats.
- Threshold setup via Boltwave, Flame Rift, Loyal Subordinate, Neheb, the Eternal and Rakdos, Lord of Riots.
- Cast-from-exile and non-hand-cast value: Passionate Archaeologist, Keeper of Secrets, Nalfeshnee, Prosper, Tome-Bound, The Lost and the Damned, The Ruinous Powers, Wild-Magic Sorcerer and Delayed Blast Fireball.
- Casts versus copies and cast/copy triggers: Exalted Flamer of Tzeentch, Kessig Flamebreather, Vivi Ornitier, Storm-Kiln Artist, Birgi, God of Storytelling, Noise Marine and Call Forth the Tempest.
- Cascade hits with mana value zero: Ancestral Vision, Inevitable Betrayal and Profane Tutor.
- Underworld Breach + Lion's Eye Diamond + Brain Freeze: graveyard fuel, escape costs, storm copies, and why the line is resource-dependent rather than a free infinite.

These are coverage notes, not a claim of certification across every card in all 100 slots or every state-dependent corner case.

## Exact-list audit coverage ledger

The remaining audit must now proceed from the 100-card frozen TXT, not infer completeness from the current narrative review alone. For each card/package, mark one of:
- **CLOSED** — materially relevant interactions covered with exact current Oracle/rules evidence.
- **NO SPECIAL INTERACTION** — card has no material rules interaction beyond ordinary use; Oracle text/role verified.
- **OPEN** — a meaningful interaction, dependency, or rules question still requires research.
- **NOT APPLICABLE** — explicitly justified.

Per-card record fields: exact exported card name; source role tag; Oracle ID; text verification date; interaction class; interaction finding; conditions/limitations; source URL(s); status; reviewer note.

The static metadata audit already validates the frozen archive/TXT hashes, 100-card count, one Abaddon commander marker, singleton/copy rules, and exact deck-scoped metadata join for 94 distinct names. Its dated Scryfall overlay is not a substitute for refreshing official Commander legality immediately before final approval.

## Step-by-step closeout order

1. **Step 1 — Interaction coverage control:** inventory all 94 distinct names and classify each against the existing review; do not alter cards.
2. Step 2 — Resolve only uncovered material interactions and dependency chains; prioritize the Breach line's exact sequencing and any remaining cast/copy, replacement-effect, zone, and timing issues.
3. Step 3 — Re-run current Oracle and official Commander legality/name identity checks for the exact frozen deck at closeout, keeping project-authorized exceptions distinct.
4. Step 4 — Independently verify final list count, singleton/copy rules, Grixis color identity and baseline hash; produce the exact copy-paste list plus audit certificate.
5. Step 5 — Present the list for explicit user approval. Only after approval can the tracker finalization gate change to YES.

## Stop rule

Do not re-open Aurora Phoenix vs Mind's Desire based on the same uninformative Forge pilot. Do not re-rank the full candidate pool. Do not change the baseline during this audit. New candidates only re-enter consideration if source-backed evidence identifies a plausible, material commander-specific improvement.

## Step 1 result — completed 2026-10-13 UTC

The exact frozen Abaddon list has been inventoried into `Abaddon_Interaction_Coverage_Inventory_2026-10-13.csv`.

- **94/94 distinct card names** are represented; the source list remains 100 total cards including commander.
- **33 names** are explicitly mentioned in the existing interaction review and require contextual scope-checking before any item is considered closed.
- **61 names** are not explicitly mentioned in that review and are queued for triage.
- “Not explicitly mentioned” does not mean a card is defective or must get a separate rules entry. The next step groups these by role and checks which actually have material rules dependencies, stateful triggers, special zone behavior, or relevant interactions.

No decklist changes were made. Existing explicit coverage remains provisional, and Abaddon's final gate remains NO.


## Step 2 result — role-based triage completed

The refined [Abaddon Interaction Triage](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Interaction_Triage_Updated_2026-10-13.csv) is now the preferred per-card triage source. It distinguishes ordinary land/ramp roles from cards with meaningful functional constraints and flags material contextual checks rather than treating every previously unmentioned card as a rules problem. The companion [Role Triage Summary](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Role_Triage_Summary_2026-10-13.md) summarizes the result.

**Next bounded step:** verify only the material contextual checks against current Oracle text and Comprehensive Rules, especially top-deck/cascade sequencing, alternate-cost spells, Jeska's Will's exile casts, Thermo-Alchemist, and any remaining named interaction questions. The worked Breach sequence has a separate updated audit and should not be re-opened unless a specific contradiction appears. No card changes; final gate NO.


## Step 3 result — material contextual interaction groups spot-checked (2026-10-13 UTC)

A bounded current-rule review was added to Section 12 of the expanded interaction review, covering top-deck/cascade sequencing, alternate/free-cost interaction, Jeska's Will exile casts, and Thermo-Alchemist threshold timing. Findings include: alternate costs do not change mana value; cascade compares the hit to the spell with cascade; mana-value-1 cantrips/tutors and mana-value-0 Pact of Negation cannot produce a lower-mana-value hit; Force of Negation's free mode is opponent-turn-only; Jeska's Will exile casts do not meet Abaddon's hand-cast condition; and Thermo-Alchemist's damage must precede the spell cast if it is to increase that spell's threshold.

**Disposition:** these four bounded groups are checked, not the entire card audit. Remaining material contextual checks include Harnfel's reverse face, Bituminous Blast, and the remaining previously mentioned cards whose explicit mention has not yet been independently confirmed in context. The exact-list live Oracle/identity refresh, final hash/count check, fresh legality check at approval, and user approval remain open. No decklist changes; final gate NO.


## Step 4 result — context checks recorded (2026-10-13 UTC)

The Harnfel face of Birgi // Harnfel and Bituminous Blast were checked in the separate [Step 4 context note](Abaddon_Step_4_Context_Check_2026-10-13.md). Harnfel creates exile-play permissions with normal costs and timing; spells cast this way do not qualify for Abaddon's hand-only cascade grant. Bituminous Blast has printed cascade and mana value 5; if cast from hand during its controller's turn at threshold five, it can gain an additional Abaddon-granted cascade. Both cascades resolve before its creature damage resolves.

These two gaps are closed only. Next bounded work unit: review Blasphemous Act's creature-only damage and own-board trade-off. No list changes; final gate remains NO.
