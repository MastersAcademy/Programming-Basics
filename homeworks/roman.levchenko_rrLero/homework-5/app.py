from TennisRaquet import TennisRacket
from TennisRacketPrice import TennisRacketPrice

# Program for saving parameters of tennis rackets
# Dictionary will consist of 2 types of rackets : with price and without price
list_of_rackets = {}

n = True
counter = 0

while n:
    print('| 1 - if you want to add racket to list without price')
    print('| 2 - if you want to add racket to list with price')
    print('| 0 - if you want to exit')
    n = int(input('\n'))

    if n == 1:
        grip_size = int(input('Input length of grip from 1 to 5'))
        square_head = int(input('\nInput size of head from 600 to 700 sq.cm'))
        weight = int(input('\nInput weight from 300 to 400 gr'))
        brand = input("\nInput trade mark 'Head', 'Wilson', 'Babolat', 'Prince'")
        racket_without_price = TennisRacket(grip_size, square_head, weight, brand)
        list_of_rackets[counter] = racket_without_price.add_racket()
        counter += 1
    elif n == 2:
        grip_size = int(input('Input length of grip from 1 to 5'))
        square_head = int(input('\nInput size of head from 600 to 700 sq.cm'))
        weight = int(input('\nInput weight from 300 to 400 gr'))
        brand = input("\nInput trade mark 'Head', 'Wilson', 'Babolat', 'Prince'")
        price = int(input('\nInput price in dollars'))
        racket_with_price = TennisRacketPrice(grip_size, square_head, weight, brand)
        list_of_rackets[counter] = racket_with_price.add_price(price)
        counter += 1
    elif n == 0:
        break
    else:
        print('Uncorrect input')


for key, val in list_of_rackets.items():
    print('Number of racket in list', key,  ' Saved parameters of racket ', val)
