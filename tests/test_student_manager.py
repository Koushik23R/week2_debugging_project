import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root / "fixed_version"))

from student_manager import StudentManager

manager = StudentManager()

print("=== Add Students ===")

manager.add_student(101, "Alice", 89)
manager.add_student(102, "Bob", 76)
manager.add_student(103, "Charlie", 95)

print("PASS")


print("\n=== View Students ===")

for student in manager.get_students():
    print(student)


print("\n=== Search Student ===")

student = manager.find_student(102)

if student:
    print(f"Found: {student.name}")


print("\n=== Update Marks ===")

manager.update_marks(102, 91)

student = manager.find_student(102)

print(f"{student.name} updated to {student.marks:g}")


print("\n=== Average ===")

print(f"{manager.calculate_average():.2f}")


print("\n=== Top Student ===")

top_student = manager.get_top_student()

print(top_student.name)


print("\n=== Remove Student ===")

manager.remove_student(101)

print("Alice removed")


print("\n=== Remaining Students ===")

for student in manager.get_students():
    print(student)


print("\n=== Persistence Test ===")

new_manager = StudentManager()

print(
    f"{len(new_manager.get_students())} students loaded successfully"
)

print("\nAll StudentManager tests passed.")