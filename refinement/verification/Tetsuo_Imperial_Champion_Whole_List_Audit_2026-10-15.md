# Tetsuo, Imperial Champion — Whole-List Audit

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Candidate SHA-256: `d6d7561f00cb56cfb86cd79024975130d718ddc7f3a1bddf0c62f61dc422822e`

## Baseline

Authoritative frozen source: `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz`, `Tetsuo__Imperial_Champion.txt`.

Baseline structure: exactly 100 cards including commander, 91 distinct names, 35 lands; Island x5, Mountain x4, Swamp x3 are the only repeats.

## Whole-list adjudication

**99/99 noncommander copies adjudicated: 87 KEEP / 12 CUT.**

### 12 cuts

1. Counterspell — Force of Will protects Tetsuo and free-cast/combat turns while tapped out.
2. Feed the Swarm — Withering Torment upgrades the creature/enchantment removal slot to instant speed.
3. Lizard Blades — Leyline Axe preserves double strike while adding trample, +1/+1, MV4 for Tetsuo, and opening-hand deployment.
4. Blackblade Reforged — Swiftfoot Boots gives tutor-able haste and hexproof, improving commander recovery and immediate attack access.
5. Thran Power Suit — Oathkeeper, Takeno's Daisho is a cleaner Samurai-specific resilience piece with MV3 and efficient equip.
6. Relentless Assault — its extra-combat text only functions when it resolves in a main phase; Tetsuo free-casts during combat. Replace with Savage Beating.
7. Seize the Day — same main-phase dependency; replace with World at War, whose delayed combat occurs after the second main phase and therefore works from a combat-time Tetsuo cast.
8. Crumbling Necropolis — replace always-tapped fixing with Volcanic Island.
9. Drowned Catacomb — replace conditional fixing with Mana Confluence.
10. Shivan Reef — replace painland with Flooded Strand.
11. Sulfurous Springs — replace painland with Marsh Flats.
12. Sulfur Falls — replace conditional dual with Misty Rainforest.

## Key keeps

- Excalibur, Sword of Eden — MV12 establishes an enormous Tetsuo spell/damage ceiling while equipping legends cheaply.
- Kaldra Compleat / Argentum Armor / Embercleave — high-MV Equipment with strong combat impact.
- Genji Glove / Hexplate Wallbreaker / Akki Battle Squad — commander-native repeat-combat engines.
- Aggravated Assault + Sword of Feast and Famine — retained repeatable combat engine that fits the Equipment/combat identity.
- Basilisk Collar — deathtouch/lifelink apply to Tetsuo's own damage-mode damage.
- Buster Sword — combat-damage card draw plus a second free-cast channel.
- Swordsman's Steel — equipment-density payoff and major Voltron scaling.
- Hammer of Nazahn / Brass Squire / Blacksmith's Talent — attachment-cost bypass and protection.
- Conqueror's Flail / Mithril Coat / Winged Boots / Padeem — protection package.
- Ancestral Vision / Profane Tutor / Wheel of Fate / Inevitable Betrayal — unusually efficient commander free-cast targets.
- Chandra's Ignition — high-value commander-damage sweeper/finisher when Tetsuo is built tall.

## Equipment challenger closeout

### Accepted

- **Leyline Axe:** MV4, double strike, trample, +1/+1, and opening-hand deployment materially beat Lizard Blades.
- **Oathkeeper, Takeno's Daisho:** Tetsuo is a Samurai, so the death-return trigger is live; it provides identity-specific resilience rather than generic protection.
- **Swiftfoot Boots:** haste is critical because Tetsuo must attack to function. It also provides hexproof without blocking the deck's own targeting.

### Rejected

- **Sword of Wealth and Power:** strong current optimized representation and real Treasure/spell-copy value, but protection from instants and sorceries creates a material self-interaction constraint with Chandra's Ignition and other beneficial spell targeting. With clean protection/value Equipment already retained, it does not beat the accepted package.
- **Shadowspear:** Basilisk Collar already supplies lifelink and deathtouch, while Leyline Axe/other Equipment cover trample; redundant relative to stronger commander-specific upgrades.
- **Komainu Battle Armor:** on-theme but lower impact than the retained high-MV, extra-combat, protection, and free-cast Equipment package.
- **Jhoira, Ageless Innovator:** slow tap-counter setup relative to existing direct artifact ramp/cheat engines.

## Spell red-team

- **Savage Beating** works during combat by design. Tetsuo may cast it from hand through his attack trigger if Equipment MV is at least 5. The additional-combat mode is immediately relevant; entwine remains an optional additional cost that can be paid even when the mana cost is not paid.
- **World at War** may be cast through Tetsuo during combat. Its effect schedules an additional combat after the second main phase rather than requiring the spell itself to resolve in a main phase. Because Tetsuo casts it from hand, rebound is live.
- **Temporal Manipulation / Time Warp** are powerful free-cast options but were rejected in favor of extra-combat cards that more directly preserve the commander's Equipment-combat identity.
- Generic Oracle/Breach/Ad Nauseam conversion rejected as identity-erasing.

## Mana structure

Candidate remains **35 lands**. Volcanic Island plus three additional fetchlands and Mana Confluence materially improve untapped U/B/R sequencing while preserving fetchable typed duals and 12 basics.

## Closeout

Candidate exhaustion and adversarial red-team review: **ZERO NEW MATERIAL IMPROVEMENTS** beyond the proposed 12-card delta.

Natural ceiling: **Power Bracket 4 — Optimized**.
