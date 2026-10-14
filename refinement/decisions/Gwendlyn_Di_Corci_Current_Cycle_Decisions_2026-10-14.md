# Gwendlyn Di Corci — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Baseline artifact: `refinement/decklists/Gwendlyn_Di_Corci_Current_Cycle_Baseline_2026-10-14.txt`  
Baseline SHA-256: `50382d9660973d81cbca84d878ece8f09fdbd45e1154cc676b3e71b156d27c20`  
Authoritative source: `GrixisFINAL60--2026.zip / Gwendlyn_Di_Corci.csv`  
Source CSV SHA-256: `b4200e0d54197135870a5a4f13ef311c5393860ec3e8d2dc9074e565bfd08495`  
Approval-candidate artifact: `refinement/decklists/Gwendlyn_Di_Corci_Approval_Candidate_2026-10-14.txt`  
Approval-candidate SHA-256: `9f1e7753978f80aa2c37e5d1f073eda9f302cb02325d39828d24a770b126fd88`

## Source reconciliation

The latest FINAL CSV/TXT export is the current card-membership baseline under the project source-of-truth rules. The older v8.1.4 card-audit material still reflects an earlier five-card configuration containing `Burning Inquiry`, `Counterspell`, `Megrim`, `The Locust God`, and `Winds of Change`; the current FINAL export instead contains `Dream Salvage`, `Fell Specter`, `Hypnotic Specter`, `Sangromancer`, and `Tourach, Dread Cantor`. The older audit is therefore treated as research evidence only and is not allowed to overwrite the current FINAL membership.

## Commander blueprint

**Primary plan:** make Gwendlyn Di Corci itself a repeatable random-discard engine. Her activated ability is intentionally the center of the list rather than merely a flavor card in a generic Grixis wheels shell.

**Support plan:** give Gwendlyn haste or pseudo-haste, untap her repeatedly, copy her activated ability, refill opposing hands with wheels and then strip them again, and convert discard into cards, mana, stolen permanents, life loss, and table pressure.

**Primary win routes:**
- Repeated Gwendlyn activations backed by `Illusionist's Bracers`, `Pemmin's Aura`, `Minamo, School at Water's Edge`, `Magewright's Stone`, `Patriar's Seal`, and `Thousand-Year Elixir` to dismantle hands while discard payoffs accrue value.
- Wheel/discard bursts through `Wheel of Fortune`, `Wheel of Misfortune`, `Windfall`, `Timetwister`, `Dark Deal`, `Reforge the Soul`, `Jace's Archivist`, and `Magus of the Wheel`, amplified by `Waste Not`, `Geth's Grimoire`, `Liliana's Caress`, `Tinybones` cards, `Sheoldred`, and `Orcish Bowmasters`.
- Resource denial/value asymmetry from `Chains of Mephistopheles`, `Notion Thief`, `Opposition Agent`, `Dauthi Voidwalker`, `Tergrid`, `Bottomless Pit`, and `Oppression`.
- Reuse premium discard and wheel spells through `Kess, Dissident Mage`, `Underworld Breach`, and `Yawgmoth's Will` where their own rules permit.

**Natural ceiling:** **Bracket 4 — Optimized.** The commander can support an oppressive, high-interaction discard-control shell, but Gwendlyn is a four-mana tap-ability commander with a once-per-activation one-card effect and needs haste/untap infrastructure. Converting the deck into generic Grixis Thoracle/Breach turbo-combo would raise generic card power while making the commander substantially less relevant, so that conversion is rejected under the commander-first philosophy.

## Accepted swaps

1. **Bone Miser → Mind Twist**
   - `Bone Miser` is a five-mana engine that rewards the controller for discarding their own cards; most of its ceiling comes from the wheel package rather than Gwendlyn.
   - `Mind Twist` is efficient, scalable random discard that directly mirrors the commander's defining mechanic and can remove multiple cards from one chosen player's hand.
   - It also remains useful as a premium recursion target for the deck's spell-recursion package.

2. **Fell Specter → Illusionist's Bracers**
   - `Fell Specter` is a four-mana discard payoff, but it does not improve Gwendlyn's actual activation rate.
   - `Illusionist's Bracers` copies Gwendlyn's nonmana activated ability whenever it is activated while equipped, producing an additional random discard without paying another tap cost and allowing a different player to be targeted with the copy.
   - This is substantially more commander-specific than another generic punishment body.

3. **Hypnotic Specter → Pemmin's Aura**
   - `Hypnotic Specter` is thematically excellent random discard, but it requires surviving summoning sickness and then connecting in combat.
   - `Pemmin's Aura` turns each available blue mana into another Gwendlyn untap/activation on the controller's turn and also supplies reactive shroud protection.
   - The accepted card raises both commander throughput and resilience rather than adding a second, slower version of the commander's effect.

4. **Sangromancer → Tinybones, Pocket Nuisance**
   - `Sangromancer` is a four-mana life-gain payoff that stabilizes but does not materially accelerate the deck's pressure or commander plan.
   - `Tinybones, Pocket Nuisance` costs three, makes each opponent discard when it enters, and converts every qualifying discard event—including Gwendlyn's random discard—into damage to each opponent.
   - It therefore functions as both immediate disruption and a scalable table-wide payoff.

5. **Feed the Swarm → Withering Torment**
   - Both preserve black access to creature/enchantment removal.
   - `Withering Torment` moves the effect to instant speed and uses a fixed two-life payment rather than variable life loss based on mana value.
   - The additional mana is justified by substantially better multiplayer timing.

6. **Island → Minamo, School at Water's Edge**
   - `Minamo` remains an untapped blue-producing land and therefore has very low deckbuilding opportunity cost.
   - Its activated ability directly untaps the legendary commander, producing another Gwendlyn activation when blue mana is available.
   - Replacing a basic Island rather than a black/red source preserves the rest of the three-color source distribution.

## Whole-list audit and retained challenged cards

All 99 noncommander slots in the current FINAL baseline were reviewed by role rather than treating rankings as automatic instructions. The following challenged cards are intentionally retained:

- **Lightning Greaves / Thousand-Year Elixir:** essential because Gwendlyn's ability uses the tap symbol and otherwise cannot normally be used the turn she enters. Elixir also supplies another untap.
- **Magewright's Stone / Patriar's Seal:** direct commander untap effects. Seal also produces mana, so these remain superior to replacing them with another generic discard spell.
- **Bottomless Pit / Oppression:** repeatable hand pressure that keeps discard payoffs live after the first wheel cycle; Bottomless Pit's random discard is especially aligned with Gwendlyn's identity.
- **Chains of Mephistopheles / Notion Thief:** high-impact draw-denial pieces that make the deck's wheel effects asymmetric and punish attempts to rebuild stripped hands.
- **Waste Not / Geth's Grimoire / Liliana's Caress / Tinybones, Trinket Thief / Tinybones, Bauble Burglar:** retained as the efficient payoff/value layer that turns opponent discard into mana, cards, theft, or damage.
- **Tergrid, God of Fright:** expensive but unusually high-ceiling in a deck repeatedly forcing opponents to discard permanents, and therefore materially connected to the primary plan.
- **Underworld Breach / Yawgmoth's Will / Kess, Dissident Mage:** retained as recursion/value infrastructure rather than a generic deterministic combo package; they replay the deck's best discard, tutor, wheel, and interaction spells.
- **Bloodchief Ascension:** retained as a low-cost life-loss payoff. `Mindcrank` is intentionally absent, so the deck is not being converted into a generic two-card combo shell.
- **Current fast mana / interaction suite:** retained because the four-mana commander needs acceleration and protection to function at its realistic optimized ceiling.

## Serious challengers rejected after second pass

- **Aphetto Alchemist:** a legitimate two-mana untapper, but summoning sickness and creature fragility make it slower than `Pemmin's Aura` and `Minamo` for the exact commander job.
- **Battlemage's Bracers:** haste plus activation copying is attractive, but each copy requires an additional mana. `Illusionist's Bracers` is the stronger repeatable activation multiplier once Gwendlyn is online, while the list already has haste/pseudo-haste infrastructure.
- **Freed from the Real:** performs the same core blue-mana untap function as `Pemmin's Aura`, but Pemmin also provides reactive shroud and other utility for only a tighter initial colored requirement.
- **Liliana of the Veil:** efficient and synergistic, but its symmetrical +1 also strips the controller and is less commander-specific than the accepted activation engines.
- **Syphon Mind / Unnerve / Necrogen Mists:** all are defensible discard cards, but they add generic redundancy rather than increasing the commander's throughput. The deck already has sufficient mass/repeatable discard.
- **Naktamun Lorespinner // Wheel of Fortune:** the prepared Wheel is synergistic, but the front half requires upkeep/low-hand setup and is slower than the existing direct wheel suite. It does not clear a stronger existing slot after direct comparison.
- **Quest for the Nihil Stone / Raiders' Wake / Painful Quandary:** payoff density is already high; these are slower or more conditional than the retained value engines and accepted commander-specific pieces.
- **Cao Cao, Lord of Wei:** another tap-to-discard creature fits the theme but costs five mana and has summoning-sickness liability; investing in Gwendlyn's own activations is stronger and more identity-driven.
- **Monument to Endurance:** rewards the controller's own discard rather than primarily exploiting opponents' random discard; it is more wheel/self-discard support than a Gwendlyn engine.
- **Mindcrank:** would create a compact combo with `Bloodchief Ascension`, but that line does not require Gwendlyn and would move the deck toward generic combo homogenization. Rejected intentionally.
- **Mox Diamond / broad fetch-land overhaul:** additional generic acceleration/fixing is defensible in isolation, but the current 35-land plus fast-mana configuration is already functional. No generic mana-base churn beats the commander-specific gain from the single `Minamo` change.

## Current-rule checkpoints before formal gate

- Gwendlyn's activated ability may be activated only during its controller's turn and uses the tap symbol; normal summoning-sickness restrictions therefore matter unless haste/pseudo-haste is supplied.
- `Illusionist's Bracers` copies the activated ability without paying its tap cost again; the copy may choose a new target.
- `Pemmin's Aura` and `Minamo` can repeatedly untap Gwendlyn as their costs can be paid. Pemmin's shroud mode is best used reactively because shroud also prevents the controller from targeting Gwendlyn with their own Minamo/Stone/Seal effects while it lasts.
- `Tinybones, Pocket Nuisance` triggers once for a given player's event of discarding one or more cards, not once per card discarded in that single event. Its own ETB causes each opponent to discard and therefore immediately feeds the discard plan.
- `Chains of Mephistopheles` replaces draws other than the first card drawn in each draw step with its discard/draw-or-mill procedure, making wheel sequencing materially asymmetric when hands are being emptied.
- `Notion Thief` can replace opponents' draws with draws for its controller, making wheel effects especially punishing after the initial discard.
- `Tergrid` only returns opponent permanent cards discarded or sacrificed while its trigger conditions are met; nonpermanent cards do not become permanents under its control.

## Closure

After the six accepted swaps, the current FINAL baseline, inherited candidate rankings, current commander evidence, direct activation-engine alternatives, recent 2026 releases, removal suite, mana base, payoff density, and generic combo temptations were challenged a second time. The second serious pass produced **ZERO NEW MATERIAL IMPROVEMENTS**.

Candidate state before formal gate:
- 100 cards
- 94 distinct names
- only basic Island, Mountain, and Swamp repeat
- 35 lands
- commander-first random-discard / activated-ability / wheels identity preserved
- target natural ceiling: Bracket 4 — Optimized
- no project legality exception expected

The candidate remains **NOT APPROVED** until the complete fail-closed Oracle/color-identity/legality/rules gate passes and the user explicitly approves the exact SHA-bound candidate.