# Daily workflow

This is the normal day-to-day usage model for Arkive.

## Typical flow

### Check project state

```bash
arkive status
```

### Create a snapshot before risky local changes

```bash
arkive snapshot create
```

Examples:

* before a large refactor
* before cleaning ignored files
* before deleting local drafts
* before reorganizing internal notes

### Inspect what exists

```bash
arkive snapshot list
arkive snapshot inspect <snapshot-id>
```

## Practical habit

A good default habit is:

> snapshot before destructive local cleanup

That is where Arkive tends to pay for itself.
