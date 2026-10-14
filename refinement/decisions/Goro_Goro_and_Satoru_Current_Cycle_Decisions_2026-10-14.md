# Goro-Goro and Satoru — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Baseline artifact: `refinement/decklists/Goro_Goro_and_Satoru_Current_Cycle_Baseline_2026-10-14.txt`  
Baseline SHA-256: `4b00e2b196ffc5a9a625265bc81e5896d4fad913c54b1d7b431f19fafe86cf7d`  
Source CSV SHA-256: `c9bc81909dba75925862c5aea21a4cb178180761cef0b3a5cf4437c24b6271e3`  
Approval-candidate artifact: `refinement/decklists/Goro_Goro_and_Satoru_Approval_Candidate_2026-10-14.txt`  
Approval-candidate SHA-256: `2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf`

## Commander blueprint

**Primary plan:** make creatures enter the battlefield this turn and connect in combat, preferably against multiple opponents and/or during multiple combat-damage steps, so Goro-Goro and Satoru repeatedly create 5/5 flying Dragon Spirits.

**Support plan:** cheap evasive or hasty attackers, ninjutsu/sneak entrants, repeatable beginning-of-combat or attack-token engines, combat-damage card advantage, Treasure generation, and extra-combat effects.

**Primary win routes:**
- Build a flying Dragon army through repeated commander triggers and win through combat.
- `Goro-Goro and Satoru + Breath of Fury` with the required fresh attacker/haste setup to loop combat phases.
- Extra-combat bursts from `Karlach, Fury of Avernus`, `Great Train Heist`, and `Aggravated Assault`.
- Convert Dragon creation into direct damage through `Dragon Tempest` and `Terror of the Peaks`.
- Snowball combat connections into mana/cards with `Grim Hireling`, `Professional Face-Breaker`, `Prosperous Thief`, `Bident of Thassa`, `Enduring Curiosity`, and the retained Ninja package.

**Natural ceiling:** **Bracket 4 — Optimized.** The commander can support explosive and deterministic combat loops, but the optimal commander-first shell remains combat/setup dependent. A generic Grixis Thoracle/Breach turbo-combo conversion would raise generic card power while reducing commander indispensability and is rejected under project philosophy.

## Accepted swaps

1. **Reinforced Ronin → Phoenix Chick**
   - Both occupy the one-mana immediate-attacker slot.
   - Phoenix Chick has flying, materially improving connection reliability for the commander's combat-damage condition.
   - Its recursion can return it tapped and attacking after the attack has been declared; it entered that turn and therefore remains a qualifying Goro-Goro and Satoru damage source if it connects.
   - Reinforced Ronin is ground-bound and becomes increasingly unreliable once normal blockers are established.

2. **Rising of the Day → Samut, Hazoret's Champion**
   - Samut supplies the same continuous global haste function for two mana rather than three and adds a 2/2 creature body.
   - Continuous haste is especially important to `Breath of Fury`: Dragon Spirits created during the loop need haste in later additional combats. Samut grants haste continuously to newly entered Dragons, unlike a previously resolved one-shot activation of Goro-Goro and Satoru.
   - The lost +1/+0 bonus to legendary creatures is less important than the mana-efficiency and creature utility gained.

3. **Feed the Swarm → Withering Torment**
   - Preserves black creature/enchantment interaction while moving from sorcery speed to instant speed.
   - Fixed two-life loss is normally less punishing than Feed the Swarm's variable mana-value life loss against expensive targets.
   - One additional mana is justified by substantially better multiplayer timing and protection against opposing engines on other turns.

4. **Combat Research → Waterbender Ascension**
   - Combat Research is a cheap but single-creature Aura that exposes the deck to removal-based card disadvantage and scales only with one attacker.
   - Waterbender Ascension rewards every creature that connects; this deck is specifically engineered to send multiple evasive/fresh creatures through combat.
   - After four quest counters, each subsequent qualifying combat-damage trigger draws a card, and Waterbend provides a repeatable way to force a critical creature through blockers.

5. **Impact Tremors → Raphael, the Nightwatcher**
   - Impact Tremors is useful generic token/ETB chip damage but is not essential to a primary win route.
   - Raphael may be cast for sneak during the declare-blockers step by returning an unblocked attacker; he then enters tapped and attacking after blockers have been declared.
   - Because Raphael entered that turn and gives attacking creatures double strike, an unblocked Raphael can itself satisfy the commander condition in both the first-strike and regular combat-damage steps. Other fresh attackers with double strike can do the same.
   - This directly increases Dragon production while preserving the deck's ninjutsu/sneak identity.

6. **Kaito, Dancing Shadow → Fire Navy Trebuchet**
   - Kaito is synergistic but four-mana and primarily a value engine; the list already contains substantial combat-damage draw and bounce/replay infrastructure.
   - Fire Navy Trebuchet creates a 2/1 flying Ballistic Boulder tapped and attacking whenever the deck attacks. The token entered that turn and therefore is a direct commander-trigger enabler if it connects.
   - It triggers again in each additional combat and does not require the Trebuchet itself to attack, making it a stronger commander-specific engine in the optimized shell.

## Whole-list audit and retained challenged cards

The complete 99-slot baseline was reviewed by functional cluster rather than treating candidate rankings as automatic instructions. The following challenged cards are intentionally retained:

- **Silver-Fur Master, Thousand-Faced Shadow, Mistblade Shinobi, Moon-Circuit Hacker, Fallen Shinobi, Nashi, Ninja of the Deep Hours, Sakashima's Student, Yuriko, Satoru Umezawa, Satoru the Infiltrator, Ingenious Infiltrator:** global Ninja trends do not override this list's unusually dense ninjutsu package. These cards provide mid-combat entrants, evasive damage, bounce/replay, and card advantage that directly support the commander.
- **Bident of Thassa / Enduring Curiosity:** retained as high-throughput combat-damage draw. They reward the same wide evasive combat pattern that produces Dragons.
- **Daring Piracy / Loyal Apprentice / Urabrask's Forge / Determined Iteration:** retained because they repeatedly generate creatures that enter in time to attack or enter attacking, and several scale with extra combats or Breath of Fury.
- **Dragon Tempest / Terror of the Peaks:** retained because they translate 5/5 Dragon creation into noncombat pressure and provide redundancy against stalled combat boards.
- **Rogue's Passage:** retained over utility-land challengers because guaranteeing one critical connection is often sufficient to start the commander or Breath of Fury engine.

## Serious challengers rejected after second pass

- **Kaito, Cunning Infiltrator:** excellent three-mana value/evasion engine, but Fire Navy Trebuchet is more direct at producing a fresh attacker every combat and the list already has deep card draw.
- **Higure, the Still Wind / Dokuchi Silencer / Throat Slitter / Orochi Soul-Reaver / Moonsnare Specialist:** all fit the Ninja plan, but their higher mana/ninjutsu costs or narrower interaction do not beat the retained Ninja package on efficiency and role density.
- **Alora, Merry Thief / Mist-Cloaked Herald / Tin Street Dodger / Tormented Soul / Invisible Stalker:** more evasion is useful, but the list already has enough one-drop/evasive enablers; adding additional low-impact bodies would displace cards that supply engines, interaction, or scaling.
- **Enduring Courage / Urabrask the Hidden / Hammer of Purphoros / Fervor:** haste redundancy is useful, but Samut is the best rate for a continuous effect and Goro-Goro and Satoru itself retains an activated haste fallback.
- **Kaito Shizuki:** strong general value but less commander-specific than retained engines.
- **Blade of Selves / Saheeli, the Sun's Brilliance / Orthion, Hero of Lavabrink:** powerful copying tools but comparatively mana-intensive and not superior to the current fresh-attacker/extra-combat plan.
- **Sokenzan, Crucible of Defiance:** near-free utility is attractive, but no existing land is sufficiently weak to justify an unnecessary mana-base change in this already functional three-color combat deck.
- **Yuffie, Materia Hunter / Maestros Diabolist / Lagomos, Hand of Hatred:** legitimate fresh-attacker/token options, but they lose to the accepted engines on efficiency or repeatability.
- **Kaito, Cunning Infiltrator and Waterbender Ascension were compared directly as value/evasion upgrades; Ascension won the slot because it scales across every combat-damage event and can make a critical creature unblockable repeatedly without consuming a planeswalker activation.**
- **Draconic Visitor / Smaug the Magnificent / Samut, Tyrant of Naktamun:** current 2026 challengers were reviewed. Draconic Visitor changes Treasure production into Dragons at a high five-mana opportunity cost; Smaug is a strong hasty Dragon but not a stronger fresh-attacker engine than Raphael; Samut, Tyrant of Naktamun is a spells-focused card and off-plan here.
- **Secret Tunnel / Access Tunnel:** utility is real, but neither is a material upgrade over the current colored-source mix plus Rogue's Passage.

## Closure

After the six accepted swaps, a second adversarial pass through the baseline, the project top-100 funnel, current EDHREC evidence, 2026 release challengers, interaction density, mana base, extra-combat lines, and the ninjutsu package produced **ZERO NEW MATERIAL IMPROVEMENTS**.

Candidate state before formal gate:
- 100 cards
- 99 distinct names
- only basic Island repeats (2 copies)
- 33 lands
- commander-first combat / fresh-entry / ninjutsu identity preserved
- target natural ceiling: Bracket 4 — Optimized
- no project legality exception expected

The candidate remains **NOT APPROVED** until the complete fail-closed Oracle/color-identity/legality/rules gate passes and the user explicitly approves it.
