# Nicol Bolas — Approval-Ready Verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #41 of 62  
Exact candidate SHA-256: `e47fdd5c31dce2d5b05e8fa8c217fe94caa16ef150057f98748254fc3c841617`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## 1. Current-state recovery

Authoritative current-cycle repository state contains **40 APPROVED / LOCKED decks** through Nekusar, the Mindrazer. The reconciled tracker identifies **Nicol Bolas** as the next unlocked deck (tracker index 40 / deck 41 of 62). The adjacent following deck is **Nicol Bolas, the Ravager // Nicol Bolas, the Arisen**, which materially informs encyclopedia differentiation.

Result: **PASS**.

## 2. Authoritative baseline reconciliation

Authoritative membership source: current FINAL exports.

- FINAL TXT: `GrixisFINALTXT60--2026.zip / Nicol_Bolas.txt`
- Raw FINAL TXT SHA-256: `33f534385e7cb618bfed3d99843cc2f4709e385b18db862d4db94a20322e8d0f`
- FINAL CSV: `GrixisFINAL60--2026.zip / Nicol_Bolas.csv`
- Raw FINAL CSV SHA-256: `3aad280a76f779084c05fad7aec07a276060b38bb2e092001af834ecc3623dad`
- Baseline total: **100 cards**
- Baseline distinct names: **99**
- Baseline lands: **39**
- Repeated baseline name: **Island x2** only

The October 11 update tracker is historical evidence only. Per project source-of-truth policy, the October 12 FINAL exports control membership.

Result: **PASS**.

## 3. Current metadata checkpoint

The repository's validated current Scryfall metadata refresh was generated on 2026-10-15 at `2026-10-15T11:29:49Z` from bulk data updated `2026-10-15T09:05:41.246Z`.

Checkpoint summary:

- 99 decklist files scanned
- 1,197 distinct names requested
- 1,197 records written
- 1,049 overlay hits
- 148 live exact lookups
- unresolved names: **0**
- overall result: **PASS**
- cache SHA-256: `c2a6f8c4c8810e8b79f01edc4986523660f745db29a55d6ac9998f6358e98f38`

Candidate additions not safely inherited from the cached baseline were separately checked against current card/rules references during refinement.

Result: **PASS**.

## 4. Exact structural verification

SHA-bound candidate file: `refinement/decklists/Nicol_Bolas_Approval_Ready_2026-10-15.txt`

- Total cards including commander: **100**
- Commander: **1x Nicol Bolas**
- Lands: **37**
- Distinct names: **99**
- Repeated names: **Island x2** only
- Nonbasic/nonbasic-card singleton violations: **0**
- Baseline delta: **29 cuts / 29 additions**
- Whole-list adjudication: **70 KEEP / 29 CUT across all 99 noncommander copies**
- Strategic nonland changes: **12 cuts / 14 additions**
- Land-card changes: **17 cuts / 15 additions**, with two net land slots converted to zero-mana acceleration in Mox Diamond and Chrome Mox

Result: **PASS**.

## 5. Commander Oracle / color identity / legality

Current Nicol Bolas text checked on 2026-10-15:

- `{2}{U}{U}{B}{B}{R}{R}`
- Legendary Creature — Elder Dragon
- Flying
- At the beginning of your upkeep, sacrifice Nicol Bolas unless you pay `{U}{B}{R}`.
- Whenever Nicol Bolas deals damage to an opponent, that player discards their hand.
- 7/7

The current ruling is strategically decisive: Nicol Bolas's discard ability triggers whenever **Nicol Bolas deals damage to an opponent for any reason**, not only combat damage.

Nicol Bolas has **U/B/R** color identity. Every candidate addition is within U/B/R identity or colorless/no-color-identity land.

Nicol Bolas is currently Commander-legal. The current official Commander banned-list checkpoint was reviewed on 2026-10-15; no candidate card is a named Commander-banned card. Wizards' October 12, 2026 Banned & Restricted announcement made Competitive Brawl changes but no tabletop Commander change affecting this candidate.

Project-specific exception required: **NONE**.

Result: **PASS**.

## 6. Ingris Stingerquill

Ingris Stingerquill says that whenever a creature you control attacks, **that creature deals 1 damage to each opponent**.

When Nicol Bolas attacks, Nicol is therefore the source of 1 damage to every opponent. Each opponent damaged by Nicol gets an independent Nicol Bolas discard-hand trigger. This occurs from the attack trigger before ordinary combat damage, so Ingris can empty all opponents' hands even if Nicol is later blocked or removed before combat damage.

Ingris is also an Elder creature, so Cavern of Souls naming Elder can cast both Nicol Bolas and Ingris with uncounterable colored mana.

Result: **PASS**.

## 7. Kediss, Emberclaw Familiar

Kediss triggers whenever a commander you control deals combat damage to an opponent. The commander then deals that much damage to each other opponent.

If Nicol Bolas connects for 7 combat damage to one opponent, Nicol is the source of the resulting 7 noncombat damage to every other opponent. Nicol's discard-hand trigger therefore triggers for the initially damaged opponent and each other opponent damaged through Kediss.

Kediss does not create commander damage for the secondary opponents because that damage is noncombat, but commander-damage accounting is irrelevant to Nicol's discard trigger.

Result: **PASS**.

## 8. Dragon Tempest

Dragon Tempest gives a flying creature haste when it enters under your control. It also triggers when a Dragon enters under your control and has **that Dragon** deal damage to any target equal to the number of Dragons you control.

Nicol Bolas is both flying and a Dragon. When Nicol enters, Dragon Tempest therefore:

1. gives Nicol haste; and
2. can make Nicol itself deal at least 1 damage to an opponent before combat.

Because Nicol is the damage source, the targeted opponent discards their hand. Dragon Tempest is therefore both haste infrastructure and a commander-trigger enabler rather than generic Dragon tribal filler.

Result: **PASS**.

## 9. Chandra's Ignition

Chandra's Ignition has target creature you control deal damage equal to its power to each other creature and each opponent. The creature, not the sorcery, is the damage source.

With an unmodified Nicol Bolas, Nicol deals 7 damage to each opponent and 7 damage to every other creature. Each opponent damaged by Nicol receives a discard-hand trigger.

This simultaneously acts as a commander-native table hand wipe and a broad creature sweeper.

Result: **PASS**.

## 10. Pain for All

Pain for All enchants a creature you control. When it enters, the enchanted creature deals damage equal to its power to another target. Whenever the enchanted creature is dealt damage, it deals that much damage to each opponent.

Enchanting Nicol Bolas therefore gives two commander-source damage modes:

- the Aura's entry trigger can make Nicol deal 7 to an opponent immediately; and
- later damage dealt to Nicol can cause Nicol to deal that much to every opponent.

Each opponent damaged by Nicol through either mode receives Nicol's discard-hand trigger. Current release notes also confirm that the reflection trigger can still resolve even if lethal damage was dealt to the enchanted creature.

Result: **PASS**.

## 11. Quicksilver Dagger / Viridian Longbow

Quicksilver Dagger grants the enchanted creature a tap ability under which **that creature deals 1 damage** to a target player or planeswalker and then you draw a card.

Viridian Longbow gives the equipped creature a tap ability under which **that creature deals 1 damage** to any target.

With either attached to Nicol Bolas, Nicol can deal 1 to an opponent without attacking. That opponent then discards their hand. Quicksilver Dagger additionally replaces the activation with a card draw; Longbow is more durable because it is Equipment rather than an Aura.

Result: **PASS**.

## 12. Curiosity after refinement

Curiosity enchants a creature and triggers whenever the enchanted creature deals damage to an opponent, allowing an optional card draw.

The baseline already contained Curiosity, but the refined candidate materially increases Nicol-sourced damage events through Ingris, Kediss, Dragon Tempest, Chandra's Ignition, Pain for All, Quicksilver Dagger, and Viridian Longbow. Curiosity therefore becomes significantly more commander-dependent and valuable in the refined shell.

Curiosity is not required for any claim of deterministic victory; it is retained as a one-mana value engine that rewards the commander's actual game plan.

Result: **PASS**.

## 13. Tinybones, Bauble Burglar / Tergrid ordering

Tinybones, Bauble Burglar triggers when an opponent discards a card and can exile that card from their graveyard with a stash counter. Tergrid, God of Fright can trigger when an opponent discards a permanent card and return that permanent from the graveyard under your control.

If both trigger from the same discarded permanent, both triggers may be placed on the stack, but the card cannot be acquired twice. Their controller chooses the order. If Tergrid moves the permanent first, Tinybones can no longer exile that card from the graveyard; if Tinybones exiles it first, Tergrid can no longer return it from the graveyard.

This is flexible overlap rather than a rules conflict or automatic double value.

Result: **PASS**.

## 14. Sangromancer

Sangromancer triggers whenever an opponent discards a card and gains 3 life for each such trigger.

Nicol Bolas causes a player to discard their **entire hand** as one effect, but each individual discarded card still satisfies Sangromancer's trigger condition. A five-card hand discarded through Nicol therefore creates five separate Sangromancer triggers for that opponent.

This produces discard-native life stabilization and replaces the baseline's less commander-aligned Megrim redundancy.

Result: **PASS**.

## 15. Aggravated Assault / Sword of Feast and Famine

Both cards remain from the baseline.

Sword of Feast and Famine triggers when the equipped creature deals combat damage to a player, causing that player to discard a card and untapping all lands you control. Aggravated Assault can be activated during a main phase for `{3}{R}{R}` to untap all creatures that attacked and create an additional combat followed by an additional main phase.

If the equipped attacker connects and the untapped lands can produce at least five usable mana in the following main phase, Aggravated Assault can create another combat. Continued successful Sword connections can repeat the sequence.

This package is retained because it amplifies Nicol's attack/damage plan rather than replacing it with an unrelated win condition.

Result: **PASS**.

## 16. Mana-base and acceleration red team

The candidate moves from **39 to 37 lands** while adding Mox Diamond, Chrome Mox, and Grim Monolith.

The reduction was deliberately capped at two lands because Nicol costs eight mana with exact colored requirements of `UUBBRR` and then asks for `UBR` each upkeep.

Final mana-base features include:

- **nine fetchlands:** Arid Mesa, Bloodstained Mire, Flooded Strand, Marsh Flats, Misty Rainforest, Polluted Delta, Scalding Tarn, Verdant Catacombs, Wooded Foothills;
- **three original duals:** Badlands, Underground Sea, Volcanic Island;
- **three shocklands:** Blood Crypt, Steam Vents, Watery Grave;
- **Xander's Lounge** as a fetchable UBR tri-land;
- **City of Brass, Mana Confluence, Command Tower, Exotic Orchard, Reflecting Pool** for broad fixing;
- multiplayer duals Luxury Suite, Morphic Pool, and Training Center;
- utility lands Ancient Tomb, Arena of Glory, Bojuka Bog, Cavern of Souls, Command Beacon, Hall of the Bandit Lord, Otawara, Shizo, and Takenuma;
- basics Island x2, Mountain, and Swamp.

Cavern of Souls naming Elder can support Nicol Bolas, Nicol Bolas, the Ravager, and Ingris Stingerquill. Arena of Glory can grant Nicol haste when its exerted mana is spent on his creature spell. Command Beacon can move Nicol from the command zone to hand to bypass future commander tax on that cast. Shizo supplies one-mana legendary-creature evasion while still tapping for black.

The candidate also retains Arcane Signet, three Signets, Fellwar Stone, three Talismans, Mana Vault, Sol Ring, Ancient Tomb, Dark Ritual, Cabal Ritual, Jeska's Will, Seething Song, and Nightscape Familiar in addition to the new fast mana.

Result: **PASS**.

## 17. Candidate exhaustion and encyclopedia differentiation

Project candidate research, the historical October 11 list, current original-Nicol evidence, commander-source damage engines, discard payoffs, haste/evasion, extra combats, protection, fast mana, planeswalker/Bolas flavor cards, alternate kills, and mana-base challengers were reviewed.

Notable rejected alternatives:

- **Nicol Bolas, Planeswalker / Nicol Bolas, God-Pharaoh / Nicol Bolas, Dragon-God:** powerful and flavorful, but importing the entire planeswalker package would materially overlap with the immediately following Nicol Bolas, the Ravager deck. The original Elder Dragon deck is kept centered on Nicol himself dealing damage and emptying hands.
- **Cruel Ultimatum / Dark Intimations:** strong flavor, but expensive one-opponent value does not beat direct commander-source hand-wipe engines.
- **Pandemonium:** can make Nicol deal 7 on entry, but symmetrically empowers every opponent's entering creatures.
- **Electropotence:** valid Nicol-source damage but imposes an additional `{2}{R}` payment after an already eight-mana commander.
- **Hermetic Study / Fire Whip / Psionic Gift:** valid pingers but weaker than Quicksilver Dagger's card draw and Viridian Longbow's reusable Equipment form.
- **Soul's Fire / Surestrike Trident:** valid commander-source damage, but Chandra's Ignition scales the effect across every opponent and the creature board.
- **Samut, Hazoret's Champion:** haste redundancy is already sufficient through Dragon Tempest, Greaves, Boots, Hall of the Bandit Lord, and Arena of Glory.
- **Karlach, Fury of Avernus:** additional-combat redundancy is less important than commander-source damage because Aggravated Assault plus Sword of Feast and Famine already provides the stronger repeat-combat package.
- **Bloodchief Ascension / Painful Quandary / Quest for the Nihil Stone / Shrieking Affliction:** aftermath payoffs exist, but they do not help Nicol create the decisive damage event; current discard-conversion density is sufficient.
- **Infect package:** efficient shortcut, but it bypasses rather than maximizes Nicol's defining hand-destruction mechanic.
- **Wheel package:** refilling opponents' hands conflicts with this deck's preference that successfully emptied hands stay empty and also overlaps with Nekusar/Gwendlyn identities.
- **Generic Oracle/Consultation or unrelated deterministic Breach packages:** raise generic Grixis power at the expense of commander necessity.

Commander-necessity test: the refined deck's strongest new lines require **Nicol Bolas himself**. Ingris, Kediss, Dragon Tempest, Chandra's Ignition, Pain for All, Quicksilver Dagger, Viridian Longbow, and Curiosity all become materially weaker or change function without Nicol's unique damage-to-discard text.

Final serious strategic pass: **ZERO NEW MATERIAL IMPROVEMENTS**.

Result: **PASS**.

## 18. Mandatory gate summary

- Current repository state recovered: **PASS**
- Current-cycle locked decks before Nicol approval: **40/62**
- Nicol Bolas correctly identified as next unlocked deck: **PASS**
- Authoritative FINAL baseline reconciled: **PASS**
- Baseline land count corrected/verified at 39: **PASS**
- Mandatory 99-slot audit: **99/99 PASS**
- Whole-list result: **70 KEEP / 29 CUT**
- Candidate-ranking / external challenger exhaustion: **PASS**
- Commander Oracle text: **PASS**
- Any-damage trigger scope: **PASS**
- Color identity: **PASS**
- Current official Commander legality checkpoint: **PASS**
- Project exceptions: **NONE REQUIRED**
- Ingris / Kediss / Dragon Tempest commander-source rules: **PASS**
- Chandra's Ignition / Pain for All commander-source rules: **PASS**
- Quicksilver Dagger / Viridian Longbow commander-source rules: **PASS**
- Tinybones / Tergrid trigger-order interaction: **PASS**
- Aggravated Assault / Sword of Feast and Famine line: **PASS**
- Mana-base / acceleration red team: **PASS**
- Adjacent-deck differentiation from Nicol Bolas, the Ravager: **PASS**
- Commander-first coherence: **PASS**
- Natural power ceiling: **Power Bracket 4 — Optimized**
- Exact 100-card count: **PASS**
- Singleton compliance: **PASS**
- Final serious pass: **ZERO NEW MATERIAL IMPROVEMENTS**

Recommended Archidekt tags: **Discard / Commander Damage / Control**.

## Final gate

**APPROVAL_READY — PASS**

Exact approval-ready candidate SHA-256: `e47fdd5c31dce2d5b05e8fa8c217fe94caa16ef150057f98748254fc3c841617`.

This record is working verification evidence only. Nicol Bolas remains **UNAPPROVED / UNLOCKED** until the user explicitly approves this exact candidate.
