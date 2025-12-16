from Book import Book


class Person:

    def __init__(self, name, email, person_id, phone_number, address):
        self.name = name
        self.email = email
        self.person_id = person_id
        self.phone_number = phone_number
        self.address = address

    def update_contact_info(self, email=None, phone_number=None, address=None):
        if email:
            self.email = email
        if phone_number:
            self.phone_number = phone_number
        if address:
            self.address = address

    # Print details of self
    def display_info(self):
        print("=" * 40)
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Person ID: {self.person_id}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Address: {self.address}")
        print("=" * 40)

    # string
    def __str__(self):
        return f"Person(Name: {self.name}, Email: {self.email}, Person ID: {self.person_id}, Phone Number: {self.phone_number}, Address: {self.address})"


class Member(Person):
    def __init__(
        self,
        name,
        email,
        person_id,
        phone_number,
        address,
        member_id,
        membership_date,
        membership_type,
        max_books_allowed,
    ):
        super().__init__(name, email, person_id, phone_number, address)
        self.member_id = member_id
        self.membership_date = membership_date
        self.borrowed_books = []
        self.membership_type = membership_type  # Standard or Prenium
        self.max_books_allowed = 5

    # Add book to borrowed_books
    def borrow_book(self, book: Book):
        if len(self.borrowed_books) < self.max_books_allowed:
            book.borrow()
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        book.return_book()

    def upgrade_membership(self):

        if self.membership_type == "Standard":
            self.membership_type = "Premium"
            self.max_books_allowed = 10
            print(f"{self.name} has successfully been upgraded to Premium")
            return True
        else:
            print(f"{self.name} is already a Premium member")
            return True

    def downgrade_membership(self):

        if self.membership_type == "Premium":
            self.membership_type = "Standard"
            self.max_books_allowed = 5
            print(f"{self.name} has successfully downgraded to Standard")
            return True
        else:
            print(f"{self.name} is already a Standard member")
            return False

    def can_borrow(self):
        return len(self.borrowed_books) < self.max_books_allowed

    def view_borrowed_books(self):
        if not self.borrowed_books:
            print("No books borrowed")
        else:
            print(f"\n{self.name}'s Borrowed Books:")
            print(f"=" * 40)
            for i, book in enumerate(self.borrowed_books, 1):
                print(f"{i}. {book}")  # Uses book's __str__()
            print(f"=" * 40)
            

    def calculate_fine(self, days_overdue):
        fine_rate = 0.50  # $0.50 per day
        return days_overdue * fine_rate

    def display_info(self):
        print("=" * 40)
        print("MEMBER INFORMATION")
        print("=" * 40)
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Person ID: {self.person_id}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Address: {self.address}")
        print("-" * 40)
        print(f"Member ID: {self.member_id}")
        print(f"Membership Date: {self.membership_date}")
        print(f"Membership Type: {self.membership_type}")
        print(f"Max Books Allowed: {self.max_books_allowed}")
        print(f"Currently Borrowed: {len(self.borrowed_books)} book(s)")
        print("=" * 40)

    def __str__(self):
        return f"Member: {self.name} ({self.membership_type}, ID: {self.member_id})"

class Librarian(Person):
    
    def __init__(self, name, email, person_id, phone_number, address, employee_id, hire_date, salary, shift):
        super().__init__(name, email, person_id, phone_number, address)
        self.employee_id = employee_id
        self.hire_date = hire_date
        self.salary = salary
        self.shift = shift
    
    def add_book_to_library(self, library, book):
        