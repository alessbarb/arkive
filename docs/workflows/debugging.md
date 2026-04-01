# Debugging workflow

When something feels wrong, keep the debugging flow simple.

## Check initialization state

```bash
arkive status
```

If the repository is not initialized, snapshot commands should not be expected to work.

## Inspect repository-local metadata

Look at:

```text
.ark/binding.json
.ark/config.json
```

These files explain how the repository is currently bound.

## Inspect vault metadata

Look at:

* `index.json`
* snapshot manifest files under `metadata/`

This helps distinguish:

* missing snapshot problems
* broken metadata problems
* restore target problems

## Test restore into a throwaway directory

Do not debug restore by targeting a valuable working directory first.

Use a scratch destination and inspect the result there.
