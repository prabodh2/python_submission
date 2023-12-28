class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def get_employee_details(self):
        return f"Employee ID: {self.emp_id}\nEmployee Name: {self.emp_name}\nEmployee Salary: {self.emp_salary}"

    def print_employee_details(self):
        print(self.get_employee_details())

# Create an Employee object
employee1 = Employee(emp_id=101, emp_name="John Doe", emp_salary=50000)

# Get and print employee details
employee1.print_employee_details()
