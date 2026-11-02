
import json
import os

FILE_NAME = "students.json"

# Load student records
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save student records
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student(students):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    if any(s["roll"] == roll for s in students):
        print("Roll number already exists!")
        return

    students.append({
        "name": name,
        "roll": roll,
        "course": course
    })

    save_students(students)
    print("Student added successfully!")

# View students
def view_students(students):
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(student)

# Search student
def search_student(students):
    roll = input("Enter roll number: ")

    for student in students:
        if student["roll"] == roll:
            print("Student found:", student)
            return

    print("Student not found.")

# Update student
def update_student(students):
    roll = input("Enter roll number: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter new name: ")
            student["course"] = input("Enter new course: ")
            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")

# Delete student
def delete_student(students):
    roll = input("Enter roll number: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")

# Main application
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                print("Thank you!")
                break
            else:
                print("Invalid choice!")

        except (OSError, json.JSONDecodeError) as error:
            print("File error:", error)

if __name__ == "__main__":
    main()
