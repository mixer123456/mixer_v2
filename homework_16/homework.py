from pywebio import start_server
from pywebio.output import put_table

import configs, constants, utils


def get_airports_by_country(file_name: str, country: str) -> list:
    ISO_COUNTRY = 5
    NAME = 2
    CSV_DELIMITER = ';'

    result = []
    with open(file_name, mode='r') as file:
        line = file.readline()
        while line:
            line = file.readline().strip()
            airport_info = line.split(CSV_DELIMITER)
            if len(airport_info) == 1:
                break

            airport_country = airport_info[ISO_COUNTRY]
            if airport_country == country:
                airport_name = airport_info[NAME]
                result.append(airport_name)

    return result


def show_airports(airports: list[str]) -> None:
    airports = utils.prepare_table_for_rendering([constants.MSG_HEADER] + airports)

    put_table(airports)


def main():
    file_name = 'airport-codes_csv.csv'
    country = 'UA'

    airports = get_airports_by_country(file_name, country)
    show_airports(airports)


if __name__ == '__main__':
    start_server(main, port=configs.SERVER_PORT)
