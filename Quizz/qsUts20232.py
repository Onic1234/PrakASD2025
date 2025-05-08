# # Here you need to make a program to design the system scenario in the library with object oriented programming concept. Here several instructions of the case study. 
# a. Create a "Book" class which has two attributes including book title and author name.
# b. Create a "Library" class with an attribute which is a list of book, and three different methods including adding a book, removing a book, and displaying the list of books. 
# c. Add a new method to the "Library" class to search the book by its author name.. 
# d. Demonstrate the functionality of your book management system by creating a "Library" object, adding some Book objects to it, searching for a book by title or author name, and removing a book from the library.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"
    def __repr__(self):
        return f"Book({self.title}, {self.author})"
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")
    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            print(book)
    def search_by_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if not found_books:
            print(f"No books found by author '{author}'.")
            return
        print(f"Books by author '{author}':")
        for book in found_books:
            print(book)
# Example usage
library = Library()
book1 = Book("To Kill a Mockingbird", "Harper Lee")
# book2 = Book("1984", "George Orwell")
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
# book4 = Book("Brave New World", "Aldous Huxley")
library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# library.add_book(book4)
# library.display_books()
# library.remove_book("1984")
# library.display_books()
# library.search_by_author("Harper Lee")
# library.search_by_author("J.K. Rowling")
# library.remove_book("The Catcher in the Rye")
library.display_books()
