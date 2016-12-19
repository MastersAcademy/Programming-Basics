from Pistol import Pistol
from AsaultRifle import AsaultRifle

pm = Pistol('Pistol Makarov',9,93.5,'Semi-auto',2,'expansive')
print(pm)

tar21 = AsaultRifle('TAR-21',5.56,460,'Auto',11)
print(tar21)

pm.check_ammo()
tar21.check_ammo()
pm.shot()
pm.shot()
pm.shot()
pm.check_ammo()
tar21._AsaultRifle__shot(10)
tar21.shot()
tar21.shot()
tar21.check_ammo()

