import sys
import unittest
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "buggy_version"))

import storage
from student_manager import StudentManager


class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.test_data_file = project_root / "tests" / "data" / "students_manager_test.json"
        self.test_data_file.parent.mkdir(parents=True, exist_ok=True)
        if self.test_data_file.exists():
            self.test_data_file.unlink()
        storage.DATA_FILE = self.test_data_file
        self.manager = StudentManager()

    def tearDown(self):
        if self.test_data_file.exists():
            self.test_data_file.unlink()

    def test_add_and_find_student(self):
        student = self.manager.add_student(101, "Alice", 89)
        self.assertIsNotNone(student)

        found = self.manager.find_student(101)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Alice")

    def test_duplicate_id_is_rejected(self):
        self.manager.add_student(102, "Bob", 76)
        duplicate = self.manager.add_student(102, "Bobby", 60)
        self.assertIsNone(duplicate)

    def test_update_marks_persists(self):
        self.manager.add_student(103, "Charlie", 70)
        self.assertTrue(self.manager.update_marks(103, 95))

        reloaded = StudentManager()
        found = reloaded.find_student(103)
        self.assertIsNotNone(found)
        self.assertEqual(found.marks, 95)

    def test_calculate_average_returns_decimal(self):
        self.manager.add_student(104, "Diana", 90)
        self.manager.add_student(105, "Eve", 95)
        self.manager.add_student(106, "Frank", 90)

        self.assertAlmostEqual(self.manager.calculate_average(), 91.6666666667, places=5)

    def test_get_top_student(self):
        self.manager.add_student(107, "Gina", 78)
        self.manager.add_student(108, "Henry", 98)

        top = self.manager.get_top_student()
        self.assertIsNotNone(top)
        self.assertEqual(top.student_id, 108)

    def test_remove_student(self):
        self.manager.add_student(109, "Ivy", 80)
        self.assertTrue(self.manager.remove_student(109))
        self.assertIsNone(self.manager.find_student(109))


if __name__ == "__main__":
    unittest.main()
