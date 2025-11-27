class SGrades:
    def __init__(self):
        """creates empty data structures for students data
        """
        self.students = []

  
    


    def findstudent(self, name: str):
        """ finding student by name"""
        
        
        stud = name.strip().lower()
        
        for st in self.students:
        
            if st["name"].lower() == stud:
                return st
        
        return None


    def addstud_to_dict(self, name: str):
        """adds student, doesnt return any"""
        val_name = self.checkname(name)
        if val_name is None:
            return

        if self.findstudent(val_name):
            print(f"Student {val_name} already exist!")
            return

        self.students.append({"name": val_name, "grades": []})
        
        print(f"Student {val_name} added!")

    
    @staticmethod
    
    
    def checkname(name: str):
        """Verifies the student's name """

        if not name or not name.strip():
            print("The name can't be empty!")
            return None

        parts = name.strip().split()

        if any(any(ch.isdigit() for ch in word) for word in parts):
            print("The name must not contain numbers")
            return None

        extra = set(" -'")

        if any(not (ch.isalpha() or ch in extra) for ch in name):
            print("The name contains invalid characters")
            return None

        return " ".join(x.capitalize() for x in parts)
    

    


    def studentsGet(self):
        """displays student averages and statistics.
        no return 
        """
        if not self.students:
            print("There is no list of students")
            return

        averages = []

        for student in self.students:
            if student["grades"]:
                avg = sum(student["grades"]) / len(student["grades"])
                averages.append(avg)
                print(f"{student['name']}`s average grade is {avg:.1f}.")
            else:
                print(f"{student['name']}`s average grade is: N/A.")

        if not averages:
            print("No grades to analyze!")
            return
        print("-" * 28)
        print(f"Max average: {max(averages):.1f}")
        print(f"Min average: {min(averages):.1f}")
        print(f"Overall average: {sum(averages) / len(averages):.1f}")

    def addgrade(self, name: str):
        """add grades to students args : name
        """
        student = self.findstudent(name)
        if not student:
            print(f"Student {name} not exist!")
            return False

        while True:
            newgrade = input("Enter the grade (or 'done' to finish): ").lower().strip()

            if newgrade == "done":
                print("The input of ratings is completed")
                break

            try:
                grade = int(newgrade)

                if not (0 <= grade <= 100):
                    print("The grade must be between 0 and 100!")
                    continue

                student["grades"].append(grade)
                print(f"Grade {grade} added for {student['name']}")

            except ValueError:
                print("Invalid input. Please enter a number.")

        return True
    
    def beststudent(self):
        """ find best student 
        no return
        """
        gradedStudents = [x for x in self.students if x["grades"]]

        if not gradedStudents:
            print("There are no grades in the list of students!")
            return

        best_student = max(gradedStudents,key=lambda st: sum(st["grades"]) / len(st["grades"]))

        best_average = sum(best_student["grades"]) / len(best_student["grades"])
        print(f"The student with the highest average is {best_student['name']} "
              f"with a grade of {best_average:.1f}.")

    def mainloop(self):
        while True:
            print("""\n--- Student Grade Analyzer ---
        1. Add a new student
        2. Add grades for a student
        3. Generate a full report
        4. Find the top student
        5. Exit program""")

            choice = input("Enter your choice: ")
            print("- " * 11)

            if choice == "1":
                name = input("Input the name of the new student: ")
                self.addstud_to_dict(name)

            elif choice == "2":
                name = input("Add grades for a student: ")
                self.addgrade(name)

            elif choice == "3":
                self.studentsGet()

            elif choice == "4":
                self.beststudent()

            elif choice == "5":
                print("Exiting program.")
                break

            else:
                print("Invalid option!")


if __name__ == "__main__":
    StudentsObj = SGrades()
    StudentsObj.mainloop()