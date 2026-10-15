# Obeka, Brute Chronologist — Current-Cycle Candidate Decisions

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #44 of 62  
Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15

Exact candidate SHA-256: `31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8`

## Final 19-card delta from authoritative FINAL baseline

### Strategic changes

| Cut | Add | Decision basis |
|---|---|---|
| Aggravated Assault | Fable of the Mirror-Breaker // Reflection of Kiki-Jiki | Removes a generic combat/Sword engine for ramp/loot plus a repeatable copy ability whose tokens carry a next-end-step sacrifice trigger Obeka can erase. |
| Anger | Swiftfoot Boots | Graveyard-dependent haste becomes reliable protection/haste for the commander; haste materially matters because Obeka's identity is an activated tap ability. |
| Combat Celebrant | Identity Thief | Generic extra combat becomes a commander-native attack trigger: exile an opponent's nontoken creature, then erase its delayed return trigger with Obeka to leave it exiled. |
| Nexus of Fate | Isochron Scepter | Seven-mana generic extra turn becomes the compact established `Scepter + Final Fortune + Obeka` infinite-turn/lock engine. |
| Seize the Day | Thousand-Year Elixir | Generic extra combat becomes commander activation infrastructure: newly controlled Obeka can use her tap ability immediately, and Elixir can untap a creature for another activation. |
| Sphinx of the Second Sun | Venser, Fervent Forger | Eight-mana generic value becomes a six-mana flash 2026 card that either copies an opponent's instant/sorcery twice or creates two copied permanents whose delayed sacrifice triggers Obeka can erase. |
| Sword of Feast and Famine | Apprentice Necromancer | Generic equipment/combat value becomes a cheap reanimation line whose next-end-step sacrifice trigger Obeka can remove. |
| The Master, Multiplied | Hate Mirage | Rather than using a six-mana permanent that independently turns off token sacrifice/exile triggers and substitutes for Obeka, use a four-mana temporary-copy spell whose liability Obeka herself converts into permanent value. |
| Time Warp | Come Back Wrong | Five-mana generic extra turn becomes three-mana removal/steal whose delayed sacrifice is exactly the type of drawback Obeka is designed to erase. |

### Mana-base changes

| Cut | Add | Decision basis |
|---|---|---|
| Blightstep Pathway // Searstep Pathway | Badlands | Fetchable untapped B/R dual. |
| Clearwater Pathway // Murkwater Pathway | Arid Mesa | Premium fetch for red-typed duals/tri-land. |
| Dragonskull Summit | Flooded Strand | Premium fetch for blue-typed duals/tri-land. |
| Drowned Catacomb | Marsh Flats | Premium fetch for Swamp-typed duals/tri-land. |
| Fabled Passage | Misty Rainforest | Faster premium fetch. |
| Riverglide Pathway // Lavaglide Pathway | Verdant Catacombs | Premium Swamp-typed fetch. |
| Shipwreck Marsh | Wooded Foothills | Premium Mountain-typed fetch. |
| Stormcarved Coast | Reflecting Pool | Better untapped three-color fixing in this established mana base. |
| Sulfur Falls | Arena of Glory | Red land that can supply two mana and grant haste to a creature spell when its mana is spent on that spell; specifically useful for Obeka. |
| Sokenzan, Crucible of Defiance | Minamo, School at Water's Edge | Blue-producing utility land that can untap Obeka or another legendary permanent. |

## Structural effect

- Baseline: **100 cards / 100 distinct names / 34 lands**.
- Candidate: **100 cards / 100 distinct names / 34 lands**.
- Whole-list audit: **80 KEEP / 19 CUT across all 99 noncommander copies**.
- Candidate repeats: **none**.
- Strategic changes: **9 cuts / 9 additions**.
- Land changes: **10 cuts / 10 additions**.

## Rules-critical conclusions

### Obeka's choice belongs to the active player

Obeka reads `{T}: The player whose turn it is may end the turn.` If we activate her during an opponent's turn, that opponent can decline. The final architecture therefore relies on clearing our delayed liabilities during our own turn, when we control the choice to end it.

### Correct next-end-step sequencing

Ending the turn before a `beginning of the next end step` trigger occurs skips that end step; the delayed trigger can wait for the next turn's end step. The safe commander-first pattern is normally:

1. reach our end step;
2. allow the liability to trigger;
3. with that delayed trigger on the stack, activate Obeka;
4. choose to end the turn;
5. the trigger is exiled from the stack and does not receive another `next end step` occurrence.

This distinction is required for Final Fortune, Hate Mirage, Come Back Wrong, Reflection of Kiki-Jiki tokens, Apprentice Necromancer, Venser tokens, and many retained temporary-value cards.

### Isochron Scepter / Final Fortune

`Isochron Scepter + Final Fortune + Obeka` is an established infinite-turn/lock line. Scepter casts a copy of Final Fortune each turn. During the extra turn's end step, Final Fortune's lose-the-game trigger goes onto the stack; Obeka ends the turn and removes that trigger. The sequence can repeat with `{2}` each turn while Obeka remains available.

### Identity Thief

Identity Thief exiles another target nontoken creature when it attacks and creates a delayed return trigger for the next end step. Letting that return trigger go on the stack and ending our turn with Obeka removes the trigger, so the exiled card remains exiled. Identity Thief's own `until end of turn` copy effect still ends normally in cleanup.

### Come Back Wrong

Come Back Wrong destroys a target creature and returns that card to the battlefield under our control, then creates a delayed next-end-step sacrifice. Obeka can remove that sacrifice trigger after it triggers, converting the spell into three-mana removal plus lasting theft.

### Fable / Reflection

Reflection of Kiki-Jiki creates a hasty nonlegendary creature token and a delayed sacrifice trigger for the next end step. Obeka can remove that delayed sacrifice trigger, allowing the token to remain after the turn ends. The haste granted only until end of turn expires normally in cleanup.

### Hate Mirage

Hate Mirage creates up to two copied creatures with haste and a next-end-step exile trigger. Obeka can remove the delayed exile trigger after it triggers; the created tokens remain.

### Apprentice Necromancer

Apprentice Necromancer returns a creature with haste and creates a next-end-step sacrifice trigger. Obeka can remove the sacrifice trigger after it triggers, making the reanimation effectively permanent absent other effects.

### Venser, Fervent Forger

Venser's permanent-copy mode creates two hasty copies of an opponent's permanent with a next-end-step sacrifice trigger. Obeka can erase those delayed sacrifice triggers on our turn, leaving both copied permanents. Venser's spell-copy mode is independently useful at flash speed and is not dependent on Obeka.

### Thousand-Year Elixir / Arena of Glory / Minamo

- Thousand-Year Elixir does not grant actual haste, but it permits activation of creature abilities as though those creatures had haste. That is sufficient for Obeka's `{T}` ability and it can later untap a creature.
- Arena of Glory can give the resulting creature spell haste if its generated mana is spent on that creature spell; this gives another immediate-activation route for Obeka.
- Minamo can untap a legendary permanent, including Obeka, enabling an additional activation window while still producing blue mana when not needed for utility.

## Candidate exhaustion — notable rejected alternatives

- **Footsteps of the Goryo — REJECT after Hellkite red-team.** Directly compatible with Obeka, but Apprentice Necromancer supplies a cheaper reusable-style reanimation slot and Hellkite Courser is too commander-specific to cut. No extra slot remained without displacing a stronger engine.
- **Goryo's Vengeance — REJECT.** Efficient at two mana but limited to legendary creatures. Apprentice Necromancer's any-creature targeting is more flexible in this list.
- **Cauldron Dance — REJECT.** Highly thematic but six mana plus combat/setup constraints are too demanding relative to the final reanimation suite.
- **Sedris, the Traitor King — REJECT.** Strong delayed-exile synergy but six mana and a broad unearth subengine would pull the deck toward Sedris's own encyclopedia identity.
- **Dawn of the Dead — REJECT.** Strong lift but five mana, heavy black upkeep requirements, and narrower pacing than the retained/additional reanimation engines.
- **Nightscape Familiar — REJECT at final slot stage.** Efficient cost reducer, but generic Grixis acceleration did not beat a commander-native delayed-trigger slot.
- **Face Yourself — REJECT.** Its token copies carry their own recurring end-step sacrifice condition when no planeswalker is controlled; removing one trigger with Obeka does not permanently remove the printed ability and creates dangerous opponent-turn recurrence.
- **Time Stop — REJECT.** Redundant six-mana end-turn effect; Obeka and Discontinuity already cover the role more efficiently.
- **Mimic Vat — REJECT.** Historical cut remains correct; three-mana setup plus repeated activation is less direct than the final clone/reanimation package.
- **Orthion, Hero of Lavabrink — REJECT.** Historical cut remains acceptable; five-mana mass-copy activation is slower than the final copy suite.
- **The Master, Multiplied — REJECT despite real synergy.** Current optimized token evidence supports it, but its strongest purpose independently prevents the sacrifice/exile triggers that Obeka is meant to manage. Commander necessity wins the final slot contest.
- **Additional generic extra turns — REJECT.** Nexus of Fate and Time Warp are powerful but less efficient and less commander-specific than the risky two-mana turn package.
- **Generic Thassa's Oracle/Consultation or unrelated Breach deterministic package — REJECT.** It could raise abstract speed but would homogenize the encyclopedia and reduce Obeka's strategic necessity.

## Hellkite Courser red-team reversal

The working pass originally proposed cutting Hellkite Courser. That was reversed before approval-ready binding.

Reasons to KEEP:
- bypasses commander tax by putting Obeka directly onto the battlefield from the command zone;
- grants Obeka haste, immediately enabling her tap ability;
- its own forced return at the next end step creates a drawback Obeka can erase;
- current optimized Obeka data shows Hellkite Courser as a high-inclusion/high-lift card.

The candidate therefore drops Footsteps of the Goryo instead of forcing a twentieth strategic change.

## Mana-base red team

Land count remains **34**.

Final premium structure includes:
- nine fetchlands: Arid Mesa, Bloodstained Mire, Flooded Strand, Marsh Flats, Misty Rainforest, Polluted Delta, Scalding Tarn, Verdant Catacombs, Wooded Foothills;
- original duals Badlands, Underground Sea, Volcanic Island;
- shocklands Blood Crypt, Steam Vents, Watery Grave;
- Xander's Lounge;
- City of Brass, Mana Confluence, Command Tower, Reflecting Pool;
- multiplayer lands Luxury Suite, Morphic Pool, Training Center;
- commander-relevant utility Arena of Glory and Minamo;
- Ancient Tomb, Otawara, Takenuma, Bojuka Bog;
- one each Island, Mountain, Swamp;
- Shivan Reef and Sulfurous Springs retained as untapped two-color sources.

The deck also retains Chrome Mox, Lotus Petal, Mana Vault, Sol Ring, Arcane Signet, Fellwar Stone, Izzet Signet, all three Talismans, Ancient Tomb, and Jeska's Will. No land-count reduction is justified.

## Final red-team result

The final pass challenged every proposed swap, all 99 baseline slots, Hellkite Courser, The Master, temporary-token/reanimation density, end-turn sequencing, interaction, commander haste/untap support, all 34 lands, and generic higher-power alternatives.

No challenger produced a material improvement without a larger cost in commander dependence, mana, speed, redundancy, or encyclopedia differentiation.

**ZERO NEW MATERIAL IMPROVEMENTS.**

**Decision closeout: PASS — candidate is APPROVAL_READY evidence only, not approved/locked.**

## Approval closeout

- Explicit user approval received: **2026-10-15**
- Canonical approved SHA-256: `31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8`
- Exact approved artifact: `refinement/decklists/Obeka_Brute_Chronologist_Approved_2026-10-15.txt`
- Current-cycle state: **APPROVED / LOCKED**
- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification**
- Next unlocked deck in tracker order: **Obeka, Splitter of Seconds (index 44 / deck 45 of 62)**.
