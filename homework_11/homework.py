import requests
from pywebio.output import put_text, put_html, put_table
from pywebio.session import run_js
from pprint import pprint

import configs, utils, constants


def get_astronauts() -> list[dict]:
    response = requests.get(url=configs.ENDPOINT_ASTROS)
    response_json = response.json()
    people = response_json['people']
    return people


def get_astronauts_names() -> list[str]:
    result = []
    astronauts = get_astronauts()
    for astronaut in astronauts:
        name = astronaut.get('name')
        result.append(name)
    return result


def get_users(start: int = 0, limit: int = 50) -> list[dict]:
    params = {
        'skip': start,
        'limit': limit,
    }
    response = requests.get(url=configs.ENDPOINT_USERS, params=params)
    response_json = response.json()
    users = response_json['users']
    return users


def filter_users_by_age(users: list[dict], age: int) -> list[dict]:
    users_list = []
    for user in users:
        if user.get('age') == age:
            users_list.append(user)
    return users_list


def get_users_names(users: list[dict]) -> list[str]:
    result = []
    for user in users:
        first_name = user.get('firstName')
        last_name = user.get('lastName')
        name = f'{first_name} {last_name}'
        result.append(name)
    return result


def get_users_names_by_age(age: int) -> list[str]:
    limit = 30
    start = 0
    users_names = []

    while True:
        users_chunk = get_users(start=start, limit=limit)
        if not users_chunk:
            break

        start += limit
        users_chunk = filter_users_by_age(users_chunk, age)
        users_names_chunk = get_users_names(users_chunk)
        users_names += users_names_chunk
    return users_names


def show_astros_and_users_names(astros: list[str], users: list[str]) -> None:
    max_length_astros = len(max(astros, key=len))
    max_length_users = len(max(users, key=len))

    COLUMN_1_LENGTH = max_length_astros
    COLUMN_2_LENGTH = max_length_users

    COLUMN_1_BORDER = '-' * (COLUMN_1_LENGTH + 2)
    COLUMN_2_BORDER = '-' * (COLUMN_2_LENGTH + 2)
    HR = f'+{COLUMN_1_BORDER}+{COLUMN_2_BORDER}+'
    print(HR)

    table = utils.get_union_table(astros, users)
    formatted_title_astro = utils.get_text(constants.TITLE_ASTROS, COLUMN_1_LENGTH)
    formatted_title_user = utils.get_text(constants.TITLE_USER, COLUMN_2_LENGTH)
    title = f'| {formatted_title_astro} | {formatted_title_user} |'
    print(title)
    print(HR)
    for astro, user in table:
        formatted_astro = utils.get_text(astro, COLUMN_1_LENGTH)
        formatted_user = utils.get_text(user, COLUMN_2_LENGTH)
        row = f'| {formatted_astro} | {formatted_user} |'
        print(row)
    print(HR)


def main():
    astronauts = get_astronauts_names()

    filter_age = 28
    users = get_users_names_by_age(filter_age)
    show_astros_and_users_names(astronauts, users)



if __name__ == '__main__':
    main()
