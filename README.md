# KeelTube Specification

This repository contains the normative protocol specification, RFCs, schemas, and policy language for KeelTube.

## Contents

- `rfcs/` — numbered requests for comments. RFC-0001 defines the protocol direction.
- `protocol/` — normative protocol documents once ratified.
- `schemas/` — JSON Schemas, examples, the demo OpenAPI document, and schema validation.

## Status

- Schemas exist for actors, channels, playback manifests, videos, signals, moderation cases,
  enforcement actions, appeals, and audit records, with examples and CI validation.
- Moderation v0.1 is frozen as of 2026-11-01. Additive changes only until v0.2.
- Core is PostgreSQL-backed and implements catalog and discovery, identity, engagement, creator
  studio upload/transcoding/HLS, watch telemetry and creator analytics, creator notifications,
  viewer report ingestion, semantic search, playlists, channel profiles, scheduled publishing,
  comment moderation, public trust records, irreversible archived-video media purge, Google/Apple/X
  social sign-in, ActivityPub federation, and read-only demo finance.
  The web client is fully built against local preview data, including the feed, watch page,
  channels, search, library, creator studio, and creator moderation record; API adapters are next.
  PeerTube-compatible ActivityPub federation v0.1 and a separate private staff moderation portal are
  implemented. Payouts are still a read-only demo.

## Checks

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.lock
.venv/bin/python scripts/validate_schemas.py
```

`requirements-dev.lock` pins the full development dependency set. `requirements-dev.txt` lists
the direct dependencies; regenerate the lock after changing it.

## Licensing

Specification text, RFCs, examples, and this repository are licensed under [CC-BY-4.0](LICENSE). Code samples are licensed under AGPL-3.0 unless stated otherwise.

## RFC process

1. Open a discussion with the problem statement.
2. Draft an RFC using the format in RFC-0001.
3. Publish it in `rfcs/` with the next number.
4. Allow at least fourteen days for comment; thirty days for constitutional or protocol-breaking changes.
5. The Maintainer Council and, where Creator rights are affected, the Creators' Council review it under the Constitution. Until those bodies are seated, the Interim Board and Interim Creators' Council review it under Article XV.
6. Accepted RFCs are normative. Rejected RFCs remain in the archive with the reasons. Every decision is recorded in the public decision log.

## Public decision log

Decisions are recorded in [`DECISIONS.md`](DECISIONS.md). A decision entry names the decision, rationale, decision-maker, date, and whether it changes the protocol.

## Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in RFC 2119.
