class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__total_copies = total_copies
        self.__available_copies = total_copies

    def borrow_book(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print("Book borrowed successfully.")
        else:
            print("No copies available.")

    def return_book(self):
        if self.__available_copies < self.__total_copies:
            self.__available_copies += 1
            print("Book returned successfully.")
        else:
            print("All copies are already in the library.")

    def display_details(self):
        print("Book ID :", self.__book_id)
        print("Title :", self.__title)
        print("Author :", self.__author)
        print("Available Copies :", f"{self.__available_copies}/{self.__total_copies}")
        print()




book1 = Book(101, "Python Programming", "Pavan Kumar", 3)

# 1. Display details
book1.display_details()

# 2. Borrow twice
book1.borrow_book()
book1.borrow_book()

# 3. Display details
book1.display_details()

# 4. Borrow twice
book1.borrow_book()
book1.borrow_book()

# 5. Return once
book1.return_book()

# 6. Display details
book1.display_details()