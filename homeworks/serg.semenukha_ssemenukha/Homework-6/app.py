from TV import BaseTV
from TVWithT2 import TVWithT2


tv1 = BaseTV("4K", 44)
tv2 = TVWithT2("FullHD", 32)

print("TV #1")
print(" - writing json")
tv1.write_json()
print(" - writing xml")
tv1.write_xml()

print()
print()

print("TV #2")
print(" - writing json")
tv2.write_json()
print(" - writing xml")
tv2.write_xml()
