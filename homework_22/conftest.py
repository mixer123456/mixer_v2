import pytest

from entities.library import Library, Book


@pytest.fixture(scope='class')
def library_creation_payload() -> dict:
    payload = {'name_of_library': 'umnIy chitach', 'owner': 'popoch'}
    return payload


@pytest.fixture(scope='class')
def library(library_creation_payload) -> Library:
    library = Library(
        name_of_library=library_creation_payload['name_of_library'],
        owner=library_creation_payload['owner'],
    )
    return library


@pytest.fixture(scope='class')
def book_creation_payload() -> dict:
    payload = {'name': 'Popugai', 'pages': 50, 'year': 2002}
    return payload


@pytest.fixture(scope='class')
def book(book_creation_payload) -> Book:
    book = Book(
        name=book_creation_payload['name'],
        pages=book_creation_payload['pages'],
        year=book_creation_payload['year']
    )
    return book
