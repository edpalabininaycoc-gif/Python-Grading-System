grades = {}  

def compute_average(p1, p2, p3):
    return (p1 + p2 + p3) / 3


def valid_grade(grade):
    return 0 <= grade <= 100


while True:
    print("\n=== STUDENT GRADING SYSTEM ===")
    print("1. Add Student")
    print("2. Edit Student")
    print("3. Delete Student")
    print("4. View Student Records")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # ADD STUDENT
    if choice == "1":
        student_id = input("Enter student ID: ").strip()

        # Check if empty
        if student_id == "":
            print("Invalid. Student ID cannot be empty.")
            continue

        # Check if numeric
        if not student_id.isdigit():
            print("Invalid. Student ID must be a number.")
            continue

        try:
            p1 = float(input("Enter P1 grade: "))
            p2 = float(input("Enter P2 grade: "))
            p3 = float(input("Enter P3 grade: "))

            # Check for invalid grade range
            if not (valid_grade(p1) and valid_grade(p2) and valid_grade(p3)):
                print("\nInvalid. Grades must be between 0 and 100.")
                print("Remarks: INVALID")
                continue  

            average = compute_average(p1, p2, p3)
            grades[student_id] = {"p1": p1, "p2": p2, "p3": p3, "average": average}

            remark = "PASSED" if average >= 50 else "FAILED"

            print("\nGrade Recorded")
            print(f"Student: {student_id}")
            print(f"P1: {p1}")
            print(f"P2: {p2}")
            print(f"P3: {p3}")
            print(f"Average: {average:.2f}")
            print(f"Remarks: {remark}")

        except ValueError:
            print("Invalid. Please enter numerical grades only.")

    # EDIT STUDENT
    elif choice == "2":
        student_id = input("Enter the student ID to edit: ")

        if student_id in grades:
            try:
                p1 = float(input("Enter new P1 grade: "))
                p2 = float(input("Enter new P2 grade: "))
                p3 = float(input("Enter new P3 grade: "))

                if not (valid_grade(p1) and valid_grade(p2) and valid_grade(p3)):
                    print("\nInvalid input! Grades must be between 0 and 100.")
                    print("Remarks: INVALID")
                    continue

                average = compute_average(p1, p2, p3)
                grades[student_id] = {"p1": p1, "p2": p2, "p3": p3, "average": average}

                remark = "PASSED" if average >= 50 else "FAILED"

                print(f"\nStudent '{student_id}' updated.")
                print(f"P1: {p1}")
                print(f"P2: {p2}")
                print(f"P3: {p3}")
                print(f"Average: {average:.2f}")
                print(f"Remarks: {remark}")

            except ValueError:
                print("Invalid input. Please enter numerical grades only.")
        else:
            print(f"Student '{student_id}' not found.")

    # DELETE STUDENT
    elif choice == "3":
        student_id = input("Enter the student ID to delete: ")
        if student_id in grades:
            del grades[student_id]
            print(f"Student '{student_id}' deleted.")
        else:
            print(f"Student '{student_id}' not found.")

    # VIEW STUDENT RECORDS
    elif choice == "4":
        if grades:
            print("\n--- STUDENT RECORDS ---")
            for student_id, data in grades.items():
                p1 = data["p1"]
                p2 = data["p2"]
                p3 = data["p3"]
                avg = data["average"]
                remark = "PASSED" if avg >= 50 else "FAILED"
                print(f"\nStudent ID: {student_id}")
                print(f"P1: {p1}")
                print(f"P2: {p2}")
                print(f"P3: {p3}")
                print(f"Average: {avg:.2f}")
                print(f"Remarks: {remark}")
        else:
            print("\nNo student records found.")

    # EXIT PROGRAM
    elif choice == "5":
        print("\nSystem closed.")
        break

    else:
        print("Invalid choice. Please enter 1-5.")