from Classes import TV
from Classes import SmartTV

ussr_tv = TV("some_format", "some_format", "signal_type", 30)
smart_tv = SmartTV("some_format", "some_format", "signal_type", 30, False, True)

#Inheritance
print(ussr_tv.lower_default_volume())
print(smart_tv.rise_default_volume())

#Encapsulation
print(smart_tv.check_usb())
# print(ussr_tv.check_internet()) 'TV' object has no attribute 'check_internet'
