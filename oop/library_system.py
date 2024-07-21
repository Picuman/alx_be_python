class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook - Title: {book.title}, Author: {book.author}, File Size: {book.file_size}")
            elif isinstance(book, PrintBook):
                print(f"PrintBook - Title: {book.title}, Author: {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book):
                print(f"Book - Title: {book.title}, Author: {book.author}")

