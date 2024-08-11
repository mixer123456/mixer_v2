def get_price_discounted(price: int | float, percent: int) -> float:
    if percent <= 0:
        raise ValueError("Percent can't be zero or negative")
    if percent >= 100:
        raise ValueError("Percent can't be bigger that 100")
    if price <= 0:
        raise ValueError("Price can't be zero or negative")
    price_with_discount = price * percent / 100
    discounted = price - price_with_discount
    return round(discounted, 2)


x = get_price_discounted(10, 20)
print(x)
