class Car():

    def __init__(self,color,petrol,engine,gear_box,speed):
        self.color = color
        self.petrol = petrol
        self.engine = engine
        self.gear_box = gear_box
        self.speed = speed
        self.__electric_current = "car battery"

    def __str__(self):
        return "color: %s, petrol: %s, engine: %s, gear_box: %s, speed %s" % (self.color, self.petrol, self.engine, self.gear_box, self.speed)

    def setElectric(self, el1):
        if self.__checkElectric(el1):
            self.__electric_current = el1
        else:
            print ('Wrong function')

    def __checkElectric(self, el1):
        return el1 == 'car battery'