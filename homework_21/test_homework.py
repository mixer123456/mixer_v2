import pytest

from homework import price_with_discount

@pytest.mark.parametrize('price, percent, expected_result', [(80,70, 24), (20, 20, 16)])
def test_price_with_discount(price: int | float, percent: int, expected_result: float):
    actual_result = price_with_discount(price, percent)
    assert actual_result == expected_result
