# M8 original-P1 bounded batch A — strict evidence boundary

Date: October 28, 2026. This document and its exact-current test fixture do not modify any owner's approved decklist or certification locks.

**Thirty-five selected original deferred P1 cases** from five final October26/27 SHA-locked decks are independently scoped with *both* a favorable and an adverse, numerically or state-bounded witness in `tests/test_m8_original_p1_batch_a_bounded.py`. The committed test blob, the tested exact-head CI run and individual method references must be available **before** any of these may be called `CURRENT_SHA_TESTED` in the separate release-evidence register. Do not self-reference a commit still under construction.

| Exact-current deck | Original tested candidate case IDs | Not tested in this batch |
|---|---|---|
| Saruman, the White Hand `dbf71bc8...` | K4–K10, E1–E2, F2–F3 (11) | W1, W2 |
| Missy `f3f8ffa6...` | K4–K7, E1–E2, F2–F3 (8) | W1–W3 |
| Rograkh/Silas Renn `97f3c0ca...` | K4, K6, K7, E1, E2, F2, F3 (7) | W1–W3 |
| Nekusar, the Mindrazer `043d2521...` | K4, K6, E1, E2, F2, F3 (6) | W2, W3 |
| Parnesse, the Subtle Brush `63b605a2...` | K4, E2, F2 (3) | W1, W2 |

## Real corrections and constraints

- **Saruman:** Stack copies are not casts; Mizzix's Mastery *casts* the copies it creates. A land-face MDFC is not cast. Harmonic Prodigy, equipped Wizard's Staff and Veyran add eligible triggers, not exponential duplication. Fall of Cair Andros and Blasphemous Act must count actual damage in excess of toughness on opposing creatures; no claims of automatic endless amass. The Black Gate targets a creature and *chooses* a player rather than targeting both. This tests a bounded target/choice precondition, not the entire Magic targeting engine.
- **Missy:** Only a real other nonartifact creature card dying and remaining returnable can become an artifact Cyberman under Missy. A face-down artifact Cyberman dying cannot itself recurse; it must flip face up first, and three reveal-only morph cards provide the legitimate route. Pyrotechnic Performer damage depends on the turned-up creature's power and Panoptic Projektor doubles qualifying face-up triggers; Dragon's Eye Savants has zero power unless modified. *They Came from the Pipes* compulsorily draws for face-down entries, risking a self-decked loop. The Valeyard increases villainous choices but cannot force opponents to choose damage rather than granting controller a draw. Aphetto Runecaster is not in this current list.
- **RogSi:** Partner taxes accumulate independently; zero printed Rograkh cost becomes {2}, {4}, etc. after command-zone recasts. Vexing Bauble self-counters spells cast for zero mana unless uncounterable or Bauble removed. An LED that discards the hand cannot simply pay for an Ad Nauseam still in hand. Final Fortune and Warrior's Oath create delayed loss obligations; life-cost draw engines need actual life.
- **Nekusar:** Draw-based damage/optional Curiosity requires a real draw, a live source and correct controller. Discard wheels trigger Waste Not/Caress, shuffle-only actions do not. Harmonic Prodigy multiplies eligible Wizard-trigger events; opponent Narset can cap draws and lifegain can undo slug pressure. The old Spiteful Visions/Phyrexian Tyranny and Peer into the Abyss claims have already been dispositioned as superseded, and remain so.
- **Parnesse:** Tempt with Mayhem produces a guaranteed source copy only if a legal spell is present; opponent acceptance is optional. Actual cast/copy frequency is not presumed from card presence. Commander plus copy enabler has real multiple-spell mana commitments. Her earlier five original P1 tested findings and superseded Replication Technique remain untouched.

## Explicit limitations

These are deterministic, bounded **rules predicates and prerequisite/adverse witnesses** only. They are not a full Magic rules engine, proof of every response-stack sequence, statistical cast-turn probability, actual opponent strategic choice, or independent J/multiplayer win rate. In particular, **the 12 high-uncertainty W-case victory claims listed above are deliberately not certified** by this batch; making their pieces present is not an end-to-end executed combo proof.

Do not count this candidate as 35 resolved dispositions until its complete tested commit/test-blob/CI evidence is pinned in a separate canonical M8 register update. All 62 decklists, exception policy, user approvals, release fingerprint and unsatisfied M8 final owner-acceptance gate remain immutable.
