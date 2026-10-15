# Marchesa, Dealer of Death — Current-Cycle Decision Closeout

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Candidate SHA-256: `34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1`  
Status: **APPROVED / LOCKED**

## Decision

The user explicitly approved the exact 2026-10-11 Takeda Ryuhei tournament-winning Marchesa configuration as the current-cycle canonical list on 2026-10-15.

This is a **48-card rebuild** from the frozen FINAL baseline, not a generic cEDH conversion. The rebuild is justified because Marchesa has current tournament evidence at genuine cEDH tables and the new architecture uses the commander's crime trigger as an active resource engine rather than treating Marchesa as a color-identity placeholder.

## Strategic architecture

- **Primary engine:** Marchesa crimes -> {1} -> top-two selection / graveyard conversion.
- **Crime density:** targeted interaction plus repeatable low-cost sources such as Spatial Binding, Hex Parasite, Spellskite, Tezzeret, Urborg, and Talon Gates.
- **Mana engine:** zero/one-mana acceleration, rituals, Bender's Waterskin, Birgi, Storm-Kiln Artist.
- **Card advantage:** Marchesa, Mystic Remora, Rhystic Study, Necropotence, Ad Nauseam, Wan Shi Tong.
- **Primary win packages:** Tainted Pact + Thassa's Oracle; Underworld Breach + Lion's Eye Diamond + Brain Freeze; Aphetto Alchemist + Hawkeye's Bow.
- **Interaction:** free and one-mana-heavy cEDH permission/bounce/removal, which frequently doubles as crime production.

## Material red-team decisions

- **Keep Lapis Lazuli Talisman.** Bender's Waterskin supplies opponent-turn mana; Lapis converts blue spells into targeted triggered abilities and, when paid for, untaps that target, creating additional Marchesa crime opportunities.
- **Use Aphetto Alchemist + Hawkeye's Bow.** This is a compact deterministic damage line and both cards retain independent engine utility.
- **Retain Spatial Binding.** Paying 1 life to target a permanent provides an exceptionally cheap repeatable crime activation.
- **Retain Hex Parasite.** The X=0 activation can still legally target a permanent, enabling low-cost repeatable crimes.
- **Retain Tezzeret, Cruel Captain.** Colorless 0-ability crime utility plus artifact tutoring for key one-mana pieces.
- **Do not restore generic baseline crime payoffs solely for theme density.** Marchesa is strongest when necessary competitive interaction itself becomes the crime engine.

## Closure

Mandatory 99-slot whole-list audit: **COMPLETE**  
Candidate exhaustion: **COMPLETE**  
Rules/combo review: **PASS**  
Official Commander legality checkpoint: **PASS**  
Singleton/color identity/count: **PASS**  
Adversarial red-team: **COMPLETE**  
Final serious pass: **ZERO NEW MATERIAL IMPROVEMENTS**  
Explicit user approval: **RECEIVED 2026-10-15**

Canonical approved artifact: `refinement/decklists/Marchesa_Dealer_of_Death_Approved_2026-10-15.txt`  
Approval record: `refinement/approvals/Marchesa_Dealer_of_Death_Approved_2026-10-15.md`

The exact SHA-bound list is now frozen for the current cycle. Do not revise, reopen, or replace it unless the user explicitly requests that action.
