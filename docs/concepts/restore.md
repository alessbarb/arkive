# Restore

Restore is the moment of truth for a preservation tool.

That is why `arkive` treats restore as a first-class concept, not as an afterthought.

## What restore means

Restore means:

- select a snapshot
- decrypt it locally
- extract it
- materialize it into a destination you choose

## Explicit destination

One of the most important rules in Arkive is this:

> restore targets must be explicit

The tool should not silently choose one for you.

That protects the user from surprises and makes restore easier to reason about.

## Why restore-first matters

A lot of systems optimize snapshot creation early.

Arkive takes the opposite view:

- recoverability matters more than cleverness
- clarity matters more than convenience
- trust matters more than compression tricks

## Best practice

Do not wait for a bad day to test restore.

Create a snapshot, then test a restore into a throwaway directory.

That habit will tell you more about the health of the system than a hundred assumptions.
