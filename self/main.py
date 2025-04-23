class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

student1 = Student("Rahim", 85)
student1.display()
student2 = Student("Ali", 90)
student2.display()