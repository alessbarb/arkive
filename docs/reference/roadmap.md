# Roadmap reference

Arkive is still early.

The roadmap is not just a list of features.
It defines the sequence in which the product becomes trustworthy.

## Current direction

### v0.1 — Foundations

- explicit repository binding
- external vault
- encrypted snapshots
- explicit restore
- minimal inspectability

### v0.2 — Config

- clearer project behavior
- include/exclude policy
- stronger metadata rules

### v0.3 — Git complement

- explicit capture semantics
- clearer product boundary against Git-managed state

### v0.4 — Logical snapshots

- possible deduplication and logical snapshot evolution
- only after restore trust is stable

## Rule of interpretation

If a future feature weakens:

- clarity
- restore confidence
- Git boundary
- local-first behavior

then it does not belong yet.
