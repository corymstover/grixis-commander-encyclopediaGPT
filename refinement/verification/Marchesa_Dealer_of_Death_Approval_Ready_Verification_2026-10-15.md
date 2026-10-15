# Marchesa, Dealer of Death — Approval-Ready Verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**  
Candidate SHA-256: `34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1`

## 1. Authoritative baseline

The current FINAL CSV/TXT exports for `Marchesa__Dealer_of_Death` reconcile at exactly 100 cards. The frozen FINAL export remains historical baseline evidence and is not modified by this refinement.

Baseline raw TXT SHA-256 recorded during recovery: `a2535035eb09e1d2ee6f3c5a21dc2c2d2a0be6777dfa0e7fb153073f664610c7`.

The approval-ready candidate is a 48-card rebuild from that baseline: 48 cuts and 48 additions, with all 99 baseline noncommander slots explicitly adjudicated in `refinement/decisions/Marchesa_Dealer_of_Death_Whole_List_Audit_2026-10-15.csv`.

## 2. Commander blueprint and natural ceiling

Marchesa, Dealer of Death is a U/B/R 3/4 Human Rogue for {U}{B}{R} with the current Oracle ability: whenever you commit a crime, you may pay {1}; if you do, look at the top two cards of your library, put one into your hand, and the other into your graveyard.

Commander-first plan:

1. Cast Marchesa early using dense fast mana.
2. Turn normal cEDH interaction and dedicated targeted activated abilities into crimes.
3. Convert each paid crime trigger into card selection plus graveyard setup.
4. Use repeatable crime engines to keep Marchesa active across the full turn cycle.
5. Close through compact deterministic cEDH lines rather than bloated generic Grixis win packages.

Natural ceiling: **Power Bracket 5 — cEDH**. This is supported by current competitive evidence, including Takeda Ryuhei's first-place Marchesa finish in a 16-player Commander event on 2026-10-11 and multiple additional September/October 2026 Marchesa placements.

## 3. Candidate structure

- Total cards: **100**
- Distinct names: **100**
- Commander: **1**
- Noncommander cards: **99**
- Lands: **29**
- Creatures: **12**
- Planeswalkers: **1**
- Instants: **29**
- Sorceries: **6**
- Enchantments: **7**
- Artifacts: **15**
- Singleton compliance: **PASS**
- Commander color identity: **B/R/U**
- Candidate color-identity compliance: **PASS**
- Project exceptions: **none**

## 4. Official legality checkpoint

Current Wizards Commander banned-list checkpoint reviewed 2026-10-15. No card in the candidate is on the current Commander banned list, and no project-specific exception is required.

Official Commander legality gate: **PASS**.

The 2026-10-12 Banned & Restricted announcement changed Competitive Brawl only; it did not introduce a new Commander ban affecting this candidate.

## 5. Key rules / interaction verification

### Marchesa crime trigger

A crime is committed when a spell, activated ability, or triggered ability you control targets an opponent, something an opponent controls, and/or a card in an opponent's graveyard. A single spell or ability can cause at most one crime. Marchesa therefore turns ordinary targeted interaction into optional {1} top-two selection.

### Aphetto Alchemist + Hawkeye's Bow

With Hawkeye's Bow equipped to an Aphetto Alchemist that can tap, activate Aphetto targeting itself. The Bow triggers when the equipped creature becomes tapped and deals 1 damage to each opponent. Aphetto then untaps itself. Repeating this loop deals deterministic lethal damage to all opponents.

**Combo functionality: PASS.**

### Spatial Binding

Spatial Binding's activated ability costs 1 life and targets a permanent to stop it from phasing out until your next upkeep. Targeting an opposing permanent is therefore a repeatable, mana-free crime source while Marchesa is present.

### Hex Parasite

Hex Parasite has `{X}{B/P}: Remove up to X counters from target permanent...`. X may be zero. Selecting an opposing permanent as the target therefore gives the deck a very cheap repeatable crime activation even when no counter needs to be removed.

### Spellskite

Spellskite's activated ability can target a spell or ability even when Spellskite cannot ultimately become that spell or ability's legal target. When the activation targets a spell or ability controlled by an opponent, the activation itself satisfies Marchesa's crime condition.

### Tezzeret, Cruel Captain

Tezzeret is colorless and Commander-legal. Its 0 ability untaps target artifact or creature, allowing it to target an opposing permanent as a crime when useful. Its -3 searches for an artifact with mana value 1 or less, including Hawkeye's Bow or Lion's Eye Diamond. Displacer Kitten can blink Tezzeret as a noncreature spell is cast; the returned Tezzeret is a new object and may activate a loyalty ability again that turn, subject to normal timing and priority.

### Urborg

The candidate uses **Urborg** (the legendary land), not Urborg, Tomb of Yawgmoth. It taps for black and can tap to target a creature and remove first strike or swampwalk until end of turn. The target may legally be a creature without either ability; targeting an opposing creature can therefore create a crime from a land slot.

### Talon Gates of Madara / Hammerheim / utility-land crimes

Talon Gates targets up to one creature when it enters; choosing an opposing creature creates a crime. Hammerheim and Urborg similarly provide targeted land abilities, increasing Marchesa-specific utility without consuming spell slots.

### Lapis Lazuli Talisman + Bender's Waterskin

Bender's Waterskin untaps during each other player's untap step and taps for one mana of any color. Lapis Lazuli Talisman creates a triggered ability whenever a player casts a blue spell; that ability can target an opposing permanent, which itself commits a crime, and paying {3} on resolution untaps the target. Waterskin provides repeatable opponent-turn mana to exploit the untap portion when useful. This package is retained as an established commander-specific engine rather than treated as a generic artifact slot.

### Compact win packages

- **Tainted Pact + Thassa's Oracle:** candidate has no duplicate card names, so Tainted Pact supports the established Oracle line.
- **Underworld Breach + Lion's Eye Diamond + Brain Freeze:** deterministic storm/graveyard win package; Marchesa's own selection ability naturally adds cards to the graveyard.
- **Aphetto Alchemist + Hawkeye's Bow:** commander-adjacent deterministic damage line described above.

Relevant combo/rules gate: **PASS**.

## 6. Candidate exhaustion and red-team review

Project top-100 Marchesa candidates were reviewed as discovery evidence, not automatic additions. The current FINAL baseline, stale-audit alternatives, current competitive Marchesa lists, dedicated crime engines, interaction replacements, mana-base challengers, and generic cEDH staples were all compared.

Specific red-team challengers included Exhibition Tidecaller, Glasses of Urza, Ghost Vacuum, Hexing Squelcher, and additional baseline crime-matters creatures.

The key red-team conclusion was **not** to maximize the raw count of cards that say or imply “crime.” At cEDH speed, Marchesa already converts the deck's necessary targeted interaction into crimes. The best commander-first shell therefore combines normal cEDH interaction with a small number of unusually efficient repeatable crime sources and compact win lines.

Lapis Lazuli Talisman was specifically challenged and retained. Its interaction with Bender's Waterskin gives the shell repeatable opponent-turn targeting/untap utility, and the exact configuration has current specialist tournament evidence.

Final serious adversarial pass: **ZERO NEW MATERIAL IMPROVEMENTS**.

## 7. Final conclusion

The exact SHA-bound candidate is:

`34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1`

It is **APPROVAL_READY** under the project's current-cycle standards:

- authoritative baseline reconciled;
- all 99 baseline noncommander slots audited;
- 100-card / singleton structure verified;
- B/R/U color identity verified;
- current official Commander legality checkpoint passed;
- no project exception required;
- relevant crime, blink/new-object, targeted-ability, and combo interactions verified;
- candidate pool exhausted;
- adversarial red-team completed;
- final serious pass yielded zero new material improvements.

**Do not lock or mark approved until the user explicitly approves this exact candidate.**
