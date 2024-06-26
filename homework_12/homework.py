import requests
from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider, \
    input_group
from pywebio.output import put_success, put_error, put_warning, put_image, put_html, put_table, put_text
from pywebio.session import run_js
from pywebio import start_server
from pprint import pprint

import configs, constants, utils


def get_animals() -> list[dict]:
    response = requests.get(configs.ENDPOINT_ANIMALS)
    data = response.json()
    animals = data['animals']
    return animals


def get_animals_summary(animals: list[dict]) -> dict:
    poisonous_cost_carrying = 0
    animals_count = 0
    animals_count_from_africa = 0
    for animal in animals:
        animals_count += animal['count']

        if animal['poisonous']:
            poisonous_cost_carrying += animal['cost_of_caring'] * animal['count']

        if animal['continent'] == constants.CNT_AFRICA:
            animals_count_from_africa += animal['count']

    return {
        'poisonous_cost_carrying': poisonous_cost_carrying,
        'animals_count': animals_count,
        'animals_count_from_africa': animals_count_from_africa,
    }


def show_animal_summary(animals_summary: dict) -> None:
    put_html(constants.MSG_POISONOUS_COST_CARRYING.format(
        poisonous_cost_carrying=animals_summary['poisonous_cost_carrying']
    ))
    put_html(constants.MSG_ANIMALS_COUNT.format(
        animals_count=animals_summary['animals_count']
    ))
    put_html(constants.MSG_ANIMALS_COUNT_FROM_AFRICA.format(
        animals_count_from_africa=animals_summary['animals_count_from_africa']
    ))


def main():
    animals = get_animals()
    animals_summary = get_animals_summary(animals)
    show_animal_summary(animals_summary)
    # put_html(constants.MSG_POISONOUS_COST_CARRYING.format(
    #     poisonous_cost_carrying=animals_summary['poisonous_cost_carrying']
    # ))
    # put_html(constants.MSG_ANIMALS_COUNT.format(
    #     animals_count=animals_summary['animals_count']
    # ))
    # put_html(constants.MSG_ANIMALS_COUNT_FROM_AFRICA.format(
    #     animals_count_from_africa=animals_summary['animals_count_from_africa']
    # ))

    utils.reload_page(configs.PAGE_RELOAD_TIMEOUT_MS)


if __name__ == '__main__':
    start_server(main, port=configs.SERVER_PORT)
