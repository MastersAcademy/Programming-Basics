from Washer import Washer
class Washer_auto(Washer):
    def __init__(self, water, power, loading, mode, extraction):
        super(Washer_auto, self).__init__(water, power, loading, mode)
        self.extraction = extraction  # 100--1000 turnover/min
    def run_on(self):
        print('start')
        self.power_run()
        if self.loading == '1':
            print('word loading 1 kg:')
        elif self.loading < '5':
            print('word loading >1 and <5 kg:')
        elif self.loading > '5':
            print('overload ')
        else:
            pass


        if self.water != 'Hot':
            print('heating water 5 min:')
        else:
            print(' water is Hot')


        if self.extraction == '1000':
            print('word extraction 1 min:')
        else:
            print('word extraction 10 min:')


        return print('finish')

