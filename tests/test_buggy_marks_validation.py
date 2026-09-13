import sys
import unittest
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "buggy_version"))

from student import Student


class TestBuggyVersionMarksValidation(unittest.TestCase):
    def test_marks_boundaries_are_allowed(self):
        self.assertEqual(Student(1, "Alice", 0).marks, 0)
        self.assertEqual(Student(2, "Bob", 100).marks, 100)

    def test_marks_above_100_are_rejected(self):
        with self.assertRaises(ValueError):
            Student(3, "Charlie", 101)

    def test_negative_marks_are_rejected(self):
        with self.assertRaises(ValueError):
            Student(4, "Diana", -1)


if __name__ == "__main__":
    unittest.main()
