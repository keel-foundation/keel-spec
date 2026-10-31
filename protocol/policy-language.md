# Policy language

**Status:** draft.

Policy is versioned code. A policy bundle is a signed JSON document with:

```json
{
  "policy_version": "1.0.0",
  "hash": "sha256:...",
  "rules": [
    {
      "reason_code": "spam.mass_production",
      "scope": "channel",
      "severity": "high",
      "penalty": ["warn", "remove", "strike", "terminate"],
      "human_review": true,
      "appeal_window_days": 365
    }
  ],
  "human_review_gates": [
    "channel.terminate",
    "channel.permanent_demonetize",
    "channel.material_suppress"
  ],
  "content_protection": {
    "piracy": true,
    "spam": true,
    "scam": true,
    "impersonation": true
  }
}
```

Rules must be testable. A policy change requires an RFC and a public decision-log entry. Emergency changes follow the Constitution's emergency provisions and must be reviewed afterwards.
