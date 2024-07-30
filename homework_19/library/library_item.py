from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title: str, author_or_director: str, year: int):
        self.title = title.title()
        self.author_or_director = author_or_director.title()
        self.year = year

    @abstractmethod
    def description(self):
        return f'Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}'
