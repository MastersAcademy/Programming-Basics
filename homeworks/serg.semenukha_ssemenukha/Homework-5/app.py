from TV import BaseTV
from TVWithT2 import TVWithT2


tv1 = BaseTV("4K", 44)
tv2 = TVWithT2("FullHD", 32)

print(tv1)
tv1.scan()

print(tv2)
tv2.scan()
