# Debugging and Troubleshooting Python Applications: Student Grade Management System

## Internship / Task Objective
The Week 2 internship task was to build practical Python debugging skills by reproducing realistic defects, identifying root causes, applying focused fixes, and validating the results with repeatable tests.

## Project Overview
The application is a command-line student grade manager. It supports adding, searching, updating, deleting, listing students, calculating an average, finding the top scorer, and persisting records in JSON.

## Tools and Technologies
Python 3.10+, standard-library `unittest`, JSON, Git, Linux command line, and Microsoft Word-compatible DOCX output.

## Application Architecture
- **Model:** `student.py` validates and serializes student records.
- **Storage:** `storage.py` reads and writes JSON and handles load failures.
- **Business logic:** `student_manager.py` coordinates CRUD operations, calculations, validation, and persistence.
- **Interface:** `main.py` provides the interactive menu.

The repository keeps `buggy_version` as the intentionally defective baseline and `fixed_version` as the corrected implementation.

## Bug Identification Table
| # | Defect in buggy_version | Corrective result in fixed_version |
|---|---|---|
| 1 | Average uses integer division | Uses true division |
| 2 | Search uses the wrong comparison | Matches IDs with equality |
| 3 | Marks above 100 are accepted | Enforces 0 through 100 |
| 4 | Updates are not persisted | Saves updates and rolls back failed saves |
| 5 | Corrupt JSON crashes loading | Returns an empty dataset safely |
| 6 | Duplicate IDs are accepted | Rejects duplicates without changing the original |
| 7 | Whitespace menu input is rejected | Strips input before validation |

## Debugging Methodology
Each bug was reproduced, compared against expected behavior, traced to its controlling function, fixed locally, and covered by automated verification. Git history was used during the final audit to restore the original defective baseline and preserve before-and-after evidence.

## Before and After
Before debugging, the baseline could truncate averages, return the wrong search result, accept invalid marks, lose updates after reload, crash on malformed JSON, create ambiguous duplicate IDs, and reject valid menu input with spaces. After debugging, the fixed implementation resolves each behavior while preserving the modular design. Duplicate insertion now leaves the original record unchanged and leaves exactly one record.

## Testing and Verification
The required suite is:

```bash
python -m unittest discover -s tests -v
```

It covers model validation, storage, manager operations, CLI input, persistence, corrupted JSON, and duplicate IDs. Final checks also cover fixed-version startup and clean exit, reload persistence, average and top-scorer calculations, and version separation.

## Results
All 24 discovered tests pass. The fixed version performs add, search, update, delete, average, and top-scorer operations correctly. The buggy version remains a reproducible seven-bug baseline. The report itself is a valid non-empty DOCX archive.

## Challenges and Solutions
The principal challenge was detecting accidental version drift: the duplicate guard had been placed in the buggy directory while tests imported that directory. Git history identified the original defective snapshots. The solution was to restore the seven defects in `buggy_version`, add the missing guard to `fixed_version`, and point regression tests at the corrected implementation.

## Conclusion
The project demonstrates an evidence-based debugging cycle with clear architecture, reproducible defects, localized corrections, automated regression protection, and documentation that accurately distinguishes the before and after implementations.

## GitHub / Repository Reference
Repository: `https://github.com/Koushik23R/week2_debugging_project`
