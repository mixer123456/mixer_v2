text = 'Весняний дощ освіжає місто, на вулицях пахне квітами.'
print(text)


food = input('Введіть назву страви, рецепт якої вам подобається: ')
recipe = input('Введіть рецепт цієї страви: ')


result1 = f'Ваша страва під назвою "{food.strip()}" дуже гарна'
meat = """🥩"""
result2 = f'{recipe} {meat}'
count = f'{recipe.count("мясо")}'


print(result1.upper())
print(result2.lower().strip())
print(count)
print(text)
