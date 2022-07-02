class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.bookmarked_page = None
    def __repr__(self):
        if self.pages == 1:
            to_be_returned = f"Book<{self.title} by {self.author}: {self.pages} page, currently on " \
                             f"page {self.current_page}"
        else:
            to_be_returned = f"Book<{self.title} by {self.author}: {self.pages} pages, currently on" \
                             f" page {self.current_page}"
        if self.bookmarked_page:
            to_be_returned += f', page {self.bookmarked_page} bookmarked'
        return to_be_returned+'>'

    def turn_page(self, amount):
        new_page = self.current_page + amount
        if 0 < new_page <= self.pages:
            self.current_page = new_page
        elif new_page < 1:
            self.current_page = 1
        else:
            self.current_page = self.pages
    def get_current_page(self):
        return self.current_page
    def place_bookmark(self):
        self.bookmarked_page = self.current_page
    def turn_to_bookmark(self):
        if self.bookmarked_page:
            self.current_page = self.bookmarked_page
    def remove_bookmark(self):
        self.bookmarked_page = None
    def get_bookmarked_page(self):
        return self.bookmarked_page
    def __eq__(self, other):
        if isinstance(other, Book):
            self_attributes = self.title, self.author,self.pages, self.current_page, self.bookmarked_page
            other_attributes = other.title, other.author,other.pages, other.current_page, other.bookmarked_page
            if self_attributes == other_attributes:
                return True
        return False
def test_book_class():
    print("Testing Book class...", end="")
    # A Book has a title, and author, and a number of pages.
    # It also has a current page, which always starts at 1. There is no page 0!
    book1 = Book("Harry Potter and the Sorcerer's Stone",
                 "J. K. Rowling", 309)
    assert (str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " +
            "J. K. Rowling: 309 pages, currently on page 1>")
    book2 = Book("Carnegie Mellon Motto", "Andrew Carnegie", 1)
    assert (str(book2) == "Book<Carnegie Mellon Motto by Andrew Carnegie: " +
            "1 page, currently on page 1>")

    # You can turn pages in a book. Turning a positive number of pages moves
    # forward; turning a negative number moves backwards. You can't move past
    # the first page going backwards or the last page going forwards
    book1.turn_page(4)  # turning pages does not return
    assert (book1.get_current_page() == 5)
    book1.turn_page(-1)
    assert (book1.get_current_page() == 4)
    book1.turn_page(400)
    assert (book1.get_current_page() == 309)
    assert (str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " +
            "J. K. Rowling: 309 pages, currently on page 309>")
    book2.turn_page(-1)
    assert (book2.get_current_page() == 1)
    book2.turn_page(1)
    assert (book2.get_current_page() == 1)

    # You can also put a bookmark on the current page. This lets you turn
    # back to it easily. The book starts out without a bookmark.
    book3 = Book("The Name of the Wind", "Patrick Rothfuss", 662)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
            "662 pages, currently on page 1>")
    assert (book3.get_bookmarked_page() == None)
    book3.turn_page(9)
    book3.place_bookmark()  # does not return
    assert (book3.get_bookmarked_page() == 10)
    book3.turn_page(7)
    assert (book3.get_bookmarked_page() == 10)
    assert (book3.get_current_page() == 17)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
            "662 pages, currently on page 17, page 10 bookmarked>")
    book3.turn_to_bookmark()
    assert (book3.get_current_page() == 10)
    book3.remove_bookmark()
    assert (book3.get_bookmarked_page() == None)
    book3.turn_page(25)
    assert (book3.get_current_page() == 35)
    book3.turn_to_bookmark()  # if there's no bookmark, don't turn to a page
    assert (book3.get_current_page() == 35)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
            "662 pages, currently on page 35>")

    # Finally, you should be able to compare two books directly
    book5 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book6 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book7 = Book("A Natural History of Dragons", "Marie Brennan", 334)
    book8 = Book("A Game of Spoofs", "George R.R. Martin", 807)
    assert (book5 == book6)
    assert (book5 != book7)
    assert (book5 != book8)
    book5.turn_page(1)
    assert (book5 != book6)
    book5.turn_page(-1)
    assert (book5 == book6)
    book6.place_bookmark()
    assert (book5 != book6)
    print("Done!")

if __name__ == '__main__':
    test_book_class()