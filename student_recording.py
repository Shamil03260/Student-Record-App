students = {}

while True:
    print("\n---STUDENT LIST---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Show Average Grade")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = int(input("ID: "))
        if student_id in students:
            print("This ID already exists")

        else:
            name = input("Name: ")
            age = input("Age: ")
            grade = int(input("Class/Grade: "))
            score = int(input("Score (0-100): "))
            if score < 0 or score > 100:
                print("Invalid score")
                
            else:
                students[student_id] = {
                    "ID": student_id,
                    "Name": name,
                    "Age": age,
                    "Class": grade,
                    "Score": score
                }
                print("Student added successfully")

    elif choice == "2":
        if len(students) == 0:
            print("Student list is empty")

        else:
            for student in students.values():
                print(student)

    elif choice == "3":
        if len(students) == 0:
            print("Nothing to delete")

        else:
            student_id = int(input("Enter the ID to delete: "))

            if student_id in students:
                del students[student_id]
                print("Student deleted successfully")

            else:
                print("ID not found")

    elif choice == "4":
        if len(students) == 0:
            print("Student list is empty")

        else:
            total = sum(student["Score"] for student in students.values())
            average = total / len(students)
            print(f"Average score of students: {average:.2f}")

    elif choice == "5":
        print("Exiting program")
        break

    else:
        print("Invalid choice, please enter a number between 1 and 5")