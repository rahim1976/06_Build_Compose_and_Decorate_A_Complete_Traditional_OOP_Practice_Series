class Engine:
    def start(self):
        return "Engine started!"

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine
    
    def start_engine(self):
        return self.engine.start()

# Testing
engine = Engine()
car = Car("Bmw", engine)
print(car.start_engine())