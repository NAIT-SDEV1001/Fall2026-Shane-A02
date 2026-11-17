from .book import Book#from the book module import the Book class

class Library:
    def __init__(self,name:str)->None:
        self.name = name
        self.books = []

    def __str__(self)->str:
        return f"{self.name}"

    #method to add a book to the library
    def add_book(self,book:Book)->None:        
        self.books.append(book)

    def list_books(self)->None:
        print("Books in library")
       
        if not self.books:
            print("No books in library")
            
        for book in self.books:
            print(book)

    #method to search for a book by its title
    #if found, return the book object
    #otherwise, return None
    def find_book(self,title:str)->Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None


# my_library = Library("Bell's books")
# my_library.add_book(Book('a','b',100,22))
# my_library.add_book(Book('c','D',100,22))
# my_library.add_book(Book('e','f',100,22))

# # my_library.list_books()

# print (my_library.find_book('c'))





