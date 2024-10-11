foods = []
prices = []
quantities = []
total = 0

while True:
    food = input('Enter a food to buy (q to Quit): ')
    if food.lower() == 'q':
        break
    else:
        price = int(input(f'Enter the price of each {food}: '))
        quantity = int(input(f'Enter the number of {food}: '))
        quantities.append(quantity)
        foods.append(food)
        prices.append(price*quantity)

print('-------Your Cart-------')

for food in foods:
    index = foods.index(food)
    print(f"{quantities[index]} x {food}", end=' ')
    print()

for price in prices:
    total += price
    
print()
print(f'Your total is Rs.{total}')    