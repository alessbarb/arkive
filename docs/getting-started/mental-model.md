# Mental model

If you understand this page, you understand `arkive`.

The product is intentionally small.
It is not trying to manage everything.

It is trying to preserve one kind of state well:

> private local workspace state that should not be lost and should not live in Git.

## The five parts

Think of `arkive` as five parts:

- repository
- `.ark`
- vault
- snapshot
- restore

## Repository

The repository is still your normal working project.

Git still does what Git does:

- commits
- branches
- collaboration
- shared history

`arkive` does not replace that.

## `.ark`

`.ark/` is the local binding layer inside the repository.

It contains lightweight metadata such as:

- project binding
- project configuration

It should stay small.

It is not the place where encrypted snapshot payloads live.

## Vault

The vault is the external storage area outside the repository.

That is where encrypted snapshot payloads and snapshot metadata live.

This separation matters because the vault may contain:

- sensitive files
- large payloads
- local-only state

## Snapshot

A snapshot is a preserved copy of local workspace state at one moment in time.

In early versions, snapshots are:

- full
- encrypted
- independent

That means one snapshot can be restored without depending on another snapshot.

## Restore

Restore is the act of materializing a chosen snapshot into a destination you specify.

That destination is always explicit.

`arkive` should never quietly decide that for you.

## One-sentence model

A good one-sentence model is this:

> Git tracks shared project history. Arkive preserves private local state.

If a future feature makes that sentence stop being true, the product is drifting.
