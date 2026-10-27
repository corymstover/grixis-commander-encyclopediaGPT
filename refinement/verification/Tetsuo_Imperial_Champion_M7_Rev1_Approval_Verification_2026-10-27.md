# Deck #55 — Tetsuo, Imperial Champion — M7 Rev1 canonical approval verification

Date: 2026-10-27 (America/Chicago)  
Cycle: `global-restart-2026-10-13`

- **Approved SHA-256, exact raw UTF-8 list:** `36890584524fb32d038ba27926af663dc98197f06f87d84a08282ce1f3fb29db`, approved by Cory's single-word "Approved" reply after the complete M7 Rev1 review and exact-head CI.
- **Preserved October 15 approved source:** `refinement/decklists/Tetsuo_Imperial_Champion_Approved_2026-10-15.txt`, raw SHA `d6d7561f00cb56cfb86cd79024975130d718ddc7f3a1bddf0c62f61dc422822e`, never overwritten.
- **Structure:** 100 physical including 1 tagged Tetsuo commander; 93 unique names; only Island ×4, Mountain ×4 and Swamp ×2 repeat; no companion or exception; 35 lands.
- **Exact swaps:** 13 cuts / 13 additions, 86 existing noncommander physical slots retained; full 99-slot decision ledger with alternate 14- and 15-swap candidates preserved in engineering.
- **Commander identity and official legality:** all 93 unique current Oracle card identities verified 2026-10-27 against public Scryfall bulk Oracle locally, within {U}{B}{R} and Commander-legal, no project exception.
- **Deck character:** Bracket 4 — Optimized; Equipment / Free-Cast Spells / Extra Combats. Proactive Tetsuo power/equip/cast-versus-damage attack choices, not generalized Grixis goodstuff.

## Source-anchored mechanical limits

- Tetsuo's trigger requires him to attack while equipped and chooses either (a) damage to any target equal to the greatest mana value among Equipment attached to him, or (b) casting an instant or sorcery spell from hand with mana value no greater than that greatest attached-Equipment mana value without paying its mana cost. These are alternative modes of the same trigger.
- If using Tainted Strike for infect on Tetsuo's targeted damage, it must be cast for available {B} after placing the selected damage-mode trigger on the stack; it cannot also be the free spell from that same trigger.
- Mjölnir, Hammer of Thor modifies noncombat damage from Tetsuo; Grafted Exoskeleton grants infect but its sacrifice consequence on becoming unattached is real. Neither line guarantees a kill without setup.
- Karlach adds a combat after the first attack combat if the appropriate trigger resolves, and timing/untap matters; extra combats do not automatically yield an extra free-cast if Tetsuo cannot attack equipped again.
- Firion's copied Equipment token is subject to legendary-rule constraints where applicable and temporary-copy sacrifices/unattachments; do not assume perpetual copies.
- Jeska's Will cast in combat does not bank red mana into postcombat main. Spells with additional costs, including Savage Beating's entwine, still require those costs even if cast without paying their mana cost.
- World at War's delayed extra combat is subject to its second-main-phase wording and available attack resources.
- The 18 source-specific finite-case assertions complement actual Oracle verification but are not a full simulation; historical `data/grixis/m6/ij/input_receipts/tetsuo-imperial-champion.json` remains input-attested, Phase B replay incomplete.

## GitHub source and proof

- [Merged engineering PR #736](https://github.com/corymstover/GrokBotMTGCompanion/pull/736) exact approved head `885bf09d513b74a1642ff0edf73212fe744e8d1a`, merged engineering SHA `e49e4eb3d334a17e6a016be14e38b9322822cef4`.
- [Dedicated Deck #55 CI #40585827350](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40585827350): SUCCESS; focused Oracle/legality/UBR plus 18 cases and structural verification.
- [Repo-wide M7 contract #40585827294](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40585827294): SUCCESS.
- Separate historical Deck #30 workflows failed and are not represented as success.
- Canonical authority `state/current_deck_overrides.json#decks.Tetsuo__Imperial_Champion` is required to read `APPROVED/LOCKED` and the identical 64-character hash.
- No reopened aggregate M6.10/M7/M8, no blanket Phase B certification or third-model acceptance is implied.
