class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        self.__borrowed_books.remove(book_title)

class UserOperations:
    users = []

    
    def add_user():
        name = input("Enter user name: ")
        library_id = input("Enter library ID using the format 'L-XXXX' where X is a digit: ")
        import re
        format_valid = re.match(r"^L-\d{4}$", library_id)
        if not format_valid:
            print("Invalid library ID format. Please try again.")
            return
        for user in UserOperations.users:
            if user.get_library_id() == library_id:
                print("Library ID already exists. Please try again.")
                return
        user = User(name, library_id)
        UserOperations.users.append(user)
        print("User added successfully.")

    
    def view_user_details():
        library_id = input("Enter library ID using the format 'L-XXXX' where X is a digit: ")
        import re
        format_valid = re.match(r"^L-\d{4}$", library_id)
        if not format_valid:
            print("Invalid library ID format. Please try again.")
            return
        for user in UserOperations.users:
            if user.get_library_id() == library_id:
                print(f"Name: {user.get_name()}")
                print(f"Borrowed Books: {', '.join(user.get_borrowed_books())}")
                return
        print("User not found.")

    
    def display_all_users():
        for user in UserOperations.users:
            print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}")

    
    def user_menu():
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            
            choice = input("Select an option: ")
            
            if choice == '1':
                UserOperations.add_user()
            elif choice == '2':
                UserOperations.view_user_details()
            elif choice == '3':
                UserOperations.display_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

            