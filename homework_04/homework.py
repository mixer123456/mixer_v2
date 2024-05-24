from constants import MSG_HR, MSG_INPUT_FOOD_NAME, MSG_INPUT_FOOD_RECIPE
from templates import TPL_FOOD_NAME,  TPL_FOOD_RECIPE

print(MSG_HR)
food = input(MSG_INPUT_FOOD_NAME).strip().upper()
recipe = input(MSG_INPUT_FOOD_RECIPE).strip().lower()

print(TPL_FOOD_NAME.format(food=food))
print(TPL_FOOD_RECIPE.format(recipe=recipe))
print(recipe.count("мясо"))
print(MSG_HR)
