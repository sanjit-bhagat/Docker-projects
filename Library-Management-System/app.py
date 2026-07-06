# -------------------------------
# Simple Library Management System
# -------------------------------

class Book:
    def __init__(self, title):
        self.title = title
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self, title):
        new_book = Book(title)
        self.books.append(new_book)
        print(f"\n✅ '{title}' added successfully.")

    # Show Available Books
    def show_books(self):
        print("\n📚 Available Books")

        available = False

        for book in self.books:
            if book.is_available:
                print(f"- {book.title}")
                available = True

        if not available:
            print("No books available.")

    # Borrow Book
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False
                print(f"\n✅ You borrowed '{title}'.")
                return

        print(f"\n❌ '{title}' is not available.")

    # Return Book
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.is_available = True
                print(f"\n✅ You returned '{title}'.")
                return

        print(f"\n❌ '{title}' was not borrowed.")


# -------------------------------
# Main Program
# -------------------------------

library = Library()

while True:

    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        library.add_book(title)

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)

    elif choice == "4":
        title = input("Enter book title to return: ")
        library.return_book(title)

    elif choice == "5":
        print("\nThank you for using the Library Management System.")
        break

    else:
        print("\n❌ Invalid choice. Please try again.")
