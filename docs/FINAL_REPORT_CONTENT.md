# Final Internship Report Content (Week 2)

## Title
Debugging and Troubleshooting Python Applications: Student Grade Management System

## 1. Introduction
This project was completed as part of the internship Week 2 objective: building practical debugging and troubleshooting skills in Python. The work focused on identifying realistic defects, reproducing them reliably, analyzing root causes, implementing minimal fixes, and validating each fix through repeatable automated tests.

The target application is a command-line Student Grade Management System built using a modular Python architecture.

## 2. Project Architecture
The codebase is organized into clearly separated modules:
- **Model Layer (`student.py`)**: student data structure, input validation, and serialization helpers.
- **Storage Layer (`storage.py`)**: JSON read/write persistence with failure handling.
- **Business Layer (`student_manager.py`)**: student operations, calculations, update/remove logic, and data coordination.
- **Interface Layer (`main.py`)**: menu-driven CLI and input interaction.

This separation reduced debugging complexity and supported targeted fixes.

## 3. Debugging Methodology
For each issue, the same workflow was used:
1. Reproduce the bug with a clear scenario.
2. Confirm expected vs actual behavior.
3. Isolate the fault to module and function.
4. Identify exact root cause in code.
5. Apply a minimal, localized fix.
6. Verify with automated tests and repeat execution.
7. Document evidence in bug report and debug log.

## 4. Bug Summary and Resolutions
### Bug 1: Average calculation incorrect
- **Root cause:** floor division (`//`) truncated decimals.
- **Fix:** switched to true division (`/`).
- **Result:** class average now returns correct decimal values.

### Bug 2: Student search incorrect
- **Root cause:** wrong comparison condition in `find_student()`.
- **Fix:** compare `student.student_id == student_id`.
- **Result:** search returns correct record or `None`.

### Bug 3: Invalid marks accepted
- **Root cause:** marks range allowed `0-1000`.
- **Fix:** restored correct validation range `0-100`.
- **Result:** invalid marks are properly rejected.

### Bug 4: Updated marks not persisted
- **Root cause:** `update_marks()` returned success before saving.
- **Fix:** call `save_students()` before success return; rollback on failure.
- **Result:** updated marks persist across restarts.

### Bug 5: Crash on corrupted JSON
- **Root cause:** missing `JSONDecodeError` handling during load.
- **Fix:** added explicit `except json.JSONDecodeError` fallback.
- **Result:** corrupted JSON now safely loads as empty dataset.

### Bug 6: Duplicate IDs accepted
- **Root cause:** missing uniqueness check before insert.
- **Fix:** reject add when `find_student(student_id)` already exists.
- **Result:** duplicate IDs are blocked.

### Bug 7: CLI whitespace input rejected
- **Root cause:** menu input was not stripped before `isdigit()`.
- **Fix:** use `input(...).strip()`.
- **Result:** valid options with surrounding spaces are accepted.

## 5. Automated Testing
The project now includes an organized unittest suite split across separate files by responsibility and bug regression coverage.

### Component Tests
- `tests/test_student.py`
- `tests/test_storage.py`
- `tests/test_student_manager.py`

### Regression Tests
- `tests/test_buggy_marks_validation.py`
- `tests/test_buggy_persistence_bug.py`
- `tests/test_buggy_json_handling_bug.py`
- `tests/test_buggy_duplicate_id_bug.py`
- `tests/test_buggy_cli_input_bug.py`

### Final Verification
- Executed command: `python -m unittest discover -s tests -v`
- Result: **24/24 tests passed**.

## 6. Code Quality and Maintainability
The final fixes were intentionally minimal and localized to avoid unnecessary redesign. Existing architecture and beginner-friendly readability were preserved throughout the debugging process.

Key quality outcomes:
- clearer reliability boundaries,
- improved error handling,
- strong regression protection,
- complete traceability from bug report to fix verification.

## 7. Internship Outcome
This submission demonstrates end-to-end debugging competency:
- bug identification,
- root cause analysis,
- practical troubleshooting,
- clean corrective coding,
- structured technical documentation,
- automated validation and professional presentation.

The repository is now submission-ready for Week 2 evaluation.
