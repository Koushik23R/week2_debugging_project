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