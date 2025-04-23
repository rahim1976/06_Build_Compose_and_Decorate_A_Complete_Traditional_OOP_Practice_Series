class Logger:
    def __init__(self):
        print("Logger object created!")

    def __del__(self):
        print("Logger object destroyed!")

# Testing
log1 = Logger()
del log1  # Explicitly destroy to see destructor