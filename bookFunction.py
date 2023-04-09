from modelBook import Book

def pBook(book):
    print(f"ISBN NO:{book.isbn_no}, Title:{book.title}, Format:{book.format}, Subject:{book.subject}"
        f" Rental:{book.rental}, Coopies:{book.copy}")

class Book_Class:
    def __init__(self):
      self.list_of_books=[]
      self.data()

    def data(self):
        book_1= Book(isbn_no="ISBN1234", title="The Solar System", book_format="Hardcover", subject="Science",
                     rental=15.00, copy=5)
        self.list_of_books.append(book_1)
        book_2= Book(isbn_no="ISBN9876", title="Types of Animal Species", book_format="Paperback", subject="Science",
                     rental=10.00, copy=8)
        self.list_of_books.append(book_2)
        book_3= Book(isbn_no="ISBN1290", title="Second World War", book_format="Hardcover", subject="History",
                     rental=12.50, copy=1)
        self.list_of_books.append(book_3)

    def add(self):
        isbn=input("Enter ISBN No:")
        title=input("Enter title of book:")
        format=input("Enter format of book:")
        subject=input("Enter Subject of book:")
        try:
            rental=float(input("Enter rental price of book per day:"))
        except ValueError:
            print("Invaild rental price so please enter crectly!!!")
            return()
        try:
            copy = int(input("Enter copy of book:"))
        except ValueError:
            print("Invaild copy so please enter crectly!!!")
            return ()

        book= Book(isbn_no=isbn, title=title, book_format=format, subject=subject, rental=rental, copy=copy)
        self.list_of_books.append(book)
        print("Book added to our libary")

    def remove(self):
        isbn=input("Enter valid ISBN No to remove book:")
        match_data=list(item for item in self.list_of_books if item.isbn_no == isbn)
        for x in match_data:
            self.list_of_books.remove(x)
            print("Book removed from our libary")



    def show_available(self):
        match_data=list(item for item in self.list_of_books if item.copy > 0)
        for x in match_data:
            pBook(x)
    def show_unavailable(self):
        match_data=list(item for item in self.list_of_books if item.copy == 0)
        if len(match_data) > 0:
            for x in match_data:
               pBook(x)
        else:
            print("all Books are availble")

    def show_lend(self):
        isbn=input("Enter ISBN to lend the book:")
        copies=int(input("Enter copies you want:"))
        match_data=list(item for item in self.list_of_books if item.isbn_no == isbn)
        for x in match_data:
            x.copy-=copies
            print("Book lent")

    def show_receive(self):
        isbn=input("Enter ISBN No to revive Book:")
        copies=int(input("Enter copies:"))
        match_data=list(item for item in self.list_of_books if item.isbn_no == isbn)
        for x in match_data:
            x.copy+=copies
            print("Book received")


    def search_by_subject(self):
        subject_name = input("enter subject to filter:")
        matched_data = list(item for item in self.list_of_books if item.subject == subject_name)
        if len(matched_data) > 0:
            for x in matched_data:
                pBook(x)


