from Washer import Washer
class Washer_manual(Washer):
     def run_on(self):
         print('start')
         self.power_run()
         if self.loading == '0':
              print('not loading kg:')
         else:
              print('loading >1 kg')


         if self.water != 'Hot': print('heating water 5 min:')
         else: print('water is Hot')


         print('Manual operation 30 min:')
         return 'finish'


