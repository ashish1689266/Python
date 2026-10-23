class Book:

    def __init__(self, title, author):

        self.title = title

        self.author = author

        self.is_borrowed = False

    def borrow(self):

        if self.is_borrowed is False:

            print("Your book is available, book borrowed!")

        else:

            print("Book unavailable!")

    def return_book(self):

        self.is_borrowed = False

        print("Book returned!")

book_1 = Book("IT", "Stephen King")

book_2 = Book("Shawshank Redemption", "Stephen King")

book_3 = Book("The Discovery of India", "Jawaharlal Nehru")

Books = [book_1, book_2, book_3]

book_1.borrow()

book_2.borrow()

book_3.borrow()

book_1.return_book()

book_2.return_book()

book_3.return_book()