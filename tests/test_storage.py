import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "fixed_version"))
sys.path.insert(0, str(project_root))

from fixed_version.student import Student
from fixed_version import storage
from fixed_version.storage import save_students, load_students

DATA_FILE = project_root / "fixed_version" / "data" / "students.json"
storage.DATA_FILE = DATA_FILE
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)


# Test 1: Save Students
print("=== Save Students ===")

students = [
    Student(101, "Alice", 89),
    Student(102, "Bob", 76),
    Student(103, "Charlie", 91)
]

if save_students(students):
    print("Saved Successfully")
else:
    print("Save Failed")


# Test 2: Load Students
print("\n=== Load Students ===")

loaded_students = load_students()

print(f"{len(loaded_students)} students loaded.")

for student in loaded_students:
    print(student)


# Test 3: Empty File
print("\n=== Empty File Test ===")

with open(DATA_FILE, "w", encoding="utf-8") as file:
    file.write("")

result = load_students()

print("PASS" if result == [] else "FAIL")


# Test 4: Corrupted JSON
print("\n=== Corrupted JSON Test ===")

with open(DATA_FILE, "w", encoding="utf-8") as file:
    file.write("{")

result = load_students()

print("PASS" if result == [] else "FAIL")


# Test 5: Missing File
print("\n=== Missing File Test ===")

if DATA_FILE.exists():
    DATA_FILE.unlink()

result = load_students()

print("PASS" if result == [] else "FAIL")

# Restore valid sample data so later runs are not left with a missing file
save_students(students)
