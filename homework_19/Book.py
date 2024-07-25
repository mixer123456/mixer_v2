from homework_19.LibraryItem import LibraryItem


class Book(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, number_of_pages: int):
        self.number_of_pages = number_of_pages
        super().__init__(title, author_or_director, year)

    def description(self):
        return f'{super().description()}, Count of pages: {self.number_of_pages}'
