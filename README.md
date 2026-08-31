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