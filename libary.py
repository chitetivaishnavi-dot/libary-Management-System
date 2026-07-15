import json
import os

FILE_NAME = "library.json"

def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists.")
            return

    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))

    books.append({
        "id": book_id,
        "name": name,
        "author": author,
        "quantity": quantity,
        "issued": 0
    })

    save_books(books)
    print("Book Added Successfully.")

def view_books():
    books = load_books()

    if not books:
        print("No Books Found.")
        return

    print("\nLibrary Books\n")

    for book in books:
        print(f"Book ID   : {book['id']}")
        print(f"Book Name : {book['name']}")
        print(f"Author    : {book['author']}")
        print(f"Available : {book['quantity']}")
        print(f"Issued    : {book['issued']}")
        print("-" * 30)

def search_book():
    books = load_books()

    keyword = input("Enter Book Name: ").lower()

    found = False

    for book in books:
        if keyword in book["name"].lower():
            print(book)
            found = True

    if not found:
        print("Book Not Found.")

def issue_book():
    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            if book["quantity"] > 0:
                book["quantity"] -= 1
                book["issued"] += 1
                save_books(books)
                print("Book Issued Successfully.")
                return
            else:
                print("Book Not Available.")
                return

    print("Book ID Not Found.")

def return_book():
    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            if book["issued"] > 0:
                book["issued"] -= 1
                book["quantity"] += 1
                save_books(books)
                print("Book Returned Successfully.")
                return
            else:
                print("No Book Issued.")
                return

    print("Book ID Not Found.")

def delete_book():
    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_books(books)
            print("Book Deleted Successfully.")
            return

    print("Book ID Not Found.")

while True:

    print("""
=====================================
      LIBRARY MANAGEMENT SYSTEM
=====================================

1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit

=====================================
""")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        print("Thank You...")
        break
    else:
        print("Invalid Choice.")