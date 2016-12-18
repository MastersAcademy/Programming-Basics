from washer import Washer

class Washer_manual(Washer):
    def __init__(self, water,power,loading,mode):
       super(Washer_manual, self).__init__(water,power,loading,mode)

#    def __str__(self):
#        return "water: %s, power: %s, loading:%s, mode: %s,extraction :%s" %(self.water,self.power,self.loading,self.mode,self.extraction)

    def run_1(self):

        if self.loading == '1': print('word loading 1 kg:')
        elif self.loading < '5': print('word loading >1 and <5 kg:')
        elif self.loading > '5': print('overload ')
        else: pass


        if self.water != 'Hot': print('heating water 5 min:')
        else:   print('water is Hot')


        if self.mode == 'manual': print('Manual operation 30 min:')
        else:  print('alarm')


        return print('finish')

