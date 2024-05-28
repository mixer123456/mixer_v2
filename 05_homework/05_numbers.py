from templates import TPL_OUTPUT
# input data
friends_count = 4

ticket_price = 500

taxi_in_park_price = 600
taxi_evening_price_markup_percent = 20

pizza_count = 2
pizza_price = 250
pizza_discount_percent = 15

air_hockey_price = 80
air_hockey_count = 8

# calculation
tickets_costs = ticket_price * friends_count

taxi_evening_markup_price = taxi_in_park_price * taxi_evening_price_markup_percent / 100
taxi_from_park_price = taxi_in_park_price + taxi_evening_markup_price
taxi_costs = taxi_in_park_price + taxi_from_park_price

pizza_discount = pizza_price * pizza_discount_percent / 100
pizzas_costs = (pizza_price - pizza_discount) * pizza_count

air_hockey_costs = air_hockey_price * air_hockey_count

total_costs = tickets_costs + taxi_costs + pizzas_costs + air_hockey_costs
distribution_of_money_between_friends = total_costs / friends_count

print(TPL_OUTPUT.format(
tickets = round(tickets_costs, 2),
taxi = round(taxi_costs, 2),
food = round(pizzas_costs, 2),
game = round(air_hockey_costs, 2),
total = round(total_costs, 2),
per_person = round(distribution_of_money_between_friends, 2)
))
