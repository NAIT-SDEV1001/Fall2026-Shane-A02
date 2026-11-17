from library_tools.book import Book
from library_tools.library import Library

def main():
    my_library = Library("Books R Fun")
    print (my_library)

    my_library.add_book(Book('a','b',100,22))
    my_library.add_book(Book('c','D',100,22))
    my_library.add_book(Book('e','f',100,22))

    my_library.list_books()

    #search for book by title
    result = my_library.find_book('e')
    if result is None:
        print("Book not found")
    else:
        print(f"Found: {result}")
    
    
if __name__ == '__main__':
    main()