import json
import sys
import unittest
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "buggy_version"))

import storage
from student import Student


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_data_file = project_root / "tests" / "data" / "students_storage_test.json"
        self.test_data_file.parent.mkdir(parents=True, exist_ok=True)
        if self.test_data_file.exists():
            self.test_data_file.unlink()
        storage.DATA_FILE = self.test_data_file

    def tearDown(self):
        if self.test_data_file.exists():
            self.test_data_file.unlink()

    def test_save_and_load_students(self):
        students = [Student(101, "Alice", 89), Student(102, "Bob", 76)]

        self.assertTrue(storage.save_students(students))

        loaded = storage.load_students()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].student_id, 101)
        self.assertEqual(loaded[1].student_id, 102)

    def test_load_missing_file_returns_empty_list(self):
        self.assertEqual(storage.load_students(), [])

    def test_load_empty_file_returns_empty_list(self):
        self.test_data_file.write_text("", encoding="utf-8")
        self.assertEqual(storage.load_students(), [])

    def test_load_corrupted_json_returns_empty_list(self):
        self.test_data_file.write_text("{", encoding="utf-8")
        self.assertEqual(storage.load_students(), [])

    def test_load_valid_json_list(self):
        payload = [{"student_id": 301, "name": "Eve", "marks": 84, "created_at": "2026-09-10T10:00:00"}]
        self.test_data_file.write_text(json.dumps(payload), encoding="utf-8")

        loaded = storage.load_students()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].name, "Eve")


if __name__ == "__main__":
    unittest.main()
