from pywebio.input import input as input_pw
from pywebio.input import NUMBER, TEXT
from pywebio.output import put_text, put_html, put_image
from pywebio import start_server
from pywebio.session import run_js

import constants
import configs


def print_h1(message: str) -> None:
    h1 = f'<h1>{message}</h1>'
    put_html(h1)


def print_h2(message: str) -> None:
    h2 = f'<h2>{message}</h2>'
    put_html(h2)


def print_username_request() -> str:
    username = input_pw(constants.MSG_USERNAME_REQUEST).strip().title()
    return username


def print_question(question: str, answer: str | int, type: str) -> bool:
    users_answer = input_pw(question, type=type)

    if type == TEXT:
        answer = answer.lower()
        users_answer = users_answer.lower()

    result = users_answer == answer
    return result


def print_great_score() -> None:
    img = open(configs.IMG_RESULT, 'rb').read()
    put_image(img, width=f'{configs.IMG_RESULT_WIDTH}px')


def print_final_score(username: str, score: int) -> None:
    message = constants.MSG_RESULT.format(
        username=username,
        score=score
    )
    put_html(message)

    if score == 5:
        print_great_score()


def print_thank_you() -> None:
    print_h2(constants.MSG_THANKS)
    timeout = str(configs.PAGE_RELOAD_TIMEOUT_MS)
    run_js('setTimeout(function(){location.reload();}, ' + timeout + ' )')


def main():
    print_h1(constants.MSG_WELCOME)

    username = print_username_request()

    total_score = 0
    answer = print_question(constants.QUESTION_1, constants.QUESTION_1_ANSWER, constants.QUESTION_1_TYPE)
    if answer:
        total_score += 1

    answer = print_question(constants.QUESTION_2, constants.QUESTION_2_ANSWER, constants.QUESTION_2_TYPE)
    if answer:
        total_score += 1

    answer = print_question(constants.QUESTION_3, constants.QUESTION_3_ANSWER, constants.QUESTION_3_TYPE)
    if answer:
        total_score += 1

    answer = print_question(constants.QUESTION_4, constants.QUESTION_4_ANSWER, constants.QUESTION_4_TYPE)
    if answer:
        total_score += 1

    answer = print_question(constants.QUESTION_5, constants.QUESTION_5_ANSWER, constants.QUESTION_5_TYPE)
    if answer:
        total_score += 1

    print_final_score(username, total_score)
    print_thank_you()


if __name__ == '__main__':
    start_server(main, port=configs.SERVER_PORT)
