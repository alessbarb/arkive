# Snapshots

A snapshot is a preserved copy of local workspace state at a specific moment.

In early versions of `arkive`, snapshots are intentionally conservative.

## Snapshot properties

Early snapshots are:

- full
- encrypted
- explicit
- independent

## Full

A snapshot captures the selected workspace state as a whole.

This is not yet a deduplicated object graph.

That choice is deliberate.

## Encrypted

Before a snapshot is stored in the vault, its payload is encrypted locally.

The repository itself does not become the secret store.

## Explicit

Snapshots are created because the user asked for them.

There are no hidden background snapshots.

## Independent

Each snapshot can be restored on its own.

That matters because it avoids fragile chains where one broken snapshot invalidates later recovery.

## Snapshot metadata

A snapshot record describes things like:

- snapshot id
- creation time
- capture mode
- compression mode
- payload path
- payload size

This makes the system inspectable without making it noisy.

## Why the model is conservative

A lot of tools jump quickly into:

- deduplication
- incremental chains
- automation
- retention logic

Those things can be useful, but early on they can also hide the most important question:

> can this snapshot be restored clearly and reliably?

Arkive currently answers that question by keeping the model simple.
