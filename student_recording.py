import statistics

students = {}

def student_system():
    while True:
        print("\n--- STUDENT SYSTEM ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Show Average Grade")
        print("5. Show Statistics (Best/Worst)")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            try:
                student_id = int(input("ID: "))
                if student_id in students:
                    print("This ID already exists!")
                    continue
            except ValueError:
                print("Invalid ID format!")
                continue

            name = input("Name: ").capitalize()

            try:
                age = int(input("Age: "))
                grade = int(input("Grade: "))
                score = int(input("Score (0-100): "))
            except ValueError:
                print("Invalid number entered!")
                continue

            if score < 0 or score > 100:
                print("Invalid score. It must be between 0 and 100.")
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
                "Grade": grade,
                "Score": score,
                "Letter": letter
            }

            print("Student added successfully!")

        elif choice == "2":
            if not students:
                print("The student list is empty.")
            else:
                for s in students.values():
                    print(s)

        elif choice == "3":
            if not students:
                print("No students to delete.")
            else:
                try:
                    delete_id = int(input("Enter ID to delete: "))
                except ValueError:
                    print("ID must be a number!")
                    continue

                if delete_id in students:
                    del students[delete_id]
                    print("Student deleted.")
                else:
                    print("ID not found.")

        elif choice == "4":
            if not students:
                print("No students to calculate average.")
            else:
                scores = [s["Score"] for s in students.values()]
                print("Average Score:", statistics.mean(scores))

        elif choice == "5":
            if not students:
                print("No data for statistics.")
            else:
                best = max(students.values(), key=lambda x: x["Score"])
                worst = min(students.values(), key=lambda x: x["Score"])

                print("\n--- STATISTICS ---")
                print(f"Best Student: {best['Name']} ({best['Score']})")
                print(f"Worst Student: {worst['Name']} ({worst['Score']})")

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please choose between 1-6.")

student_system()
