print("Library Management System")

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self,title):
        self.books.append(Book(title))
        print("Book added")
        
    def borrow_book(self,title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book borrowed")
                return
            print("Book not available")