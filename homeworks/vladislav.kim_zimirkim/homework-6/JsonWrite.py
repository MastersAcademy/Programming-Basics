import json
from Gun import Gun
tar21 = Gun('TAR-21',5.56,460,'Auto',11)
dict = {}
dict['name'] = 'TAR-21'
dict['caliber'] = '5.56'
dict['barrel_length'] = '460'
dict['type_of_reload'] = 'Auto'
dict['ammount_of_ammo'] = '11'
with open ("AsaultRifle.json", "w") as Gun:
    json.dump(dict, Gun, indent=4)