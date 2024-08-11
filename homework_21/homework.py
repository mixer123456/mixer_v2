def price_with_discount(price: int | float, percent: int) -> float:
    if percent <= 0:
        raise ValueError('Too small percent')
    if percent > 100:
        raise ValueError('Too big percent')
    if price <= 0:
        raise ValueError("Aren't you have money?")
    discount = percent / 100 * price
    price_with_percent = price - discount
    return round(price_with_percent, 2)


x = price_with_discount(10, 20)
print(x)
