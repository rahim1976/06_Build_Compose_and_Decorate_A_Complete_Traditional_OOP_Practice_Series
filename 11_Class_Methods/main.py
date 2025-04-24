class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Test the class
book1 = Book("Python 101")
book2 = Book("Data Science")
print(f"Total books: {Book.total_books}")