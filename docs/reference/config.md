# Config reference

Arkive currently keeps project-local configuration inside `.ark/config.json`.

This model is still early, but the intent is already clear.

## Current role of project config

Project config defines repository-specific behavior such as:

- capture mode
- compression mode
- include patterns
- exclude patterns
- encryption metadata choices

## Current default shape

The current default config includes sections like:

- `capture`
- `encryption`

## Design direction

Project config should stay:

- explicit
- readable
- local to the repository
- separate from heavy snapshot storage

It should explain project behavior, not become a second vault.
