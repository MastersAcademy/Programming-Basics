from Truck import Truck
from Automobile import Automobile

gaz = Truck(4, 3.3, 'Truck', 100)
print(gaz)

lanos = Automobile(4, 1.5, 'sedan', 5)
print(lanos)

gaz._Car__set_oil_level()

print(gaz.load_weight(10))
print(gaz.load_weight(50))
print(gaz.load_weight(50))
print(lanos.load_passenger(3))
print(lanos.load_passenger(3))

gaz.start_engine()
gaz.start_engine()
gaz.drive()
gaz.stop_engine()
gaz.start_engine()
gaz.start_engine()

print(gaz.drive())
print(lanos.drive())
