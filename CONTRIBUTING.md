# Contributing to arkive

Thank you for considering contributing to `arkive`.

This document outlines the development model, setup steps, and contribution expectations.

## Project philosophy

Before adding features, protect the core model:

- local-first
- explicit snapshot creation
- explicit restore targets
- restore-first design
- Git complement, never Git replacement
- lightweight repository metadata, heavy state outside the repo
- conservative security model

Examples of things to avoid unless strongly justified:

- hidden automatic snapshots
- background watchers or daemons
- storing heavy snapshot payloads inside `.ark/`
- turning arkive into a second Git history
- introducing optimization before restore behavior is fully trustworthy
- inventing custom cryptographic schemes

## Code of Conduct

Be respectful, provide constructive feedback, and keep discussion focused on technical improvement and product clarity.

## Development setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/labrynx/arkive.git
   cd arkive
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install development dependencies**

   ```bash
   pip install -U pip
   pip install -e .[dev]
   ```

4. **Run the tests**

   ```bash
   pytest
   ```

## Project structure

```text
arkive/
├── docs/               # User and planning documentation
├── src/arkive/         # Main package
│   ├── adapters/       # External boundary helpers (filesystem, git, input)
│   ├── cli/            # Typer CLI (commands, callbacks, presenters, prompts)
│   ├── config/         # Local project/app configuration loading and defaults
│   ├── crypto/         # Encryption primitives, passphrase handling, envelope model
│   ├── domain/         # Core domain models and result objects
│   ├── packaging/      # Archive and manifest construction
│   ├── repository/     # Binding, index, vault, and persistence access
│   ├── services/       # Command orchestration and business logic
│   ├── utils/          # Pure helpers
│   ├── constants.py
│   ├── errors.py
│   └── __main__.py
├── tests/              # Unit and integration tests
└── README.md
```

## Architectural note

The project follows a layered structure:

* **CLI layer** → user input, output, and command wiring
* **Service layer** → orchestration and use-case logic
* **Domain layer** → models, rules, and result shapes
* **Repository layer** → persistence and project/vault access
* **Crypto layer** → encryption and passphrase flow
* **Packaging layer** → archive and manifest construction
* **Utils layer** → pure reusable helpers

This separation matters because `arkive` must remain:

* testable
* explicit
* restore-first
* evolvable toward later storage models without CLI breakage

## Adding a new command

1. **Define the service**

   * add a function in `src/arkive/services/...`
   * inputs must be explicit
   * outputs should use structured result models where appropriate
   * raise `ArkiveError` subclasses for user-facing failures

2. **Add the CLI command**

   * add the Typer command in `src/arkive/cli/commands/...`
   * use arguments and options explicitly
   * do not hide important behavior behind prompts unless the command is intentionally interactive
   * use presenters for formatting

3. **Update documentation**

   * update `README.md` if workflows change
   * update docs and planning docs if the command changes the product model
   * update roadmap or backlog if the change affects release scope

4. **Write tests**

   * unit tests for service and presenters
   * integration tests for CLI flow
   * failure-path coverage where behavior matters

## Special guidance for snapshot features

Snapshot-related work must follow these rules:

* snapshot creation must be explicit
* restore destination must be explicit
* restore behavior must never depend on hidden defaults
* storage optimization must not outrank restore confidence
* repository-local metadata must stay lightweight
* snapshot payloads must stay outside the repository

A good litmus test is:

> Does this change make restore safer, clearer, or more trustworthy?

If not, it probably does not belong yet.

## Special guidance for Git-related features

Git-related features must preserve the product boundary:

* Git remains the system of shared project history
* Arkive remains the system of private local state preservation

Do not introduce:

* branch-like Arkive concepts
* merge semantics
* collaborative history features
* workflows that blur the boundary between Git and Arkive

## Code style

* Use `ruff format` for formatting
* Use `ruff check` for linting
* Keep functions small and explicit
* Prefer stable result objects over ad-hoc dicts where possible
* Avoid hidden convenience behavior
* Use docstrings when they clarify behavior, side effects, or failure conditions

## Running tests

* Run the full suite:

  ```bash
  pytest
  ```

* Run a specific test file:

  ```bash
  pytest tests/unit/services/test_snapshot_create_service.py
  ```

* Run with coverage:

  ```bash
  pytest --cov=arkive
  ```

## Submitting changes

1. Create a branch from `main` with a descriptive name
2. Make the change with tests
3. Ensure linting, formatting, typing, and tests pass
4. Commit with a clear imperative message
5. Open a pull request explaining what changed and why

When a change alters:

* snapshot semantics
* restore behavior
* vault structure
* Git complement framing
* encryption behavior

explain that explicitly in the pull request.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

Thank you for helping make `arkive` better.
