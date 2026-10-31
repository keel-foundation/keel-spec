# Schemas

JSON Schemas and OpenAPI fragments for the protocol.

| Schema | Status | Purpose |
|---|---|---|
| `actor.schema.json` | TODO | Actor, keys, inbox/outbox |
| `channel.schema.json` | TODO | Creator channel |
| `video.schema.json` | Draft 0.1 | Video manifest, hashes, captions, license |
| `signal.schema.json` | Draft 0.1 | Detection signal |
| `moderation-case.schema.json` | Draft 0.1 | Case and evidence bundle |
| `enforcement-action.schema.json` | Draft 0.1 | Decision and Statement of Reasons |
| `appeal.schema.json` | Draft 0.1 | Appeal and decision |
| `audit-record.schema.json` | Draft 0.1 | Hash-chained ledger entry |
| `payout-entry.schema.json` | TODO | Double-entry ledger line |
| `export-bundle.schema.json` | TODO | Portable creator archive |

`openapi.yaml` documents the current demo API.

Every schema has at least one example in `examples/`. Run:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_schemas.py
```

The validator checks schema meta-validity, validates every example, and validates `openapi.yaml`. CI runs the same command.

The first contracts to ratify are `video`, `signal`, `moderation-case`, `enforcement-action`, `appeal`, and `audit-record`. They are the contract between `core`, `pipeline`, `web`, and `moderation`.
