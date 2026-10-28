from app import add_book, view_books

def test_add_and_view_books():
    books_list = view_books()
    books_list.clear()
    
    add_book("Test Book")
    
    assert len(books_list) == 1
    assert books_list[0]["title"] == "Test Book"
    assert books_list[0]["issued"] == False
