import pytest

from homework import get_price_discounted


class TestGetPriceDiscounted:
    def test_too_small_discount(self):
        with pytest.raises(ValueError):
            get_price_discounted(80, -70)

    def test_too_big_discount(self):
        with pytest.raises(ValueError):
            get_price_discounted(80, 700)

    def test_too_small_money(self):
        with pytest.raises(ValueError):
            get_price_discounted(-40454, 50)

    def test_str_instead_int_or_float(self):
        with pytest.raises(TypeError):
            get_price_discounted(40454, '50')
