# arkive

> Arkive is not about storing everything.
> It is about preserving what should not be lost.

**Git keeps the history you share. arkive preserves the local state you keep private.**

[![CI](https://github.com/labrynx/arkive/actions/workflows/ci.yml/badge.svg)](https://github.com/labrynx/arkive/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/labrynx/arkive/blob/main/LICENSE)

---

## What is this?

Most Git repositories already have a history.

But that history usually excludes exactly the things developers still do not want to lose:

- private local notes
- `.env` files
- internal drafts
- ignored but valuable files
- workspace state that should never be committed

`arkive` is a local-first encrypted snapshot tool for that gap.

It gives you a simple model:

- **the repository** keeps shared project history through Git
- **`.ark/`** keeps lightweight local arkive metadata
- **the vault** stores encrypted snapshots outside the repository
- **restore** rebuilds a chosen local state explicitly into a chosen destination

So you get:

- no sensitive local state in Git
- no hidden background sync
- no guesswork about where snapshots live
- explicit encrypted local preservation

---

## Install

```bash
pip install arkive
```

Or from source:

```bash
git clone https://github.com/labrynx/arkive
cd arkive
pip install -e .
```

---

## Quickstart

```bash
arkive init
arkive status
arkive snapshot create
arkive snapshot list
arkive snapshot inspect <snapshot-id>
arkive snapshot restore <snapshot-id> ./restore-target
```

---

## What problem does arkive solve?

Git is already excellent at:

* source history
* collaboration
* commits
* branching
* reviewable changes

But Git is not meant to be the canonical home for:

* private local-only documentation
* `.env` files
* ignored but important material
* sensitive working files
* personal notes tied to a project
* local workspace state you do not want to publish

`arkive` exists for that boundary.

It is not a Git replacement.

It is a **local encrypted preservation layer** for private workspace state.

---

## How it works

The model is simple:

* **Git** manages shared project history
* **`.ark/`** binds the repository to arkive metadata
* **vault** stores encrypted snapshots outside the repo
* **snapshot** captures a frozen local state
* **restore** recreates that state explicitly

Think of it like this:

> Git tracks what you share. Arkive preserves what you keep local.

---

## Repository vs vault

Inside the repository:

```text
repo/
└── .ark/
    ├── binding.json
    └── config.json
```

Outside the repository:

```text
~/.local/share/arkive/vault/
└── <project-slug>--<project-id>/
    ├── snapshots/
    ├── index.json
    └── metadata/
```

This separation matters because:

* snapshot payloads may be large
* snapshots may contain sensitive material
* repository-local storage creates commit risk
* the repository should stay clean and portable

---

## Snapshot model

In early versions, snapshots are:

* full
* encrypted
* independent
* explicitly created

That means:

* each snapshot can be restored on its own
* snapshots do not depend on each other
* restore stays simple and trustworthy

This is intentionally conservative.

`arkive` prefers restore confidence over clever storage tricks.

---

## Why not just tar + encryption?

Because the value is not only in packing files.

The value is in having a consistent local model:

* explicit project binding
* stable vault layout
* repeatable snapshot creation
* inspectable snapshot index
* restore-first behavior
* encrypted local state outside the repository

`arkive` is not trying to be a general backup engine.
It is trying to be a trustworthy local preservation layer for project state.

---

## Common commands

```bash
# initialize and inspect repository state
arkive init
arkive status

# create and inspect snapshots
arkive snapshot create
arkive snapshot list
arkive snapshot inspect <snapshot-id>

# restore
arkive snapshot restore <snapshot-id> <destination-dir>
```

---

## Design principles

* Local-first: no required remote system
* Explicit: no hidden snapshots or background processes
* Restore-first: recoverability beats optimization
* Conservative security: standard primitives only
* Git complement: arkive preserves what Git should not keep
* Lightweight repository metadata: heavy snapshot data stays outside the repo

---

## Security model

* Snapshots are encrypted before being stored in the vault
* The repository keeps only lightweight local metadata in `.ark/`
* Sensitive workspace material should not be exposed outside encrypted payloads unnecessarily
* Restore is explicit and target-driven
* Arkive assumes a trusted local machine

Important:

> If the machine is compromised, local private state is compromised.

`arkive` is not a cloud secrets platform.
It is a local encrypted preservation layer.

---

## Roadmap direction

Early releases focus on:

* trustworthy encrypted snapshots
* explicit restore
* stable vault and metadata model
* clear project binding

Later releases may introduce:

* configurable capture policy
* Git-aware capture modes
* file-level deduplicated logical snapshots

But only after the restore and trust model is solid.

---

## Documentation

* [Planning README](https://github.com/labrynx/arkive/blob/main/docs/planning/arkive/README.md)
* [Roadmap](https://github.com/labrynx/arkive/blob/main/docs/planning/arkive/roadmap.md)
* [Internal roadmap](https://github.com/labrynx/arkive/blob/main/docs/planning/arkive/roadmap-internal.md)
* [Storage model](https://github.com/labrynx/arkive/blob/main/docs/planning/arkive/design/storage-model.md)
* [Git complement model](https://github.com/labrynx/arkive/blob/main/docs/planning/arkive/design/git-complement.md)
