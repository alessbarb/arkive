# Vault reference

The vault is the external storage location for Arkive snapshot state.

## Location

By default, the vault lives outside the repository.

Typical examples use a path like:

```text
~/.local/share/arkive/vault/
```

## Per-project directory

Each initialized repository is associated with its own vault directory, typically shaped like:

```text
<project-slug>--<project-id>
```

## Vault contents

A project vault directory usually contains:

* `snapshots/`
* `index.json`
* `metadata/`

## Responsibilities

The vault is responsible for holding:

* encrypted snapshot payloads
* snapshot index state
* snapshot metadata

The repository is responsible only for lightweight local binding and config metadata.
