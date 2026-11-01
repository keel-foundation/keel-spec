# Schemas

JSON Schemas and OpenAPI fragments for the protocol.

| Schema | Status | Purpose |
|---|---|---|
| `actor.schema.json` | Draft 0.1 | Actor, identity, keys, inbox/outbox |
| `channel.schema.json` | Draft 0.1 | Creator channel |
| `playback-manifest.schema.json` | Draft 0.1 | MP4/HLS playback locations |
| `video.schema.json` | Draft 0.1 | Video manifest, hashes, captions, license |
| `signal.schema.json` | Draft 0.1 | Detection signal |
| `moderation-case.schema.json` | Draft 0.1 | Case and evidence bundle |
| `enforcement-action.schema.json` | Draft 0.1 | Decision and Statement of Reasons |
| `appeal.schema.json` | Draft 0.1 | Appeal and decision |
| `audit-record.schema.json` | Draft 0.1 | Hash-chained ledger entry |
| `payout-entry.schema.json` | TODO | Double-entry ledger line |
| `export-bundle.schema.json` | TODO | Portable creator archive |

`openapi.yaml` documents the current demo API. Moderation v0.1 is frozen as of 2026-11-01;
additive changes only until v0.2. See [DECISIONS.md](../DECISIONS.md).

Every schema has at least one example in `examples/`. Run:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_schemas.py
```

The validator checks schema meta-validity, resolves cross-schema references, validates every
example, and validates `openapi.yaml`. CI runs the same command.

The first contracts to ratify are `actor`, `channel`, `playback-manifest`, `video`, `signal`,
`moderation-case`, `enforcement-action`, `appeal`, and `audit-record`. They are the contract
between `core`, `pipeline`, `web`, and `moderation`.

## Required fields for the walking skeleton

- `actor`: `id`, `type`, `handle`, `display_name`, `created_at`, `updated_at`.
- `channel`: `id`, `actor_id`, `handle`, `name`, `created_at`, `updated_at`.
- `playback-manifest`: `mp4_url`.
- `video`: `id`, `channel_id`, `title`, `status`, `visibility`, `content_hash`,
  `duration_seconds`, `playback`, `license`, `created_at`, `updated_at`.
- `signal`: `id`, `source`, `signal_type`, `created_at`.
- `moderation-case`: `id`, `subject`, `status`, `severity`, `policy_refs`, `signals`,
  `evidence`, `created_at`, `updated_at`.
- `enforcement-action`: `id`, `case_id`, `action_type`, `scope`, `policy_clause`,
  `statement_of_reasons`, `human_reviewer`, `status`, `effective_at`, `appeal_deadline`,
  `audit_record_hash`, `created_at`.
- `appeal`: `id`, `action_id`, `appellant`, `grounds`, `statement`, `submitted_at`, `status`,
  `reviewer`, `decision`, `reasoning`, `decided_at`.
- `audit-record`: `seq`, `type`, `at`, `payload`, `prev_hash`, `hash`.
