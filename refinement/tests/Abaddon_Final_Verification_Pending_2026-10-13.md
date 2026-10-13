# Abaddon Final Verification Run — 2026-10-13

This is a blocker record, not a pass certificate.

The frozen compact archive remains verified by the prior package audit (SHA-256 `f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20`) and Abaddon's authoritative TXT SHA-256 remains `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`. However, the connected GitHub action exposes the archive as base64 text and does not provide a remote shell or workflow-dispatch action to execute the committed independent parser against those bytes in this session. The parser is committed for a local/CI run. This session therefore does not claim that parser's output has been executed or independently reproduced here.

The latest committed dated global Scryfall refresh is not a live approval-time refresh. The web interface could not access the Scryfall named-card endpoints directly during this run; the official Wizards Commander banned list was reachable and had no Abaddon-specific change recorded in the October 12, 2026 announcement. Exact identity/Oracle legality confirmation is therefore not claimed newly completed during this session.

**Gate:** structural verification rests on the already committed independent baseline audit and hash manifest; new parser execution and current approval-time Scryfall confirmation remain pending. The final list must not be marked approved or locked until the exact baseline is presented and the user explicitly approves it.
