from typing import Callable


def decorator():
    def _decorator(func: Callable):
        def wrapper(*args):
            result = func(*args)
            return {'result': result}

        return wrapper

    return _decorator


@decorator()
def add_two_numbers(first_numbers: int, second_number: int) -> int:
    result = first_numbers + second_number
    return result


result = add_two_numbers(150, 150)
print(result)


@decorator()
def say_hello(name: str) -> str:
    result = f'Hello {name}'
    return result


result = say_hello('Max')
print(result)

# result = wrapper(add_two_numbers, 5, 7)
# print(result)
