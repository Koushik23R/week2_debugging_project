from student import Student
from storage import load_students, save_students


class StudentManager:
    def __init__(self) -> None:
        self._students = load_students()

    def get_students(self) -> list[Student]:
        return self._students.copy()

    def add_student(self, student_id: int, name: str, marks: float) -> Student | None:
        student = Student(student_id, name, marks)

        self._students.append(student)

        if save_students(self._students):
            return student

        self._students.pop()
        return None

    def find_student(self, student_id: int) -> Student | None:
        for student in self._students:
            if student.student_id == student_id:
                return student

        return None

    def remove_student(self, student_id: int) -> bool:
        student = self.find_student(student_id)

        if student is None:
            return False

        self._students.remove(student)

        if save_students(self._students):
            return True

        self._students.append(student)
        return False

    def update_marks(self, student_id: int, new_marks: float) -> bool:
        if not (0 <= new_marks <= 100):
            return False

        student = self.find_student(student_id)

        if student is None:
            return False

        old_marks = student.marks
        student.marks = new_marks

        if save_students(self._students):
            return True

        student.marks = old_marks
        return False

    def calculate_average(self) -> float:
        if not self._students:
            return 0.0

        total = sum(student.marks for student in self._students)
        return total / len(self._students)

    def get_top_student(self) -> Student | None:
        if not self._students:
            return None

        return max(
            self._students,
            key=lambda student: student.marks
        )