# Week 2 Internship Project: Student Grade Management System

## Objective
This project demonstrates a complete Python debugging workflow: reproduce defects, isolate root causes, apply minimal fixes, test the corrected behavior, and document the evidence.

## Version Separation
- `buggy_version/` is the intentionally defective baseline and preserves all seven documented bugs.
- `fixed_version/` is the corrected implementation after debugging.
- `tests/` imports `fixed_version` and verifies the corrected behavior.

## Features
The CLI can add, view, search, update, and delete students, calculate the class average, and find the top scorer. Records persist in JSON.

## Architecture
- `student.py`: model, validation, and serialization
- `storage.py`: JSON persistence and load-error handling
- `student_manager.py`: business rules and student operations
- `main.py`: menu-driven command-line interface

## Tools
Python 3.10+, standard-library `unittest`, Git, JSON, and Microsoft Word report output (`.docx`).

## Run
```bash
python fixed_version/main.py
python -m unittest discover -s tests -v
```

Run `python buggy_version/main.py` only when reproducing the documented baseline defects.

## Documented Bugs
1. Integer average calculation
2. Incorrect student search comparison
3. Marks above 100 accepted
4. Updated marks not persisted
5. Corrupted JSON crashes loading
6. Duplicate IDs accepted
7. Whitespace menu input rejected

The complete reproduction details, expected and actual behavior, root causes, resolutions, and statuses are in `docs/BUG_REPORT.md`. The chronological work log is in `docs/DEBUG_LOG.md`, and the Word-report source is in `docs/FINAL_REPORT_CONTENT.md`.

## Verification
The final required suite is `python -m unittest discover -s tests -v`; it covers the corrected fixed version and passes all 24 tests.
