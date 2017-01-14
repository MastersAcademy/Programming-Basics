#!/usr/bin/env python3
import json
from classes5 import Human
girl = Human('green', 'blond', '60', '175')
dict = {"eye_colour":"green", "hair_colour":"blond", "weight":"60", "height":"175"}
print (dict)
out_file = open("homework6.json","w")
json.dump(dict,out_file, indent=4)
out_file.close()