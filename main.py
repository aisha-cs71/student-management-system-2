students = {}

def add_student():
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    students[name] = grade
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
    else:
        for name, grade in students.items():
            print(f"{name}: {grade}")
        print()

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted.\n")
    else:
        print("Student not found.\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice.\n")
