import csv

def get_airports_by_country(file_name: str, country: str) -> list[str]:
    DELIMITER = ';'
    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=DELIMITER)
        airports = [row['name'] for row in reader if row['iso_country'] == country]
    return airports


def show_airports(airports: list[str]) -> None:
    for (i, airport) in enumerate(airports):
        print(f'{i} - {airport}')

def main():
    country = 'UA'
    filename = 'airport-codes_csv.csv'

    airports = get_airports_by_country(filename, country)
    show_airports(airports)


if __name__ == '__main__':
    main()