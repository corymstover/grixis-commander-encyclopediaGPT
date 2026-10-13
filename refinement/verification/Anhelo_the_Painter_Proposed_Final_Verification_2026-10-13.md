# Anhelo, the Painter — Final Verification and Lock Record

**Date:** 2026-10-13  
**Status:** FINALIZED AND LOCKED — exact revised list approved by user on 2026-10-13  
**Frozen baseline:** 2026-10-12 FINAL TXT export; preserved unchanged  
**Proposed swap:** cut 1x Talrand's Invocation; add 1x Cryptic Pursuit  
**Card delta:** one-for-one replacement only

## 1. Exact proposed list and hashes

- Copy/paste list: `refinement/decklists/Anhelo_the_Painter_Proposed_Final_2026-10-13.txt`
- Clean-list SHA-256 (UTF-8, LF, trailing newline): `2e104d738a8025cfbde83c510f40456d1dc9d6c78cf4873394164f60996f4a3c`
- Frozen baseline TXT SHA-256: `60da19b0969ef944f5e44bed99f7ad5f17afa935271149cc82aca965b765cf25`
- Frozen source: `GrixisFINALTXT60--2026.zip`, member `Anhelo__the_Painter.txt`

The frozen source export is not overwritten.

## 2. Structural integrity

- Card quantity total: **100**.
- Distinct card names: **94** (including commander).
- Commander: exactly one, Anhelo, the Painter, first in the copy/paste list.
- Singleton: **PASS**; only Island x3, Mountain x3 and Swamp x3 repeat, all basics.
- Talrand's Invocation: removed exactly once.
- Cryptic Pursuit: added exactly once.
- No other card name or quantity changed.

## 3. New card Oracle text, identity, and legality

**Cryptic Pursuit — {2}{U}{R}, Enchantment; color identity UR.** Current Oracle text: “Whenever you cast an instant or sorcery spell from your hand, manifest the top card of your library. Whenever a face-down creature you control dies, exile it if it’s an instant or sorcery card. You may cast that card until the end of your next turn.” Commander legality: legal. UR color identity fits Anhelo's UBR identity.

**Outgoing Talrand's Invocation** is a legal blue sorcery that creates two 2/2 blue Drake creature tokens with flying.

References:
- Wizards of the Coast Streets of New Capenna release notes for Cryptic Pursuit: https://media.wizards.com/2022/downloads/SNC_Release_Notes/EN_MTGSNC_Release_Notes_20220331.pdf
- Cryptic Pursuit current card text / legality: https://mtg.wtf/card/pncc/70p/Cryptic-Pursuit
- Anhelo Oracle text and casualty rulings: https://mtg.wtf/card/ncc/100/Anhelo-the-Painter
- EDHREC Anhelo core data: https://edhrec.com/commanders/anhelo-the-painter/core

## 4. Commander-specific interaction

Anhelo gives the first instant or sorcery spell cast each turn casualty 2. A face-down manifested permanent is a 2/2 creature, so it can be sacrificed to pay casualty 2 on a later spell. If the manifested card is an instant or sorcery and that face-down creature dies, Cryptic Pursuit's triggered ability exiles that card and permits casting it until the end of the next turn.

When a spell is cast from hand, Cryptic Pursuit manifests once for that cast. The copy created by casualty is not cast, so it does not generate a second manifest trigger. Spells cast from graveyards do not trigger Cryptic Pursuit because they were not cast from hand.

## 5. Strategic assessment

Cryptic Pursuit converts repeated instant/sorcery casts from hand into additional 2/2 bodies that can pay Anhelo's casualty cost, while potentially recovering manifested instant/sorcery cards when those bodies die. This gives Anhelo an engine that simultaneously supports spell duplication and resource availability.

Talrand's Invocation is a solid four-mana one-shot: it immediately creates two flying tokens and can make four if copied by Anhelo. The deck already has Talrand, Sky Summoner plus Baral and Kari Zev, Judith, Lagomos, Poppet Stitcher, Army of the Damned, Black Market Connections and Ghoulish Procession as token/fodder sources. The proposed swap trades immediate flying board presence for a repeatable engine and conditional spell recovery. The four-mana enchantment needs subsequent spells to generate value and only triggers on spells cast from hand, so this is an identity-focused proposal rather than an unconditional upgrade in every game state.

Ghoulish Procession is retained because it can trigger when a nontoken creature is sacrificed to casualty and can produce fodder across turn cycles.

No gameplay win-rate or representative multiplayer testing claim is made.

## 6. Final approval gate

- 100-card count and structural integrity: **PASS**.
- Singleton compliance: **PASS**.
- New card Oracle text, color identity, and Commander legality: **PASS**.
- Relevant Anhelo/casualty/manifest interaction: **PASS**.
- Frozen baseline preserved: **PASS**.
- Exact revised list approved for final lock: **PASS — user approved on 2026-10-13**.
- Tracker `final_gate_passed`: **YES**.

## 7. Approval and preservation record

The user explicitly approved and locked this exact revised 100-card list on 2026-10-13. Standing instruction from this date forward: auto-approve future deck recommendations once the project's verification gates pass; do not pause for routine approval. Genuine hard-gate failures or unresolved source conflicts still block finalization. The only deck change is Talrand's Invocation -> Cryptic Pursuit. Frozen baseline exports remain unchanged.
