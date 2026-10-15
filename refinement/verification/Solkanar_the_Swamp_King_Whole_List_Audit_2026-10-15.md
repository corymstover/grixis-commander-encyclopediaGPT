# Sol'kanar the Swamp King — mandatory whole-list audit

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #52 of 62  
Status: working audit; not user approval

Authoritative baseline: FINAL TXT member `Sol_kanar_the_Swamp_King.txt` from the frozen October 12 source package.

Candidate: `refinement/decklists/Solkanar_the_Swamp_King_Approval_Ready_2026-10-15.txt`  
Candidate SHA-256: `7d39fff42b91263e83415feef1e69d048c54f8b4e2226b8430fb584076d19106`

## Audit result

- Commander: **Sol'kanar the Swamp King**.
- Noncommander copies adjudicated: **99/99**.
- Result: **94 KEEP / 5 CUT**.
- Baseline: **100 cards / 95 distinct names / 36 lands**.
- Candidate target: **100 cards / 95 distinct names / 35 front-face lands + Fell Mire MDFC = 36 functional land-capable slots**.
- Candidate repeats: **Swamp x6 only**.
- Singleton: **PASS target** — only a basic land repeats.
- Commander color identity target: **U/B/R**.
- Project legality exception required: **NO**.
- Per-copy adjudication ledger: `refinement/decisions/Solkanar_the_Swamp_King_Whole_List_Decision_Ledger_2026-10-15.csv`.

## Final five-card delta

1. Feed the Swarm -> Withering Torment
2. Fellwar Stone -> The Soul Stone
3. Blightstep Pathway // Searstep Pathway -> Fell the Profane // Fell Mire
4. Dragonskull Summit -> Raucous Theater
5. Drowned Catacomb -> Undercity Sewers

## Commander-first findings

- **Withering Torment** is a black instant that destroys a creature or enchantment for a fixed two-life payment. It preserves the critical black-enchantment answer role of Feed the Swarm while improving timing and lowering the worst-case life cost. Casting it triggers Sol'kanar and Demon's Horn.
- **The Soul Stone** is an indestructible two-mana black mana rock. Unlike Fellwar Stone, casting it is itself a black-spell event for Sol'kanar/Demon's Horn. Its late-game harness ability can convert an expendable creature into repeatable upkeep reanimation.
- **Fell the Profane // Fell Mire** converts a land slot into a black removal spell when mana is no longer needed. The land face can enter untapped for 3 life, and the spell face triggers Sol'kanar/Demon's Horn.
- **Raucous Theater** and **Undercity Sewers** are actual Swamps. They therefore count for Cabal Coffers and Consuming Corruption, are doubled by Crypt Ghast when tapped for black mana, trigger Dread Presence when they enter under the deck's control, and remain fetchable typed duals. Their surveil 1 ETB offsets part of the tempo cost of entering tapped.
- The candidate preserves **Blanket of Night + Urborg** redundancy, **Painter's Servant + Grindstone**, all compact life-loop pieces, Aetherflux Reservoir, Bolas's Citadel, K'rrik, and the full premium tutor/ramp package.

## Source reconciliation

The frozen FINAL TXT is decklist truth. The v8.1.4 card audit contains a documented stale identity-resolution ambiguity for `Starscape Cleric`; the exact baseline printing is BLB #116 and is the black Bat Cleric, not a token object. The current-cycle gate must resolve that exact printing rather than inheriting the stale ambiguity.

Historical project review correctly rejected **Staff of the Death Magus**, **Epicure of Blood**, and **Tainted Well** as insufficient improvements over the existing lifegain/drain and Swamp infrastructure. This refinement preserves that conclusion rather than applying ranked candidates automatically.

## Candidate exhaustion

Material challengers reviewed include Staff of the Death Magus; Evil Presence; Diamond Mare; Prism Ring; Bloodthirsty Aerialist; Contaminated Ground; Epicure of Blood; Filth; Veinwitch Coven; Wall of Limbs; Tainted Well; Defile; Nightcreep; Countersquall; Witch's Cottage; Leechridden Swamp; Pristine Talisman; Boggart Trawler // Boggart Bog; Verdant Catacombs; additional fetchlands; and generic Force of Will / Thoracle-Breach conversion.

- **Staff / Diamond Mare / Prism Ring:** redundant trigger-only lifegain pieces. Demon's Horn already triggers on every player's black spells, and Painter's Servant makes that ceiling much higher than these narrower alternatives.
- **Evil Presence / Contaminated Ground / Tainted Well / Nightcreep:** redundant with Blanket of Night and Urborg for enabling swampwalk/Swamp infrastructure; too low-impact when the global effects are already present.
- **Epicure / Defiant Bloodlord-style payoffs:** five-plus-mana versions lose to Vito, Starscape Cleric, Marauding Blight-Priest and Enduring Tenacity.
- **Defile:** efficient, but Consuming Corruption already occupies the Swamp-scaling removal slot while also gaining life; Withering Torment adds the more important instant-speed enchantment answer.
- **Witch's Cottage / Leechridden Swamp:** on-theme Swamps, but their mono-black/tapped constraints do not beat the candidate's premium fixing and typed surveil duals.
- **Pristine Talisman:** lifegain synergy does not compensate for moving a two-mana ramp slot to three mana.
- **Boggart Trawler / Boggart Bog:** useful MDFC graveyard hate, but Bojuka Bog remains a zero-spell-cost graveyard exile land and Rakdos Charm supplies instant-speed redundancy.
- **Force of Will:** rejected because the authoritative baseline has too few blue nonland pitch cards for reliable use; Counterspell remains deterministic.
- **Generic Thoracle/Breach conversion:** rejected under no-forced-homogenization. Sol'kanar remains a black-spell/lifegain/Swamp-matters deck with compact commander-adjacent combos rather than a generic Grixis combo shell.

After the full 99-copy audit, current optimized-Sol'kanar comparison, modern MDFC/current-card review, Swamp-infrastructure review, mana-base red team, black-spell-density review, and generic-combo challenge:

**ZERO NEW MATERIAL IMPROVEMENTS.**

**Whole-list audit result: PASS FOR CANDIDATE CONSTRUCTION — exact Oracle/legality/rules gate remains required before approval-ready presentation.**
