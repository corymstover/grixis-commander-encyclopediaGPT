# Abaddon Step 4 — Context Check

**Date:** 2026-10-13 UTC  
**Branch:** `refinement/campaign-2026-10-12`  
**Deck changes:** None  
**Finalization gate:** NO

## Scope

This bounded step checked two previously identified contextual gaps: the Harnfel face of Birgi // Harnfel, and Bituminous Blast.

## Findings

- **Harnfel, Horn of Bounty:** Discarding a card is the activation cost; the ability exiles the top two cards and permits playing them that turn. Spells actually cast from exile can trigger applicable cast-from-exile payoffs but do not qualify for Abaddon's hand-only cascade grant. Normal costs and timing restrictions apply.
- **Bituminous Blast:** Mana value 5, instant, printed cascade, and 4 damage to target creature. If cast from hand during its controller's turn with Abaddon on the battlefield and at least five aggregate opponent life lost that turn, it gains a second cascade instance. Those cascade triggers resolve above the Blast, before its damage resolves. A Blast cast from another zone keeps printed cascade but does not receive Abaddon's hand-cast grant.

## Evidence

- Wizards, *Kaldheim Release Notes* (Birgi // Harnfel card text and play permission): https://media.wizards.com/2021/downloads/KHM_Release_Notes/EN_MTGKHM_ReleaseNotes_20210113.pdf
- Bituminous Blast card text and rulings: https://www.mtg.wtf/card/c16/182/Bituminous-Blast
- Magic Comprehensive Rules: https://magic.wizards.com/en/rules

## Disposition and next step

Both contextual gaps are checked. This does not certify all remaining interaction claims or the exact-list Oracle/identity gate. Next bounded step: verify Blasphemous Act's own-board interaction and opportunity cost. The live Oracle/identity refresh, final list/hash checks, current official legality check at approval, and explicit user approval remain required. No cards changed.
