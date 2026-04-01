# First project

This page walks through a realistic first use of `arkive`.

## Scenario

You have a repository that contains things you do not want to commit, but also do not want to lose:

- local notes
- draft documents
- ignored files
- sensitive configuration
- working material outside normal Git history

You want a local encrypted safety layer for that state.

## Step 1 — initialize the repository

At the repository root:

```bash
arkive init
```

This creates `.ark/` and provisions a vault directory outside the repository.

## Step 2 — inspect the binding

```bash
arkive status
```

Read the output carefully once.

You should understand:

* where `.ark/` lives
* where the vault lives
* how many snapshots exist

That is the core binding model.

## Step 3 — create a snapshot

```bash
arkive snapshot create
```

You will be asked for a passphrase.

At this stage, the most important thing is not speed.
It is trust.

You should know that:

* the snapshot is encrypted
* the payload is outside the repository
* the snapshot is indexed
* the repository stays lightweight

## Step 4 — inspect what was created

```bash
arkive snapshot list
arkive snapshot inspect <snapshot-id>
```

This gives you visibility before you ever test restore.

That matters.

A preservation tool that cannot be inspected easily becomes hard to trust.

## Step 5 — test restore on purpose

Do not wait for an emergency.

Create a destination directory and restore there:

```bash
mkdir -p ./restore-check
arkive snapshot restore <snapshot-id> ./restore-check
```

Testing restore early is one of the best habits you can build with a tool like this.

## What success looks like

A successful first project is not just “the command ran”.

It is this:

* you understand the repository ↔ vault split
* you can create a snapshot deliberately
* you can inspect snapshot metadata
* you can restore into an explicit destination
