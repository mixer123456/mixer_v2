from pprint import pprint

from pywebio.output import put_table

import utils


def get_airports_by_country(file_name: str, country: str) -> list:
    result = []
    ISO_COUNTRY = 5
    NAME = 2
    CSV_SEPARATOR = ';'

    with open(file_name, mode='r') as file:
        line = file.readline()
        while line:
            line = file.readline().strip()
            airport_info = line.split(CSV_SEPARATOR)
            if len(airport_info) == 1:
                break

            airport_country = airport_info[ISO_COUNTRY]
            if airport_country == country:
                airport_name = airport_info[NAME]
                result.append(airport_name)

    return result


def show_airports(file_name: str, country: str) -> None:
    airports = utils.prepare_table_for_rendering(get_airports_by_country(file_name, country))

    put_table(airports)


def main():
    airports = get_airports_by_country('airport-codes_csv.csv', 'UA')
    show_airports('airport-codes_csv.csv', 'UA')
    pprint(airports)


if __name__ == '__main__':
    main()
