# Adaptive Pipeline v2 — freeze checklist

The architecture is ready to freeze when all items below are true.

- [x] Frozen 62-deck baseline is independently verified.
- [x] Current-cycle approval/lock state has one canonical authority.
- [x] Historical tracker data is preserved without overriding current state.
- [x] Stages are content-addressed and resumable.
- [x] Material input changes invalidate affected analyses.
- [x] Oracle/legality changes can invalidate project-wide card-fact conclusions.
- [x] Transient failures use bounded retry; permanent failures fail closed.
- [x] Multi-deck work supports bounded concurrency and isolates per-deck failures.
- [x] Telemetry measures runtime, cache reuse, retries, blockers, and hotspots.
- [x] Commander-first variant comparison rejects identity/integrity regressions.
- [x] Automation cannot approve or lock decks.
- [x] Optimization stopping rules prevent endless architecture churn.
- [ ] Full repository quality gate green on the final branch head.
- [ ] Adaptive pipeline quality gate green on the final branch head.

After both final CI gates are green, freeze v2 and redirect effort to deck refinement. Reopen architecture only under the documented stopping-rule exceptions.
