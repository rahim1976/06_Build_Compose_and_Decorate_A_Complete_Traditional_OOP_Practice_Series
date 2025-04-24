class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Testing
result = TemperatureConverter.celsius_to_fahrenheit(39)
print(f"39°C in Fahrenheit: {result}")