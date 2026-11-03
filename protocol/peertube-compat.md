# PeerTube compatibility matrix

**Status:** draft. Not yet tested.

This document records the exact PeerTube version, endpoints, object shapes, and known gaps. Compatibility claims must be versioned and backed by tests.

| Capability | PeerTube version | Status | Notes |
|---|---|---|---|
| WebFinger actor discovery | TBD | TODO | |
| Fetch video object | TBD | TODO | |
| Follow channel | TBD | TODO | |
| Receive new video activity | TBD | TODO | |
| Expose actor/outbox | TBD | TODO | |
| Comments | TBD | TODO | |
| Import video metadata | TBD | TODO | |
| Import captions/thumbnails | TBD | TODO | |
| Moderation labels | N/A | Extension | `keeltube:trustLabels` |

## Compatibility rules

1. Unknown `keeltube:*` properties must be ignored by PeerTube parsers.
2. A KeelTube instance must not require PeerTube to understand payouts or appeals.
3. Attribution and license metadata must survive federation.
4. A failed compatibility test is a release blocker for a "PeerTube-compatible" claim.

The first implementation target should be a pinned PeerTube release, recorded here with the commit hash and test fixtures.
