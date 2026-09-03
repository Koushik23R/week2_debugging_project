import sys
sys.path.append(r'D:\INTERNSHIP\YUVA_INTERN\week2_debugging_project\fixed_version')

try:
    from student_manager import StudentManager
    print('IMPORT_OK')
except Exception:
    import traceback
    traceback.print_exc()
