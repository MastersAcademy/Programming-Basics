from computer import computer
from laptop import laptop

voltage = int (input (" Input your voltage? "))
computer1 = computer('ARTLINE_Home_H43_v02','Win10','win_pc', voltage)
hp = laptop('HP_Pavilion_dv6-6c55er','Win10','laptop_pc', voltage)
print(computer1)
print(computer1.working())
print(hp)
print(hp.working())
