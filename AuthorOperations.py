
class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

class AuthorOperations:
    authors = []

    
    def add_author():
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        author = Author(name, biography)
        AuthorOperations.authors.append(author)
        print("Author added successfully.")

    
    def view_author_details():
        name = input("Enter author name: ")
        for author in AuthorOperations.authors:
            if author.get_name() == name:
                print(f"Name: {author.get_name()}")
                print(f"Biography: {author.get_biography()}")
                return
        print("Author not found.")

    
    def display_all_authors():
        for author in AuthorOperations.authors:
            print(f"Name: {author.get_name()}")

    
    def author_menu():
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            
            choice = input("Select an option: ")
            
            if choice == '1':
                AuthorOperations.add_author()
            elif choice == '2':
                AuthorOperations.view_author_details()
            elif choice == '3':
                AuthorOperations.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
