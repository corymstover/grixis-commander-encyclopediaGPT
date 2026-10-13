# Anhelo, the Painter — New-Cycle Refinement & Verification Certificate

**Deck:** #4 of 62  
**Verification date:** 2026-10-13 (America/Chicago)  
**Baseline source:** `GrixisFINALTXT60--2026.zip` and `GrixisFINAL60--2026.zip`, frozen 2026-10-12  
**Baseline raw TXT SHA-256:** `60da19b0969ef944f5e44bed99f7ad5f17afa935271149cc82aca965b765cf25`  
**Baseline raw CSV SHA-256:** `1749131175f78e123deee0fc1e1f5a5f57ecc898ab5946e3f33a3fd0fa3d7b1d`  
**Normalized baseline-list SHA-256:** `7ae557bb81a2d9d3596061c3aff8a2efa4cf3f244e628ba0f9dc50c28aaa8c5f`  
**Revised raw TXT SHA-256:** `7fd898ffc4c3aad208cfd33361912bfefcff4754ec662b532ec5d0a5fcefbd4a`

## 1. Structural integrity

- Baseline CSV/TXT count: **100 cards / 94 unique names**; source TXT and CSV quantities reconcile.
- Revised deck: **100 cards / 94 unique names / 34 lands**.
- Commander marker: exactly once, on the first line (`1x Anhelo, the Painter [Commander]`).
- Singleton: **PASS**; repeated card names are only Island ×3, Mountain ×3 and Swamp ×3. No duplicate nonbasic names.
- Revised CSV/TXT quantity map: **PASS — exact name/quantity match**.
- The source archives are immutable; this revision is stored separately.

## 2. Identity, Oracle, current legality and exception boundary

- Commander color identity: **UBR**; all revised card identities fit within UBR.
- Project Scryfall refresh checkpoint: generated `2026-10-13T07:03:26.694525Z`, from data bulk-updated `2026-10-12T21:06:24.577Z`; 5,964/5,964 exact printing/name joins, no unresolved Oracle IDs/text, identity mismatches, or unexpected illegal statuses outside registered project exceptions.
- Five current baseline names not directly represented in the older deck-scoped audit (`A Little Chat`, `Bloodghast`, `Flawless Forgery`, `Maestros Charm`, `Thunderclap Drake`) were additionally checked using current card references. Deekah and Make an Example were individually checked for Oracle text, color identity, Commander legality and relevant rulings.
- Current official Commander banned-list checkpoint was checked on 2026-10-13. The October 12 Wizards announcement’s changes apply to Competitive Brawl, not tabletop Commander. No revised-list card appears on the official Commander banned list, and no project-specific exception is used. See [official list](https://mtgcommander.net/index.php/banned-list/) and [October 12 B&R announcement](https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026).

## 3. Commander-first strategy and changes

Anhelo grants casualty 2 to the first instant or sorcery **cast each turn**. The deck’s intended sequence is to maintain a power-2-or-greater creature or create one, turn one high-value instant/sorcery per turn into a copy, then maximize cast/copy triggers, graveyard reuse, copied removal and high-impact finishers.

- **Added Deekah, Fractal Theorist; cut Talrand, Sky Summoner.** Deekah triggers on casting **or copying** the instant/sorcery. When Anhelo copies the qualifying spell, both the original spell and its copy produce a Fractal with counters equal to that spell’s mana value. Talrand’s ability triggers on casting, not the copy. Cost of change: Deekah costs five rather than four and its tokens do not fly; Talrand’s four-mana flying-token engine was significant and its loss is explicit.
- **Added Make an Example; cut Talrand’s Invocation.** The copied four-mana spell makes each opponent split their current creatures into two piles, and you choose which pile is sacrificed. The casualty copy resolves first, then the original asks each opponent to form piles from the remaining creatures. Cost of change: the deck gives up a four-Drake flying burst from Talrand’s Invocation (one copy plus original) in exchange for copied multiplayer creature control. Existing token engines and Army of the Damned remain.

## 4. Rules and interactions verified

- **Casualty and stack order:** a casualty-2 sacrifice is paid once as an additional cost to the original spell; when paid, a spell copy is created on the stack and resolves before the original. The copy is not cast.
- **Deekah Magecraft:** its Oracle trigger includes copying instant or sorcery spells, so the Anhelo-created spell copy triggers Magecraft independently. A copy of an MV-4 spell produces another 4/4 Fractal from Deekah.
- **Make an Example:** current Oracle text and ruling confirm each opponent separates their creatures into two piles; the deck’s controller chooses the pile each opponent sacrifices. Copy and original resolve separately, so the original uses the board after the first resolution.
- **Copy/combo package retained:** `Dualcaster Mage` plus `Twinflame` remains a valid conditional token-copy loop if Twinflame has a legal initial target and an opponent does not interrupt; each Dualcaster ETB can copy Twinflame targeting a newly created Dualcaster. It is not claimed to be interruption-proof.
- **Ral, Storm Conduit + Reiterate + Mana Geyser:** conditional mana-positive repeat line only if Mana Geyser produces enough red mana per iteration to repay Reiterate with buyback (at least six total red). No unconditional-combo or win claim is made.

## 5. Candidate review and decisions

- Candidate CSV records **16 unique options**: 2 accepted/implemented and 14 rejected with rationales.
- High-ranking candidates are not auto-adds. Jadar was considered but rejected for this pass: it only creates its decayed Zombie at your end step if you control no decayed creature; the existing Ghoulish Procession can make a token when a nontoken creature (including the casualty sacrifice) dies, once per turn, including on opponents’ turns.
- The EDHREC Optimized page displayed 173 decklists when retrieved. Recorded snapshot metrics: Deekah 23% (39/173, Lift 45), Make an Example 25% (44/173, Lift 50), Talrand 57% (98/173, Lift 29), Talrand’s Invocation 6.4% (11/173, Lift 108). These are date-stamped inclusion signals, not evidence of win-rate superiority. The inherited broad-cohort rank file dated October 12 is labelled separately.

## 6. Consistency / performance assessment

The final library includes 14 main-deck creature cards with printed power 2 or greater that can ordinarily pay casualty 2 when on the battlefield (the creature card set includes Deekah, not Talrand). Exact hypergeometric calculation for drawing at least one of these 14 cards in an opening seven from 99 is **66.8447%**; for at least two, **25.7152%**. This is descriptive draw density only; it does not model mulligans, casting, surviving removal, generated tokens, game state or player decisions. No qualified matched-start multiplayer test was available. No win-rate or empirical superiority claim is made.

## 7. Final gate results

| Gate | Result |
|---|---|
| Source provenance and baseline integrity | **PASS** |
| Exact 100 cards, singleton, and CSV/TXT reconciliation | **PASS** |
| Oracle, identity, legality, official banned list, exception audit | **PASS** |
| Commander-first strategic reassessment | **PASS** |
| Candidate decisions and additions/cuts ledger | **PASS** |
| Relevant rules/interaction checks | **PASS** |
| Consistency/performance | **PASS WITH LIMITS** — exact hypergeometric calculation only; no qualified gameplay comparison |
| Revision file, exact hash and certificate | **PASS** |

**Final status: `APPROVED / LOCKED — ALL TECHNICAL GATES PASSED`.** This applies only to the exact revised TXT bytes with SHA-256 `7fd898ffc4c3aad208cfd33361912bfefcff4754ec662b532ec5d0a5fcefbd4a`. Any subsequent card-list change requires a new verification revision. No separate user approval is required by the 2026-10-13 active-cycle protocol.