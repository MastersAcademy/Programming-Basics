from aircraft import aircraft
class airplane (aircraft):

    def __init__(self,trapdoor,fuel,weight):
        self.fuel = fuel
        self.trapdoor=trapdoor
        self.weight=weight

    def takeoff (self):
        if self.fuel =='full' and self.trapdoor =='close' and self.weight<100 :
            print ('takeoff is permitted')
        else:
            print (' WARNING! Fuel low, takeoff is not permitted')


#class_instance = airplane('close','full',90)

