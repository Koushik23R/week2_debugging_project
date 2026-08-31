import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from fixed_version.student import Student

print("=== Create Student ===")
student = Student(101, "Alice", 89)

print("\n=== Print Student ===")
print(student)

print("\n=== Convert to Dictionary ===")
student_dict = student.to_dict()
print(student_dict)

print("\n=== Recreate from Dictionary ===")
recreated_student = Student.from_dict(student_dict)

print("\n=== Print Again ===")
print(recreated_student)


print("\n=== Invalid Name Test ===")
try:
    Student(1, "", 90)
    print("FAIL: Expected ValueError")
except ValueError as e:
    print(f"PASS: {e}")


print("\n=== Invalid Marks Test ===")
try:
    Student(1, "Bob", 150)
    print("FAIL: Expected ValueError")
except ValueError as e:
    print(f"PASS: {e}")
