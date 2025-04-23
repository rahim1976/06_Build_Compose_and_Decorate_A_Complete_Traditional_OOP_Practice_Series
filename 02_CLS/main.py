class Counter:
    count = 0 

    def __init__(self):
        Counter.count += 1  # Increment count when a new object is created

    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")
        
# Testing
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
Counter.display_count() 