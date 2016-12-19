from Car import Car

class MyCar(Car):
    def description(self):
        self.engine = '350 h.m.'
        self.gear_box = 6
        self.speed = '120 mph'

obj1 = MyCar('Black', '12 L/62 mph', '350 h.m.', '6', '120 mph')
print("Color: ", obj1.color)
print("Petrol: ", obj1.petrol)
print("Engine: ", obj1.engine)
print("Gear_box: ", obj1.gear_box)
print("Speed: ", obj1.speed)
#print(obj1.engine, obj1.gear_box, obj1.speed, obj1.color, obj1.petrol)