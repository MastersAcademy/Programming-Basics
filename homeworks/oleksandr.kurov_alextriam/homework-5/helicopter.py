from aircraft import aircraft

class helicopter(aircraft):

    def __init__(self,trapdoor,fuel,windspeed):
        self.windspeed = windspeed
        self.fuel = fuel
        self.trapdoor=trapdoor

    def takeoff (self):

        if self.fuel =='full' and self.windspeed < 10:
            print ('takeoff is permitted')
        else:
            print (' WARNING! Fuel low, takeoff is not permitted')

#class_instance = helicopter ('close','full', 9)
