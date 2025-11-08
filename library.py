print("Library Management System")
print(">>")
print("Input Command: l= list, a=add, s=search, b=borrow, r=return, d=delete, q=quit")
n = input("Enter command: ")
library = [
{"title": "Python Basics", "author": "John Doe", "year": 2020, "available": True},
{"title": "Data Science Handbook", "author": "Jane Smith", "year": 2018, "available": False}
]
# while n != "q":
if n == "l":
    for i, book in enumerate(library, start=1):
        status = "Available" if book["available"] else "Borrowed"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {status}")
        
elif n == "a":
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = int(input("Enter publication year: "))
    library.append({"title": title, "author": author, "year": year, "available": True})
    print(f'Book "{title}" added to the library.')
elif n == "s":
    search_title = input("Enter book title to search: ")
    found = False
    for book in library:
        if book["title"].lower() == search_title.lower():
            status = "Available" if book["available"] else "Borrowed"
            print(f'Found: {book["title"]} by {book["author"]} ({book["year"]}) - {status}')
            found = True
            break
    if not found:
        print("Book not found.")
elif n == "b":
    borrow_title = input("Enter book title to borrow: ")
    for book in library:
        if book["title"].lower() == borrow_title.lower():
            if book["available"]:
                book["available"] = False
                print(f'You have borrowed "{book["title"]}".')
            else:
                print(f'Sorry, "{book["title"]}" is currently borrowed.')
            break
    else:
        print("Book not found.")
elif n == "r":
    return_title = input("Enter book title to return: ")
    for book in library:
        if book["title"].lower() == return_title.lower():
            if not book["available"]:
                book["available"] = True
                print(f'You have returned "{book["title"]}".')
            else:
                print(f'"{book["title"]}" was not borrowed.')
            break
    else:
        print("Book not found.")
elif n == "d":
    delete_title = input("Enter book title to delete: ")
    for i, book in enumerate(library):
        if book["title"].lower() == delete_title.lower():
            del library[i]
            print(f'Book "{delete_title}" has been deleted from the library.')
            break
    else:
        print("Book not found.")
elif n == "q":
    print("Exiting the Library Management System.")
    
# print(library[0])