# Security reference

Arkive has a conservative security model.

That is a strength, but it is important to describe it honestly.

## What Arkive protects

Arkive protects snapshot payloads at rest in the vault by encrypting them before storage.

## What Arkive does not claim to solve

Arkive does not claim to solve:

- endpoint compromise
- remote synchronization security
- team-wide secret distribution
- cloud secrets management
- operating system hardening

## Core assumptions

Arkive assumes:

- a trusted local machine
- deliberate user-driven workflows
- explicit restore targets
- local passphrase entry at snapshot creation and restore time

## Security design principles

- use standard primitives
- avoid custom crypto design
- minimize sensitive metadata exposure
- keep the repository lightweight and non-secret
- prefer explicit operations over hidden automation

## Practical guidance

If a machine is compromised, local private state should be considered compromised too.

Arkive lowers risk around stored local snapshot payloads.
It does not eliminate the broader risk of a hostile local environment.
