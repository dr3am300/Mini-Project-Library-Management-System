from UserOperations import UserOperations
from BookOperations import BookOperations
from AuthorOperations import AuthorOperations



def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            BookOperations.book_menu()
        elif choice == '2':
            UserOperations.user_menu()
        elif choice == '3':
            AuthorOperations.author_menu()
        elif choice == '4':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()











    
        
    
        
        
        
        
        