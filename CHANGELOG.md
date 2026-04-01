# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added

* initial local-first `arkive` CLI foundation
* repository initialization flow with `arkive init`
* repository status inspection with `arkive status`
* snapshot lifecycle commands:
  * `arkive snapshot create`
  * `arkive snapshot list`
  * `arkive snapshot inspect`
  * `arkive snapshot restore`
* repository-local `.ark/` metadata model
* external vault layout for snapshot storage
* snapshot index persistence
* snapshot manifest persistence
* encrypted snapshot payloads using:
  * `scrypt` for key derivation
  * `AES-256-GCM` for authenticated encryption
* archive packaging helpers for full snapshot creation and restore
* typed domain models for project, snapshot, restore, status, and vault layout
* layered package structure across:
  * CLI
  * services
  * domain
  * repository
  * crypto
  * packaging
  * utils
* reusable CLI helpers for arguments and line-based output
* baseline integration tests for:
  * init/status
  * snapshot create
  * snapshot list
  * snapshot inspect
  * snapshot restore
* baseline unit test structure across package layers

---

### Changed

* aligned CLI output around presenters and CLI-local output helpers
* removed cross-layer output drift by moving terminal emission responsibility into the CLI layer
* refined package exports through minimal `__init__.py` files with clearer public surfaces
* normalized app version resolution through `importlib.metadata`
* tightened archive extraction behavior using explicit safe tar extraction filtering
* improved typing across services, repository helpers, and manifest handling
* simplified output architecture by preferring:
  * presenters for rendering
  * CLI helpers for emission
  * pure utils for non-UI helpers

---

### Deprecated

* nothing yet

---

### Removed

* legacy-style shared output helper usage from `utils/output.py`
* duplicated and rescued code fragments inherited from earlier `envctl` exploration
* unnecessary CLI callback/result placeholder patterns that did not contribute to the current model

---

### Fixed

* pytest collection issues caused by duplicate test module names
* test passphrase prompting by isolating `getpass` patching to test scope only
* mypy issues related to:
  * generic typing
  * literal narrowing
  * config payload typing
  * tarfile mode typing
* Ruff issues around:
  * import order
  * callable typing
  * command argument definitions
* tar extraction deprecation warning by using a safe extraction filter
* CLI command wiring and import/export consistency across subpackages

---

### Security

* encrypted snapshots are now stored outside the repository by default
* repository-local state remains lightweight and non-secret
* restore remains explicit and destination-driven
* tar extraction behavior was hardened to reduce unsafe archive extraction risk

---

### Build

* project now passes:
  * `ruff check`
  * `ruff format`
  * `mypy`
  * `pytest`
* package structure and exports were stabilized for future growth

---

### Notes

* this is the first real alpha foundation of `arkive`
* the focus so far has been trust, explicitness, and architectural clarity
* future work should continue to protect the product boundary:
  * Git manages shared history
  * Arkive preserves private local state