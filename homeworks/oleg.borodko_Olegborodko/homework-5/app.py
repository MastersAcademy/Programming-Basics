from Sundial import Sundial
from ElectronicClock import ElectronicClock
from SandClock import SandClock
from Clockmaker import Clockmaker

sundail1 = Sundial("10m", "100kg", "very long")
sundail1.show_time()
print("=" * 30)

electronic1 = ElectronicClock("5cm", "0.2kg", "4 years", "steel")
electronic1.show_time()
#print(electronic1.__battery_stock) encapsulation
print("=" * 30)

sand1 = SandClock("10cm", "0.2kg", "long", 3)
sand1.start()
print("=" * 30)

clockmaker1 = Clockmaker("Sasha", 24, 200)
clockmaker1.clock_buy(electronic1)
clockmaker1.clock_buy(sundail1)


