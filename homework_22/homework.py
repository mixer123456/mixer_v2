class TooManyBooks(Exception):
    pass


class ZeroOrNegativePageError(Exception):
    pass


class SoOldBookError(Exception):
    pass


class Library:
    def __init__(self, name_of_library: str, owner: str):
        self.books = []
        self.name_of_library = name_of_library.title()
        self.owner = owner.title()
        if len(self.books) > 100:
            raise TooManyBooks(f'Too many books in {self.name_of_library}')

    def add_book(self, book: 'Book'):
        self.books.append(book)

    def take_away_book(self, book: 'Book'):
        book_index = self.books.index(book)
        self.books.pop(book_index)

    def __str__(self) -> str:
        return f'<Name of library: {self.name_of_library}, owner:  {self.owner}, list of books: {self.books}>'

    __repr__ = __str__


class Book:
    def __init__(self, name: str, pages: int, year: int):
        self.name = name
        self.pages = pages
        self.year = year
        if pages <= 0:
            raise ZeroOrNegativePageError("Count of pages can't be zero or negative")
        if year < 1900:
            raise SoOldBookError("So old book")

    def __str__(self) -> str:
        return f'<Name of book: {self.name}, count of pages: {self.pages}, year of  issue: {self.year}>'

    __repr__ = __str__


library = Library('Umrfrf', 'popow')
book = Book('Popugai', 50, 2002)
book2 = Book('Elephant', 60, 2005)
library.add_book(book)
library.add_book(book2)
library.take_away_book(book2)
print(library)
print(library.books)
print(book)
