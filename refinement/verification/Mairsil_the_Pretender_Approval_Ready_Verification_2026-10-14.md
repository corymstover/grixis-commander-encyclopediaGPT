# Mairsil, the Pretender — Current-Cycle Approval-Ready Verification — 2026-10-14

Cycle: `global-restart-2026-10-13`
Tracker position: deck #33 of 62 (tracker index 32)
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**
Proposed-list SHA-256 (working candidate only): `51e8fd18c7ded6744a4fa2f871925a0679f85dada3e6e517334bd13c07889ee5`

## Authoritative-state recovery

- `state/current_deck_overrides.json` contains 32 current-cycle APPROVED/LOCKED decks through Mai and Zuko and contains no Mairsil entry.
- The tracker still contains stale unlocked rows for some decks already locked in state; current-cycle state therefore controls continuity.
- The next unlocked commander in tracker order is Mairsil, the Pretender.

## Baseline source reconciliation

Authoritative current baseline is `GrixisFINAL60--2026.zip :: Mairsil__the_Pretender.csv`, reconciled to `GrixisFINALTXT60--2026.zip :: Mairsil__the_Pretender.txt`, 100 cards.

The inherited v8.1.4 `deck_card_audit.csv` contains an older Mairsil revision. The current final export differs 5-for-5:

- Current final only: Endling; Gilded Lotus; Nevinyrral's Disk; Oriq Loremage; Torchling.
- Stale audit only: Azami, Lady of Scrolls; Cavern Harpy; Counterspell; Faithless Looting; Vivi Ornitier.

Per project source hierarchy, the latest final CSV/TXT export is the deck-membership baseline. No stale audit card was silently carried forward.

## Commander identity and natural ceiling

Current Oracle text: Mairsil cages an artifact or creature card from hand or graveyard on entry, has all activated abilities of owned exiled cards with cage counters, and restricts each acquired ability instance to once each turn.

The optimized plan is therefore:

1. put premium activated-ability payloads into hand/graveyard,
2. repeatedly enter/blink/copy Mairsil to add cage counters,
3. use haste/untap/cost reduction to maximize acquired tap abilities,
4. exploit caged cards whose static/triggered drawbacks are not copied,
5. close through commander-specific activated-ability loops and outlets.

Natural ceiling: **Power Bracket 4 — Optimized**. The deck is lethal, tutor-dense, fast-mana enabled, and combo-capable, but the project should not replace the cage-toolbox identity with a tournament-metagame cEDH shell.

## Exact proposed changes from authoritative baseline

1. Puppet Strings -> Pack Rat
2. Underworld Breach -> Faithless Looting
3. Animate Dead -> Essence Flux
4. Mirror-Mad Phantasm -> Displacer Kitten
5. Reanimate -> Spark Double
6. Fabled Passage -> Minamo, School at Water's Edge

## Rules / Oracle conclusions

- **Pack Rat:** Mairsil gains the activated ability `{2}{B}, Discard a card: Create a token that's a copy of this creature.` Mairsil's ruling changes self-reference to Mairsil. A creature entering as a copy of Mairsil triggers the cage ETB; the trigger remains even if the legend rule immediately removes one copy. This makes Pack Rat a repeatable discard-to-cage engine.
- **Essence Flux:** blinking Mairsil returns it as a new object. Existing caged cards remain exiled with cage counters, and the returning Mairsil triggers another cage entry. As a new object it receives fresh acquired ability instances.
- **Displacer Kitten:** each noncreature spell can blink Mairsil; the returned card is explicitly a new object, producing another cage ETB and fresh activation instances.
- **Spark Double:** enters as a nonlegendary copy of Mairsil and triggers Mairsil's cage ETB. Although copy effects do not copy non-copy effects that granted the original Mairsil abilities, Spark Double copies Mairsil's printed static cage ability, so once on the battlefield it independently gains all activated abilities from the owner's caged cards.
- **Minamo:** untaps target legendary permanent, directly supporting Mairsil's tap-ability engine while still functioning as an untapped blue source.
- **Faithless Looting:** one-mana draw-two/discard-two plus flashback is direct cage setup because Mairsil may cage from the graveyard.
- **Asmodeus retained:** Mairsil gains activated abilities, not Asmodeus's static Binding Contract replacement effect; the caged `{B}{B}{B}: Draw seven cards` therefore draws normally.
- **Quicksilver Elemental retained:** established Mairsil combo engine that can create fresh instances of acquired activated abilities and enables infinite-mana/draw lines with Gilded Lotus plus Staff of Domination, Morphling, or Horseshoe Crab.
- **Rings of Brighthearth retained:** copies Mairsil’s nonmana activated abilities. With Pack Rat caged, Rings can copy the Pack Rat activation; the copied ability does not require paying the discard cost again and creates another Mairsil-copy ETB/cage trigger.
- **Marvin retained:** Marvin gains Mairsil's acquired activated abilities while its own ruling confirms it does not gain static abilities. Mairsil's separate once-per-turn restriction is static, so Marvin provides a parallel activated-ability engine without inheriting that restriction.
- **Mirror-Mad removed:** its ruling confirms that if another creature gains its ability and no Mirror-Mad Phantasm is found, all cards in the library are milled. The proposed list does not rely on that unsafe self-mill route.

## Whole-list audit / candidate exhaustion

- All 99 noncommander slots were reviewed role by role; audit CSV records every baseline card.
- Project top-100 Mairsil candidates were reviewed as discovery evidence, including Pendant of Prosperity, Argent Sphinx, Avatar of Woe, Pili-Pala, Planar Incision, Mirage Mirror, Ulamog's Dreadsire, Necrotic Ooze, Pack Rat, Essence Flux, Minamo, Spark Double, Displacer Kitten, Agatha's Soul Cauldron, The One Ring, and tail candidates.
- Current EDHREC optimized/activated-ability evidence was checked independently; it supports the existing Mairsil core and materially supports Pack Rat, Spark Double, and the blink package, but popularity was not treated as authority.
- Newer external challengers and generic cEDH packages were reviewed and rejected where they weakened commander necessity or shifted the shell toward generic Grixis combo.
- Cavern Harpy was reconsidered because it appears in the stale audit; Pack Rat/Essence Flux/Displacer Kitten provide materially more efficient cage-reset functionality without repeatedly recasting Mairsil.
- Planar Incision was compared directly to Essence Flux; the one-mana Flux is better for the commander-primary target.
- Rings of Brighthearth was the strongest provisional cut challenger. Final red-team corrected that provisional cut: Rings has direct new synergy with caged Pack Rat and remains highly commander-specific. Reanimate is the weaker slot because generic creature recursion competes with Mairsil’s desire to leave cage payloads in the graveyard.

## Red-team / second-pass closure

Adversarial pass rechecked:

- commander-copy and legend-rule timing,
- blink/new-object behavior,
- Spark Double copy-layer implications,
- Pack Rat self-reference,
- Mirror-Mad self-mill danger,
- Asmodeus static-vs-activated distinction,
- Marvin static-vs-activated distinction,
- Quicksilver combo functionality,
- 32-land mana structure,
- tutor/ramp/interaction density,
- graveyard setup versus excessive generic recursion,
- Rings + Pack Rat copied-activation interaction,
- candidate-ranking bias,
- current 2026 alternatives,
- mana-base modernization versus commander-specific utility.

A provisional Rings cut was overturned during the final adversarial pass in favor of cutting Reanimate. After applying that correction and rerunning the affected checks, the next serious pass produced **ZERO NEW MATERIAL IMPROVEMENTS**. Additional generic fetchland/dual-land substitutions were not manufactured because the existing 32-land shell is already highly fixed and only Minamo creates a material commander-specific improvement.

## Structural gate

Proposed list verification:

- Exactly 100 cards including commander: PASS
- Exactly 100 distinct names: PASS
- Exactly one commander: PASS
- Singleton compliance: PASS
- Land count: 32
- Commander color identity: U/B/R; proposed additions all fit: PASS
- Official Commander legality: PASS; no Mairsil project exception required
- Unexpected named Commander-banned cards: none
- Whole-list audit complete: PASS
- Candidate exhaustion: PASS
- Red-team pass: PASS
- Zero-new-material-improvement closure: PASS
- Commander-necessity / strategic-coherence check: PASS

**Result: APPROVAL_READY. Do not update current-cycle state or tracker to APPROVED/LOCKED until explicit user approval.**
