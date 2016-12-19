from MobileTelephone import  MobilePhone


class IphoneFive(MobilePhone):


    def __init__(self, model, version, screen, width, height, the_weight, camera, cpu):
        MobilePhone.__init__(self, model, version, screen, width, height, the_weight, camera)
        self.cpu = cpu


    def __str__(self):
        return 'model: %s, version: %s, screen: %s, width: %s, height: %s, the weight: %s, camera: %s, video resolution: %s, CPU: $s' % (self.model, self.version, self.screen, self.width, self.height, self.the_weight, self.camera, self.cpu)


    def inclusion_mobile(self):
        self.on = 'on'
        self.off = 'off'

        inclusion = str(input('Turn on the phone '))

        if self.on == inclusion:
            print('You turn the phone on')
        elif inclusion != None:
            print('Blank lines are not accept')
        else:
            print('Try again')
