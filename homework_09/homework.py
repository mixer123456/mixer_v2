from pywebio.input import textarea, select, checkbox, radio, input as input_pw, slider
from pywebio.output import put_success, put_error

import configs, constants
from utils import start_server, reload_page

reviews_info = []


def thank_you_page(username: str, rating: int) -> None:
    if rating >= 7:
        put_success(constants.MSG_GOOD_FILM.format(
            username=username
        ))
    else:
        put_error(constants.MSG_BAD_FILM.format(
            username=username
        ))


def main():
    username = input_pw(constants.REQUEST_USERNAME)
    film_name = input_pw(constants.REQUEST_FILM)
    film_genre = select(constants.REQUEST_GENRE, options=constants.GENRE_LIST)
    film_review = textarea(constants.REQUEST_REVIEW)
    film_rating = slider(constants.REQUEST_RATING, min_value=1, max_value=10)
    film_emotions = checkbox(constants.REQUEST_EMOTIONS, options=constants.EMOTIONS_LIST)
    film_share = radio(constants.REQUEST_USER_SHARE, options=constants.SHARE_LIST)

    thank_you_page(username, film_rating)

    reviews_info.append([
        username,
        film_name,
        film_rating,
        film_share,
    ])

    reload_page(configs.PAGE_RELOAD_TIME_MS)


start_server(main, configs.SERVER_PORT, __name__)
