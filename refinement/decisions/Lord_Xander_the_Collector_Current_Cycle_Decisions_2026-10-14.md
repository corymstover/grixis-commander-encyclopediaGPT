# Lord Xander, the Collector — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Tracker deck id: `Lord_Xander__the_Collector`  
Authoritative TXT: `GrixisFINALTXT60--2026.zip / Lord_Xander__the_Collector.txt`  
Source TXT SHA-256: `6525dcb9e2165610e832998d94b1b929cd2b30e2701706ca91a77611bafa371c`  
Clean baseline SHA-256: `f66d97734cf16799a569f44a00209e4981fc977538c07cc7b1fe0d3e01ba5960`  
Approval candidate SHA-256: `92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787`

## Commander blueprint

**Primary identity:** Xander trigger multiplication — reanimate/copy a seven-mana commander, then exploit his ETB discard, declared-attack half-library mill, and dies half-board sacrifice.

**Secondary identity:** high-power Grixis control/combo support that protects the commander plan or converts Xander’s mill/attack pressure into a deterministic close. Compact backup combos may remain, but Xander must remain the clearest strategic reason for the deck’s construction.

**Natural ceiling:** **Power Bracket 4 — Optimized.** Contemporary EDHREC shows roughly 185–188 user-bracketed optimized Xander lists but only about 14 self-labeled cEDH lists. No material current tournament evidence was found that justifies replacing the commander-first shell with generic Grixis cEDH.

## Exact proposed changes

1. `Grindstone` → `Auton Soldier`
   - Painter/Grindstone is a commander-independent mill package. Auton Soldier can enter as a nonlegendary Xander with myriad, immediately generating Xander’s ETB trigger. When declared as an attacker it generates Xander’s attack trigger plus myriad; the myriad tokens enter as Xander copies and generate further ETB triggers.
2. `Painter's Servant` → `Phantasmal Image`
   - Image is a two-mana Xander trigger burst. It enters as Xander and creates the ETB trigger; the legend rule can then put Image-Xander into the graveyard, creating a Xander death trigger while the original commander remains.
3. `Narset, Parter of Veils` → `Cruel Calculations`
   - The list retains Notion Thief as its wheel payoff. Cruel Calculations converts Xander’s attack directly into a massive three-mana draw spell by counting cards actually put from the targeted player’s library into their graveyard that turn.
4. `Reliquary Tower` → `Hall of Echoes`
   - Both occupy a colorless land slot, but Hall can become Xander before combat and suspends the legend rule for the turn. If Hall has been continuously controlled since the beginning of the turn, Hall-Xander can be declared as an additional attacker and generate its own Xander attack trigger. Hall does not enter when it copies, so it does not generate Xander’s ETB trigger.

## Important retained packages

- `Bruvac the Grandiloquent`, `Fraying Sanity`, and `Riverchurn Monument` directly convert Xander’s half-library attack into near/immediate library exhaustion.
- `Blade of Selves`, `Helm of the Host`, `Roaming Throne`, `Sakashima of a Thousand Faces`, `Spark Double`, `Molten Duplication`, `Saw in Half`, and `Strionic Resonator` are retained because they multiply Xander’s own triggers rather than merely adding generic mill.
- `Feign Death`, `Animate Dead`, `Persist`, `Reanimate`, and `Entomb` retain the reanimation axis that makes a seven-mana commander realistic.
- `Duskmantle Guildmage + Mindcrank`, `Underworld Breach + Lion's Eye Diamond + Brain Freeze`, and `Aggravated Assault + Sword of Feast and Famine` remain compact secondary closes. The Assault/Sword line also converts directly into repeated Xander attack triggers.

## Candidate exhaustion / rejected challengers

- `Fractured Sanity`, `Ruin Crab`, `Hedron Crab`, `Consuming Aberration`, `Syr Konrad, the Grim`, `The Mindskinner`, `Fleet Swallower`, and `Traumatize`: additive mill is lower leverage than multiplying Xander’s half-library trigger in this shell.
- `The Master of Lake-town`: strong new mill engine and redundant combo partner for Duskmantle Guildmage, but it does not improve Xander’s triggers enough to displace the retained interaction/value floor.
- `Irenicus's Vile Duplication`: excellent persistent nonlegendary Xander copy, but Spark Double/Sakashima/Helm already cover that role; Phantasmal Image supplies a unique two-mana ETB-plus-death line and Auton Soldier supplies multiplayer myriad leverage.
- `Phyrexian Metamorph`: efficient clone, but redundant after the selected clone package and does not outperform Image’s rate or Auton’s multiplayer ceiling.
- `Panharmonicon`: doubles only the ETB trigger; Roaming Throne and Strionic Resonator cover more of Xander’s text.
- `Displacer Kitten` / `Deadeye Navigator`: repeated Xander flicker is real, but repeated half-hand discard has diminishing returns and these engines require more setup than the chosen copy package.
- `Jidoor, Aristocratic Capital // Overture`: the half-library Adventure is thematic, but the land enters tapped and the Adventure costs six; not enough to replace the current mana quality.
- `Kitsune's Technique`: another half-library effect, but it does not outperform the existing Bruvac/Fraying/Monument conversions.
- `The One Ring`, `Opposition Agent`, `Orcish Bowmasters`, free interaction, and premium tutors were challenged as generic staples and retained because a seven-mana commander requires a high interaction/consistency floor at Bracket 4.
- Additional generic Oracle/Consultation packages were rejected because they increase commander-independence rather than improve Xander’s natural strategy.

After the whole-list audit, current optimized/cEDH comparison, October 2026 card review, copy/legend-rule challenge, mana review, combo review, and adversarial candidate pass, **ZERO NEW MATERIAL IMPROVEMENTS** remain beyond the four swaps above.

## Structural state

- Candidate: **100 cards**
- Distinct names: **97**
- Repeated names: `Island x2`, `Mountain x2`, `Swamp x2` only
- Lands: **33**
- Commander identity: **U/B/R**
- Expected project exceptions: **none**
- Proposed ceiling: **Power Bracket 4 — Optimized**
- Approval state: **NOT APPROVED** pending fresh SHA-bound complete gate and explicit user approval.
