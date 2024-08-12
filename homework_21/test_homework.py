import pytest

from homework import get_price_discounted


class TestGetPriceDiscounted:
    @pytest.mark.parametrize('price, discount, extended_result', [(60, 30, 30), (59, 27, 32), (476, 80, 396)])
    def test_success(self, price, discount, extended_result):
        actual_result = get_price_discounted(price, discount)
        assert actual_result == extended_result

    def test_discount_zero_or_negative(self):
        with pytest.raises(ValueError):
            get_price_discounted(80, -70)

    def test_discount_too_big(self):
        with pytest.raises(ValueError):
            get_price_discounted(80, 700)

    def test_price_zero_or_negative(self):
        with pytest.raises(ValueError):
            get_price_discounted(0, 50)

    def test_discount_incorrect_type(self):
        with pytest.raises(TypeError):
            get_price_discounted(150, '50')

    def test_price_incorrect_type(self):
        with pytest.raises(TypeError):
            get_price_discounted('150', 50)
