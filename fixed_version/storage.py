"""
storage.py

Handles saving and loading student records from JSON storage.
"""

import json
from pathlib import Path

from student import Student

DATA_FILE = Path("data/students.json")


def save_students(students: list[Student]) -> bool:
    """
    Save a list of Student objects to JSON.

    Returns:
        True if successful, False otherwise.
    """
    try:
        # Ensure the directory exists before writing the file
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        data = [student.to_dict() for student in students]

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    except OSError:
        return False


def load_students() -> list[Student]:
    """
    Load Student objects fromurns:
        List of Student objects, or an empty list if loading fails.
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()

            if not content:
                return []

            data = json.loads(content)

        return [Student.from_dict(student_data) for student_data in data]

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

    except OSError:
        return []