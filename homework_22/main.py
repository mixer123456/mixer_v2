from entities.book import Book
from entities.library import Library


library = Library('Umrfrf', 'popow')
book = Book('Popugai', 50, 2002)
book2 = Book('Elephant', 60, 2005)
library.add_book(book)
library.add_book(book2)
library.take_away_book(book2)
print(library)
print(library.books)
print(book)
