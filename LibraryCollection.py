class Book:
    def __init__(self, title, author, genre, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id


class BorrowedBook:
    def __init__(self, book, member, due_date):
        self.book = book
        self.member = member
        self.due_date = due_date


# Books
books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
    Book("1984", "George Orwell", "Dystopian"),
    Book("To Kill a Mockingbird", "Harper Lee", "Classics"),
    Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy")
]

members = [
    Member("Abdullah", 101),
    Member("Ahad", 102),
    Member("Talha", 103)
]

borrowed_books = [
    BorrowedBook(books[0], members[0], "2023-01-15"),
    BorrowedBook(books[2], members[1], "2023-01-20"),
    BorrowedBook(books[3], members[2], "2023-01-10")
]

print("Available Books:")
for book in books:
    if book.available:
        print(f"{book.title} by {book.author} - Genre: {book.genre}")

print("\nBorrowed Books:")
for borrowed_book in borrowed_books:
    print(f"{borrowed_book.book.title} borrowed by {borrowed_book.member.name}, Due date: {borrowed_book.due_date}")

print("\nLibrary Members:")
for member in members:
    print(f"Name: {member.name} - Member ID: {member.member_id}")
