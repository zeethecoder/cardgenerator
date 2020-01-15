import random

symbols = ["\u2665","\u2666","\u2660","\u2663"]
numbers = ['A',1, 2, 3, 4, 5, 6, 7, 8, 9, 10,'K','Q','J']

random_symbols = random.choice(symbols)
random_numbers = random.choice(numbers)

# joining lists but doesnt work
# the_card = random_numbers + random_symbols

print(random_numbers)

