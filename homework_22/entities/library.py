from exeption import TooManyBooks
from entities.book import Book


class Library:
    def __init__(self, name_of_library: str, owner: str):
        self.books = []
        self.name_of_library = name_of_library.title()
        self.owner = owner.title()
        if len(self.books) > 100:
            raise TooManyBooks(f'Too many books in {self.name_of_library}')

    def add_book(self, book: Book):
        self.books.append(book)

    def take_away_book(self, book: Book):
        book_index = self.books.index(book)
        self.books.pop(book_index)

    def __str__(self) -> str:
        return f'<Name of library: {self.name_of_library}, owner:  {self.owner}, list of books: {self.books}>'

    __repr__ = __str__