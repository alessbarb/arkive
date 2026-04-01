# Snapshots reference

This page focuses on snapshot behavior.

## Snapshot identifier

Each snapshot has an id that uniquely identifies it inside the project vault.

## Snapshot record

A snapshot record contains metadata such as:

- snapshot id
- project id
- creation time
- capture mode
- compression
- payload path
- payload size

## Snapshot manifest

A snapshot manifest provides additional structured metadata associated with the snapshot.

## Current model

At the moment, snapshots are:

- full
- encrypted
- individually restorable

## Current limitations

The current model does not yet provide:

- deduplicated object storage
- snapshot diffing
- selective restore by path
- retention policies
- background snapshot automation

That is intentional.
