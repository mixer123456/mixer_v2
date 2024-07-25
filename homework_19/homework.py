from homework_19.library.Book import Book
from homework_19.library.DVD import DVD
from homework_19.library.Magazine import Magazine

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
