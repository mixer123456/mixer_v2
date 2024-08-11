import pytest

from homework import get_price_discounted

@pytest.mark.parametrize('price, percent, expected_result', [(80,70, 24), (20, 20, 16)])
def test_price_with_discount(price: int | float, percent: int, expected_result: float):
    actual_result = get_price_discounted(price, percent)
    assert actual_result == expected_result
