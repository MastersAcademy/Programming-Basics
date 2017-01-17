from Sundial import Sundial
from ElectronicClock import ElectronicClock
from SandClock import SandClock
from Clockmaker import Clockmaker
from ParserJsonXml import ParserJsonXml
from SaveResult import SaveResult

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

#=====

json1 = ParserJsonXml(clockmaker1)
print(json1.parser_json())
print(json1.parser_xml())

json2 = ParserJsonXml(electronic1)

save1 = SaveResult()
save1.save_to("json", json1.parser_json())
save1.save_to("xml", json1.parser_xml())
save1.save_to("json", json2.parser_json())
save1.save_to("xml", json2.parser_xml())



