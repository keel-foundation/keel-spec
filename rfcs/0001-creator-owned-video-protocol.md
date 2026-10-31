# RFC-0001: Creator-Owned Video Protocol, PeerTube-Compatible, Moderation-First

- **RFC number:** 0001
- **Title:** Creator-owned video protocol, PeerTube-compatible, moderation-first
- **Status:** Draft
- **Author(s):** TubeKeel maintainers
- **Created:** 31 October 2026
- **Discussion:** GitHub Discussions (RFC-0001)
- **Requires:** The Keel Covenant (private draft, pending ratification), technical whitepaper (private draft)
- **Normative language:** RFC 2119

---

## Abstract

TubeKeel is an open, federated protocol for creator-owned video. It is designed to interoperate with PeerTube through ActivityPub where PeerTube's object model is sufficient, and to extend that model with portable creator identity, moderation records, appealable enforcement, content protection, and transparent payouts.

This RFC defines the protocol direction, the compatibility boundary, the moderation-first data model, and the first implementation milestones. It does not define every endpoint or schema; those follow in later RFCs and in `spec/protocol/`.

The central claim is simple: **a video protocol is not legitimate if it can erase a creator's livelihood without specific notice, human review, a real appeal, and a portable exit.**

---

## 1. Motivation

Centralized video platforms enforce policy at a scale that makes individual review impossible. The result is a structural bias toward fast, blunt, irreversible action:

- legitimate creators are caught in spam and AI-slop sweeps;
- channel-level penalties amplify one error across an entire archive;
- notices are vague, so creators cannot rebut the actual allegation;
- appeals are fast, opaque, and often feel automated;
- demonetization and termination both destroy livelihoods;
- piracy, impersonation, and scam ads make the platform unsafe;
- creators cannot leave without losing their audience.

Existing open projects solve parts of this. PeerTube federates video but does not provide a creator bill of rights, independent appeals, transparent payouts, or content protection as protocol primitives. Owncast is live-only. Invidious and FreeTube are clients. Odysee/LBRY explores crypto-native content but not due process.

TubeKeel's differentiator is not the player. It is the governance engine expressed as protocol.

---

## 2. Goals

1. **Creator ownership.** Creators own their content, metadata, audience relationship, and payout history.
2. **Portability.** Export and import are first-class, documented, and available before, during, and after an enforcement action.
3. **PeerTube compatibility.** A TubeKeel instance can follow, be followed by, and exchange video objects with PeerTube instances where the object model allows.
4. **Moderation-first.** Every enforcement action has a specific reason, evidence, human decision, audit record, appeal path, and published outcome statistics.
5. **Content protection.** Piracy, unauthorized re-upload, impersonation, spam, scams, fraud, and fake engagement are first-class threats.
6. **Transparent payouts.** A double-entry ledger, published holdback rules, and creator-visible balances.
7. **Federation without a single gatekeeper.** No instance, company, or foundation is the only gateway.
8. **Constitutional limits.** The protocol encodes the Creator Covenant; it does not merely recommend it.

---

## 3. Non-goals

- Replacing PeerTube's entire vocabulary in v1.
- Building a recommendation algorithm that maximizes engagement at any cost. Discovery starts with subscriptions, search, and transparent ranking.
- Supporting anonymous, unmoderated, or unaccountable hosting.
- Providing a cryptocurrency or speculative token.
- Solving every jurisdiction's copyright, privacy, and safety law in the protocol. Instances remain responsible for local compliance.
- Promising free unlimited storage or bandwidth.

---

## 4. Design principles

The protocol is subordinate to the Constitution. The Constitution and whitepaper are private drafts until ratification; public summaries live in `keel-docs`. The following principles are normative for design decisions:

- **Human decision before irreversible harm.** Automation may flag, triage, and apply temporary protective holds. A human with authority to reverse MUST confirm channel-level termination, permanent demonetization, or material suppression.
- **Specific notice.** An enforcement action MUST carry a Statement of Reasons: policy clause, content identifier, timestamp, evidence, decision-maker, and appeal route.
- **Proportionality.** Penalties MUST follow the published matrix. Related-channel enforcement MUST require specific evidence of common control.
- **Portability.** Every creator MUST be able to export content, metadata, captions, analytics, moderation records, and payout history in documented formats.
- **Transparency.** Enforcement volumes, automation rates, appeal volumes, reversal rates, and median decision times MUST be published quarterly.
- **Content protection.** Piracy, impersonation, spam, scams, and fraud MUST be treated as serious harms, not growth hacks.
- **No AI as final judge.** AI may detect, prioritize, translate, and draft. It MUST NOT be the final decision-maker for an enforcement action.

---

## 5. Protocol overview

TubeKeel has six protocol layers:

1. **Identity.** Actors, channels, keys, and portable creator identity.
2. **Content.** Video objects, manifests, captions, thumbnails, and content hashes.
3. **Federation.** ActivityPub discovery, inbox/outbox, signatures, and instance policy documents.
4. **Moderation.** Signals, cases, enforcement actions, appeals, audit records, and transparency aggregates.
5. **Protection.** Fingerprints, piracy matching, spam/scam signals, impersonation, and account security.
6. **Economics.** Payout ledger, holdbacks, and creator-visible balances.

These layers are separable. An instance MAY implement content and federation without payouts; it MUST implement the moderation and portability layers to use the TubeKeel name and federation seal.

---

## 6. PeerTube compatibility

### 6.1 Compatibility stance

TubeKeel is **PeerTube-compatible, not PeerTube-derived**. The goal is interoperability, not a fork. We reuse PeerTube's ActivityPub object model where it is sufficient, and document every extension explicitly.

An instance is "PeerTube-compatible" for the purposes of this RFC when it can:

1. resolve a PeerTube actor via WebFinger;
2. fetch and parse a PeerTube video object;
3. follow a PeerTube channel and receive new video activities;
4. expose its own actors and videos in a form PeerTube can follow;
5. preserve attribution and license metadata across federation.

Full compatibility is tested against a pinned PeerTube release in `spec/protocol/peertube-compat.md`. Compatibility claims MUST be versioned and tested, not asserted.

### 6.2 Reused vocabulary

Where available, TubeKeel uses:

- ActivityPub actors and inbox/outbox collections;
- WebFinger for discovery;
- HTTP Signatures for server-to-server authentication;
- PeerTube's video, channel, and comment representations;
- ActivityStreams activities (`Create`, `Update`, `Delete`, `Announce`, `Follow`, `Accept`, `Reject`, `Flag`) for the corresponding actions.

### 6.3 Extensions

TubeKeel adds a `tubekeel` namespace for properties that PeerTube does not define:

- `tubekeel:contentHash` — SHA-256 of the canonical media manifest.
- `tubekeel:policyVersion` — the policy bundle used for a decision.
- `tubekeel:statementOfReasons` — a link to the Statement of Reasons.
- `tubekeel:appealUrl` — the creator-facing appeal route.
- `tubekeel:auditDigest` — the hash-chain digest for the decision.
- `tubekeel:trustLabels` — content-protection and provenance labels.
- `tubekeel:payoutAccount` — an opaque payout reference, never a bank secret.
- `tubekeel:exportBundle` — a link to the creator's export manifest.

Extensions MUST be optional for reading and MUST NOT break PeerTube's parser. Unknown properties are ignored by compatible peers.

### 6.4 Federation of moderation

Moderation records are not silently federated. An instance MAY publish:

- aggregate transparency data;
- a signed policy document;
- content-protection labels;
- a public blocklist of instances or actors.

An instance MUST NOT publish another creator's private evidence or personal data. Cross-instance moderation follows the Instance Covenant and the label semantics in `spec/protocol/moderation-labels.md`.

### 6.5 Import and migration

A creator migrating from PeerTube or another compatible instance MUST be able to import:

- video files and manifests;
- metadata, captions, thumbnails, and licenses;
- channel identity and public subscriber graph where lawful;
- moderation history, where the source instance provides it.

Import MUST preserve content hashes so that attribution and piracy matching survive migration.

---

## 7. Moderation-first architecture

### 7.1 Signals

A **Signal** is an observation, not a decision. It has:

- `signal_id`;
- `source` (`automated`, `user_report`, `priority_flagger`, `instance`, `court_order`);
- `signal_type` (`spam`, `scam`, `piracy`, `impersonation`, `harassment`, `csam`, `copyright`, `other`);
- `confidence` and `model_version` where automated;
- `evidence_ref`;
- `created_at`.

Signals MAY be combined into a case. Signals alone MUST NOT terminate a channel.

### 7.2 Cases

A **ModerationCase** groups signals, content, and history for human review. It has:

- `case_id`;
- `subject` (video, channel, account, or instance);
- `policy_refs`;
- `evidence_bundle`;
- `severity`;
- `status` (`open`, `reviewing`, `decided`, `appealed`, `closed`);
- `assignee` and `reviewer`;
- `created_at`, `updated_at`.

### 7.3 Enforcement actions

An **EnforcementAction** is a decision. It MUST include:

- `action_id`;
- `case_id`;
- `action_type` (`warn`, `remove`, `age_restrict`, `demonetize`, `suspend`, `terminate`, `label`, `downrank`);
- `scope` (`video`, `channel`, `account`, `instance`);
- `policy_clause`;
- `statement_of_reasons`;
- `human_reviewer`;
- `effective_at`, `expires_at`;
- `appeal_deadline`;
- `audit_record_hash`.

Channel-level termination and permanent demonetization MUST have a human reviewer. Automated temporary holds MUST expire within 72 hours unless a human extends them with a recorded reason.

### 7.4 Appeals

An **Appeal** MUST be available for every enforcement action. It has:

- `appeal_id`;
- `action_id`;
- `appellant`;
- `grounds` (`new_evidence`, `procedural_error`, `policy_misapplication`, `identity`, `other`);
- `submitted_at`;
- `reviewer` (independent of the original decision);
- `decision` and `reasoning`;
- `decided_at`.

The appeals service MUST enforce the service levels in the Constitution, Schedule C. A second appeal MUST be available on new evidence or procedural error.

### 7.5 Audit ledger

Every action, review, and appeal MUST be recorded in an append-only, hash-chained ledger:

```
record_hash = SHA-256(prev_hash || canonical_json(record))
```

The ledger MUST be exportable. Creators MUST be able to read their own records. The public MUST be able to read aggregates and redacted decisions. A periodic anchor (for example, a signed daily digest) provides tamper evidence outside the database.

### 7.6 Transparency

The transparency report is generated from the ledger and telemetry, not hand-edited. It MUST include the fields in the Constitution, Schedule D, including:

- enforcement actions by policy and instance;
- automation share;
- appeal volume and reversal rate;
- median and 95th-percentile decision time;
- piracy, spam, scam, impersonation, and account-takeover actions;
- payout reliability and holdbacks;
- the Creator Trust Index.

### 7.7 Content protection

Content protection is a protocol layer, not a support queue:

- **Fingerprints.** Creators MAY register perceptual and exact hashes of their work. Matching runs at ingest and on demand.
- **Piracy and re-upload.** A match creates a case, not an automatic termination. The original creator is notified; the alleged re-uploader gets notice and an appeal.
- **Copyright.** Notice-and-takedown, counter-notice, and repeat-infringer workflows follow the instance's legal obligations. False claims are treated as abuse.
- **Spam and scams.** Rate limits, behavioral signals, link scanning, payment-fraud detection, bot detection, and purchased-engagement detection feed the same case system.
- **Impersonation.** Verified identity, badge policy, and a human review path for impersonation claims.
- **Account security.** Multi-factor authentication, session control, login alerts, and human-led recovery. A compromised channel is a victim, not a voluntary violator.

---

## 8. Core data model

The first schemas live in `spec/schemas/`. The minimum objects are:

- `Actor` — a person, channel, or instance actor with keys and inbox/outbox.
- `Channel` — a creator's public identity and subscription target.
- `Video` — media manifest, hashes, captions, license, and visibility.
- `Signal` — an observation that may become evidence.
- `ModerationCase` — the review unit.
- `EnforcementAction` — the decision.
- `Appeal` — the challenge.
- `AuditRecord` — the hash-chained journal entry.
- `PayoutEntry` — a double-entry ledger line.
- `ExportBundle` — the portable creator archive.

All identifiers are opaque, globally unique, and stable across export/import.

---

## 9. API surface (v1 draft)

The API is versioned under `/api/v1`. The first endpoints are:

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/health` | Liveness and readiness |
| `POST` | `/videos` | Create an upload session |
| `GET` | `/videos/{id}` | Video metadata and playback manifest |
| `GET` | `/channels/{id}` | Channel metadata |
| `POST` | `/channels/{id}/subscribe` | Subscribe |
| `GET` | `/feed` | Subscription feed |
| `POST` | `/moderation/signals` | Ingest a signal (internal/service auth) |
| `GET` | `/moderation/cases/{id}` | Case status and evidence summary |
| `POST` | `/moderation/cases/{id}/decide` | Record a human decision |
| `POST` | `/moderation/actions/{id}/appeal` | File an appeal |
| `GET` | `/moderation/ledger/{record}` | Read an audit record |
| `GET` | `/exports/{channel}` | Request an export bundle |
| `GET` | `/payouts/{channel}` | Ledger and payout status |

Federation endpoints follow ActivityPub and are documented separately. The OpenAPI document will be generated from `spec/schemas/openapi.yaml` once the first schemas are stable.

---

## 10. Payouts and portability

Payouts use a double-entry ledger. Every accrual, holdback, adjustment, and payout is a balanced entry. During an appeal, earnings are held back, not clawed back. The creator sees the same ledger the platform sees.

Portability is a protocol requirement:

- an export bundle contains media, metadata, captions, thumbnails, analytics, moderation records, and payout history;
- the bundle includes hashes and a manifest so it can be imported elsewhere;
- import MUST preserve attribution and content hashes;
- export MUST NOT be conditioned on silence, waiver, or deletion of the appeal.

---

## 11. Security and privacy

- Server-to-server federation uses HTTP Signatures and rotated keys.
- Creator and viewer data is minimized and purpose-limited.
- Evidence bundles are access-controlled and redacted for third parties.
- Legal requests are reviewed by counsel and disclosed in aggregate where lawful.
- CSAM and terrorism content follows emergency procedures with post-hoc human review and legal reporting.
- No protocol feature requires mass surveillance of viewers.

---

## 12. Alternatives considered

**Build a new federation protocol.** Rejected for v1. PeerTube already has an ecosystem, a video object model, and ActivityPub tooling. A new protocol would add adoption cost without improving creator rights.

**Use AT Protocol as the primary substrate.** Interesting for portable identity and data repos, but the video hosting and federation model is less mature for this use case. A bridge can be explored later.

**Use IPFS for hot video.** Rejected for v1. Content addressing is useful for integrity, but IPFS delivery is not cost-competitive for mainstream video and adds legal and UX complexity.

**Build a single monolithic platform.** Rejected. It recreates the gatekeeper problem and makes exit harder.

**Make moderation a plugin.** Rejected. Moderation is a protocol primitive; if it is optional, the Creator Covenant is optional.

---

## 13. Rollout

**Phase 0 — Specification (this RFC):** schemas, PeerTube compatibility matrix, policy language draft.

**Phase 1 — Core:** upload, transcode, HLS playback, channels, subscriptions, auth, object storage. Single instance, invite-only creators.

**Phase 2 — Moderation:** signals, cases, human review, appeals, audit ledger, transparency report, content protection basics.

**Phase 3 — Federation:** PeerTube-compatible ActivityPub, instance registry, labels, blocklists, cross-instance appeals.

**Phase 4 — Economics and scale:** payouts, memberships, import/export at scale, second instance, legal entity, DSA/FTC compliance.

Each phase has a public demo and a written retrospective. No phase is "done" until the Creator Covenant tests pass.

---

## 14. Open questions

1. Which PeerTube vocabulary gaps require extensions rather than new object types?
2. Should moderation labels be signed per instance, per federation, or both?
3. What is the minimum viable content-fingerprinting system that is accurate and affordable?
4. How should cross-instance appeals work when the original instance is unavailable?
5. Which payout rails and jurisdictions are supported first?
6. How do we prevent the Creator Trust Index from becoming a marketing metric?
7. What is the legal structure for the flagship instance versus the Foundation?

---

## 15. References

- The Keel Covenant — private draft, not public until ratification.
- Technical whitepaper — private draft, not public until ratification.
- ActivityPub (W3C Recommendation).
- ActivityStreams 2.0 (W3C Recommendation).
- PeerTube ActivityPub documentation.
- RFC 2119 — Key words for requirement levels.
- Digital Services Act (EU) 2022/2065, Articles 17, 20, and 21.

---

## 16. Decision

This RFC is a **draft**. It is accepted when:

1. the PeerTube compatibility matrix is reviewed by at least two implementers;
2. the moderation data model is reviewed by the Maintainer Council and the Creators' Council;
3. the security and privacy sections are reviewed by counsel;
4. the first three schemas are published in `spec/schemas/`;
5. the Maintainer Council records a decision in the public decision log.

Comments should be filed in the RFC discussion. Silence is not consent for protocol-breaking changes.
