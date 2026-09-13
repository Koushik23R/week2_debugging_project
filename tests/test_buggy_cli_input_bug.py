import sys
import unittest
from pathlib import Path
from unittest.mock import patch

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "buggy_version"))

import main


class DummyManager:
    def get_students(self):
        return []

    def add_student(self, student_id, name, marks):
        return None

    def find_student(self, student_id):
        return None

    def update_marks(self, student_id, new_marks):
        return False

    def remove_student(self, student_id):
        return False

    def calculate_average(self):
        return 0.0

    def get_top_student(self):
        return None


class TestBuggyVersionCliInputHandling(unittest.TestCase):
    def test_menu_choice_with_whitespace_is_accepted(self):
        with patch.object(main, "StudentManager", return_value=DummyManager()):
            with patch("builtins.input", side_effect=[" 8 "]):
                with patch("builtins.print") as mock_print:
                    main.main()

        printed_messages = [
            " ".join(str(arg) for arg in call.args) for call in mock_print.call_args_list
        ]
        self.assertIn("Thank you for using Student Grade Management System.", printed_messages)
        self.assertNotIn("Please enter a valid number.", printed_messages)


if __name__ == "__main__":
    unittest.main()
