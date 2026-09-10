import sys
import unittest
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "buggy_version"))

from student import Student


class TestStudent(unittest.TestCase):
    def test_create_valid_student(self):
        student = Student(101, "Alice", 89)
        self.assertEqual(student.student_id, 101)
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.marks, 89)

    def test_name_is_trimmed(self):
        student = Student(102, "  Bob  ", 76)
        self.assertEqual(student.name, "Bob")

    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            Student(103, "   ", 50)

    def test_marks_out_of_range_raise(self):
        with self.assertRaises(ValueError):
            Student(104, "Charlie", -1)
        with self.assertRaises(ValueError):
            Student(105, "Charlie", 101)

    def test_to_dict_and_from_dict(self):
        original = Student(106, "Diana", 91)
        data = original.to_dict()
        reconstructed = Student.from_dict(data)

        self.assertEqual(reconstructed.student_id, original.student_id)
        self.assertEqual(reconstructed.name, original.name)
        self.assertEqual(reconstructed.marks, original.marks)


if __name__ == "__main__":
    unittest.main()
