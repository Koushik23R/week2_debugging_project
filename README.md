# Week 2 Internship Project: Student Grade Management System

## Internship Details
- **Internship:** YuvaIntern – Junior Python Developer Internship
- **Task:** Week 2 – Debugging and Troubleshooting Python Applications
- **Project:** Student Grade Management System
- **Name:** Koushik R
- **Institution:** East West Institute of Technology, Bengaluru
- **Branch:** Artificial Intelligence and Machine Learning
- **Email:** kowshikr3932@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/koushik-r-a33a272a6/
- **GitHub:** https://github.com/Koushik23R/week2_debugging_project.git

## Objective
This project demonstrates a complete Python debugging workflow: reproduce defects, isolate root causes, apply minimal fixes, test the corrected behavior, and document the evidence.

## Version Separation
- `buggy_version/` is the intentionally defective baseline and preserves all seven documented bugs.
- `fixed_version/` is the corrected implementation after debugging.
- `tests/` imports `fixed_version` and verifies the corrected behavior.

## Prerequisites
- Python 3.10 or later
- Git (optional, for repository management)
- No third-party Python packages are required

## Architecture
- `student.py`: model, validation, and serialization
- `storage.py`: JSON persistence and load-error handling
- `student_manager.py`: business rules and student operations
- `main.py`: menu-driven command-line interface

## Project Structure

```text
week2_debugging_project/
├── buggy_version/          # Original implementation with intentional bugs
├── fixed_version/          # Corrected implementation
├── tests/                  # Automated unit tests
├── docs/
│   ├── BUG_REPORT.md       # Detailed bug analysis
│   ├── DEBUG_LOG.md        # Chronological debugging log
│   └── FINAL_REPORT_CONTENT.md
├── README.md
├── requirements.txt
└── report.docx

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
