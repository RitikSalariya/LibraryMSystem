class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def list_books(self):
        if not self.books:
            print("No books in library yet ")
            return
        for i, book in enumerate(self.books, 1):
            print(f"{i}) {book}")

    def add_book(self):
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        year = input("Enter year: ").strip()
        self.books.append(Book(title, author, year))
        print("Book added successfully!")

    def search_books(self):
        term = input("Enter search term: ").strip().lower()
        found = False
        for i, book in enumerate(self.books, 1):
            if term in book.title.lower() or term in book.author.lower():
                print(f"{i}) {book.title} by {book.author} ({book.year})")
                found = True
        if not found:
            print("No matching books found.")

    def borrow_book(self):
        if not self.books:
            print("No books available to borrow.")
            return
        try:
            index = int(input("Enter book index to borrow: "))
            if 1 <= index <= len(self.books):
                book = self.books[index - 1]
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f'You borrowed "{book.title}"')
                else:
                    print("Book is already borrowed.")
            else:
                print("Invalid book index.")
        except ValueError:
            print("Invalid input, please enter a number.")

    def return_book(self):
        try:
            index = int(input("Enter book index to return: "))
            if 1 <= index <= len(self.books):
                book = self.books[index - 1]
                if book.is_borrowed:
                    book.is_borrowed = False
                    print("Book returned successfully!")
                else:
                    print("This book was not borrowed.")
            else:
                print("Invalid book index.")
        except ValueError:
            print("Invalid input, please enter a number.")

    def delete_book(self):
        try:
            index = int(input("Enter book index to delete: "))
            if 1 <= index <= len(self.books):
                book = self.books.pop(index - 1)
                print(f'Book "{book.title}" deleted successfully!')
            else:
                print("Invalid book index.")
        except ValueError:
            print("Invalid input, please enter a number.")


def main():
    library = Library()
    print("Welcome to Library Management System!")
    print("Input Command: l= list, a=add, s=search, b=borrow, r=return, d=delete, q=quit")
    while True:
        print("> ", end="")
        command = input().strip().lower()

        if command == "l":
            library.list_books()
        elif command == "a":
            library.add_book()
        elif command == "s":
            library.search_books()
        elif command == "b":
            library.borrow_book()
        elif command == "r":
            library.return_book()
        elif command == "d":
            library.delete_book()
        elif command == "q":
            print("Goodbye!")
            break
        
        
        else:
            print("Invalid command. Options: [l=list, a=add, s=search, b=borrow, r=return, d=delete, q=quit]")


if __name__ == "__main__":
    main()
