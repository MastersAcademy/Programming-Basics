from Door import Door
from ArmoredDoor import ArmoredDoor


door1 = Door("Berez", 85, 210, "Brown", 4515)
door2 = Door("Berez", 95, 200, "White", 4815)
door3 = ArmoredDoor("Straj", 105, 200, "Black", 6545, "Cylindrical")

door1.description_of_door()
door2.description_of_door()
door3.description_of_door()

