import statistics

students = {}

def student_system():
    print("--- STUDENT SYSTEM ---")
    print("1. Admin")
    print("2. Teacher")

    choice1 = input("Make your choice: ")

    # --------------- ADMIN ---------------
    if choice1 == "1":
        while True:
            print("\n--- STUDENT LIST ---")
            print("1. Add student")
            print("2. View students")
            print("3. Delete student")
            print("4. Show average grade")
            print("5. Show statistics")
            print("6. Exit")

            choice = input("Make your choice: ")

            # ADD STUDENT
            if choice == "1":
                try:
                    student_id = int(input("ID: "))
                    if student_id in students:
                        print("This ID already exists")
                        continue
                except ValueError:
                    print("ID must be a number")
                    continue

                name = input("Name: ").capitalize()
                if not name.isalpha():
                    print("Name must contain only letters")
                    continue

                try:
                    age = int(input("Age: "))
                    grade = int(input("Class: "))
                    score = int(input("Score (0-100): "))
                except ValueError:
                    print("Age, class and score must be numbers")
                    continue

                if score < 0 or score > 100:
                    print("Score must be between 0 and 100")
                    continue

                if score >= 91:
                    letter = "A"
                elif score >= 81:
                    letter = "B"
                elif score >= 71:
                    letter = "C"
                elif score >= 61:
                    letter = "D"
                elif score >= 51:
                    letter = "E"
                else:
                    letter = "F"

                students[student_id] = {
                    "ID": student_id,
                    "Name": name,
                    "Age": age,
                    "Class": grade,
                    "Score": score,
                    "Grade": letter
                }

                print("Student added successfully")

            # VIEW STUDENTS
            elif choice == "2":
                if not students:
                    print("Student list is empty")
                else:
                    for student in students.values():
                        print(student)

            # DELETE STUDENT
            elif choice == "3":
                if not students:
                    print("No students to delete")
                else:
                    try:
                        delete_id = int(input("Enter ID to delete: "))
                        if delete_id in students:
                            del students[delete_id]
                            print("Student deleted")
                        else:
                            print("ID not found")
                    except ValueError:
                        print("ID must be a number")

            # AVERAGE SCORE
            elif choice == "4":
                if not students:
                    print("Student list is empty")
                else:
                    scores = [s["Score"] for s in students.values()]
                    print("Average score:", statistics.mean(scores))

            # STATISTICS
            elif choice == "5":
                if not students:
                    print("Student list is empty")
                else:
                    scores = [s["Score"] for s in students.values()]
                    max_score = max(scores)
                    min_score = min(scores)

                    for s in students.values():
                        if s["Score"] == max_score:
                            print("Best student:", s["Name"], "-", max_score)
                        if s["Score"] == min_score:
                            print("Worst student:", s["Name"], "-", min_score)

            # EXIT
            elif choice == "6":
                print("Exiting program")
                break

            else:
                print("Invalid choice (1–6)")

    # --------------- TEACHER ---------------
    elif choice1 == "2":
        while True:
            print("\n--- STUDENT LIST ---")
            print("1. Add student")
            print("2. View students")
            print("3. Show average grade")
            print("4. Show statistics")
            print("5. Exit")

            choice = input("Make your choice: ")

            if choice == "1":
                try:
                    student_id = int(input("ID: "))
                    if student_id in students:
                        print("This ID already exists")
                        continue
                except ValueError:
                    print("ID must be a number")
                    continue

                name = input("Name: ").capitalize()
                if not name.isalpha():
                    print("Name must contain only letters")
                    continue

                try:
                    age = int(input("Age: "))
                    grade = int(input("Class: "))
                    score = int(input("Score (0-100): "))
                except ValueError:
                    print("Invalid input")
                    continue

                if score < 0 or score > 100:
                    print("Score must be between 0 and 100")
                    continue

                if score >= 91:
                    letter = "A"
                elif score >= 81:
                    letter = "B"
                elif score >= 71:
                    letter = "C"
                elif score >= 61:
                    letter = "D"
                elif score >= 51:
                    letter = "E"
                else:
                    letter = "F"

                students[student_id] = {
                    "ID": student_id,
                    "Name": name,
                    "Age": age,
                    "Class": grade,
                    "Score": score,
                    "Grade": letter
                }

                print("Student added successfully")

            elif choice == "2":
                if not students:
                    print("Student list is empty")
                else:
                    for student in students.values():
                        print(student)

            elif choice == "3":
                if not students:
                    print("Student list is empty")
                else:
                    scores = [s["Score"] for s in students.values()]
                    print("Average score:", statistics.mean(scores))

            elif choice == "4":
                if not students:
                    print("Student list is empty")
                else:
                    scores = [s["Score"] for s in students.values()]
                    max_score = max(scores)
                    min_score = min(scores)

                    for s in students.values():
                        if s["Score"] == max_score:
                            print("Best student:", s["Name"], "-", max_score)
                        if s["Score"] == min_score:
                            print("Worst student:", s["Name"], "-", min_score)

            elif choice == "5":
                print("Exiting program")
                break

            else:
                print("Invalid choice (1–5)")

    else:
        print("Invalid choice (1–2)")

student_system()
