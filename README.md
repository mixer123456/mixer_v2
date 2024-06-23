# mixer_v2

* команди щоб активувати віртуальне оточення на macOs
* python3 -m venv <назва папки віртуального оточення>
* source ./venv/bin/activate
* comand + option + L - code auto format

использование ф строк или кантоканацыя
def get_dict_key(input_student: dict) -> str:
    name = input_student.get('name')
    surname = input_student.get('surname')
    return f'{name} {surname}'



def show_avg_mark_group(avg_mark: float) -> None:
    put_html(constants.MSG_HEADER_AVG_MARK_GROUP)
    put_html(constants.MSG_BLOCK_AVG_MARK_GROUP.format(
        avg_mark=round(avg_mark, 1)
    ))
