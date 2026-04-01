# Encryption

Arkive encrypts snapshot payloads before storing them in the vault.

This is a core part of the trust model, but it should still be understood in realistic terms.

## What is encrypted

The snapshot payload is encrypted before it is persisted in the vault.

The repository itself is not turned into an encrypted workspace.
The encryption boundary is the stored snapshot payload.

## Current model

The current implementation uses:

- `scrypt` for key derivation
- `AES-256-GCM` for authenticated encryption

This is a conservative and standard approach.

## What the passphrase does

The passphrase is used to derive the encryption key that protects the snapshot payload.

It is required when:

- creating a snapshot
- restoring a snapshot

## What encryption does not solve

Encryption protects stored payloads, but it does not magically protect a compromised machine.

If the local environment is compromised, then:

- plaintext can be exposed during normal use
- passphrase entry can be observed
- restored data can be read

That is why Arkive is honest about its scope.

It is a local encrypted preservation layer, not a full endpoint security system.

## Design rule

Arkive should continue to use standard primitives and avoid inventing custom cryptographic schemes.
