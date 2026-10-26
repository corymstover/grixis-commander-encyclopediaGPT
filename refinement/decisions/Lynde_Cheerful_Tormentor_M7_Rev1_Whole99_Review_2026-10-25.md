# Deck #31 — Lynde, Cheerful Tormentor M7 Rev1 whole-99 final decision

Raw locked candidate: `6e088891b3c92b632d95e4b6dbd83ffedb06834f812e6728cc5bfa7bdc13556e`. Historical baseline: `05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166`. Exact oracle, candidate alternatives and final decisiveness contract in [merged engineering PR #710](https://github.com/corymstover/GrokBotMTGCompanion/pull/710). Cory approved the complete list once.

Commander-first plan: move real Aura Curses to your graveyard via controlled sacrifice/destruction; Lynde returns them attached to you at the next end step, then moves one Curse per upkeep to an opponent for two cards. Maintain Curse of Misfortunes, low-cost Curses and removal, Paradox Haze, The Ninth Doctor, Obeka, Claws of Gix and Despotic Scepter, and enchantment-entry damage/draw infrastructure.

## Eight selected changes

1. **Court of Vantress ← Cruel Reality.** Repeatable Curse copies while monarch instead of a seven-mana Curse that punishes the owner after Lynde reattaches it.
2. **Extravagant Replication ← Curse of Death's Hold.** Upkeep enchantment/Curse copying versus a -1/-1 effect that can harm Lynde's board when returned.
3. **Barrin, Master Wizard ← Torment of Scarabs.** Paid targeted bounce using a sacrificed Curse as an activation cost, returning that Curse with Lynde.
4. **Into the Pit ← Curse of the Restless Dead.** Top-of-library access paid with sacrificing a nonland permanent; additional Curse-return opportunity.
5. **Staff of Compleation ← Nightscape Familiar.** Repeatable owned-Curse destruction for Lynde at {T} and 1 life, accepting lost early spell discount.
6. **Urza's Saga ← Mountain.** Finds Claws of Gix or Despotic Scepter, trading a basic red source for limited-lifetime colorless Saga.
7. **Otawara, Soaring City ← Island.** Blue source with optional Channel bounce, not falsely represented as a Curse-to-graveyard outlet.
8. **Shizo, Death's Storehouse ← Swamp.** Black source with legendary creature fear support, at the cost of a fetchable basic.

## Opportunity costs and stopping decision

Four physical Curse faces were cut: 21 to 17. Court copies only if you keep monarchy; Replication costs six; Barrin needs mana, sacrifice and creature target; Into the Pit has extra sacrifice/normal cast cost; Staff spends life/taps and loses Nightscape discounts; Saga reduces color fixing and destroys itself; Otawara's bounce cannot trigger Lynde's battlefield-to-graveyard clause; Shizo is narrow legendary combat utility. These costs were disclosed.

The entire 99-card baseline was evaluated by retained Curse density, mana base, draw, graveyard transitions, upkeep trigger ownership, enchantment synergy, protection, interaction, and candidate opportunity cost. EDHREC top-inclusion and high-lift research plus off-ranked Barrin, Into the Pit, Staff, Saga, Otawara and Shizo alternatives informed the final review. Two complete alternative 100s—seven swaps (keep Nightscape), six swaps (keep Torment and Restless Dead)—were rejected as less consistent Curse-reset engines. Post-eight possible additions, including Curse of Chaos and Strionic Resonator, did not support another credible improvement without re-adding owner-rejected cards or undermining commander identity. Eight is an assessed quality boundary, not a capped swap count.

Power Bracket 4 — Optimized. Tags Curses / Enchantress / Control. No forced Grixis Breach turbo combo.

## Evidence

- Candidate, 26 candidate judgments, heightened alternatives: `data/grixis/m7/decision_reviews/Lynde__Cheerful_Tormentor_rev1.json`.
- Oracle identity / Commander legality for all 96 distinct names: `data/grixis/m7/research_challengers/Lynde__Cheerful_Tormentor_ChatGPT_Rev1_Oracle_Index_20261025.json`; receipts dated October 23 plus October 25 specific corroborations.
- M6 5 P0 / 8 P1 exact Rev1 finite source-paid case groups: `tests/test_m7_lynde_rev1_exact.py`, verified by [GitHub Actions PASS](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40255939513).
- Historical Stage A corrected only by separate versioned metadata overlay PR #711. Reviewer technical independence remains false.
- Full 100 and 35 lands; count and provenance are independently rechecked by the canonical lock tests. No universal gameplay engine or quantitative win-rate claimed.
