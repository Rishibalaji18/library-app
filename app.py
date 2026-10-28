books = []

def add_book(title):
    books.append({"title": title, "issued": False})
    return f"Book added: {title}"

def view_books():
    return books

if __name__ == "__main__":
    print("--- Library System Started ---")
    print(add_book("Python Basics"))
    print("Current Books:", view_books())
