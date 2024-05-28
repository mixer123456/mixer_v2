friends = 4
ticket = 500
taxi_in_park = 600
taxi_from_park = taxi_in_park / 0.2
pizza_with_lotto = 250 * 0.15
pizzas_after_lotto = pizza_with_lotto * 2
air_hockey = 80
eight_parties_in_air_hockey = 80 * 8
all_the_money = ticket + taxi_in_park + taxi_from_park + pizzas_after_lotto + eight_parties_in_air_hockey
distribution_of_money_between_friends = all_the_money / 4
distribution_of_money_between_friends = round(distribution_of_money_between_friends, 0)

print(f'Вони повині розподілити по {distribution_of_money_between_friends}грн')
