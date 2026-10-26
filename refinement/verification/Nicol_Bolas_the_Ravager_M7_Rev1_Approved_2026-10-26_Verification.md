# Deck #42 — Nicol Bolas, the Ravager // Nicol Bolas, the Arisen — M7 Rev1 approved verification

Date: 2026-10-26
Cycle: global-restart-2026-10-13
Status: **OWNER-APPROVED EXACT LIST; CANONICAL LOCK ELIGIBLE**
Power Bracket: 4 — Optimized
Archidekt tags: Superfriends / Transform / Proliferate

## Exact source authority and historical preservation

- New canonical approved file: `refinement/decklists/Nicol_Bolas_the_Ravager_M7_Rev1_Approved_2026-10-26.txt`.
- Exact raw SHA-256: `acfa7922e262805a15932b53b1399acdf6ddf5592c8a3793fafdeec720ad4693`.
- Previous 2026-10-15 approved source is immutable and still present: `refinement/decklists/Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt`.
- Previous approved source raw SHA-256: `5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e`.
- Owner expressly approved exact M7 Rev1 SHA on 2026-10-26; no second approval required.
- Engineering evidence PR: https://github.com/corymstover/GrokBotMTGCompanion/pull/724, merged `a540ee2ec82d4a1583118dfba1e93fd8d74f468c`.
- Exact-head GitHub Actions source/legality run: https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40415604217 — **SUCCESS**.
- Candidate and technical test source: `data/grixis/m7/candidate_lists/Nicol_Bolas__the_Ravager_chatgpt_rev1.txt` and `data/grixis/m7/nicol_bolas_ravager_rev1/`.

## Structural + live data gate

- 100 physical cards including 1x transformed double-faced commander; 98 text rows; 98 distinct names.
- Exactly Island x2 and Swamp x2 repeat, both basic lands; zero nonbasic singleton violations.
- Lands: 34 (same as previous approved baseline).
- Six exact one-for-one nonland swaps; color identity: blue/black/red; no project-authorized exception needed.
- Source file SHA-256 and 2026-10-15 baseline source SHA-256 both pass source-bound CI.
- Six scoped Python source/finite-interaction tests: **6/6 PASS**.
- Live Scryfall card collection for 98/98 distinct names: **all resolved, all officially Commander legal, all within U/B/R** on the 2026-10-26 engineering CI run.
- Eleven strategically relevant Oracle-card witness sets (including the commander and six additions): **PASS**.
- No full randomized multiplayer trials, measured win-rate claim, independent third model, or aggregate M6/M7/M8 milestone acceptance is inferred.

## Six exact owner-approved swaps

| Cut | Addition | Commander-first reason |
|---|---|---|
| The Eldest Reborn | Aetheric Amplifier | Earlier three-chapter attrition swapped for mana rock and repeatable paid loyalty doubling; resolves the formal Pass C NEEDS TESTING question with documented tradeoff, not fictional win-rate evidence. |
| Nicol Bolas, the Deceiver | Teferi's Talent | Exchange eight-mana low-tempo Bolas walker for draw-trigger loyalty counters and potential -12 planeswalker activation-timing emblem. Three other Bolas-named walkers and transformed Arisen remain. |
| Jaya's Phoenix | Experimental Augury | Instant-speed low-cost card selection plus proliferate rather than five-mana flying/recursion payoff. |
| Tinybones, Bauble Burglar | Time Warp | Full extra turn with untap, draw and legal renewed planeswalker loyalty activation, replacing narrow one-time Ravager ETB discard payoff. |
| Tergrid, God of Fright // Tergrid's Lantern | Chandra, Torch of Defiance | Flexible four-mana planeswalker: RR acceleration toward paid transform, card access and creature removal, instead of conditional discard theft without wheel density. |
| Liliana's Talent | Vronos, Masked Inquisitor | Protects up to two *other* planeswalkers by next-end-step phasing and bounces up to one nonland permanent per opponent, replacing vulnerable aura mass-reanimation package. |

## Rules and limitations explicitly checked

1. Ravager front cast cost is **{1}{U}{B}{R}** (mana value 4), NOT the zero-MV DFC parser artifact. Transform activation costs **{4}{U}{B}{R}** or **{2}{U}{B}{R}** with Training Grounds. The separate transform ability neither casts a spell nor pays commander tax.
2. Aetheric Amplifier's {4},{T} counter doubling is sorcery-speed; it cannot provide mana with {T} and also tap to double in the same interval without a separate untapper. Doubling Arisen's seven loyalty to fourteen permits -12 if otherwise legal; that ultimate leaves one library card and **does not directly kill** the opponent.
3. Teferi's Talent triggers separately for each card drawn by Arisen's +2. Copying a loyalty ability via Rowan's Talent or Rings does not pay its loyalty cost a second time.
4. Time Warp grants a real new turn with untap, but a spell on the stack can be countered; Savor the Moment's skip-untap hypothesis was rejected rather than incorrectly treated as equivalent.
5. Vronos's +1 targets up to two *other* walkers and phases them at the **beginning of next end step**, rather than immediately on activation. Its -2 can return up to one targeted nonland permanent of each opponent.
6. Displacer Kitten blinking transformed Arisen returns front-face Ravager, not the planeswalker; existing Chain Veil / Rings / Teferi interactions are paid multi-piece lines with actual timing and mana requirements.
7. The adjacent original Nicol Bolas Deck #41 remains a separate discard / commander-damage / control list. Ravager #42 retains its transform / proliferate / superfriends specialization.
8. The immutable Oct15 baseline, all other deck files/state entries, and project-specific exceptions are preserved.

## Owner authority and next checkpoint

Cory wrote: **"Approve Deck #42 Nicol Bolas, the Ravager M7 Rev1, exact raw SHA-256 acfa7922e262805a15932b53b1399acdf6ddf5592c8a3793fafdeec720ad4693. Proceed with canonical locking and verification."**

Approval pertains to exactly this source file and authorizes the versioned canonical PR, verification and post-merge LOCKED state. A successful engineering PR alone does not constitute canonical locking. Next deck #43 Norman Osborn // Green Goblin.
