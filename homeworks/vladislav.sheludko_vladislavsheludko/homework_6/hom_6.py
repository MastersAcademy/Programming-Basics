import json
from Car import Car
mycar = Car('Black', '12 L/60 mph', '350 h.m.', '6', '120 mph')
dict = {"Color": "Black", "Petrol": "12 L/60 mph", "Engine": "350 h.m.", "Gear_box": "6", "Speed": "120 mph"}
with open("home_6.json","w") as mycar:
    json.dump(dict, mycar, indent = 2)
