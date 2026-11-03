# Public decision log

This log records decisions that affect the protocol, the repositories, and the public governance surface. Private board, finance, legal, personnel, and security decisions are recorded in the private governance repository.

| Date | Decision | Rationale | Decision-maker | Status |
|---|---|---|---|---|
| 2026-10-31 | RFC-0001 published for a 14-day review | Establish the creator-owned, PeerTube-compatible, moderation-first direction | KeelTube maintainers | Draft |
| 2026-10-31 | Code repos use AGPL-3.0; spec and public docs use CC-BY-4.0 | Keep network services and protocol text open | KeelTube maintainers | Accepted |
| 2026-10-31 | The demo is local-only and uses a synthetic classifier signal | Avoid overstating the current implementation while the real pipeline is built | KeelTube maintainers | Accepted |
| 2026-10-31 | The audit ledger is append-only JSONL with a verifiable hash chain | Make the trust primitive testable before moving it to PostgreSQL and an external anchor | KeelTube maintainers | Accepted |
| 2026-10-31 | Public governance summaries are published while the full Constitution remains private until ratification | Give creators the rights and appeal process without publishing unratified private records | KeelTube maintainers | Accepted |
| 2026-11-01 | Freeze the moderation v0.1 contract | Roles, appeals, queue, ledger, and contract tests are stable enough to build the console against; add to v0.1 only in a backward-compatible way, otherwise supersede with v0.2 | KeelTube maintainers | Accepted |

Add a row when a decision is made. Do not edit history; supersede an entry with a new row.
