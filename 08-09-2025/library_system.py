class Library:
    def __init__(self,books):
        self.books=books
    def borrow(self,title):
        if self.books[title]>=1:
            self.books[title]-=1
            print("Borrowed successfully.")
        else:
            print("Stock not available")
    def return_book(self,title):
        if title in self.books:
            self.books[title]+=1
            print("Stock Increased")
        else:
            print("New Stock arrived")
    def show_books(self):
        print(self.books)
lib = Library({"Python 101": 3, "Data Science": 2})
print(lib.borrow("Python 101"))
print(lib.return_book("Data Science"))
lib.show_books()