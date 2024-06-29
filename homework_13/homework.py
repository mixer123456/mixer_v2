from pprint import pprint

# завдання 1
# 1 - є дані по успішності школярів двох класів - потрібно створити обєднаний словник (новий) з інформацією про успішність всіх учнів 9-х класів

student_grades_9a = {
    "Олександр Іванович Петров": 85,
    "Марія Сергіївна Іванова": 90,
    "Дмитро Олександрович Сидоров": 78
}

student_grades_9b = {
    "Катерина Петрівна Коваленко": 88,
    "Іван Дмитрович Кузьменко": 92,
    "Ольга Вікторівна Литвиненко": 80
}

all_students_1= {}
all_students_1.update(student_grades_9a)
all_students_1.update(student_grades_9b)
pprint(all_students_1)

all_students_2 = {**student_grades_9a, **student_grades_9b}
pprint(all_students_2)
# завдання 2
text = """
Технології розвиваються стрімко. Кожен день ми спостерігаємо нові досягнення в науці та техніці. Комп'ютери стають все потужнішими, а програмне забезпечення – складнішим. Проте, разом з цими досягненнями зростає і потреба в нових спеціалістах, здатних працювати з сучасними технологіями.
Важливо пам'ятати, що розвиток технологій впливає не лише на виробництво, але й на повсякденне життя людей. Смартфони, комп'ютери, розумні будинки, інтернет речей – все це робить наше життя зручнішим і ефективнішим. Технології змінюють наше життя кожного дня.
Однак, не слід забувати про кібербезпеку. Захист даних стає все важливішим питанням, адже зростання обсягу цифрової інформації вимагає надійних рішень для її захисту. Розробка нових методів шифрування та аутентифікації – ключ до безпеки в цифровому світі. Технології безпеки постійно розвиваються.
Таким чином, можна сказати, що технологічний прогрес має свої переваги та виклики. Основне завдання – знаходити баланс між інноваціями та безпекою, щоб забезпечити стабільний розвиток суспільства. Технології завжди будуть важливими для розвитку суспільства.
"""

def delete_punctuation(text: str) -> str:
    return text.replace('.','').replace(',', '').replace('-', '')

text = delete_punctuation(text).lower()
text_list = text.split()
text_set = set(text_list)
task_2 = len(text_set)


print(f'{task_2 = }')



# завдання 3
# завдання на роботу зі списками (використати зрізи)
# Створіть початковий список letters з літерами англійського алфавіту.
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Літери від C до G включно.
task_3_1 = letters[2:7]
print(f'{task_3_1 = }')

# Кожну другу літеру, починаючи з A.
task_3_2 = letters[::2]
print(f'{task_3_2 = }')

# Літери від Z до Q у зворотному порядку.
task_3_3 = letters[:-11:-1]
print(f'{task_3_3 = }')

# Перші 3 літери алфавіту.
task_3_4 = letters[0:3]
print(f'{task_3_4 = }')
