class aircraft:

    def __init__(self,trapdoor,fuel):
        self.fuel = fuel
        self.trapdoor=trapdoor

    def takeoff (self):
        if self.fuel =='full':
            print ('takeoff is permitted')
        else:
            print (' WARNING! Fuel low, takeoff is not permitted')



class_instance = aircraft ('close','full')


