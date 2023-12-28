class Student:
    # Class variable to keep track of the total number of students
    total_students = 0

    def __init__(self, name, department):
        # Instance variables
        self.name = name
        self.department = department

        # Increment the total number of students
        Student.total_students += 1

    def display_info(self):
        print(f"Name: {self.name}, Department: {self.department}")

# Example usage:
def admit_students():
    # Creating student objects and admitting them to different departments
    student1 = Student("Alice", "PGDM")
    student2 = Student("Bob", "BTech")
    student3 = Student("Charlie", "PGDM")

    # Displaying student information
    print("Admitted Students:")
    student1.display_info()
    student2.display_info()
    student3.display_info()

    # Displaying total number of students
    print(f"Total Students Admitted: {Student.total_students}")

# Admit students and display information
admit_students()
