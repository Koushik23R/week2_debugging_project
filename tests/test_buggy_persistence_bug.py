import sys
import unittest
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "buggy_version"))

import storage
from student_manager import StudentManager


class TestBuggyVersionPersistence(unittest.TestCase):
    def setUp(self):
        self.test_data_file = project_root / "tests" / "data" / "students_persistence_bug.json"
        self.test_data_file.parent.mkdir(parents=True, exist_ok=True)
        if self.test_data_file.exists():
            self.test_data_file.unlink()
        storage.DATA_FILE = self.test_data_file

    def tearDown(self):
        if self.test_data_file.exists():
            self.test_data_file.unlink()

    def test_updated_marks_are_persisted_after_reload(self):
        manager = StudentManager()
        manager.add_student(2001, "Alice", 80)
        updated = manager.update_marks(2001, 95)

        self.assertTrue(updated)

        reloaded_manager = StudentManager()
        reloaded_student = reloaded_manager.find_student(2001)

        self.assertIsNotNone(reloaded_student)
        self.assertEqual(reloaded_student.marks, 95)


if __name__ == "__main__":
    unittest.main()
