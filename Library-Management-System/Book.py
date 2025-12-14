class Book:
    def __init__(
        self, book_id, title, author, publisher, publication_year, genre, total_copies
    ):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_year = publication_year
        self.genre = genre
        self.total_copies = total_copies
        self.available_copies = total_copies

    # @return - boolean
    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    # @return - boolean
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def is_available(self):
        return self.available_copies > 0

    def update_copies(self, new_total):
        self.total_copies = new_total

    # Show book details
    def display_info(self):
        print("=" * 40)
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publisher: {self.publisher}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Genre: {self.genre}")
        print(f"Total Copies: {self.total_copies}")
        print(f"Available Copies: {self.available_copies}")
        print("=" * 40)

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.available_copies}/{self.total_copies})"
