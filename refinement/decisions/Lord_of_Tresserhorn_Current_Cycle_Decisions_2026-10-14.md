# Lord of Tresserhorn — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Commander: `Lord of Tresserhorn`  
Tracker deck id: `Lord_of_Tresserhorn`  
Authoritative source TXT: `GrixisFINALTXT60--2026.zip / Lord_of_Tresserhorn.txt`  
Authoritative source TXT SHA-256: `eec34e6514206af7c0ea5f6b4cec1e7ec0098a8a4c6f47d96c6fb6dae5f6009e`  
Authoritative source CSV SHA-256: `dd6a78ef1829f72fbeec3baa7402a5137e69e132bff51a52574b296b2d6fd55f`  
Current-cycle clean baseline: `refinement/verification/lord_of_tresserhorn_2026-10-14/Lord_of_Tresserhorn_Current_Cycle_Baseline_2026-10-14.txt`  
Clean-baseline SHA-256: `55fd1bdb746ad9604e9a23031d080d30b708e99716a96527f1a3c3769c16942a`  
Approval candidate: `refinement/decklists/Lord_of_Tresserhorn_Approval_Candidate_2026-10-14.txt`  
Approval-candidate SHA-256: `95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e`

## Source reconciliation

The frozen October source contains exactly 100 cards and 98 distinct names; the only repeated name is `Swamp` at three copies. The supplied CSV/TXT source package reconciliation is PASS, and no project-specific legality exception applies.

The mandatory slot-by-slot audit is preserved at `refinement/decisions/Lord_of_Tresserhorn_Whole_List_Audit_2026-10-14.csv`. One adversarial correction supersedes that first-pass ledger: `Dictate of Erebos` changes from **KEEP** to **CUT**, and `Muddle the Mixture` is **ADD**. The exact SHA-bound approval candidate and this closeout are authoritative.

## Commander blueprint and natural ceiling

### Primary identity — Tresserhorn Voltron / Infect with drawback suppression

Lord is a four-mana 10/4 Zombie with a severe enters trigger: lose 2 life, sacrifice two creatures, and an opponent draws two cards. The strongest realistic Lord deck should treat that drawback as a deckbuilding puzzle rather than merely accept it. The primary engine therefore combines:

- permanent suppression: `Torpor Orb`, `Karn, Argent Defender`;
- temporary suppression: `Dress Down`;
- triggered-ability counters: `Stifle`, `Tale's End`;
- reliable evasion/haste/protection: `Brotherhood Regalia`, `Shizo, Death's Storehouse`, `Rogue's Passage`, `Wonder`, `Anger`, `Arena of Glory`, Boots/Greaves, `Not of This World`, `Slip Out the Back`, `Stubborn Denial`, `Deflecting Swat`;
- 10-power conversion: `Tainted Strike`, `Phyresis`, `Kediss, Emberclaw Familiar`, `Chandra's Ignition`, `Uncaged Fury`, `Pain for All`, `Shadowspear`.

Current 2026 optimized Lord evidence is concentrated in Infect/Voltron rather than sacrifice: the optimized sample has roughly 28 user-bracketed decks, with `Tainted Strike`, `Stifle`, `Torpor Orb`, `Phyresis`, `Kediss`, `Chandra's Ignition`, `Dress Down`, and `Shizo` among the highest-synergy cards. Contemporary self-tagged cEDH evidence for the exact commander is too small to justify converting the list into generic Grixis cEDH.

**Natural ceiling: Power Bracket 4 — Optimized.**

### Secondary identity — Zombie sacrifice / recursion parity and compact backup combos

The baseline's sacrifice theme is not discarded. It is narrowed to the pieces that solve Lord's own creature-sacrifice requirement or form genuine deterministic engines:

- recurring/renewable fodder: `Bitterblossom`, `Bloodghast`, `Jadar`, `Ophiomancer`, `Nether Traitor`, `Reassembling Skeleton`, `Shambling Ghast`, `Headless Rider`, `Wilhelt`;
- free/core outlets: `Carrion Feeder`, `Viscera Seer`, `Goblin Bombardment`, `Ashnod's Altar`, `Phyrexian Altar`, `Warren Soultrader`, plus land-slot `High Market` / `Phyrexian Tower`;
- combo spine: `Gravecrawler`, `Rooftop Storm`, `Pitiless Plunderer`, `Warren Soultrader`;
- compact payoffs: `Blood Artist`, `Zulaport Cutthroat`, `Diregraf Captain`, `Goblin Bombardment`.

This preserves Lord's Zombie/sacrifice personality while preventing the deck from remaining a generic aristocrats shell with a 10/4 commander attached.

## Exact current-cycle changes — 27 one-for-one swaps

### Nonland cuts

1. `Accursed Marauder` — ETB edict conflicts with Torpor/Karn.
2. `Dictate of Erebos` — final red-team cut; five-mana secondary-engine payoff is less valuable than `Muddle the Mixture` tutoring the primary two-mana engine.
3. `Fleshbag Marauder` — ETB edict conflicts with Torpor/Karn.
4. `Garna, the Bloodflame` — five-mana reactive recursion is too slow.
5. `Grafted Exoskeleton` — six total mana and unattach sacrifice liability; `Phyresis` is a cleaner two-mana infect conversion.
6. `Grave Pact` — `{B}{B}{B}{B}` secondary payoff; removed with Dictate to focus the shell.
7. `Mayhem Devil` — redundant backup sacrifice payoff after deterministic drain/Bombardment lines are retained.
8. `Merciless Executioner` — ETB edict conflicts with Torpor/Karn.
9. `Pawn of Ulamog` — redundant sacrifice-mana engine after the stronger Gravecrawler engines remain.
10. `Plaguecrafter` — ETB interaction conflicts with Torpor/Karn.
11. `Priest of Forgotten Gods` — tap/summoning-sickness and two-creature activation cost are too slow.
12. `Reanimate` — strong generic card but low dedicated reanimation density and little direct commander leverage.
13. `Temur Battle Rage` — base Lord deals only 20 commander damage with double strike; `Uncaged Fury` makes him 11 power and therefore 22 commander damage.
14. `Whispersilk Cloak` — shroud blocks our own `Tainted Strike`, `Chandra's Ignition`, `Pain for All`, and `Slip Out the Back`.
15. `Woe Strider` — redundant three-mana outlet and its Goat ETB is blanked by Torpor/Karn.
16. `Yahenni, Undying Partisan` — redundant three-mana sacrifice outlet.

### Nonland adds

1. `Anger` — Lord's own ETB can sacrifice it, turning on haste immediately afterward if a Mountain is controlled.
2. `Brotherhood Regalia` — one-mana legendary equip; ward and unblockable without self-shroud.
3. `Chandra's Ignition` — direct 10-power table conversion; lethal poison with `Phyresis` or `Tainted Strike`.
4. `Deflecting Swat` — free commander protection/redirection once Lord is controlled.
5. `Karn, Argent Defender` — two-mana current card whose static ability prevents artifact/creature enters events from causing triggered abilities; directly suppresses Lord's drawback.
6. `Muddle the Mixture` — live counterspell whose transmute finds key mana-value-two cards including `Torpor Orb`, `Phyresis`, `Brotherhood Regalia`, `Nightscape Familiar`, Boots, signets, and several Zombie-engine pieces.
7. `Mystic Remora` — efficient card flow after pruning slower aristocrat-value pieces.
8. `Nightscape Familiar` — cheap Zombie fodder, generic-cost reduction for Lord, Gravecrawler enabler, and regenerating body.
9. `Not of This World` — Lord's 10 power turns targeted permanent protection into a zero-mana spell.
10. `Pain for All` — converts Lord's power into immediate noncombat damage and can reflect damage dealt to Lord across the table.
11. `Phyresis` — two-mana permanent infect on a 10-power commander.
12. `Slip Out the Back` — one-mana protection plus a permanent +1/+1 counter, making Lord 11 power for later combat lines.
13. `Stifle` — one-mana direct answer to Lord's enters trigger.
14. `Stubborn Denial` — one-mana hard counter for noncreature spells while Lord is present.
15. `Tale's End` — redundant trigger suppression plus broad legendary/ability interaction.
16. `Torpor Orb` — canonical commander-drawback suppression.
17. `Uncaged Fury` — base Lord becomes 11/5 double strike and deals 22 commander damage in one unblocked combat.

### Land cuts

1. `Crumbling Necropolis`
2. `Dragonskull Summit`
3. `Drowned Catacomb`
4. `Hall of the Bandit Lord`
5. `Haunted Ridge`
6. `Path of Ancestry`
7. `Reliquary Tower`
8. `Riverglide Pathway // Lavaglide Pathway`
9. `Shipwreck Marsh`
10. `Stormcarved Coast`
11. `Sulfur Falls`

These are primarily tapped/conditional/low-impact sources. `Reliquary Tower` is the deliberate land-count reduction.

### Land adds

1. `Arena of Glory` — red source and commander haste engine.
2. `Badlands` — fetchable untapped BR dual.
3. `Cavern of Souls` — naming Zombie makes Lord and much of the secondary engine uncounterable.
4. `Mana Confluence` — unconditional Grixis fixing.
5. `Marsh Flats` — fetchable typed-dual access and Bloodghast landfall fuel.
6. `Misty Rainforest` — fetchable typed-dual access and Bloodghast landfall fuel.
7. `Phyrexian Tower` — land-slot sacrifice outlet / `{B}{B}` conversion.
8. `Shizo, Death's Storehouse` — untapped black source plus low-cost fear for the legendary commander.
9. `Underground Sea` — fetchable untapped UB dual.
10. `Volcanic Island` — fetchable untapped UR dual.

The candidate moves from **36 lands to 35**, while materially improving untapped fixing and adding commander-specific utility. The existing low-cost rocks/talismans/signets, Nightscape Familiar, and land quality support this reduction.

## Verified strategic/rules lines to carry into the final rules gate

1. **Suppress the drawback:** Torpor Orb/Karn prevent the Lord enters trigger from triggering; Dress Down must already be active as Lord enters; Stifle/Tale's End can counter the triggered ability once it is on the stack.
2. **Infect combat:** `Tainted Strike` makes base Lord 11 power with infect for the turn; any player dealt that combat damage receives lethal poison.
3. **Kediss poison spread:** after an infect Lord deals combat damage to one opponent, Kediss causes Lord itself to deal the same amount to each other opponent; infect applies to that noncombat damage while Lord still has infect.
4. **Ignition poison:** `Phyresis` + `Chandra's Ignition` causes Lord to deal 10 infect damage to each opponent. With `Tainted Strike`, Lord is 11 power and the same line deals 11 infect.
5. **Commander-damage one-shot:** `Uncaged Fury` turns base Lord into 11/5 double strike for 22 combat damage if both damage steps connect.
6. **Pain for All:** its Aura ETB makes the enchanted Lord deal damage equal to his power to another target. If Lord has infect at resolution, that damage is infect. If Lord is dealt damage, the Aura's second trigger can make Lord deal that much to each opponent. A regeneration shield can save Lord from lethal damage such as `Blasphemous Act`; regeneration cannot save sacrifice or lethal -X/-X.
7. **Anger:** if Lord's enters trigger is allowed to resolve and sacrifices Anger, Anger is then in the graveyard; with a Mountain controlled, Lord has haste after resolution.
8. **Rooftop Storm / Gravecrawler:** with another Zombie and a free sacrifice outlet, Rooftop Storm permits Gravecrawler to be repeatedly cast from the graveyard for `{0}`. Bombardment kills directly; Altars generate mana; drain payoffs kill through death triggers.
9. **Phyrexian Altar / Pitiless Plunderer / Gravecrawler:** with another Zombie, sacrifice Gravecrawler to Altar for black, Plunderer creates Treasure, spend the black to recast Gravecrawler, and repeat to generate arbitrary Treasure/death/cast events.
10. **Warren Soultrader / Gravecrawler:** with another Zombie, each loop pays 1 life and makes one Treasure to recast Gravecrawler. `Blood Artist` or `Zulaport Cutthroat` offsets the life payment while opponents lose life, creating a deterministic kill loop.
11. **Muddle the Mixture:** transmute finds mana-value-two pieces at sorcery speed; it remains a normal counterspell when not transmuted.
12. **Shroud sequencing:** Lightning Greaves must be moved off Lord before targeting him with our own finisher/protection spells. Brotherhood Regalia's ward does not create this self-targeting problem.

## Candidate exhaustion / adversarial challenge

The following serious challengers were reviewed and rejected after the 27-swap candidate was assembled:

- `Embercleave` — another lethal double-strike route, but expensive and less reliable than `Uncaged Fury` in a list that is not primarily go-wide.
- `Psychotic Fury` — draws a card but does not increase base Lord above 10 power; therefore not a clean single-card commander-damage kill.
- `Distortion Strike` — efficient evasion and +1 power, but the candidate already has reusable/land-slot evasion and needs protection/suppression more than another one-turn unblockable effect.
- `Glistening Oil` — reusable infect, but `Phyresis` is cleaner and `Tainted Strike` already supplies instant-speed redundancy.
- `Mask of Griselbrand` — strong lifelink/flying/death draw, but its equip cost is high and Regalia/Shadowspear better support immediate kill turns.
- `The Black Gate` / `Minas Morgul, Dark Fortress` — useful evasion lands, but their activation/targeting restrictions are weaker than Shizo/Rogue's Passage for this exact shell.
- `Sundial of the Infinite` / `Obeka, Brute Chronologist` — can neutralize the Lord trigger but require more setup than Torpor/Karn/Stifle/Tale's End/Dress Down.
- `Phyrexian Dreadnought` — shares the suppression package and is powerful, but is a second threat rather than an improvement to Lord's own strategy; backup slots are already occupied by coherent Zombie loops.
- `Rhystic Study` / `The One Ring` — excellent generic value but not required after `Mystic Remora`, Undead Augur, Wilhelt, tutors, and the low curve are retained.
- `Cyclonic Rift`, `Fierce Guardianship`, and additional generic Grixis staples — individually powerful, but the selected interaction suite better protects/suppresses/converts Lord specifically and avoids homogenizing the encyclopedia entry.
- `Hatred` / `Fling` / `Kazuul's Fury` — explosive but either life-intensive or noncombat conversions that do not outperform the cleaner infect/double-strike packages.
- a generic `Thassa's Oracle` / Consultation or Breach package — rejected outright as a higher-ceiling Grixis shell that would make Lord incidental rather than indispensable.

After the slot-by-slot audit, current 2026 optimized-comparison pass, Reality Fracture card review, mana reconstruction, combo verification, self-nonbo review, and final `Dictate of Erebos` → `Muddle the Mixture` adversarial correction, there are **ZERO NEW MATERIAL IMPROVEMENTS** remaining under the commander-first stopping standard.

## Candidate structural state

- Total cards: **100**
- Distinct names: **98**
- Repeated name(s): **Swamp x3 only**
- Lands: **35**
- Commander: **Lord of Tresserhorn**
- Intended color identity: **B/R/U**
- Project exceptions expected: **none**
- Proposed natural ceiling: **Power Bracket 4 — Optimized**

The candidate remains **NOT APPROVED** pending the exact SHA-bound complete fail-closed Oracle/color-identity, official Commander legality, rules, structure, and singleton gate plus explicit user approval.
