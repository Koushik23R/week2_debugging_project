# Week 2 Internship Project: Debugging and Troubleshooting Python Applications

## Project Objective
This repository demonstrates a complete debugging workflow for a beginner-friendly Python CLI application.

The goal was to:
- identify reproducible bugs,
- analyze root causes,
- apply minimal fixes,
- verify fixes with automated tests,
- and document the full troubleshooting process professionally.

---

## Application Overview
The project implements a **Student Grade Management System** with features to:
- add students,
- view student records,
- search by ID,
- update marks,
- remove students,
- calculate class average,
- identify the top-scoring student.

---

## Repository Structure
```text
week2_debugging_project/
├── buggy_version/                  # Debugged and corrected application used for internship phases
│   ├── main.py
│   ├── student.py
│   ├── student_manager.py
│   ├── storage.py
│   └── data/students.json
├── fixed_version/                  # Baseline reference implementation
├── tests/                          # Automated unittest suite (component + regression tests)
│   ├── test_student.py
│   ├── test_storage.py
│   ├── test_student_manager.py
│   ├── test_buggy_marks_validation.py
│   ├── test_buggy_persistence_bug.py
│   ├── test_buggy_json_handling_bug.py
│   ├── test_buggy_duplicate_id_bug.py
│   └── test_buggy_cli_input_bug.py
├── docs/
│   ├── BUG_REPORT.md               # Bug-by-bug professional report
│   ├── DEBUG_LOG.md                # Chronological debugging and development log
│   └── FINAL_REPORT_CONTENT.md     # Submission-ready final report content
├── data/students.json
├── requirements.txt
└── report.docx
```

---

## Architecture
The application follows a modular structure:
- `student.py`: data model and validation
- `storage.py`: JSON persistence layer
- `student_manager.py`: business logic layer
- `main.py`: CLI interaction layer

This separation made debugging easier by isolating failures to specific layers.

---

## Debugging Scope and Outcomes
### Identified Bugs (Phase 3)
1. Average calculation truncation
2. Incorrect search condition
3. Invalid marks accepted
4. Marks update not persisted
5. Crash on corrupted JSON
6. Duplicate student IDs accepted
7. CLI menu whitespace input rejection

### Resolution Status
All seven bugs are resolved and documented with root cause + fix details in `docs/BUG_REPORT.md` and `docs/DEBUG_LOG.md`.

---

## Setup and Execution
### Requirements
- Python 3.10+ (standard library only)

### Install
No external packages are required.

### Run Application
```bash
python buggy_version/main.py
```

### Run Automated Tests
```bash
python -m unittest discover -s tests -v
```

---

## Verification Summary
- Full automated suite passing: **24/24 tests**
- Regression tests added for all fixed Phase 4 bugs
- Error-handling behavior validated for persistence and JSON corruption scenarios

---

## Documentation
- `docs/BUG_REPORT.md`: structured bug report with reproduction, expected/actual behavior, root causes, fixes, and status.
- `docs/DEBUG_LOG.md`: phase-wise implementation, debugging actions, verification evidence, and outcomes.
- `docs/FINAL_REPORT_CONTENT.md`: polished narrative content ready to convert into final Word submission.

---

## Internship Deliverable Checklist
- [x] Corrected Python application free from documented bugs
- [x] Detailed debugging log
- [x] Professional bug report
- [x] Documentation of debugging process
- [x] Automated tests validating fixes
- [x] Submission-ready project documentation

This repository now represents a complete and professional debugging/troubleshooting internship submission.
