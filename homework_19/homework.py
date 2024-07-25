from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title: str, author_or_director: str, year: int):
        self.title = title.title()
        self.author_or_director = author_or_director.title()
        self.year = year

    @abstractmethod
    def description(self):
        return f'Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}'


class Book(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, number_of_pages: int):
        self.number_of_pages = number_of_pages
        super().__init__(title, author_or_director, year)

    def description(self):
        return f"Book's title: {self.title}, Book's author/director: {self.author_or_director}, Year: {self.year}, Count of pages: {self.number_of_pages}"


class Magazine(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, issue_number: int):
        self.issue_number = issue_number
        super().__init__(title, author_or_director, year)

    def description(self):
        return f"Magazine's title: {self.title},Magazine's author/director: {self.author_or_director}, Year: {self.year}, Issue number: {self.issue_number}"


class DVD(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, duration: int):
        self.duration = duration
        super().__init__(title, author_or_director, year)

    def description(self):
        return f"DVD's title: {self.title},DVD's author/director: {self.author_or_director}, Year: {self.year}, Duration: {self.duration}"


book1 = Book('The Hobbit', 'J.R.R. Tolkien', 1937, 320)
book2 = Book('The Lord of the Rings', 'J.R.R. Tolkien', 1954, 752)
book3 = Book('The Silmarillion', 'J.R.R. Tolkien', 1977, 365)

magazine1 = Magazine('Time', 'Time Inc.', 1926, 504)
magazine2 = Magazine('Time', 'Time Inc.', 1926, 90)
magazine3 = Magazine('Time', 'Time Inc.', 1926, 361)

dvd1 = DVD('The Lord of the Rings: The Fellowship of the Ring', 'Peter Jackson', 2001, 178)
dvd2 = DVD('The Lord of the Rings: The Two Towers', 'Peter Jackson', 2002, 179)
dvd3 = DVD('The Lord of the Rings: The Return of the King', 'Peter Jackson', 2003, 201)


def main():
    print(book1.description())
    print(book2.description())
    print(book3.description())

    print(magazine1.description())
    print(magazine2.description())
    print(magazine3.description())

    print(dvd1.description())
    print(dvd2.description())
    print(dvd3.description())


if __name__ == '__main__':
    main()
