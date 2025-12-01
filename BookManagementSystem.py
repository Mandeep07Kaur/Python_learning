books = [
    {"title": "Kiki", "available": True},
    {"title": "Rara", "available": False},
    {"title": "Pupi", "available": True}
]

def add_books(books, title):
    new_book = {"title": title, "available": True}
    books.append(new_book)
    return books

def borrow_book(books, title):
    for book in books:
        if book["title"] == title:
            if book["available"] == True:
                book["available"] = False         # FIXED
                print("Book borrowed")
                return books
            else:
                print("Book already borrowed")
                return books
    print("Book not found")
    return books

def return_book(books, title):
    for book in books:
        if book["title"] == title:
            book["available"] = True             # FIXED
            print("Book returned")
            return books
    print("Book not found")
    return books

def list_unavailable(books):
    unavailable_titles = []
    for book in books:
        if book["available"] == False:           # FIXED
            unavailable_titles.append(book["title"])
    return unavailable_titles

print(books)
borrow_book(books, "Pupi")
print(list_unavailable(books))
