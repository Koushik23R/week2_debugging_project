# Bug Report

## Bug 1

### Title

Average calculation returns incorrect value.

### Type

Logic Error

### Steps to Reproduce

1. Add three students.
2. Select "Calculate Average".

### Expected

91.67

### Actual

91

### Root Cause

The `calculate_average()` method used floor division (`//`), which truncates the decimal portion and returns an integer-like result instead of a floating-point average.

### Resolution

Updated the calculation to use true division (`/`) so the average is returned as a decimal value matching the expected result.

### Status

Closed

---

## Bug 2

### Title

Student search returns incorrect result.

### Type

Conditional Logic

### Steps to Reproduce

1. Add students.
2. Search by ID.

### Expected

Correct student.

### Actual

Wrong student returned.

### Root Cause

The `find_student()` method compared `student_id != student_id` instead of checking whether the current student's `student_id` matched the requested ID, so it returned the wrong record or a false match.

### Resolution

Updated the condition to return a student only when `student.student_id == student_id`, and otherwise continue searching until no match is found.

### Status

Closed

---

## Bug 3

### Title

Invalid marks accepted.

### Type

Validation

### Steps to Reproduce

1. Add a student with marks 250.

### Expected

Validation error.

### Actual

Student added successfully.

### Root Cause

The `Student` model in `buggy_version/student.py` validated marks against `0-1000` instead of `0-100`, so out-of-range marks like `250` were treated as valid.

### Resolution

Corrected the validation range to `0-100` and added automated unit tests to verify valid boundaries and rejection of invalid marks.

### Status

Closed

---

## Bug 4

### Title

Updated marks are not persisted after restarting the application.

### Type

Persistence Error

### Steps to Reproduce

1. Add a student.
2. Update the student's marks.
3. Exit the application.
4. Restart the application.
5. View the student's record.

### Expected

The updated marks should be saved and displayed after restarting.

### Actual

The student's old marks are displayed because the update was not saved.

### Root Cause

In `buggy_version/student_manager.py`, `update_marks()` returned `True` immediately after changing the in-memory value, without calling `save_students()`.

### Resolution

Updated `update_marks()` to persist changes with `save_students(self._students)` before returning success, and rollback to old marks if persistence fails.

### Status

Closed

---

## Bug 5

### Title

Application crashes when the JSON data file is corrupted.

### Type

File I/O Error

### Steps to Reproduce

1. Open `students.json`.
2. Corrupt the JSON data (for example, remove a closing brace).
3. Run the application.

### Expected

The application should handle the corrupted file gracefully and display an appropriate error or load an empty dataset.

### Actual

The application crashes with a `JSONDecodeError`.

### Root Cause

`buggy_version/storage.py` did not handle `json.JSONDecodeError` inside `load_students()`, so corrupted JSON bubbled up and crashed the application path that loads student data.

### Resolution

Added explicit handling for `json.JSONDecodeError` in `load_students()` to safely return an empty list when JSON is corrupted.

### Status

Closed

---

## Bug 6

### Title

Duplicate student IDs are accepted.

### Type

Business Logic Error

### Steps to Reproduce

1. Add a student with ID `101`.
2. Add another student using the same ID `101`.

### Expected

The application should reject duplicate student IDs and notify the user.

### Actual

Both student records are added successfully with the same ID.

### Root Cause

`add_student()` in `buggy_version/student_manager.py` did not check whether the given `student_id` already existed before appending a new student.

### Resolution

Added a duplicate-ID guard in `add_student()` to return failure when `find_student(student_id)` already matches an existing record.

### Status

Closed

---

## Bug 7

### Title

Menu input containing leading or trailing spaces is rejected.

### Type

Input Validation Error

### Steps to Reproduce

1. Run the application.
2. At the main menu, enter a valid option with leading or trailing spaces (for example, ` 1` or `1 `).

### Expected

The application should trim whitespace and accept the menu option.

### Actual

The application rejects the input and displays an invalid menu choice message.

### Root Cause

In `buggy_version/main.py`, menu input was read without trimming whitespace, so values like `" 1"` or `"1 "` failed `isdigit()` validation.

### Resolution

Updated menu input handling to call `.strip()` before validation, allowing valid numeric choices with leading/trailing spaces.

### Status

Closed