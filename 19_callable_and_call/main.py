class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, number):
        return self.factor * number

# Testing
multiplier = Multiplier(3)
print(callable(multiplier))  # Check if object is callable
result = multiplier(5)       # Call object like a function
print(result)