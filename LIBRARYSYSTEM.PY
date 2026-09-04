class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added successfully")
    def show_books(self):
        if not self.books:
            print("No Books available in the library")
            return
        print("\n========== Book List ==========")
        for book in self.books:
            status = "Issued" if book.issued else "Available"
            print(f"Title: {book.title}  |  Author: {book.author}  |  Status: {status}")
    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.issued:
                    book.issued = True
                    print(f"'{book.title}' issued successfully")
                    return
                else:
                    print(f"'{book.title}' is already issued")
                    return
        print("Book is not Found")
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.issued:
                    book.issued = False
                    print(f"'{book.title}' returned succesfully")
                    return
                else:
                    print(f"'{book.title}' was not issued")
                    return
        print("Book is not Found")
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                status = "Issued" if book.issued else "Available"
                print("\nBook Found")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Status: {book.status}")
                return
        print("Book is not Found")
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"'{book.title}' removed successfully")
                return
        print("Book is not Found")
library = Library()
while True:
    print("\n=============== LIBRARY MANAGEMENT SYSTEM ===============")
    print("1: Add Book")
    print("2: Show Books")
    print("3: Issue Book")
    print("4: Return Book")
    print("5: Search Book")
    print("6: Remove Book")
    print("7: Exit")
    choice = input("Enter your Choice")
    if choice == "1":
        title = input("Enter the Book Title: ")
        author = input("Enter Author Name: ")
        book = Book(title, author)
        library.add_book(book)
    elif choice == "2":
        library.show_books()
    elif choice == "3":
        title = input("Enter Book Title to Issue: ")
        library.issue_book(title)
    elif choice == "4":
        title = input("Enter Book Title to Return: ")
        library.return_book(title)
    elif choice == "5":
        title = input("Enter Book Title to Search: ")
        library.search_book(title)
    elif choice == "6":
        title = input("Enter Book Title to Remove: ")
        library.remove_book(title)
    elif choice == "7":
        print("Thank you for using Library Management System")
        break