# Debugging and Development Log

## Version Separation
The repository intentionally keeps two implementations. `buggy_version` is the original seven-bug baseline restored from the bug-introduction history. `fixed_version` contains the corrections. The regression suite imports `fixed_version`.

## Method
For each issue, the workflow was: reproduce the behavior, compare expected and actual results, locate the controlling function, identify the root cause, make a localized fix, and verify with unittest and manual checks.

## Bug Fix Record

### Bug 1: Average calculation
The baseline used floor division and returned 91 for marks 90, 95, and 90. The fixed manager uses true division and returns approximately 91.67.

### Bug 2: Student search
The baseline returned a student whose ID differed from the requested ID. The fixed manager compares IDs for equality and returns `None` when there is no match.

### Bug 3: Marks validation
The baseline accepted marks through 1000. The fixed model enforces the inclusive range 0 through 100, including rejecting 101 and negative values.

### Bug 4: Persistence
The baseline changed marks only in memory and returned success before saving. The fixed manager saves updated records and restores the old value when saving fails; reload tests confirm durability.

### Bug 5: Corrupted JSON
The baseline allowed `JSONDecodeError` to escape during startup. The fixed storage layer catches it and returns an empty list while preserving valid-file loading.

### Bug 6: Duplicate IDs
The baseline appended every new record. The fixed manager checks for an existing ID before creating the new record. The regression test proves first insertion succeeds, the duplicate is rejected, the original name and marks remain unchanged, and one record remains; search, update, and delete are also verified.

### Bug 7: CLI whitespace
The baseline validated the raw menu string. The fixed CLI strips whitespace before `isdigit()`, so ` 8 ` exits cleanly.

## Testing and Final Audit
The suite contains component tests and regression tests for all seven corrections. The required command is:

```bash
python -m unittest discover -s tests -v
```

The final audit also checks CLI startup and clean exit, persistence after reload, corrupted JSON handling, all manager operations, version separation against Git history, and the generated DOCX archive.
