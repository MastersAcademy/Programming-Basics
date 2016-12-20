from Vehicle import Vehicle

from Car import Car

from Cargo_car import Cargo_car

Car1 = Car('4', 'Cherkassy', 'Kiev', 'Petrol engine', 'true')

Cargo_car1 = Cargo_car('4', 'Cherkassy', 'Kiev', 'Petrol engine', 'true')

print("Car who are you?")
print(Car1.move_passangers())
print("lets move cargo?")
print(Car1.move_cargo())
print("where will you go?")
print(Car1.move_to)
print("I want to change this city")
print(Car1.change_move_to())

print("Cargo car who are you?")
print(Cargo_car1.move_cargo())
print("lets move cargo?")
print(Cargo_car1.move_passangers())
print("where will you go?")
print(Cargo_car1.move_to)
print("I want to change this city")
print(Car1.change_move_to())