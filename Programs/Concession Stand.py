
menu = {'pizza': 750,
        'popcorn': 350,
        'burger': 250,
        'fries': 250,
        'coke': 80,
        'fanta': 80}

cart = []
total = 0

print('----------MENU-----------')

for key, value in menu.items():
    print(f'{(key).capitalize():10} Rs.{value}')
print('-------------------------')

while True:
    food = input('Enter the food you want to buy (q to Quit):')

    if (food.lower())== 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"Sorry, we don't sell {food.capitalize()}.")

print('-----------YOUR ORDER---------')
for food in cart:
    print(f'{food.capitalize()}', end=' ')
    total += menu.get(food)

print()
print(f"Your total is Rs.{total}")