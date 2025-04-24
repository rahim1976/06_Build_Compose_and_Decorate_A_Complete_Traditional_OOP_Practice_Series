class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee 

    def show_employee(self):
        return f"Department: {self.dept_name}, Employee: {self.employee.name}"

# Test the class
emp = Employee("Rahim")
dept = Department("IT", emp)
print(dept.show_employee())