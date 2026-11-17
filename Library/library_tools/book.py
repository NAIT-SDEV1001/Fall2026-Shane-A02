class Book:
    def __init__(self,title:str, author:str, pages:int, price:float)->None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    #override __str__
    def __str__(self) ->str:
        return f"{self.title} by {self.author}"

    #when comparing objects we need to override __eq__ to define what equals means
    #we will say a book is the same if the author AND title are the same
    def __eq__(self, other:Book)->bool:
        return self.title == other.title and self.author == other.author    

# book1 = Book('a','b',100,23)
# book2 = Book('c','d',100,23)
# book3 = Book('c','d',100,23)

# books = [book1,book2,book3]

# print (book1 == book3)
# #comparing objects also could happen with IN
# test_book = Book('c','j',200,11)
# print (test_book in books)


    

# print(Book('a','b',100,23))

