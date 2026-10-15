# Nicol Bolas, the Ravager // Nicol Bolas, the Arisen — Current-Cycle Candidate Decisions

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #42 of 62  
Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15

Exact candidate SHA-256: `5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e`

## Final 16-card delta from authoritative FINAL baseline

| Cut | Add | Decision basis |
|---|---|---|
| Dark Deal | Training Grounds | One-shot wheel/discard becomes one-mana direct commander support: Ravager's `{4}{U}{B}{R}` transform activation is reduced by `{2}` to `{2}{U}{B}{R}`. |
| Liliana of the Veil | The Theorist, Jace Beleren | Low-impact multiplayer attrition walker becomes a current four-mana planeswalker that draws during every opponent's draw step, makes blockers, and can bounce an artifact/creature from each opponent. |
| Nicol Bolas | Nicol Bolas, Planeswalker | Original Elder Dragon is now the defining commander of locked deck #41; the eight-mana Bolas planeswalker instead reinforces this deck's distinct Superfriends identity and supplies removal/theft/ultimate pressure. |
| Notion Thief | Rings of Brighthearth | Generic wheel-lock support becomes an ability-copy engine for loyalty abilities, The Chain Veil, Karn's Bastion, fetchlands, and other nonmana activations. |
| Opposition Agent | Sanctum Lurker | Generic tutor stax becomes direct planeswalker infrastructure: walkers survive at 0 loyalty and gain a multiplayer-drain `[+2]` ability. |
| Orcish Bowmasters | Dreamtide Whale | Generic draw punishment becomes repeated multiplayer proliferate whenever any player casts a second spell each turn. |
| Sheoldred, the Apocalypse | Tezzeret the Seeker | Generic value becomes a planeswalker that tutors The Chain Veil / Rings / Ichormoon / mana artifacts directly to the battlefield and can untap artifact engine pieces. |
| The One Ring | Rowan's Talent | Generic card draw becomes a direct loyalty multiplier; attaching it to the Arisen or another key planeswalker copies each activated loyalty ability without copying the loyalty cost. |
| Waste Not | Displacer Kitten | Wheel-dependent discard payoff becomes an optional Ravager ETB reset engine and a way to reuse Deepglow Skate or other nonland permanents. |
| Wheel of Fortune | Deliver Unto Evil | Generic wheel becomes Bolas-specific recursion: after Ravager transforms, controlling the Arisen satisfies the Bolas-planeswalker condition and returns up to four targeted graveyard cards to hand. |
| Windfall | Ripples of Potential | Generic wheel becomes two-mana proliferate plus optional phasing protection for permanents that receive counters. |
| Bojuka Bog | Cavern of Souls | Tapped graveyard hate can conflict with the Arisen's `-4`; Cavern protects the Elder Dragon commander cast while improving tempo. |
| Shipwreck Marsh | Reflecting Pool | Conditional slowland becomes near-perfect untapped fixing in the no-budget three-color mana base. |
| Sulfurous Springs | Wooded Foothills | Painland becomes another premium typed-dual/basic fetch. |
| Island (one of three) | Arid Mesa | Retains two Islands while adding another premium fetch for Mountain-typed duals/tri-land/basic. |
| Swamp (one of three) | Verdant Catacombs | Retains two Swamps while adding another premium fetch for Swamp-typed duals/tri-land/basic. |

## Structural effect

- Baseline: **100 cards / 96 distinct names / 34 lands**.
- Candidate: **100 cards / 98 distinct names / 34 lands**.
- Whole-list audit: **83 KEEP / 16 CUT across all 99 noncommander copies**.
- Candidate repeats: **Island x2 and Swamp x2 only**.
- Strategic changes: **11 cuts / 11 additions**.
- Land changes: **5 cuts / 5 additions**.
- Land count is deliberately preserved at the authoritative baseline's 34 because the deck already contains a dense fast-mana package and requires both four-mana commander deployment and a seven-mana transform activation.

## Commander-first rules decisions

### Training Grounds

Ravager's transform ability is an activated ability of a creature you control while Ravager is on its creature face. Training Grounds reduces the generic portion by `{2}`, from `{4}{U}{B}{R}` to `{2}{U}{B}{R}`. It does not alter colored symbols and does not apply once Nicol is a planeswalker because the relevant creature activated ability no longer exists on that face.

### Displacer Kitten / double-faced reset

Displacer Kitten can blink front-face Ravager after a noncreature spell, returning the card as a new object on its front face and retriggering the each-opponent discard ETB.

If Kitten blinks the transformed Arisen, the card likewise returns front-face up because a double-faced card enters front face by default unless an effect specifically instructs it to enter transformed. This is therefore an intentional reset line, not a way to blink the Arisen and keep the planeswalker face.

### Deliver Unto Evil

The transformed commander is a **Bolas planeswalker**, so Deliver Unto Evil's enhanced condition is satisfied while the Arisen is controlled. The spell can then return all of its up-to-four legal targeted graveyard cards to hand rather than allowing an opponent to withhold two.

### Rowan's Talent / Rings of Brighthearth

Both copy activated loyalty abilities, but the copied abilities do not repeat the loyalty cost. Rowan's Talent automatically copies the enchanted planeswalker's activated loyalty ability; Rings requires `{2}` when its trigger resolves. This lets the candidate multiply the Arisen's draw, removal, reanimation, or ultimate abilities without falsely adding/removing loyalty for the copies.

### The Chain Veil / Rings / Teferi engine

The Chain Veil's activated ability is nonmana, so Rings may copy it for `{2}`. Official Chain Veil rules state that each additional resolution grants each planeswalker another loyalty activation that turn.

With Teferi, Temporal Archmage plus The Chain Veil plus Rings and mana permanents that can collectively produce six mana after Teferi's `-1` untaps them (for example Mana Vault + Sol Ring + a one-mana permanent/land), the deck can repeat the following engine:

1. Pay `{4}` to activate The Chain Veil and `{2}` for Rings, producing two Chain Veil resolutions.
2. Use one Teferi activation to `-1`, untapping The Chain Veil and enough mana permanents to produce six again.
3. Use another Teferi activation on `+1` to restore the loyalty spent by `-1`.
4. Spend the refreshed six mana to activate/copy The Chain Veil again.
5. Each pair of Chain Veil resolutions adds two more loyalty activations, replacing the two Teferi activations consumed by the loop.

The loop can therefore generate arbitrarily many Chain Veil resolutions / planeswalker loyalty-activation permissions while Teferi's loyalty remains stable. This is a multi-piece Bracket-4 combo engine, not a claim that any two of these cards alone are infinite.

### Sanctum Lurker

Sanctum Lurker prevents the normal state-based action that puts planeswalkers into their owners' graveyards for having 0 loyalty. A surviving 0-loyalty planeswalker can later activate the granted `[+2]` ability when timing/activation restrictions permit, putting loyalty counters on itself as the activation cost.

### Ripples of Potential / Dreamtide Whale

Ripples proliferates first, then may phase out any chosen permanents you control that received counters that way. Phasing does not remove the counters, giving the deck a two-mana loyalty-growth/protection play.

Dreamtide Whale can proliferate loyalty counters whenever a player casts their second spell in a turn. Proliferate can also add a time counter to the Whale itself, extending its vanishing clock when strategically useful.

### Dark Intimations

Dark Intimations remains because it converts multiplayer sacrifice/discard into recursion and draw, and its graveyard rider gives the next **Bolas planeswalker spell** an additional loyalty counter. This rider applies to Bolas planeswalker cards cast as planeswalker spells; it is not treated as a bonus to Ravager's activated transformation, which is not casting a planeswalker spell.

## Candidate exhaustion — notable rejected alternatives

- **Cruel Ultimatum — REJECT.** Flavorful but seven mana and focused on one opponent; the final list has higher commander/planeswalker leverage at the same upper curve.
- **Ugin, the Spirit Dragon — REJECT.** Extremely powerful but generic and expensive; the deck already has abundant high-end Bolas walkers and cheaper sweepers.
- **Dack Fayden — REJECT at final slot stage.** Efficient three-mana planeswalker, but does not outperform the retained/additional loyalty engines, multiplayer draw, or artifact tutor roles.
- **Ashiok, Dream Render — REJECT.** Strong graveyard hate/tutor suppression, but graveyard exile can directly reduce targets for the Arisen's `-4` and Deliver Unto Evil.
- **Thrummingbird / Experimental Augury — REJECT.** Useful proliferate redundancy, but Dreamtide Whale, Ripples, Flux Channeler, Inexorable Tide, Tezzeret's Gambit, Karn's Bastion, Ichormoon Gauntlet, and Tekuthal already provide sufficient density.
- **Teferi's Talent — REJECT.** Powerful, but five mana and slower to multiply loyalty abilities; Rowan's Talent immediately copies the commander's activated loyalty ability at four mana.
- **Interplanar Beacon / Turbulent Wetlands — REJECT.** Planeswalker-flavored utility does not beat the no-budget fetch/dual/five-color fixing infrastructure after mana red-team review.
- **Deflecting Swat / Force of Negation — REJECT at final slot stage.** Excellent interaction, but the candidate already retains premium free/cheap protection and further interaction would require cutting identity engines.
- **Ajani Unrelenting — REJECT.** Strong 2026 planeswalker, but six mana and not more synergistic than the finalized Bolas/proliferate/Chain Veil core.
- **Additional wheel effects — REJECT.** They overlap Nekusar/Gwendlyn and refill opponents after Ravager's discard; this deck is intentionally Superfriends/transform first.
- **Generic Thassa's Oracle/Consultation or unrelated Breach packages — REJECT.** They can raise abstract power while reducing commander necessity and homogenizing the encyclopedia.

## Mana-base red team

Final land count remains **34**, exactly matching the authoritative baseline.

The candidate now has:
- nine fetchlands: Arid Mesa, Bloodstained Mire, Flooded Strand, Marsh Flats, Misty Rainforest, Polluted Delta, Scalding Tarn, Verdant Catacombs, Wooded Foothills;
- original duals Badlands, Underground Sea, Volcanic Island;
- shocklands Blood Crypt, Steam Vents, Watery Grave;
- Xander's Lounge;
- City of Brass, Mana Confluence, Command Tower, Reflecting Pool;
- Luxury Suite, Morphic Pool, Training Center;
- utility lands Ancient Tomb, Cavern of Souls, Karn's Bastion, Otawara, Takenuma, Urborg;
- basics Island x2, Mountain x1, Swamp x2.

The 34-land count is supported by Chrome Mox, Lotus Petal, Mana Vault, Mox Diamond, Mox Opal, Sol Ring, Arcane Signet, Dimir/Izzet/Rakdos Signets, Fellwar Stone, all three Talismans, Ancient Tomb, and Jeska's Will. No land was removed net in this refinement.

## Final red-team result

The final serious pass challenged all 16 swaps, every retained planeswalker, the Chain Veil package, transform support, blink/reset lines, graveyard tension, proliferate density, interaction density, wheel removal, and all 34 candidate lands.

No challenger produced a material improvement without a larger opportunity cost in mana, commander dependence, internal synergy, graveyard compatibility, or encyclopedia differentiation.

**ZERO NEW MATERIAL IMPROVEMENTS.**

**Decision closeout: PASS — candidate is APPROVAL_READY evidence only, not approved/locked.**

## Approval closeout

- Explicit user approval received: **2026-10-15**
- Canonical approved SHA-256: `5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e`
- Exact approved artifact: `refinement/decklists/Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt`
- Current-cycle state: **APPROVED / LOCKED**
- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification**
- Next unlocked deck in tracker order: **Norman Osborn // Green Goblin (index 42 / deck 43 of 62)**.
