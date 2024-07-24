from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint


@dataclass(frozen=True)
class Params:
    BOOK_NUMBER_OF_PAGES = randint(50, 201)
    MAGAZINE_ISSUE_NUMBER = randint(1, 1001)
    DVD_DURATION = randint(3, 6)


class LibraryItem(ABC):
    def __init__(self, title: str, author_or_director: str, year: int):
        self.title = title.title()
        self.author_or_director = author_or_director.title()
        self.year = year

    @abstractmethod
    def description(self):
        return f'Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}'


class Book(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int):
        self.number_of_pages = Params.BOOK_NUMBER_OF_PAGES
        super().__init__(title, author_or_director, year)

    def description(self):
        return f"Book's title: {self.title}, Book's author/director: {self.author_or_director}, Year: {self.year}, Count of pages: {self.number_of_pages}"


class Magazine(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int):
        self.issue_number = Params.MAGAZINE_ISSUE_NUMBER
        super().__init__(title, author_or_director, year)

    def description(self):
        return f"Magazine's title: {self.title},Magazine's author/director: {self.author_or_director}, Year: {self.year}, Issue number: {self.issue_number}"


class DVD(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int):
        self.duration = Params.DVD_DURATION
        super().__init__(title, author_or_director, year)

    def description(self):
        return f"DVD's title: {self.title},DVD's author/director: {self.author_or_director}, Year: {self.year}, Duration: {self.duration}"


book = Book('Ivanhoe', 'Walter Scott', 1819)
print(book.description())
magazine = Magazine('Time', 'Henry Luce', 1923)
print(magazine.description())
dvd = DVD('Lord of The Ring', 'Peter Jackson', 2001)
print(dvd.description())
