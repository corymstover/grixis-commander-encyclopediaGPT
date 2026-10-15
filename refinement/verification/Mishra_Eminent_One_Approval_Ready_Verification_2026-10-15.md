# Mishra, Eminent One — Approval-Ready Verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Exact candidate SHA-256: `ca94785fa43094a0053aac5c87e517c9cfaafb34c3baf9b3eccb067a167dd1a0`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## 1. Authoritative baseline reconciliation

- Authoritative source: current FINAL TXT/CSV exports (`GrixisFINALTXT60--2026.zip` / `GrixisFINAL60--2026.zip`).
- Baseline: **100 cards / 100 distinct names / 34 lands**.
- Raw FINAL TXT SHA-256: `0b33d376fc8cc82966b5004ae992ab19ffee8ebda69e710c61ac936be8696dd6`.
- Normalized current-cycle baseline SHA-256: `831dbbdb0ba5006612205b961b513f477afa113a327b200dad5883dd962032f2`.
- Candidate ranking data contains stale membership for this commander and was used only as research, never as authority over FINAL membership.

Result: **PASS**.

## 2. Exact structural verification

Exact SHA-bound candidate:
- Total cards including commander: **100**
- Lands: **34**
- Distinct card names: **100**
- Commander count: **1**
- Commander: **Mishra, Eminent One**
- Singleton compliance: **PASS**

Result: **PASS**.

## 3. Color identity

Mishra's color identity is **U/B/R**. The retained baseline already passed the project's current identity audit, and every incoming card is within U/B/R:
- Determined Iteration — R
- Machine God's Effigy — U
- Ichor Wellspring — colorless
- Master Transmuter — U
- Prized Statue — colorless
- Transmute Artifact — U
- Lich's Relic — B
- Nihil Spellbomb — B
- Repurposing Bay — U
- The Mightstone and Weakstone — colorless
- Uthros Research Craft — U
- Badlands — B/R
- Flooded Strand — colorless
- Misty Rainforest — colorless
- Verdant Catacombs — colorless
- Inventors' Fair — colorless

Result: **PASS**.

## 4. Current Oracle / official Commander legality checkpoint

Mishra's current Oracle text and copy rules were checked against Wizards' The Brothers' War release notes. The current Wizards Commander banned list was checked on 2026-10-15; no candidate card appears on the Commander banned list. The October 12, 2026 B&R announcement contains no Commander-format change affecting this candidate. Incoming cards were separately checked for current Commander legality, including the October 2, 2026 Reality Fracture card Lich's Relic.

Unexpected banned/illegal cards: **NONE**.  
Project-specific exceptions required: **NONE**.

Result: **PASS**.

## 5. Mishra Warform copy rules

Mishra creates a token copy of the targeted noncreature artifact but overwrites its name with Mishra's Warform, makes it a 4/4 Construct artifact creature in addition to its other types, and gives it haste until end of turn. Except for the stated name/type/power/toughness changes, the token copies the source artifact's copiable characteristics. It does not copy counters, tapped status, Auras, or other non-copy effects. If the source has X in its mana cost, X is 0 for the copy.

Consequences applied to the candidate:
- ETB abilities on copied artifacts trigger normally.
- Mana cost/mana value are retained unless changed by the copy effect, enabling mana-value-based sacrifice/tutor interactions.
- Tap abilities on the Warform can be used immediately because Mishra grants haste.
- A copied legendary artifact produces a legendary Warform; multiple legendary permanents named Mishra's Warform are subject to the legend rule.

Result: **PASS**.

## 6. Determined Iteration / Gonti's Aether Heart

Mishra and Determined Iteration both trigger at the beginning of combat. Their controller can order the triggers so Mishra resolves first and creates a Warform. Determined Iteration's populate instruction does not target the token in advance; on resolution it can copy the newly created creature token.

With Gonti's Aether Heart, this produces enough energy through the Heart/Warform artifact-entry triggers to exile a Warform for an extra turn. The sequence repeats on each extra turn, producing a documented infinite-turn lock.

Existing Strionic Resonator and Lithoform Engine variants with Gonti's Aether Heart were also independently retained and verified.

Result: **PASS**.

## 7. Worldwalker Helm / Urza / Thousand-Year Elixir

The retained four-card commander-native package is:
- Mishra, Eminent One
- Worldwalker Helm
- Urza, Lord High Artificer
- Thousand-Year Elixir

Mishra creates a hasty Warform copy of Worldwalker Helm and the Helm replacement effect also creates a Map. Urza turns artifact taps into blue mana. The Warform Helm can create another token copy of itself; Worldwalker Helm's replacement effect produces additional Maps. Thousand-Year Elixir allows the newly created non-hasty copies to activate tap abilities immediately. This supports the documented infinite artifact-token / creature-ETB / blue-mana loop.

Result: **PASS**.

## 8. New Warform targets and sacrifice engines

### Ichor Wellspring
A normal Warform copy draws once when it enters and once when it is sacrificed into the graveyard at the beginning of the end step. The token ceasing to exist after reaching the graveyard does not prevent the graveyard-from-battlefield trigger.

### Prized Statue
A normal Warform copy creates a Treasure on entry and another when sacrificed into the graveyard, producing two artifact tokens from one Mishra combat trigger.

### Lich's Relic
The Warform retains the Equipment's ETB triggered ability. On entry, its controller may pay {2}; when that payment is made, the reflexive trigger can destroy up to one target creature or planeswalker controlled by each opponent. This converts each Mishra combat into repeatable multiplayer creature/planeswalker removal while the source Relic remains available to copy again.

### Nihil Spellbomb
A Warform copy has haste and may immediately sacrifice itself to exile a target player's graveyard. Its graveyard trigger can still trigger from the token entering the graveyard; paying {B} draws a card.

### The Mightstone and Weakstone
A Warform copy gets the Powerstone's ETB choice (draw two or give a creature -5/-5) and can immediately tap for {C}{C} because Mishra gives it haste. The original and Warform have different names, so simply controlling one of each does not invoke the legend rule.

Result: **PASS**.

## 9. Repurposing Bay / mana value

Warform retains the copied artifact's mana cost and mana value. The token remains on the battlefield through the postcombat main phase unless otherwise removed. Repurposing Bay may therefore sacrifice an expendable Warform during the postcombat main phase and search for an artifact with mana value exactly one greater than that Warform's mana value, putting the searched artifact directly onto the battlefield.

Result: **PASS**.

## 10. Machine God's Effigy / Master Transmuter

Machine God's Effigy may enter as a copy of a creature while remaining an artifact rather than a creature and gaining `{T}: Add {U}`. The copy effect and added mana ability are part of its copiable values. Mishra can therefore later copy a noncreature Effigy; the resulting Warform becomes an artifact creature and retains the copied creature abilities plus the Effigy's added mana ability.

This is especially useful with nonlegendary artifact-engine creatures such as Master Transmuter, Goblin Engineer, and Goblin Welder. Copying a legendary creature with Machine God's Effigy still copies that supertype/name and must respect the legend rule.

Master Transmuter itself can return an expendable artifact as an activation cost and put a high-impact artifact from hand directly onto the battlefield. Thousand-Year Elixir materially improves access to its tap ability.

Result: **PASS**.

## 11. Uthros Research Craft

Uthros Research Craft has station and turns on its artifact-cast draw trigger at three or more charge counters. Mishra has power 5, so in a precombat main phase Mishra can station the Craft once and put five charge counters on it. Tapping Mishra this way does not prevent his beginning-of-combat triggered ability from triggering.

Once active, Uthros draws for each artifact spell cast, and its official ruling confirms that the draw trigger resolves even if the artifact spell is countered or otherwise leaves the stack without resolving.

Result: **PASS**.

## 12. Transmute Artifact

Transmute Artifact sacrifices an artifact during resolution, searches for an artifact card, and puts it directly onto the battlefield when the mana-value condition/payment is satisfied. The sacrifice is an effect, not an additional casting cost. This interaction was not conflated with Mishra's Warform sacrifice timing.

Result: **PASS**.

## 13. Mana-base red team

The candidate remains at **34 lands**. Badlands and three additional fetchlands replace lower-flexibility Pathway/channel sources, increasing access to the existing shocklands, original duals, basics, and Xander's Lounge. Inventors' Fair replaces the tapped Bojuka Bog after dedicated graveyard interaction is moved into Nihil Spellbomb; Fair adds an artifact tutor land when metalcraft is satisfied.

Artifact lands, Mishra's Workshop, Academy Ruins, Urza's Saga, Otawara, Takenuma, and Xander's Lounge survive the final pass because their artifact/recursion/tutor/utility roles justify their slots.

Result: **PASS**.

## 14. Mandatory strategic gates

- 99 noncommander slots independently adjudicated: **99/99**
- Whole-list result: **83 KEEP / 16 CUT**
- Candidate-ranking review: **COMPLETE**
- Current optimized Mishra evidence reviewed: **COMPLETE**
- Commander identity test: **PASS**
- Mana-base red team: **PASS**
- Rules/combo red team: **PASS**
- Adversarial final pass: **COMPLETE**
- Final serious strategic pass: **ZERO NEW MATERIAL IMPROVEMENTS**

## 15. Power and identity classification

**Power Bracket 4 — Optimized**.

Recommended Archidekt tags:
- **Artifacts**
- **Tokens**
- **Combo**

The deck's strongest deterministic lines are three- or four-piece commander-dependent engines centered on Mishra's Warform ability. Generic Breach/Brain Freeze is removed rather than used to manufacture a cEDH ceiling disconnected from the commander.

## Final gate

**APPROVAL_READY — PASS**

This document does not constitute user approval. Mishra, Eminent One remains **UNAPPROVED / UNLOCKED** until the user explicitly approves this exact SHA-bound candidate.
