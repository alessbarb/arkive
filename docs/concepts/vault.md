# Vault

The vault is the external storage location where Arkive keeps snapshot state.

It lives outside the repository on purpose.

## Why the vault is external

The vault is not inside `.ark/` because snapshot storage has different properties from repository-local metadata.

Snapshot storage may be:

- sensitive
- large
- private
- unsuitable for accidental Git inclusion

That is why `.ark/` stays lightweight and the vault stays external.

## Typical layout

A vault usually looks like this:

```text
~/.local/share/arkive/vault/<project-slug>--<project-id>/
├── snapshots/
├── index.json
└── metadata/
```

## What lives there

### `snapshots/`

Encrypted payload files.

### `index.json`

The list of known snapshots for the project.

### `metadata/`

Additional per-snapshot metadata such as manifests.

## What the vault is not

The vault is not:

* a Git repository
* a cloud sync layer
* a collaboration service
* a magic black box

It is local structured storage for encrypted preserved state.

## Practical rule

If `.ark/` is the local binding layer, the vault is the real storage layer.

That distinction should stay clear in both code and docs.
