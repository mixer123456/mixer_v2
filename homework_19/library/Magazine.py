from homework_19.library.LibraryItem import LibraryItem


class Magazine(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, issue_number: int):
        self.issue_number = issue_number
        super().__init__(title, author_or_director, year)

    def description(self):
        return f'{super().description()}, Issue number: {self.issue_number}'
