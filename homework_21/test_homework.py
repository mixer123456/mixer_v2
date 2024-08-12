import pytest

from homework import get_price_discounted

testing_args_success = [
    (80, 70, 10),
    (50, 20, 30),
    (60, 35, 25),
]


@pytest.mark.parametrize('price, percent, expected_result', testing_args_success)
def test_price_discounted_success(price: int | float, percent: int, expected_result: float):
    actual_result = get_price_discounted(price, percent)
    assert actual_result == expected_result


testing_args_fail = [
    (80, '70', 10),
    (-50, 20, 30),
    (60, 350, 25),
    (60, -40, 25),
]


@pytest.mark.parametrize('price, percent, expected_result', testing_args_fail)
def test_price_discounted_fail(price: int | float, percent: int, expected_result: float):
    actual_result = get_price_discounted(price, percent)
    assert actual_result == expected_result
