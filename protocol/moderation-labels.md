# Moderation labels

**Status:** draft.

Moderation labels describe content or instance properties. They are not punishments by themselves, and they must not be used for silent suppression.

## Label fields

- `label_id`
- `subject` — video, channel, actor, or instance
- `label` — `piracy`, `spam`, `scam`, `fraud`, `impersonation`, `harassment`, `csam`, `terrorism`, `age_restricted`, `copyright`
- `severity` — `info`, `warning`, `severe`
- `source` — `automated`, `human`, `instance`, `court_order`
- `evidence_ref`
- `issued_at`, `expires_at`
- `appeal_url`
- `issuer` — instance actor

## Federation rules

1. Labels travel with content when the issuing instance publishes them.
2. Labels are signed by the issuing instance.
3. A receiving instance may accept, downrank, or block a label, but must publish its policy.
4. Labels must not reveal private evidence or personal data.
5. A label that materially suppresses reach is an enforcement action and must be appealable.

## Prohibited uses

- Silent shadowbanning without a label and an appeal path.
- Labeling a creator's entire channel for a single ambiguous video.
- Using a label to avoid the human review gate for termination.
