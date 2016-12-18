class Car:

    def __init__(self):
        self.color = "Red"
        self.petrol = "10 L/62mph"
        self.__electric_current = 'car battery'

    def colors(self, col1):
        self.color = col1

    def petrols(self, pet1):
        self.petrol = pet1
  # інкапсуляція
    def setElectric(self, el1):
        if self.__checkElectric(el1):
            self.__electric_current = el1
        else:
            print ('Wrong function')

    def __checkElectric(self, el1):
        return el1 == 'car battery'
# наслідуючий клас
class MyCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.engine = '350 h.m.'
        self.gear_box = 6
        self.speed = '120 mph'

obj1 = Car()
print(obj1.color)
print(obj1.petrol)
obj1.colors("Red")
print(obj1.color)
obj1.petrols("Red")
print(obj1.petrol)

obj2 = MyCar()
obj2.colors("Black")
obj2.petrols("12 L/62 mph ")
print(obj2.engine, obj2.gear_box, obj2.speed, obj2.color, obj2.petrol)

