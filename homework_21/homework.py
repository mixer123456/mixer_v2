def get_price_discounted(price: int | float, discount: int) -> float:
    if discount <= 0:
        raise ValueError("Percent can't be zero or negative")
    if discount >= 100:
        raise ValueError("Percent can't be 100 and bigger")
    if price <= 0:
        raise ValueError("Price can't be zero or negative")
    discounted = price - discount
    return round(discounted, 2)
