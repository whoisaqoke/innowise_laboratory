students = []

def add_student():
    name = input("Enter student name: ").strip()
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student already exists.")
            return
    students.append({"name": name, "grades": []})
    print(f"Student '{name}' added successfully.")

def add_grades():
    name = input("Enter student name: ").strip()
    for student in students:
        if student["name"].lower() == name.lower():
            while True:
                grade_input = input("Enter a grade (or 'done' to finish): ").strip()
                if grade_input.lower() == "done":
                    break
                try:
                    grade = int(grade_input)
                    if 0 <= grade <= 100:
                        student["grades"].append(grade)
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            return
    print("Student not found.")

def show_report():
    if not students:
        print("No students added yet.")
        return

    print("--- Student Report ---")
    total_sum = 0
    total_count = 0
    max_avg = None
    min_avg = None

    for student in students:
        grades = student["grades"]
        try:
            avg = sum(grades) / len(grades)
            print(f"{student['name']}'s average grade is {avg:.1f}.")
            total_sum += avg
            total_count += 1
            max_avg = avg if max_avg is None else max(max_avg, avg)
            min_avg = avg if min_avg is None else min(min_avg, avg)
        except ZeroDivisionError:
            print(f"{student['name']}'s average grade is N/A.")

    if total_count > 0:
        overall_avg = total_sum / total_count
        print("-----------------------------")
        print(f"Max Average: {max_avg:.1f}")
        print(f"Min Average: {min_avg:.1f}")
        print(f"Overall Average: {overall_avg:.1f}")
    else:
        print("No grades available to calculate averages.")

def find_top_student():
    valid_students = [s for s in students if s["grades"]]
    if not valid_students:
        print("No students with grades to evaluate.")
        return
    top_student = max(valid_students, key=lambda s: sum(s["grades"]) / len(s["grades"]))
    top_avg = sum(top_student["grades"]) / len(top_student["grades"])
    print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg:.1f}.")

def main():
    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_student()
            elif choice == 2:
                add_grades()
            elif choice == 3:
                show_report()
            elif choice == 4:
                find_top_student()
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please select from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
