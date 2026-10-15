# Sol'Kanar the Tainted — mandatory whole-list audit

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #53 of 62  
Status: working audit; not user approval

Authoritative baseline: FINAL TXT member `Sol_kanar_the_Tainted.txt` from the frozen October 12 source package.

Candidate: `refinement/decklists/Solkanar_the_Tainted_Approval_Ready_2026-10-15.txt`  
Candidate SHA-256: `72a3b14e93d884d98397e000fe45df430beb538a106097a69dfc2491da8d7a58`

## Audit result

- Commander: **Sol'Kanar the Tainted**.
- Noncommander copies adjudicated: **99/99**.
- Result: **86 KEEP / 13 CUT**.
- Baseline: **100 cards / 93 distinct names / 35 lands**.
- Candidate target: **100 cards / 93 distinct names / 35 lands**.
- Candidate repeats: **Island x3 / Mountain x3 / Swamp x4 only**.
- Singleton: **PASS target** — only basic lands repeat.
- Commander color identity target: **U/B/R**.
- Project legality exception required: **NO**.
- Per-copy adjudication ledger: `refinement/decisions/Solkanar_the_Tainted_Whole_List_Decision_Ledger_2026-10-15.csv`.

## Final thirteen-card delta

1. Arcane Denial -> Force of Will
2. Fellwar Stone -> Mana Vault
3. Feed the Swarm -> Withering Torment
4. Lightning Greaves -> Deflecting Swat
5. Clackbridge Troll -> Immortal Coil
6. Brainstealer Dragon -> Captive Audience
7. Disrupt Decorum -> Conjurer's Closet
8. Dragonskull Summit -> Badlands
9. Drowned Catacomb -> Underground Sea
10. Riverglide Pathway // Lavaglide Pathway -> Volcanic Island
11. Shivan Reef -> Flooded Strand
12. Sulfurous Springs -> Marsh Flats
13. Underground River -> Misty Rainforest

## Commander-first findings

- **Immortal Coil** is a materially stronger gift than Clackbridge Troll. Fateful Handoff can draw four and give it away; Donate, Harmless Offering, Bazaar Trader, Coveted Falcon and Shifting Grift also support transfer. Once an opponent controls Coil, Bojuka Bog or Rakdos Charm can empty that player's graveyard and trigger Coil's losing-game ability.
- **Captive Audience** replaces a seven-mana generic theft-value creature with a seven-mana permanent that literally enters under an opponent's control and imposes three severe political/punishment modes. It better expresses the deck's giftable-curse identity.
- **Conjurer's Closet** provides a second repeatable end-step reset beside Thassa. By stacking the triggers so Sol'Kanar's chosen mode resolves before the blink, Closet returns him as a new object with all four modes available again. It also reuses Baleful Strix, Ertai Resurrected and Kardur ETBs.
- **Lightning Greaves** is cut because shroud can prevent Thassa, Closet and Planar Incision from targeting Sol'Kanar. **Deflecting Swat** replaces that protection slot without blocking friendly blink effects and is often free while Sol'Kanar is controlled.
- **Force of Will** replaces Arcane Denial as higher-ceiling tap-out protection; the final gate must independently verify a healthy blue pitch pool.
- **Mana Vault** turns the lowest-impact generic two-mana rock into burst acceleration that can supply Sol'Kanar's two generic mana while three lands supply U/B/R.
- **Withering Torment** upgrades Feed the Swarm's creature/enchantment coverage to instant speed with fixed life loss.
- Six land changes replace conditional/pain/face-locked sources with three original duals and three fetchlands. Forbidden Orchard and Homeward Path are deliberately preserved because their effects are commander-specific.

## Preserved engines

The candidate retains Demonic Pact; Archfiend of the Dross; Greed's Gambit; Illusions of Grandeur; Plague Reaver; Donate; Harmless Offering; Bazaar Trader; Blim; Jon Irenicus; Kain; Khârn; Xantcha; Coveted Falcon; Fateful Handoff; Puca's Mischief; Role Reversal; Shifting Grift; Sudden Substitution; The Trickster-God's Heist; Thassa, Deep-Dwelling; Planar Incision; Homeward Path; and the existing interaction/tutor core.

## Source reconciliation

The frozen FINAL TXT is decklist truth. The v8.1.4 `deck_card_audit.csv` membership snapshot is stale for this deck and still contains pre-finalization cards such as An Offer You Can't Refuse, Counterspell, Opposition Agent, Reliquary Tower and Crumbling Necropolis. Those stale rows are useful only for Oracle metadata, not deck membership. Historical October 11 refinement already established Demonic Pact, Archfiend of the Dross, Greed's Gambit, Kain and Thassa as strong commander-native upgrades, and the later 62-deck review correctly rejected Modify Memory as redundant five-mana exchange density. This pass preserves those decisions.

## Candidate exhaustion

Material challengers reviewed include Modify Memory; Abyssal Persecutor; Akroan Horse; Sleeper Agent; Witch Hunt; Djinn of Infinite Deceits; Pendant of Prosperity; Alexios, Deimos of Kosmos; Steel Golem; Endless Whispers; Wishclaw Talisman; Sanctum of Eternity; Ghostly Flicker; Essence Flux; Blur; Bilbo, Luckwearer // Burglar's Plot; Deadpool, Trading Card; Alicia Masters, Skilled Sculptor; Venser, Fervent Forger; Turbulent Crater; Turbulent Wetlands; and generic Oracle/Breach conversion.

- **Modify Memory / Bilbo's Burglar's Plot / Trade-style exchanges:** redundant and expensive beside Role Reversal, Shifting Grift, Puca's Mischief and existing transfer engines.
- **Abyssal Persecutor / Steel Golem / Akroan Horse:** thematic gifts, but Immortal Coil is a substantially stronger closer and no second curse slot clearly beats the retained core.
- **Alicia Masters, Skilled Sculptor:** rejected despite its ability to reclaim a fourth-mode Sol'Kanar. Its end-step ownership reset would also undo Xantcha, Kain, Khârn, Jon Irenicus gifts and other creature donations that the deck intentionally wants opponents to keep.
- **Sanctum of Eternity:** commander-specific but slower and colorless; Homeward Path, Planar Incision and Coveted Falcon already provide recovery without weakening colored-source density.
- **Ghostly Flicker / Essence Flux / Blur:** valid one-shot resets, but Conjurer's Closet wins the additional slot because it is repeatable and does not consume protection every fourth turn.
- **Deadpool, Trading Card:** text-box exchange is novel but replaces rather than amplifies Sol'Kanar's own text and introduces upkeep life loss; not commander-first here.
- **Venser, Fervent Forger:** powerful six-mana opponent-copy value, but does not solve Sol'Kanar's reset/transfer bottleneck and is less identity-specific than the adopted curse/blink changes.
- **Turbulent Crater / Turbulent Wetlands:** current legal typed duals, but premium original dual/fetch upgrades provide better speed and fetch flexibility.
- **Generic Oracle/Breach conversion:** rejected under no-forced-homogenization.

After the full 99-copy audit, current-card challenger review, optimized-Sol'Kanar comparison, gift-kill review, blink/recovery-density review, mana-base red team, protection review and generic-combo homogenization challenge:

**ZERO NEW MATERIAL IMPROVEMENTS.**

**Whole-list audit result: PASS FOR CANDIDATE CONSTRUCTION — exact Oracle/legality/rules gate remains required before approval-ready presentation.**
