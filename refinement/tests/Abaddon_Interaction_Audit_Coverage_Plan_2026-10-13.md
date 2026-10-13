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
