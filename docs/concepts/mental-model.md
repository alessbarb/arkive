# Mental model

`arkive` is easiest to understand when you stop thinking of it as “backup software” in the general sense.

It is narrower than that.

It is a local encrypted preservation layer for project state that does not belong in Git.

## The key distinction

A repository usually contains two kinds of state.

### Shared state

This belongs to Git.

It should be:

- tracked
- committed
- reviewed
- shared deliberately

### Private local state

This belongs to Arkive.

It may be:

- sensitive
- local-only
- ignored by Git
- intentionally absent from project history

That distinction is the center of the product.

## The core objects

`arkive` works through a small set of objects:

- repository
- `.ark/`
- vault
- snapshot
- restore

### Repository

The place where your project lives.

### `.ark/`

A lightweight local metadata directory inside the repository.

### Vault

The external storage location for real snapshot state.

### Snapshot

An encrypted preserved copy of a repository state.

### Restore

An explicit reconstruction into a destination you choose.

## The practical rule

If you need collaboration history, use Git.

If you need local encrypted preservation of state that should not be committed, use Arkive.

That is the product boundary.
