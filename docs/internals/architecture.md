# Architecture

This page describes the current internal structure of `arkive`.

The architecture is intentionally layered.

## Layers

### CLI

Responsible for:

- command wiring
- argument binding
- prompt handling
- presenter-driven output

### Services

Responsible for:

- orchestration
- use-case execution
- coordination between layers

### Domain

Responsible for:

- typed models
- structured result shapes
- product concepts such as project binding, snapshots, restore, and status

### Repository

Responsible for:

- reading and writing persisted metadata
- binding access
- index access
- manifest access

### Crypto

Responsible for:

- passphrase validation
- key derivation
- encryption and decryption helpers

### Packaging

Responsible for:

- archive creation
- archive extraction
- manifest construction

### Utils

Responsible for:

- pure reusable helpers
- filesystem helpers
- JSON helpers
- hashing
- path rendering
- time helpers

## Design intent

The point of this structure is simple:

- business logic should not depend on terminal behavior
- repositories should not decide product semantics
- CLI should not contain hidden domain logic
- crypto should stay encapsulated
- snapshot storage can evolve later without collapsing the whole codebase

## Current architectural direction

The current codebase favors:

- explicit flows
- small services
- typed boundaries
- local-first behavior
- restore-first design
