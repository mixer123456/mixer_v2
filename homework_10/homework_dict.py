"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку 
здійснюється за механізмом 
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення, 
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""
students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
# ваш код нижче !!!!!!!! вище нічого не змінюємо
from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider, \
    input_group
from pywebio.output import put_success, put_error, put_warning, put_image, put_html, put_table, put_text
from pywebio.session import run_js
from pywebio import start_server
from pprint import pprint

import configs, constants, utils


def get_dict_key(input_student: dict) -> str:
    name = input_student.get('name')
    surname = input_student.get('surname')
    return f'{name} {surname}'


def translate_key(key: str) -> str:
    dictionary = {
        'email': 'Пошта',
        'age': 'Вік',
        'phone': 'Номер телефону',
        'avg_mark': 'Середній бал',
    }
    return dictionary[key]


def add_student(input_student: dict) -> None:
    student = {
        translate_key('email'): input_student['email'],
        translate_key('age'): input_student['age'],
        translate_key('phone'): input_student['phone'],
        translate_key('avg_mark'): input_student['avg_mark'],
    }
    key = get_dict_key(input_student)
    students[key] = student


def request_student_data() -> dict:
    input_student = input_group(
        constants.MSG_FORM_LABEL,
        [
            input_pw(constants.MSG_NAME, placeholder=constants.PLACEHOLDER_NAME, name='name', required=True),
            input_pw(constants.MSG_SURNAME, placeholder=constants.PLACEHOLDER_SURNAME, name='surname', required=True),
            input_pw(constants.MSG_EMAIL, placeholder=constants.PLACEHOLDER_EMAIL, name='email', required=True),
            slider(constants.MSG_AGE, name='age', min_value=18, max_value=40, required=True),
            input_pw(constants.MSG_PHONE, placeholder=constants.PLACEHOLDER_PHONE, name='phone', required=True),
            slider(constants.MSG_AVG_MARK, name='avg_mark', type=FLOAT, min_value=0.0, max_value=100.0, required=True),
        ]
    )
    return input_student


def get_good_students(students: dict, avg_mark: float) -> list:
    result = []
    for name, student_data in students.items():
        student_avg_mark = student_data.get(translate_key('avg_mark'))
        if student_avg_mark >= avg_mark:
            item = [
                name,
                student_avg_mark
            ]
            result.append(item)
    return result


def show_good_students(good_students: list) -> None:
    put_html(constants.MSG_HEADER_GOOD_STUDENTS)
    put_table(good_students, [
        constants.MSG_NAME,
        constants.MSG_AVG_MARK
    ])


def get_avg_mark_group(students: dict) -> float:
    result = 0

    students_list = students.values()
    students_count = len(students_list)

    for student_data in students_list:
        student_avg_mark = student_data.get(translate_key('avg_mark'))
        result += student_avg_mark

    result /= students_count

    return result


def show_avg_mark_group(avg_mark: float) -> None:
    put_html(constants.MSG_HEADER_AVG_MARK_GROUP)
    put_html(constants.MSG_BLOCK_AVG_MARK_GROUP.format(
        avg_mark=round(avg_mark, 1)
    ))


def get_students_list(students: dict) -> list:
    result = []
    for name, student_data in students.items():
        item = [
            name,
            student_data.get(translate_key('avg_mark')),
            student_data.get(translate_key('phone')) or constants.MSG_EMPTY_PHONE,
            student_data.get(translate_key('email')) or constants.MSG_EMPTY_EMAIL
        ]
        result.append(item)
    return result


def show_students_list(students_list: list) -> None:
    put_html(constants.MSG_HEADER_LIST_STUDENTS)
    put_table(students_list, [
        constants.MSG_NAME,
        constants.MSG_AVG_MARK,
        constants.MSG_PHONE,
        constants.MSG_EMAIL
    ])


def main():
    input_student = request_student_data()
    add_student(input_student)

    good_students = get_good_students(students, 90)
    show_good_students(good_students)

    avg_mark_group = get_avg_mark_group(students)
    show_avg_mark_group(avg_mark_group)

    students_list = get_students_list(students)
    show_students_list(students_list)

    utils.reload_page(configs.PAGE_RELOAD_TIMEOUT_MS)


if __name__ == '__main__':
    start_server(main, port=configs.SERVER_PORT)
