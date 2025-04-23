class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable
    
    def start(self):  # Public method
        print(f"The {self.brand} car is starting!")

# Test the class
car1 = Car("Bmw")
print(car1.brand)  # Access public variable
car1.start()      # Access public method