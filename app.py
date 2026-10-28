books = []

def add_book(title):
    books.append({"title": title, "issued": False})
    return f"Book added: {title}"

def view_books():
    return books

def issue_book(title):
    for book in books:
        if book["title"] == title and not book["issued"]:
            book["issued"] = True
            return f"Book issued: {title}"
    return f"Book not available"

if __name__ == "__main__":
    print("--- Upgraded Library System ---")
    add_book("Python Basics")
    print(issue_book("Python Basics"))
    print("Current Books Status:", view_books())
