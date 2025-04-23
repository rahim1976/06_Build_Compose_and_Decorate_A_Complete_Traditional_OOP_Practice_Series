class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # Public variable
        self._salary = salary      # Protected variable
        self.__ssn = ssn           # Private variable

# Test the class
emp = Employee("Rahim", 50000, "444-555-1234")
print("Public name:", emp.name)         # Access public variable
print("Protected _salary:", emp._salary) # Access protected variable
try:
    print("Private __ssn:", emp.__ssn)   # Try accessing private variable
except AttributeError as e:
    print("Error accessing __ssn:", e)