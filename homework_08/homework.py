from pywebio.input import input as input_pw
from pywebio.input import NUMBER
from pywebio.output import put_text, put_html, put_image
from pywebio import start_server
from pywebio.session import run_js

MSG_WELCOME = 'Вітаємо на нашій вікторині.'
MSG_USERNAME = 'Ваше імʼя'
MSG_QUESTION_1 = 'коли почалась друга світова війна?'
MSG_QUESTION_2 = 'через яку країну почалася 1 світова війна? (написати потрібно тільки назву країни)'
MSG_QUESTION_3 = 'коли Українська Народна Республіка (УНР) стала незалежною?'
MSG_QUESTION_4 = 'в честь кого назвали Напалеоновскі воїни? (писати поотрібно так: "В честь (імʼя правителя)"'
MSG_QUESTION_5 = 'хто відкрив шлях до Індії?'
MSG_THANKS = 'Дякуємо за участь у нашій вікторині. Гарного вам дня!'
total_score = 0
question_1_answer = 1939
question_2_answer = 'Австріїська імперія'
question_3_answer = 1917
question_4_answer = 'В честь Напалеона Бонапарта'
question_5_answer = 'Васко да Гама'
img_end = 'five_stars.jpeg'
img_end_width = 200


def convert_string_to_number(string_like_number: str) -> int:
    if string_like_number.isdigit():
        result = int(string_like_number)
        return result


def get_formatted_html_h1(message: str) -> str:
    result_h1 = f'<h1>{message}</h1>'
    return result_h1


def get_formatted_html_h2(message: str) -> str:
    result_h2 = f'<h2>{message}</h2>'
    return result_h2


def main():
    put_html(
        get_formatted_html_h1(MSG_WELCOME)
    )
    username = input_pw(MSG_USERNAME)
    question_1 = input_pw(f'{username}, {MSG_QUESTION_1}', type=NUMBER)
    question_2 = input_pw(f'{username}, {MSG_QUESTION_2}')
    question_3 = input_pw(f'{username}, {MSG_QUESTION_3}', type=NUMBER)
    question_4 = input_pw(f'{username}, {MSG_QUESTION_4}')
    question_5 = input_pw(f'{username}, {MSG_QUESTION_5}')
    if question_1 == question_1_answer:
        put_text('Правильно')
        score_1 = 1
    else:
        put_text('Неправильно')
        score_1 = 0
    if question_2 == question_2_answer:
        put_text('Правильно')
        score_2 = 1
    else:
        put_text('Неправильно')
        score_2 = 0
    if question_3 == question_3_answer:
        put_text('Правильно')
        score_3 = 1
    else:
        put_text('Неправильно')
        score_3 = 0
    if question_4 == question_4_answer:
        put_text('Правильно')
        score_4 = 1
    else:
        put_text('Неправильно')
        score_4 = 0
    if question_5 == question_5_answer:
        put_text('Правильно')
        score_5 = 1
    else:
        put_text('Неправильно')
        score_5 = 0
    total_score = score_1 + score_2 + score_3 + score_4 + score_5
    if total_score >= 0 and total_score < 5:
        put_text(f'Кількість балів: {total_score}')
    if total_score == 5:
        put_text(f'Кількість балів: {total_score}')
        img = open(img_end, 'rb').read()
        put_image(img, width=f'{img_end_width}px')
    put_html(
        get_formatted_html_h2(MSG_THANKS)
    )
    run_js('setTimeout(function(){location.reload();}, 3000)')


if __name__ == '__main__':
    start_server(main, port=20000)
