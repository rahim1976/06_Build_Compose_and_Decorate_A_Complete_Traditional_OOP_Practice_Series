class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Testing
prod = Product("Computer", 10000)
print(prod.price)  # Get price
prod.price = 8000  # Set price
print(prod.price)  # Get updated price
del prod.price     # Delete price
try:
    print(prod.price)  # Try accessing deleted price
except AttributeError as e:
    print(f"Error: {e}")