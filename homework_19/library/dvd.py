from homework_19.library.library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, duration: int):
        self.duration = duration
        super().__init__(title, author_or_director, year)

    def description(self):
        return f'{super().description()}, Duration: {self.duration}'
