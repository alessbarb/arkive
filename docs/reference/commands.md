# Commands reference

This page describes the current CLI surface of `arkive`.

## `arkive init`

Initialize the current repository for Arkive.

### Usage

```bash
arkive init [PATH]
```

### What it does

* creates `.ark/`
* writes repository-local binding metadata
* provisions the external vault layout

### Notes

Initialization is explicit.
It should fail clearly if the repository is already initialized.

---

## `arkive status`

Show the current Arkive status of a repository.

### Usage

```bash
arkive status [PATH]
```

### What it shows

* repository path
* initialization state
* project id
* project slug
* `.ark` path
* vault path
* snapshot count
* capture mode
* compression mode

---

## `arkive snapshot create`

Create an encrypted snapshot.

### Usage

```bash
arkive snapshot create [PATH]
```

### What it does

* packages repository state
* encrypts the payload
* stores it in the vault
* writes metadata and index records

---

## `arkive snapshot list`

List snapshots for the current repository.

### Usage

```bash
arkive snapshot list [PATH]
```

---

## `arkive snapshot inspect`

Inspect one snapshot record and manifest.

### Usage

```bash
arkive snapshot inspect <SNAPSHOT_ID> [PATH]
```

---

## `arkive snapshot restore`

Restore one snapshot into an explicit destination directory.

### Usage

```bash
arkive snapshot restore <SNAPSHOT_ID> <DESTINATION_DIR> [PATH]
```

### Important

Restore does not silently pick a destination.
You must choose it.
