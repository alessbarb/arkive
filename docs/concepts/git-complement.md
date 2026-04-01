# Git complement

`arkive` complements Git.
It does not replace it.

This boundary is one of the most important design decisions in the project.

## What Git is good at

Git is excellent at:

- shared history
- collaboration
- branching
- merging
- code review
- long-lived project evolution

That is not what Arkive is trying to reimplement.

## What Git is not meant to keep

Even in healthy repositories, there is often state people do not want to commit:

- local notes
- drafts
- `.env` files
- ignored but useful files
- sensitive workspace material
- private project context

That is the space where Arkive becomes useful.

## The one-line framing

A good framing is this:

> Git keeps what the project shares. Arkive keeps what the developer keeps local.

## What Arkive should avoid becoming

Arkive should not become:

- a second Git history
- a branching system
- a collaboration layer
- a merge engine
- a review workflow

Once it starts doing those things, the product gets muddy fast.

## Why this matters

Without this boundary, Arkive risks becoming “backup-ish but unclear”.

With this boundary, the value is obvious:

- Git for shared project history
- Arkive for private local preservation
