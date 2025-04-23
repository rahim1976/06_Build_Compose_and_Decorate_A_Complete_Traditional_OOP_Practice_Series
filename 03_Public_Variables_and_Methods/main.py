class Car:
    def __init__(self, brand):
        self.brand = brand 
    
    def start(self):  
        print(f"The {self.brand} car is starting!")

# Test the class
car1 = Car("Bmw")
print(car1.brand)
car1.start()      