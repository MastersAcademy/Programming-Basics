from DesktopLamp import DesktopLamp
from SmartDesktopLamp import SmartDesktopLamp

# creating instances
my_desktop_lamp = DesktopLamp("black", 17, "regular desktop lamp", 10.15)
my_smart_desktop_lamp = SmartDesktopLamp("green", 21, 50.99, True, True)

# serializing
my_desktop_lamp.encode_json()
my_desktop_lamp.encode_xml()
print()

# printing
print("*** Desktop lamp ***")
print("Lamp properties are: ")
print(my_desktop_lamp)
print(my_desktop_lamp.turn_light_on())
print(my_desktop_lamp.turn_light_off())
print()
print("*** Smart desktop lamp ***")
print("Smart lamp properties are: ")
print(my_smart_desktop_lamp)
print(my_smart_desktop_lamp.turn_light_on())
print(my_smart_desktop_lamp.turn_light_off())
print(my_smart_desktop_lamp.connect_to_network())
print(my_smart_desktop_lamp.exchange_data())
