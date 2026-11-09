from .book import Book

class Library:
    def __init__(self, name: str)->None:
        self.name = name
        self.books = []

    def __str__(self) -> str:
        return f"{self.name}"
    
    #method to add books to the library
    def add_book(self, book: Book)->None:
        self.books.append(book)

    def list_books(self)->None:
        print("Books in library:")
        if not self.books:
            print("No books in library")

        for book in self.books:
            print (book)    

#Method to search for a book by title
#if found return the book object
#otherwise return None
    def find_book(self,title: str)->Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None