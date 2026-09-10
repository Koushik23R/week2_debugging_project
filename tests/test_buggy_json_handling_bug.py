import json
import sys
import unittest
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "buggy_version"))

import storage


class TestBuggyVersionJsonHandling(unittest.TestCase):
    def setUp(self):
        self.test_data_file = project_root / "tests" / "data" / "students_json_bug.json"
        self.test_data_file.parent.mkdir(parents=True, exist_ok=True)
        storage.DATA_FILE = self.test_data_file

    def tearDown(self):
        if self.test_data_file.exists():
            self.test_data_file.unlink()

    def test_corrupted_json_returns_empty_list(self):
        self.test_data_file.write_text("{", encoding="utf-8")
        students = storage.load_students()
        self.assertEqual(students, [])

    def test_valid_json_still_loads(self):
        self.test_data_file.write_text(
            json.dumps(
                [
                    {
                        "student_id": 3001,
                        "name": "Alice",
                        "marks": 88,
                        "created_at": "2026-09-10T10:00:00",
                    }
                ]
            ),
            encoding="utf-8",
        )
        students = storage.load_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].student_id, 3001)


if __name__ == "__main__":
    unittest.main()
