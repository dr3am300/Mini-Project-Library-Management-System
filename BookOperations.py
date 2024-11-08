class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_borrowed = False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def is_borrowed(self):
        return self.__is_borrowed

    def borrow(self):
        self.__is_borrowed = True

    def return_book(self):
        self.__is_borrowed = False

class BookOperations:
    books = []

    
    def add_book():
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        publication_date = input("Enter publication date (YYYY-MM-DD): ")
        import re
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", publication_date):
            print("Invalid date format. Please try again.")
            return
        book = Book(title, author, genre, publication_date)
        BookOperations.books.append(book)
        print("Book added successfully.")

    
    def borrow_book():
        title = input("Enter book title to borrow: ")
        for book in BookOperations.books:
            if book.get_title() == title and not book.is_borrowed():
                book.borrow()
                print("Book borrowed successfully.")
                return
        print("Book not available or already borrowed.")

    
    def return_book():
        title = input("Enter book title to return: ")
        for book in BookOperations.books:
            if book.get_title() == title and book.is_borrowed():
                book.return_book()
                print("Book returned successfully.")
                return
        print("Book not found or not borrowed.")

    
    def search_book():
        title = input("Enter book title to search: ")
        for book in BookOperations.books:
            if book.get_title() == title:
                print(f"Title: {book.get_title()}")
                print(f"Author: {book.get_author()}")
                print(f"Genre: {book.get_genre()}")
                print(f"Publication Date: {book.get_publication_date()}")
                print(f"Status: {'Borrowed' if book.is_borrowed() else 'Available'}")
                return
        print("Book not found.")

    
    def display_all_books():
        for book in BookOperations.books:
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, Status: {'Borrowed' if book.is_borrowed() else 'Available'}")

    
    def book_menu():
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            
            choice = input("Select an option: ")
            
            if choice == '1':
                BookOperations.add_book()
            elif choice == '2':
                BookOperations.borrow_book()
            elif choice == '3':
                BookOperations.return_book()
            elif choice == '4':
                BookOperations.search_book()
            elif choice == '5':
                BookOperations.display_all_books()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
        
        
    
    
