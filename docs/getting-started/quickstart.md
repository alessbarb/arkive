# Quickstart

This is the fastest way to understand `arkive`.

## 1. Initialize a repository

Run this at the root of the repository you want to protect:

```bash
arkive init
```

This creates a lightweight `.ark/` directory inside the repository and binds the project to a local vault outside the repository.

## 2. Check the current state

```bash
arkive status
```

You should see:

* repository path
* whether the repo is initialized
* project id
* project slug
* `.ark` location
* vault location
* snapshot count

## 3. Create your first snapshot

```bash
arkive snapshot create
```

You will be prompted for a passphrase.

This command:

* packages the current repository state
* encrypts it locally
* stores the encrypted payload in the external vault
* records snapshot metadata in the index

## 4. List available snapshots

```bash
arkive snapshot list
```

This shows the snapshots known for the current repository.

## 5. Inspect one snapshot

```bash
arkive snapshot inspect <snapshot-id>
```

This prints:

* the snapshot record
* the snapshot manifest

It does not restore anything.

## 6. Restore a snapshot

```bash
arkive snapshot restore <snapshot-id> ./restore-target
```

This restores the selected snapshot into the destination you choose.

`arkive` never silently restores into some hidden location.

## What to remember

If you only remember four things, remember these:

* `.ark/` is lightweight repository metadata
* the vault is outside the repository
* snapshots are encrypted
* restore is always explicit
