
principal = 0
rate = 0
interest = 0

while True:
    principal = float(input('Enter the principle amount: '))
    if principal < 0:
        print('Principal amount cannot be less than zero.')
    else: 
        break

while True:
    rate = float(input('Enter the interest rate: '))
    if rate < 0:
        print('Interest rate cannot be less than zero.')
    else: 
        break

while True:
    time = int(input('Enter the time in years: '))
    if time < 0:
        print('Time cannot be less than zero.')
    else: 
        break

total = principal * pow((1 + rate / 100), time)

print(f'Your balance after {time} year/s is Rs.{total: .3f}')
