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

### Status

Open

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

### Status

Open

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

### Status

Open

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

### Status

Open

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

### Status

Open

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

### Status

Open

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

### Status

Open