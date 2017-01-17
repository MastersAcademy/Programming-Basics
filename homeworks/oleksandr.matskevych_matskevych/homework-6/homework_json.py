import json
from washing_machine import washing_machine
wm = washing_machine('1000', 'color', 'yes')
dict = {"rpm":"1000", "led_control":"color", "self_clean":"yes"}
print (dict)
out_file = open("homework6.json","w")
json.dump(dict, out_file, indent=4)
out_file.close()