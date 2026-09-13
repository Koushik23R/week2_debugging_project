# Bug Report

## Version Scope
`buggy_version` is the intentionally defective baseline. `fixed_version` is the corrected implementation. Each status below means the defect is resolved in `fixed_version` while remaining reproducible in `buggy_version` as preserved evidence.

## Summary
All seven documented bugs are reproducible in the baseline and corrected in the fixed version.

| ID | Title | Type | Status |
|---|---|---|---|
| 1 | Average calculation uses integer division | Logic error | Closed in fixed_version |
| 2 | Student search uses the wrong comparison | Conditional logic | Closed in fixed_version |
| 3 | Marks validation allows values above 100 | Validation | Closed in fixed_version |
| 4 | Updated marks are not persisted | Persistence error | Closed in fixed_version |
| 5 | Corrupted JSON causes a crash | File I/O error | Closed in fixed_version |
| 6 | Duplicate student IDs are accepted | Business logic | Closed in fixed_version |
| 7 | Menu input with whitespace is rejected | Input validation | Closed in fixed_version |

## Bug 1: Average calculation uses integer division
**Bug type:** Logic error

**Steps to reproduce:** Add students with marks 90, 95, and 90, then calculate the average in `buggy_version`.

**Expected behavior:** The average is approximately 91.67.

**Actual behavior:** The baseline returns 91 because the fractional part is discarded.

**Root cause:** `calculate_average()` uses floor division (`//`).

**Resolution:** `fixed_version/student_manager.py` uses true division (`/`).

**Status:** Closed in `fixed_version`; reproducible in `buggy_version`.

## Bug 2: Student search uses the wrong comparison
**Bug type:** Conditional logic

**Steps to reproduce:** Add two students, then search for the second student's ID in `buggy_version`.

**Expected behavior:** The student with the requested ID is returned, or `None` if no match exists.

**Actual behavior:** The baseline returns the first student whose ID is different from the requested ID.

**Root cause:** `find_student()` uses `student.student_id != student_id` instead of equality.

**Resolution:** `fixed_version/student_manager.py` checks `student.student_id == student_id`.

**Status:** Closed in `fixed_version`; reproducible in `buggy_version`.

## Bug 3: Marks validation allows values above 100
**Bug type:** Validation

**Steps to reproduce:** Create a student with marks `250` in `buggy_version`.

**Expected behavior:** A `ValueError` is raised because marks must be 0 through 100.

**Actual behavior:** The baseline accepts the student.

**Root cause:** The baseline validates against `0-1000`.

**Resolution:** `fixed_version/student.py` enforces `0 <= marks <= 100`.

**Status:** Closed in `fixed_version`; reproducible in `buggy_version`.

## Bug 4: Updated marks are not persisted
**Bug type:** Persistence error

**Steps to reproduce:** Add a student, update marks, create a new manager, and reload the student in `buggy_version`.

**Expected behavior:** The new marks remain after reload.

**Actual behavior:** The baseline reports success but reloads the old marks.

**Root cause:** The baseline returns `True` after the in-memory assignment without calling `save_students()`.

**Resolution:** `fixed_version/student_manager.py` saves the list and rolls back the in-memory value if saving fails.

**Status:** Closed in `fixed_version`; reproducible in `buggy_version`.

## Bug 5: Corrupted JSON causes a crash
**Bug type:** File I/O error

**Steps to reproduce:** Replace the data file contents with invalid JSON and initialize the manager in `buggy_version`.

**Expected behavior:** Loading fails safely and returns an empty dataset.

**Actual behavior:** `JSONDecodeError` escapes from the baseline loader.

**Root cause:** The baseline does not catch `json.JSONDecodeError`.

**Resolution:** `fixed_version/storage.py` catches the decode error and returns `[]`.

**Status:** Closed in `fixed_version`; reproducible in `buggy_version`.

## Bug 6: Duplicate student IDs are accepted
**Bug type:** Business logic error

**Steps to reproduce:** Add ID `101` twice with different names or marks in `buggy_version`, then search or delete by ID.

**Expected behavior:** The first insert succeeds; the duplicate is rejected, the original remains unchanged, and exactly one record exists.

**Actual behavior:** The baseline accepts both records, so ID-based operations can act on the first matching record only.

**Root cause:** The baseline `add_student()` has no uniqueness check before appending.

**Resolution:** `fixed_version/student_manager.py` rejects an existing ID before constructing or appending a replacement. Tests verify the original record, count, search, update, and delete behavior.

**Status:** Closed in `fixed_version`; reproducible in `buggy_version`.

## Bug 7: Menu input with whitespace is rejected
**Bug type:** Input validation error

**Steps to reproduce:** Enter ` 8 ` at the main menu in `buggy_version`.

**Expected behavior:** The input is trimmed and the application exits cleanly.

**Actual behavior:** The baseline rejects the otherwise valid numeric input.

**Root cause:** The baseline calls `isdigit()` on the untrimmed input.

**Resolution:** `fixed_version/main.py` strips menu input before validation.

**Status:** Closed in `fixed_version`; reproducible in `buggy_version`.
