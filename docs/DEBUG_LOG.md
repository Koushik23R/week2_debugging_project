# Debugging & Development Log

This document records the development progress, implementation decisions, verification steps, and debugging activities performed throughout the project.

---

## Phase 1 – Project Initialization

**Date:** 2026-08-31

### Work Completed
- Created the project repository.
- Organized the project into separate directories for:
  - `buggy_version`
  - `fixed_version`
  - `tests`
  - `docs`
- Added initial project files:
  - `README.md`
  - `requirements.txt`
  - `report.docx`
  - `.gitignore`

### Verification
- Confirmed the project structure was created successfully.
- Initialized Git repository.
- Made the initial commit.

### Outcome
The project structure is ready for implementation.

---

## Phase 2.1 – Project Planning and Architecture

**Date:** 2026-08-31

### Work Completed
- Selected **Student Grade Management System (CLI)** as the project.
- Defined application objectives.
- Planned application features.
- Designed modular architecture.
- Documented the initial project roadmap.
- Updated the README with the project overview.

### Verification
- Reviewed the planned folder structure.
- Confirmed that responsibilities of each module were clearly separated.

### Outcome
A clear development plan and modular architecture were established before implementation.

---

## Phase 2.2 – Student Model

**Date:** 2026-09-03

### Work Completed
- Implemented the `Student` class.
- Added validation for:
  - Student name
  - Marks (0–100)
- Implemented:
  - `to_dict()`
  - `from_dict()`
  - `__str__()`
- Added timestamps using `datetime`.

### Verification
- Successfully created student objects.
- Verified dictionary serialization.
- Verified object reconstruction from dictionaries.
- Confirmed invalid names raise `ValueError`.
- Confirmed invalid marks raise `ValueError`.

### Outcome
The `Student` model is complete, tested manually, and ready for integration with the storage layer.

## Phase 2.3 – Storage Layer

**Date:** 2026-09-03

### Work Completed
- Implemented JSON persistence.
- Added save and load functions.
- Used Student serialization/deserialization methods.
- Implemented error handling for missing, empty, and corrupted JSON files.

### Verification
- Successfully saved student records.
- Successfully reloaded student records.
- Verified graceful handling of missing files.
- Verified graceful handling of empty files.
- Verified graceful handling of corrupted JSON.

### Outcome
The storage layer is complete and ready for integration with the Student Manager.

## Phase 2.4 – Student Manager

**Date:** 2026-09-03

### Work Completed
- Implemented the StudentManager class.
- Added student management operations.
- Integrated the storage layer.
- Implemented average calculation and topper identification.

### Verification
- Verified add, remove, search, and update operations.
- Confirmed data persistence after restarting the manager.
- Verified average calculation and top student retrieval.

### Outcome
The business logic layer is complete and ready to be connected to the command-line interface.

## Phase 2.5 – Command Line Interface

**Date:** 2026-09-04

### Work Completed
- Implemented the interactive CLI.
- Added menu-driven navigation.
- Connected all options to the StudentManager.
- Implemented input validation and friendly error messages.

### Verification
- Verified all menu operations.
- Confirmed invalid inputs are handled gracefully.
- Confirmed application exits cleanly.
- Verified persistence after restarting.

### Outcome
The Student Grade Management System is now fully functional and ready to be used as the baseline application before introducing intentional bugs.

## Phase 3 – Buggy Version

**Date:** 2026-09-04

### Work Completed
- Created a baseline copy of the working application.
- Verified that the copied version behaves identically to the fixed version.
- Prepared the project for controlled bug introduction.

### Verification
- Successfully executed the copied application.
- Confirmed identical functionality before introducing defects.

### Outcome
A stable baseline for the debugging phase has been established.

## Phase 3.1 – Bug Set 1

**Date:** 2026-09-07

### Work Completed
- Introduced three intentional software defects.
- Verified that each bug could be reproduced.
- Created the initial bug report.

### Verification
- Confirmed incorrect average calculation.
- Confirmed incorrect search behavior.
- Confirmed invalid marks were accepted.

### Outcome
The first set of reproducible bugs is ready for systematic debugging.

## Phase 3.2 – Bug Set 2

**Date:** 2026-09-07

### Work Completed
- Introduced four additional defects.
- Verified reproducible persistence, file handling, business logic, and CLI input issues.
- Updated the bug report with all newly discovered defects.

### Verification
- Confirmed updated marks are not persisted.
- Confirmed corrupted JSON causes an application failure.
- Confirmed duplicate IDs are accepted.
- Confirmed menu input with whitespace is mishandled.

### Outcome
Seven documented, reproducible bugs are now available for the debugging phase.

---

## Phase 4 – Debugging & Troubleshooting

**Date:** 2026-09-08

### Investigation
- Reproduced the average calculation defect in `buggy_version/student_manager.py`.
- Confirmed the root cause was floor division in `calculate_average()`.
- Verified the bug affected the output value without changing the surrounding student logic.

### Fix Applied
- Updated the average calculation to use true division (`/`) so the result remains a floating-point value.
- Kept the change limited to the average calculation and did not modify unrelated manager methods.

### Verification
- Ran the calculation with representative marks and confirmed the result is `91.67`.
- Rechecked the module to ensure the original bug no longer reproduces.

### Outcome
- The average value now matches the expected decimal result and the debugging phase for Bug 1 is complete.

## Phase 4.2 – Bug 2 Resolution

**Date:** 2026-09-08

### Investigation
- Reproduced the student search defect in `buggy_version/student_manager.py`.
- Confirmed the comparison in `find_student()` was using the wrong value, causing the method to return the wrong record instead of the matching student.

### Fix Applied
- Corrected the condition in `find_student()` to return a student only when `student.student_id == student_id`.
- Kept the fix limited to the search logic and did not alter any unrelated manager behavior.

### Verification
- Searched for student ID `102` and confirmed the method returns the correct student record: `ID:102 | Bob | Marks:91`.
- Searched for a missing student ID and confirmed the result is `Student not found.`

### Outcome
- The student search now returns the correct record and Bug 2 is resolved.

## Phase 4.3 – Bug 3 Resolution

**Date:** 2026-09-10

### Investigation
- Reproduced the marks validation defect in `buggy_version/student.py` by creating a student with marks `250`.
- Confirmed the constructor accepted invalid marks because the range check was `0-1000` instead of `0-100`.

### Fix Applied
- Updated the marks validation condition in `Student.__init__()` to enforce the correct range `0-100`.
- Kept the fix limited to the validation logic without changing unrelated class behavior.

### Verification
- Added automated tests in `tests/test_buggy_marks_validation.py`.
- Verified that marks `0` and `100` are accepted.
- Verified that marks `101` and `-1` raise `ValueError`.

### Outcome
- Invalid marks are now rejected correctly, and Bug 3 is resolved with automated verification.

## Phase 4.4 – Bug 4 Resolution

**Date:** 2026-09-10

### Investigation
- Reproduced the persistence defect by updating a student's marks, restarting the manager, and observing old marks in reloaded data.
- Identified that `update_marks()` in `buggy_version/student_manager.py` returned success before writing changes to disk.

### Fix Applied
- Restored persistence flow in `update_marks()` so it calls `save_students(self._students)` after in-memory update.
- Kept rollback logic to restore previous marks when save fails.

### Verification
- Added `tests/test_buggy_persistence_bug.py` to verify updated marks remain after creating a new manager instance.
- Confirmed the test passes and updated marks persist across reload.

### Outcome
- Marks updates are now durably saved, and Bug 4 is resolved.

## Phase 4.5 – Bug 5 Resolution

**Date:** 2026-09-10

### Investigation
- Reproduced startup failure by corrupting the JSON file and loading the application.
- Traced failure to `load_students()` in `buggy_version/storage.py`, where `json.loads()` raised `JSONDecodeError` without dedicated handling.

### Fix Applied
- Added `except json.JSONDecodeError: return []` in `load_students()` to gracefully handle corrupted JSON content.
- Kept the storage API behavior unchanged for valid JSON and other error paths.

### Verification
- Added `tests/test_buggy_json_handling_bug.py`.
- Verified corrupted JSON now returns an empty list instead of crashing.
- Verified valid JSON still loads student records correctly.

### Outcome
- Corrupted JSON no longer crashes loading flow, and Bug 5 is resolved.

## Phase 4.6 – Bug 6 Resolution

**Date:** 2026-09-10

### Investigation
- Reproduced the duplicate ID issue by adding two students with the same ID.
- Confirmed `add_student()` in `buggy_version/student_manager.py` lacked a pre-insert uniqueness check.

### Fix Applied
- Added a guard in `add_student()` to reject insertion when `find_student(student_id)` finds an existing record.
- Kept the change minimal and localized to creation flow.

### Verification
- Added `tests/test_buggy_duplicate_id_bug.py`.
- Verified first insert succeeds, duplicate insert fails, and final in-memory record count remains unchanged.

### Outcome
- Duplicate student IDs are now rejected correctly, and Bug 6 is resolved.

## Phase 4.7 – Bug 7 Resolution

**Date:** 2026-09-10

### Investigation
- Reproduced CLI failure by entering a valid menu option with surrounding spaces.
- Confirmed `choice` in `buggy_version/main.py` was validated without stripping whitespace first.

### Fix Applied
- Updated menu input read path to `input(...).strip()` before numeric validation.
- Left all menu routing logic unchanged.

### Verification
- Added `tests/test_buggy_cli_input_bug.py`.
- Verified `" 8 "` is accepted as valid input and exits cleanly without invalid-number warning.

### Outcome
- CLI now handles leading/trailing spaces for menu options, and Bug 7 is resolved.

## Phase 5 – Automated Testing

**Date:** 2026-09-10

### Work Completed
- Reworked legacy script-style test files into proper `unittest` test modules.
- Organized tests by responsibility in separate files:
  - `tests/test_student.py`
  - `tests/test_storage.py`
  - `tests/test_student_manager.py`
  - plus bug-focused regression tests (`test_buggy_*` files).
- Isolated storage-related tests with dedicated test JSON files under `tests/data`.

### Verification
- Ran `python -m unittest discover -s tests -v`.
- Confirmed all tests pass (24/24), including regression checks for all fixed bugs.

### Outcome
- The repository now has structured, repeatable automated testing that validates both core behavior and resolved defects.

## Phase 6 – Documentation and Final Report Preparation

**Date:** 2026-09-10

### Work Completed
- Polished `README.md` into a submission-ready project document.
- Added `docs/FINAL_REPORT_CONTENT.md` containing structured final-report narrative ready for Word conversion.
- Enhanced `docs/BUG_REPORT.md` with an executive summary and status table.
- Preserved all prior phase evidence while improving presentation and clarity.

### Verification
- Reviewed documentation consistency across README, debug log, bug report, and test coverage.
- Re-ran automated tests to confirm documentation updates did not alter application behavior.

### Outcome
- Repository documentation is now professional, complete, and aligned with internship evaluation criteria.