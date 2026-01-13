import statistics

students = {}

def student_system():
    while True:
        print("---STUDENT SYSTEM---")
        print("1. Admin")
        print("2. Teacher")
        print("3. Student")
        print("4. Exit")

        choice1 = input("Make your choice: ")

        # --------------- ADMIN ---------------
        if choice1 == "1":
            password = input("Password: ")
            if password != "123qwerty":
                print("Wrong password!")
            else:
                while True:
                    print("---STUDENT LIST---")
                    print("1. Add Student")
                    print("2. View Students")
                    print("3. Delete Student")
                    print("4. Show Average Score")
                    print("5. Show Statistics")
                    print("6. Exit")

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
                            print("Age, class, and score must be numbers")
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
                        print("Student added successfully!")

                    elif choice == "2":
                        if len(students) == 0:
                            print("Student list is empty")
                        else:
                            for s in students.values():
                                print(s)

                    elif choice == "3":
                        if len(students) == 0:
                            print("No students to delete")
                        else:
                            try:
                                delete_id = int(input("Enter ID to delete: "))
                                if delete_id in students:
                                    del students[delete_id]
                                    print("Deleted successfully")
                                else:
                                    print("ID not found")
                            except ValueError:
                                print("ID must be a number")

                    elif choice == "4":
                        if len(students) == 0:
                            print("List is empty")
                        else:
                            scores = [s["Score"] for s in students.values()]
                            print("Average Score:", statistics.mean(scores))

                    elif choice == "5":
                        if len(students) == 0:
                            print("List is empty")
                        else:
                            scores = [s["Score"] for s in students.values()]
                            max_score = max(scores)
                            min_score = min(scores)
                            for s in students.values():
                                if s["Score"] == max_score:
                                    print("Top Student:")
                                    print("Name:", s["Name"], "Score:", max_score)
                                if s["Score"] == min_score:
                                    print("Lowest Student:")
                                    print("Name:", s["Name"], "Score:", min_score)

                    elif choice == "6":
                        print("Exiting admin menu...")
                        break

                    else:
                        print("Invalid choice, select 1-6")

        # --------------- TEACHER ---------------
        elif choice1 == "2":
            password = input("Password: ")
            if password != "1234":
                print("Wrong password!")
            else:
                while True:
                    print("---STUDENT LIST---")
                    print("1. Add Student")
                    print("2. View Students")
                    print("3. Show Average Score")
                    print("4. Show Statistics")
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
                            print("Score must be 0-100")
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
                        print("Student added successfully!")

                    elif choice == "2":
                        if len(students) == 0:
                            print("Student list is empty")
                        else:
                            for s in students.values():
                                print(s)

                    elif choice == "3":
                        if len(students) == 0:
                            print("List is empty")
                        else:
                            scores = [s["Score"] for s in students.values()]
                            print("Average Score:", statistics.mean(scores))

                    elif choice == "4":
                        if len(students) == 0:
                            print("List is empty")
                        else:
                            scores = [s["Score"] for s in students.values()]
                            max_score = max(scores)
                            min_score = min(scores)
                            for s in students.values():
                                if s["Score"] == max_score:
                                    print("Top Student:")
                                    print("Name:", s["Name"], "Score:", max_score)
                                if s["Score"] == min_score:
                                    print("Lowest Student:")
                                    print("Name:", s["Name"], "Score:", min_score)

                    elif choice == "5":
                        print("Exiting teacher menu...")
                        break

                    else:
                        print("Invalid choice, select 1-5")

        # --------------- STUDENT ---------------
        elif choice1 == "3":
            name = input("Enter your name: ").capitalize()
            student_names = [s["Name"] for s in students.values()]
            if name not in student_names:
                print("Name not found")
            else:
                while True:
                    print("---STUDENT MENU---")
                    print("1. View All Students")
                    print("2. Show Average Score")
                    print("3. Show Statistics")
                    print("4. Exit")

                    choice = input("Make your choice: ")

                    if choice == "1":
                        if len(students) == 0:
                            print("List is empty")
                        else:
                            for s in students.values():
                                print(s)

                    elif choice == "2":
                        if len(students) == 0:
                            print("List is empty")
                        else:
                            scores = [s["Score"] for s in students.values()]
                            print("Average Score:", statistics.mean(scores))

                    elif choice == "3":
                        if len(students) == 0:
                            print("List is empty")
                        else:
                            scores = [s["Score"] for s in students.values()]
                            max_score = max(scores)
                            min_score = min(scores)
                            for s in students.values():
                                if s["Score"] == max_score:
                                    print("Top Student:")
                                    print("Name:", s["Name"], "Score:", max_score)
                                if s["Score"] == min_score:
                                    print("Lowest Student:")
                                    print("Name:", s["Name"], "Score:", min_score)

                    elif choice == "4":
                        print("Exiting student menu...")
                        break

                    else:
                        print("Invalid choice, select 1-4")

        elif choice1 == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, select 1-4")

student_system()
