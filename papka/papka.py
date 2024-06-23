list_of_random_numbers = [9, 22, 11, 33, 50, 311, 155, 63, 324]
def find_max_value(numbers: list[float]) -> float:
    max = numbers[0]
    i = 0
    for item in numbers:
        print(i,  item)
        i += 1
        if max < item:
            max = item
    return max



def find_min_value(numbers: list[float]) -> float:
    min = numbers[0]
    for item in numbers:
        if min > item:
            min = item
    return min

print(len(list_of_random_numbers))

def find_sum_of_all_element(numbers: list[float]) -> float:
    result = 0
    for item in numbers:
        result += item
    return result

def find_average(numbers: list[float]) -> float:
    summa = 0
    for item in numbers:
        summa += item
    result = summa / len(numbers)
    return result


def find_number_greater_than_(numbers: list[float], number: float) -> list[float]:
    result = []
    for item in numbers:
        if item >= number:
            result.append(item)
    return result

def is_even_number(number: float) -> bool:
    result = number % 2
    return result == 0

def get_text(text: str, length: int, symbol = '.') -> str:
    print(text, symbol * 10)
    repeat = length - len(text)

    return text + symbol * repeat

list_of_random_strings = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "iceberg",
]

def get_longest_string(strings: list[str]) -> str:
    max_string = strings[0]
    for item in strings:
        if len(max_string) < len(item):
            max_string = item
        print()
    return max_string



# first_element = list_of_random_strings[-9]
# last_element = list_of_random_strings[-1]
# print(first_element)


#
# result = get_max_value(list_of_random_strings)
# result2 = max(list_of_random_strings, key=len)
# print(result, result2)

list1 = [
    "apple",
    "banana",
    "cherry",
]

list2 = [
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "iceberg",
]

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



    # print()

result = get_union_table(list1, list2)
print(result)

