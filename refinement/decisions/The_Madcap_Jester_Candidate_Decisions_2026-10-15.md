# The Madcap Jester — Candidate Decisions

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Candidate SHA-256: `caeffc07503581cd3ecba798ebc4e09d48f07310f1f117ce3b90a04b5ca6bfa7`

Status: working decision closeout; not user approval

## Commander-first blueprint

The Madcap Jester is a Grixis exile-theft commander whose defining resource engine is turning library exile caused by spells and abilities you control into temporary access to opponents' cards. The attack trigger is a built-in three-opponent exile burst; the optimized shell therefore values (1) efficient library-exile effects that become functional tutors/draw with Jester, (2) ways to safely connect or immediately attack when that line is useful, (3) cast-from-exile payoffs and mana conversion, and (4) compact Grixis wins that the exile engine can assemble without replacing the commander's identity.

Current external cEDH evidence supports a Bracket 5 natural ceiling: the EDHREC cEDH analysis specifically identifies Extract, Tasha's Hideous Laughter, Ashiok, Nightmare Weaver, Psychic Surgery, Underworld Breach, Thassa's Oracle, Demonic Consultation and Tainted Pact as core or representative pieces of the optimized plan. Current optimized data also supports Dauthi Voidwalker and Lightning Greaves as live candidates.

## Final proposed delta

1. Ashiok, Nightmare Muse -> Ashiok, Nightmare Weaver
2. Brainstealer Dragon -> Dauthi Voidwalker
3. Etali, Primal Storm -> Demonic Consultation
4. Thief of Sanity -> Tainted Pact
5. Counterspell -> Lightning Greaves

## Accepted changes

- **Ashiok, Nightmare Weaver:** three mana and an immediately usable +2 that exiles the top three cards of an opponent's library. With Jester, that one ability turns all three into playable resources through the end of the next turn. It is substantially faster and more direct than five-mana Nightmare Muse's token-mediated exile plan.
- **Dauthi Voidwalker:** two-mana graveyard hate plus theft. More importantly, when a spell or ability you control would put cards from an opponent's library into their graveyard, Dauthi's replacement effect changes that event to exile; the modified event can trigger Jester. This creates a commander-specific interaction with Brain Freeze while leaving self-mill for the Breach line intact.
- **Demonic Consultation:** completes the already-present Thassa's Oracle line at one mana. This does not create a new generic shell from scratch; Oracle is already in the frozen baseline and the current cEDH Jester evidence treats Oracle/empty-library as one of the deck's natural compact finishes.
- **Tainted Pact:** second compact Oracle enabler and flexible instant-speed tutor. The candidate has 100 distinct card names, so there is no duplicate-name stop built into the deck.
- **Lightning Greaves:** Jester's attack trigger is a major native resource engine. Haste converts a four-mana commander cast into immediate exile access, while shroud protects the fragile 3/2; the attack and exile triggers do not target Jester, so shroud does not interfere with the commander engine.

## Cuts

- **Ashiok, Nightmare Muse:** five mana and requires creating/attacking or blocking with a token before its +1 becomes a repeatable library-exile engine. Nightmare Weaver produces immediate direct library exile for two less mana.
- **Brainstealer Dragon:** seven mana is too slow for the natural cEDH ceiling; the cast-from-exile tax/value text is powerful but does not justify the setup cost over Dauthi's two-mana engine/hate profile.
- **Etali, Primal Storm:** six mana plus an attack requirement without native haste is a slower, less reliable version of what the commander already wants to do.
- **Thief of Sanity:** requires combat damage from a fragile three-mana creature before generating one stolen card; it loses to the compact Oracle infrastructure at the optimized ceiling.
- **Counterspell:** the list retains Force of Will, Force of Negation, Fierce Guardianship, Pact of Negation, Mana Drain, Swan Song, Deadly Rollick and Deflecting Swat. UU Counterspell is the cleanest interaction cut for haste/protection that directly unlocks Jester's attack engine.

## Retained commander-specific core

Extract, Sadistic Sacrament, Bitter Ordeal, Tasha's Hideous Laughter, Psychic Surgery, Inside Information, Jester's Cap, Jester's Scepter, Ensnared by the Mara, Dragon's Smile, Don Andres, Gonti, Prosper, Party Thrasher, Passionate Archaeologist, Nalfeshnee, Plargg and Nassari, Sire of Stagnation, Circu, Laughing Jasper Flint and Wild-Magic Sorcerer remain because they express or exploit the opponent-library/exile/cast-from-exile game plan strongly enough to justify their slots.

## Material challengers rejected

- **Uba Mask:** strong theoretical interaction, but the static replacement effect does not trigger Jester by itself and it symmetrically replaces the deck's own normal draws, materially conflicting with Rhystic Study and Mystic Remora. It can make a spell/ability you control that would cause an opponent to draw instead cause library exile, but that narrower upside does not beat the accepted package.
- **Memory Vessel:** enormous one-shot exile volume but costs five mana, is sorcery-speed, sacrifices itself, and also gives opponents access to their exiled seven while locking normal hands. The existing lower-cost one-sided exile engines are more reliable at the cEDH ceiling.
- **Fathom Feeder:** five-mana activated exile/draw engine is too slow; ingest requires combat damage.
- **Raven Guild Master / Mist Intruder / Benthic Infiltrator / Rootwater Thief:** combat-dependent exile engines are weaker than Jester's own attack trigger plus cheaper spell/ability-based exile.
- **Opposition Agent:** an excellent cEDH card, but its primary value is generic search denial and it already supplies its own play permission. No commander-specific slot is weaker enough to justify displacing the preserved exile engine for it.
- **Ad Nauseam:** raw cEDH power is real, but the identity-driven list intentionally retains several four-to-seven-mana exile payoffs. Tasha's Hideous Laughter functions as the commander-specific burst-access engine, while Necropotence, Rhystic Study and Mystic Remora already supply conventional card velocity.
- **Grim Monolith / Simian Spirit Guide / Talisman of Creativity:** strong acceleration, but the current colored mana package is already dense and the remaining slower mana pieces have direct exile/cast-from-exile utility. No clean identity-positive cut remains.
- **Mental Misstep / Flusterstorm / Pyroblast / Red Elemental Blast:** efficient cEDH interaction, but the candidate retains a dense free/one-to-two-mana protection suite. Adding more would require cutting commander-specific engines rather than genuinely weak cards.
- **Hexing Squelcher / Orcish Bowmasters / The One Ring:** powerful generic cEDH value/protection pieces, but they do not outperform the retained commander-specific exile engines under the project's identity-first rule.

## Project-exception / official-legality distinction

The Madcap Jester and Dragon's Smile remain intentionally allowed by the project's future-release exception. Wizards' current product page states that new-to-Magic Mystery Booster Commander Edition cards become Commander-legal on **November 13, 2026**. On this project's current date, 2026-10-15, they therefore remain project-valid exceptions and must not be represented as currently officially Commander-legal. All other candidate cards require current official Commander legality with no exception.

## Closeout

Whole-list audit target: **99/99 noncommander copies adjudicated; 94 KEEP / 5 CUT**.

Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS** after the challenger review above.

Natural ceiling: **Power Bracket 5 — cEDH**.

Proposed Archidekt tags: **Exile Theft / Library Control / Grixis Combo**.
