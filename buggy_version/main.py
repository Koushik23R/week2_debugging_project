"""
main.py

Command Line Interface for the Student Grade Management System.
"""


from student_manager import StudentManager

def print_menu() -> None:
    """Display the main menu."""

    print("\n===============================")
    print(" Student Grade Management System")
    print("===============================")
    print("1. View Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Remove Student")
    print("6. Class Average")
    print("7. Top Student")
    print("8. Exit")


def main() -> None:
    """Main application loop."""

    manager = StudentManager()

    while True:
        print_menu()

        choice = input("Enter your choice: ").strip()

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        # Option 1 - View Students
        if choice == 1:
            students = manager.get_students()

            if not students:
                print("No students found.")
            else:
                print("\nStudents:")
                for student in students:
                    print(student)

        # Option 2 - Add Student
        elif choice == 2:
            try:
                student_id = int(input("Student ID: "))
            except ValueError:
                print("Invalid student ID.")
                continue

            name = input("Name: ").strip()

            if not name:
                print("Name cannot be empty.")
                continue

            try:
                marks = float(input("Marks: "))
            except ValueError:
                print("Invalid marks.")
                continue

            student = manager.add_student(
                student_id,
                name,
                marks
            )

            if student is not None:
                print("Student added successfully.")
            else:
                print("Failed to add student.")

        # Option 3 - Search Student
        elif choice == 3:
            try:
                student_id = int(input("Student ID: "))
            except ValueError:
                print("Invalid student ID.")
                continue

            student = manager.find_student(student_id)

            if student is not None:
                print(student)
            else:
                print("Student not found.")

        # Option 4 - Update Marks
        elif choice == 4:
            try:
                student_id = int(input("Student ID: "))
            except ValueError:
                print("Invalid student ID.")
                continue

            try:
                new_marks = float(input("New Marks: "))
            except ValueError:
                print("Invalid marks.")
                continue

            if manager.update_marks(student_id, new_marks):
                print("Marks updated successfully.")
            else:
                print("Failed to update marks.")

        # Option 5 - Remove Student
        elif choice == 5:
            try:
                student_id = int(input("Student ID: "))
            except ValueError:
                print("Invalid student ID.")
                continue

            if manager.remove_student(student_id):
                print("Student removed successfully.")
            else:
                print("Student not found.")

        # Option 6 - Class Average
        elif choice == 6:
            average = manager.calculate_average()
            print(f"Class Average: {average:.2f}")

        # Option 7 - Top Student
        elif choice == 7:
            top_student = manager.get_top_student()

            if top_student is None:
                print("No students available.")
            else:
                print("Top Student:")
                print(top_student)

        # Option 8 - Exit
        elif choice == 8:
            print("Thank you for using Student Grade Management System.")
            break

        # Invalid Choice
        else:
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()