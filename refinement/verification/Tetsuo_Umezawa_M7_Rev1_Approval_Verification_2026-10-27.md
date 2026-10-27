# Deck #54 — Tetsuo Umezawa — M7 Rev1 canonical approval verification

Date: 2026-10-27 (America/Chicago)  
Cycle: `global-restart-2026-10-13`

- **Approved raw UTF-8 SHA-256:** `e00196135931bde6e380e47d5ffe9e4360d4756f00ad083ee5ed0757919fddd7`. Previous raw Oct15 SHA `14ca66ceae4d634630a85aa1787731cfe840fd9fc2093bc37ad5dc17d1539ff6` remains preserved.
- **Structural:** exactly 100 physical including 1 Tetsuo commander, 93 distinct names, only basic Islands (3), Mountains (3), Swamps (4) repeat; no companion/exception.
- **Mana base:** 35 land-faced cards and a Sink into Stupor // Soporific Springs MDFC; seven true functional land replacements improve `{U}{B}{B}{R}` availability with life/nonbasic tradeoffs.
- **Oracle:** 93/93 current Scryfall Oracle identities, official Commander legal and U/B/R on 2026-10-27; no unresolved or split errors.
- **Owner-selected 19 real swaps:** 12 spell/engine/protection changes, seven land improvements, 80 original library physical positions retained after comparing the full 99.
- **Alternate count not quota:** complete 18- and 21-swap versions physically staged and hash-attested; stronger exact enemy-target generation/removal justified stopping at 19.

## Source-paid interaction boundaries

- Original Tetsuo `{U}{B}{R}` cast, `{U}{B}{B}{R}, {T}` destroys a tapped or blocking creature; untapped blocking creatures are valid while attacking/goad alone does not automatically make a creature tapped.
- Tetsuo cannot be targeted by Aura spells (ordinary Pemmin's Aura casting cannot enchant him). Equipping is possible.
- Icy Manipulator and Puppet Strings can generate tapped enemy targets, but each requires its own ready state and mana cost; untap events do not refund four colored activation mana.
- Thornbite Staff untaps equipped Tetsuo on a creature actually dying, not for every attempted kill. Dramatic Reversal untaps nonland permanents, not lands.
- Isochron Scepter plus Dramatic Reversal loops only with sufficient productive nonland mana rocks (2 spent to activate Scepter per cycle); color and targets still matter. No guaranteed immediate win claimed.
- Uphill Battle taps creatures played by opponents, not all token creatures; Toxic Deluge requires life and affects Tetsuo too.
- Historical `data/grixis/m6/ij/input_receipts/tetsuo-umezawa.json` remains input-attested only, Phase B replay false. The new 22 source-bound tests do not serve as sealed M6 I/J or universal Magic engine.

## Exact-head review

- [Merged engineering PR #735](https://github.com/corymstover/GrokBotMTGCompanion/pull/735): source head `bd3c95fef93197e6503990a35778f7a06298ce87`, merged `bdbee1eaaf96cfbd9ba1d321cadf69411c5e7b58`.
- [Deck54 run #40576836188](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40576836188): SUCCESS; live 93-name verification + 22 bounded mechanical cases.
- [Repository M7 contract #40576836147](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40576836147): SUCCESS, 94/94 steps.
- Two unrelated historical Deck30 Lord Xander workflows on same commit failed; not counted as passes, not altered by Tetsuo approval.
- Canonical approval authority: `state/current_deck_overrides.json#decks.Tetsuo_Umezawa` must read **APPROVED/LOCKED** and same exact approved SHA.
- Approval scope: Cory's single-word 'Approve' directly following the full 100 and exact raw SHA-bound owner-ready packet. No repeat user action.
- Bracket 4 — Optimized. Tags Tap/Untap / Forced Combat / Activated Abilities. No overall M6.10, M7, M8 or third-model acceptance implied.
