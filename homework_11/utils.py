def get_union_table(list1: list[str], list2: list[str]) -> list[list[str]]:
    result = []
    count_list1 = len(list1)
    count_list2 = len(list2)
    count = max(count_list1, count_list2)
    for iterator in range(count):
        element_1 = ''
        if iterator < count_list1:
            element_1 = list1[iterator]

        element_2 = ''
        if iterator < count_list2:
            element_2 = list2[iterator]

        result.append([element_1, element_2])

    return result


def get_text(text: str, length: int, symbol=' ') -> str:
    repeat = length - len(text)

    return text + symbol * repeat
