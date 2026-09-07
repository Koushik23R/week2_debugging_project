# Week 2 - Debugging and Troubleshooting Python Applications

## Objective

This project demonstrates the process of identifying, reproducing, debugging, and resolving bugs in a Python application. The focus is on applying systematic debugging techniques while maintaining clean code and proper documentation.

## Project Structure

```text
week2_debugging_project/
│
├── buggy_version/        # Application with intentionally introduced bugs
├── fixed_version/        # Corrected and refactored application
├── tests/                # Automated unit tests
├── docs/
│   ├── BUG_REPORT.md     # Summary of identified bugs
│   └── DEBUG_LOG.md      # Step-by-step debugging process
├── README.md
├── requirements.txt
└── report.docx
```

## Development Roadmap

- Create the initial application
- Introduce realistic bugs
- Perform code review
- Document identified issues
- Debug and fix each issue
- Add automated tests
- Prepare final documentation and report

## Technologies Used

- Python 3.x
- JSON (Standard Library)
- unittest (Standard Library)
- pathlib
- datetime

## Planned Application

The project demonstrates debugging techniques using a Student Grade Management System developed as a command-line application.

The application will allow users to:

- Add student records
- View students
- Search students
- Update marks
- Delete records
- Calculate class average
- Display the highest scoring student

The project follows a modular architecture separating the CLI, business logic, data model, and storage layers.

## Learning Goals

The primary objectives of this project are to:

- Practice systematic debugging techniques.
- Identify and reproduce software defects.
- Document the debugging process clearly.
- Improve code readability through refactoring.
- Validate fixes using manual and automated testing.
- Maintain clean version control throughout development..

## Current Progress

Phase 2.2 – Student Model
Implemented the Student model with the following features:
- Student ID, name, marks, and creation timestamp
- Input validation for student name and marks
- Serialization using to_dict()
- Deserialization using from_dict()
- Readable string representation using __str__()

Verification
The Student model was manually tested for:
- Creating valid student records
- Converting objects to dictionaries
- Reconstructing objects from dictionaries
- Rejecting empty student names
- Rejecting marks outside the valid range (0–100)
All tests passed successfully.

### Phase 2.3 – Storage Layer

Implemented the persistence layer responsible for storing and retrieving student records.

Features:

- Save student records to JSON
- Load student records from JSON
- Graceful handling of missing files
- Graceful handling of empty files
- Graceful handling of corrupted JSON

All persistence functionality was manually verified before integration.

### Phase 2.4 – Student Manager

Implemented the business logic layer responsible for managing student records.

Features:

- Add students
- Remove students
- Search students by ID
- Update marks
- Calculate class average
- Identify the highest-scoring student

The manager automatically saves all changes using the storage layer.

### Phase 2.5 – Command Line Interface

Implemented the user interface for the Student Grade Management System.

Features:

- Interactive menu
- Input validation
- Student management operations
- Statistics display
- Graceful error handling

The CLI delegates all business operations to the StudentManager and focuses only on user interaction.

## Phase 3 – Buggy Version

A separate copy of the fully functional application was created to simulate real-world debugging scenarios.

The buggy version will be modified incrementally by introducing realistic software defects related to validation, persistence, conditional logic, file handling, and calculations. This approach preserves the working implementation while providing a controlled environment for debugging.

### Phase 3.1 – Initial Bug Introduction

Introduced a controlled set of realistic defects into the buggy version of the application to simulate common software issues involving validation, conditional logic, and calculations. Each issue has been documented in the bug report and will be investigated and resolved during the debugging phase.