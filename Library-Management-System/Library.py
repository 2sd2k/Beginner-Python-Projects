from turtle import title
from Book import Book
class Library:
    def __init__(self, library_name, books, members, librarians, transactions):
        self.library_name = library_name
        self.books = books # list
        self.members = members # list
        self.librarians = librarians # list
        self.transactions = transactions # list
        
    # If book already in collection, 
    def add_book(self, book: Book):
        # Add book to collection
        if book not in self.books:
            self.books.append(book)
            print(F"'{book.title}' successfully added")
            return True
        print(f"Error: '{book.title} already in library'")
        return False
        
    # Find book_id in self.books, ensure all copies are available. Remove book from the list
    # @return True if successfully removed book from list, false otherwise
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available_copies == book.toal_copies:
                    self.books.remove(book)
                    print(f"{book.title} successfully removed from library")
                    return True
                else:
                        print(f"Cannot remove '{book.title}': {book.total_copies - book.available_copies} copy(ies) currently borrowed")
                        return False
        print(f"'{book.title}' could not be found in library")
        return False
    
    # Check if member already member, then add to members list
    # @return True if successfully added, false otherwise
    def add_member(self, member):
        if member in self.members:
            print(f"{member.name} is already a member")
            return False
        self.members.append(member)
        print(f"Congratulations! {member.name} has become a member!")
        return True
    
    # Find member in members list, then remove
    def remove_member(self, member_id):
        
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"Successfully removed {member_id}. Sad to see you go :(")
                return True
        print(f"Could not find {member_id} in members list")
        return False
    
    # Add librarian to librarians list
    def add_librarian(self, librarian):
        if librarian in self.librarians:
            print(f"{librarian.name} is already a librarian")
            return False
        self.librarians.append(librarian)
        print(f"Congratulations! {librarian.name} is now a librarian")
        return True

    # Search for book
    def find_book(self, book_id=None, title=None):
        
    
                
            