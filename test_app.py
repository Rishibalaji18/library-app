from app import add_book, view_books, issue_book

def test_add_and_view_books():
    books_list = view_books()
    books_list.clear()
    add_book("Test Book")
    assert len(books_list) == 1
    assert books_list[0]["title"] == "Test Book"

def test_issue_book():
    books_list = view_books()
    books_list.clear()
    add_book("DevOps Guide")
    
    result = issue_book("DevOps Guide")
    assert result == "Book issued: DevOps Guide"
    assert books_list[0]["issued"] == True