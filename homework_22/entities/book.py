from exeption import ZeroOrNegativePageError, SoOldBookError


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
