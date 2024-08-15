import pytest

from entities.book import Book, ZeroOrNegativePageError, SoOldBookError


class TestLibrary:
    def test_library_creation_name(self, library):
        assert library.name_of_library == 'Umniy Chitach', library.owner == 'Popoch'

    def test_library_add_book_and_take_away(self, library, book):
        library.add_book(book)
        library.add_book(book)
        library.take_away_book(book)
        assert len(library.books) == 1


class TestBook:
    def test_book_creation_success(self, book):
        assert book.name == 'Popugai'
        assert book.pages == 50
        assert book.year == 2002

    @pytest.mark.parametrize('name, pages, year', [('Popugai', '50', 2002), ('Popugai', 50, '2002')])
    def test_book_type_error(self, name: str, pages: int, year: int):
        with pytest.raises(TypeError):
            Book(name, pages, year)

    @pytest.mark.parametrize('name, pages, year', [('Popugai', 0, 2002), ('Popugai', -50, 2002)])
    def test_book_zero_or_negative_pages(self, name: str, pages: int, year: int):
        with pytest.raises(ZeroOrNegativePageError):
            Book(name, pages, year)

    def test_book_so_old_book(self):
        with pytest.raises(SoOldBookError):
            Book('Popugai', 50, 1899)
