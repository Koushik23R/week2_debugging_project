from __future__ import annotations #optional
"""
student.py

Contains the Student class representing a single student record.

The class stores student information and provides helper methods
for serialization and display.
"""

#imports
from datetime import datetime

class Student:
    """Represents a single student record."""
    def __init__(self, student_id: int, name: str, marks: float):
        # Validate name
        name = name.strip()

        if not name:
            raise ValueError("Name cannot be empty or contain only whitespace.")


        # Validate marks
        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100.")

        # Use a more descriptive attribute name to avoid shadowing built-in 'id'
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.created_at = datetime.now()

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "marks": self.marks,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        student = cls(
            data["student_id"],
            data["name"],
            data["marks"]
        )

        student.created_at = datetime.fromisoformat(
            data["created_at"]
        )

        return student

    def __str__(self) -> str:
        return f"ID:{self.student_id} | {self.name} | Marks:{self.marks:g}"