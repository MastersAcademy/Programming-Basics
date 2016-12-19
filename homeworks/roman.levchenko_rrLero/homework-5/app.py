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
        grip_size = int(input('Введите размер ручки от 1 до 5'))
        square_head = int(input('\nВведите площалдь головы от 600 до 700'))
        weight = int(input('\nВведите вес от 300 до 400 гр'))
        brand = input("\nВведите торговую марку 'Head', 'Wilson', 'Babolat', 'Prince'")
        racket_without_price = TennisRacket(grip_size, square_head, weight, brand)
        list_of_rackets[counter] = racket_without_price.add_racket()
        counter += 1
    elif n == 2:
        grip_size = int(input('Введите размер ручки от 1 до 5'))
        square_head = int(input('\nВведите площалдь головы от 600 до 700'))
        weight = int(input('\nВведите вес от 300 до 400 гр'))
        brand = input("\nВведите торговую марку 'Head', 'Wilson', 'Babolat', 'Prince'")
        price = int(input('\nВеедите цену ракетки в долларах'))
        racket_with_price = TennisRacketPrice(grip_size, square_head, weight, brand)
        list_of_rackets[counter] = racket_with_price.add_price(price)
        counter += 1
    elif n == 0:
        break
    else:
        print('Неккоректный ввод')


for key, val in list_of_rackets.items():
    print('Номер ракетки в списке', key,  ' Сохраненные параметры ракетки ', val)
