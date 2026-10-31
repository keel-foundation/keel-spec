# Schemas

JSON Schemas and OpenAPI fragments for the protocol.

## Planned schemas

| Schema | Status | Purpose |
|---|---|---|
| `actor.schema.json` | TODO | Actor, keys, inbox/outbox |
| `channel.schema.json` | TODO | Creator channel |
| `video.schema.json` | Draft 0.1 | Video manifest, hashes, captions, license |
| `signal.schema.json` | TODO | Detection signal |
| `moderation-case.schema.json` | Draft 0.1 | Case and evidence bundle |
| `enforcement-action.schema.json` | Draft 0.1 | Decision and Statement of Reasons |
| `appeal.schema.json` | TODO | Appeal and decision |
| `audit-record.schema.json` | TODO | Hash-chained ledger entry |
| `payout-entry.schema.json` | TODO | Double-entry ledger line |
| `export-bundle.schema.json` | TODO | Portable creator archive |

The first three schemas to ratify are `video`, `moderation-case`, and `enforcement-action`. They are the contract between `core`, `pipeline`, and `moderation`.
