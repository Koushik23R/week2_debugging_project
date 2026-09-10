import sys
import unittest
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "buggy_version"))

import storage
from student_manager import StudentManager


class TestBuggyVersionDuplicateIdHandling(unittest.TestCase):
    def setUp(self):
        self.test_data_file = project_root / "tests" / "data" / "students_duplicate_id_bug.json"
        self.test_data_file.parent.mkdir(parents=True, exist_ok=True)
        if self.test_data_file.exists():
            self.test_data_file.unlink()
        storage.DATA_FILE = self.test_data_file

    def tearDown(self):
        if self.test_data_file.exists():
            self.test_data_file.unlink()

    def test_duplicate_student_id_is_rejected(self):
        manager = StudentManager()

        first_student = manager.add_student(4001, "Alice", 90)
        second_student = manager.add_student(4001, "Bob", 75)

        self.assertIsNotNone(first_student)
        self.assertIsNone(second_student)
        self.assertEqual(len(manager.get_students()), 1)


if __name__ == "__main__":
    unittest.main()
