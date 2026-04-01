# Platforms

Arkive is designed as a local-first command-line tool with cross-platform intentions, but current behavior should still be read pragmatically.

## Current assumptions

Arkive assumes:

- a local filesystem
- a user-controlled working environment
- normal file and directory permissions
- a Python runtime compatible with the supported versions

## Current storage examples

Documentation examples typically use Unix-style paths such as:

```text
~/.local/share/arkive/
```

That reflects the current primary development environment.

## Important note

Platform-neutral design is a goal, but filesystem behavior, permissions, and path conventions may still vary by system.

When in doubt, test:

* initialization
* snapshot creation
* restore

on the target platform directly.
