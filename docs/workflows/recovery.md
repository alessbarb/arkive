# Recovery workflow

Recovery is where Arkive must be trusted.

## Recommended recovery flow

### 1. Identify the snapshot

```bash
arkive snapshot list
arkive snapshot inspect <snapshot-id>
```

### 2. Choose a safe destination

Create or choose an explicit restore directory.

```bash
mkdir -p ./restore-target
```

### 3. Restore

```bash
arkive snapshot restore <snapshot-id> ./restore-target
```

### 4. Verify restored contents

Check the result before copying anything back into your working repository.

## Why this workflow is explicit

Recovery should be deliberate.

The goal is not “quick magic”.
The goal is “clear restoration with minimal ambiguity”.
