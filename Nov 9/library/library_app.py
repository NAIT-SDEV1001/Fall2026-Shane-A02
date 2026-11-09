from library_tools.book import Book
from library_tools.library import Library


def main():
    library = Library("Not a library")
    print (library)
    
    library.add_book(Book('a','b',100,200))
    library.add_book(Book('c','d',1200,100))
    library.add_book(Book('e','f',200,400))
    library.list_books()

    #search for book
    result = library.find_book('z')
    if result is None:
        print("Book not found")
    else:
        print(f"Found: {result}")

if __name__ == '__main__':
    main()