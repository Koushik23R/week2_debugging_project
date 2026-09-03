import sys
from pathlib import Path
import json

project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

from fixed_version.student_manager import StudentManager
from fixed_version import storage
from fixed_version.student import Student

# Ensure storage file path
DATA_FILE = project_root / "fixed_version" / "data" / "students.json"
storage.DATA_FILE = DATA_FILE
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

# Helper
def read_file():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None

print('Resetting students.json to empty list')
with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump([], f)

results = {}

# 1. Students load on startup (after file contains pre-existing students)
# Create a manager, add two students, then create a fresh manager to test loading
m1 = StudentManager()
results['initial_load_empty'] = (m1.get_students() == [])

# 2. Add works
print('Adding students: Alice(101), Bob(102), Charlie(103)')
m1.add_student(101, 'Alice', 89)
m1.add_student(102, 'Bob', 76)
m1.add_student(103, 'Charlie', 95)
students_after_add = m1.get_students()
results['add_works'] = (len(students_after_add) >= 3 and any(s.student_id==101 for s in students_after_add))
file_content = read_file()
results['file_after_add'] = (isinstance(file_content, list) and any(s['student_id']==101 for s in file_content))

# 3. Search works
s = m1.find_student(102)
results['search_works'] = (s is not None and s.name == 'Bob')

# 4. Update works
ok_update = m1.update_marks(102, 91)
s_updated = m1.find_student(102)
file_content = read_file()
file_marks = None
for item in (file_content or []):
    if item.get('student_id')==102:
        file_marks = item.get('marks')
results['update_returns_true'] = ok_update is True
results['update_in_memory'] = (s_updated is not None and abs(s_updated.marks - 91) < 1e-6)
results['update_in_file'] = (file_marks == 91)

# 5. Average works
avg = m1.calculate_average()
expected_avg = (89 + 91 + 95) / 3
results['average_works'] = abs(avg - expected_avg) < 1e-6

# 6. Top student works
top = m1.get_top_student()
results['top_works'] = (top is not None and top.student_id == 103)

# 7. Remove works
removed = m1.remove_student(101)
results['remove_returns_true'] = removed is True
results['remove_in_memory'] = (m1.find_student(101) is None)
file_content = read_file()
results['remove_in_file'] = not any(item.get('student_id')==101 for item in (file_content or []))

# 8. Persistence after restart
new_manager = StudentManager()
loaded = new_manager.get_students()
results['persistence_count'] = len(loaded)
results['persistence_matches'] = any(s.student_id==102 and abs(s.marks-91)<1e-6 for s in loaded) and any(s.student_id==103 for s in loaded)

# 9. No crashes
results['no_crashes'] = True  # script reached here

# Print summary
print('\nVerification results:')
for k,v in results.items():
    print(f"{k}: {'PASS' if v else 'FAIL'}")

# Detailed loaded students
print('\nFinal loaded students:')
for s in new_manager.get_students():
    print(s)

print('\nDone')
