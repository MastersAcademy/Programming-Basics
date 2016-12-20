from MobileTelephone import MobilePhone


class IphoneFourS(MobilePhone):


    def __init__(self, model, version, screen, width, height, the_weight, camera, video_resolution):
        MobilePhone.__init__(self, model, version, screen, width, height, the_weight, camera)
        self.video_resolution = video_resolution

    def __str__(self):
        return 'model: %s, version: %s, screen: %s, width: %s, height: %s, the weight: %s, camera: %s, video resolution: %s' % (self.model, self.version, self.screen, self.width, self.height, self.the_weight, self.camera, self.video_resolution)

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


    def menu_button(self):
        self.click = 'click'

        button_mobile = str(input('Press the menu button (click) '))

        if self.click == button_mobile:
            print('You have entered a menu, icons appear on the screen')


    def icons(self):
        self.calculator = 'on-click'

        calculator = str(input('Click on the icon calculator (on-click) '))

        if calculator == 'on-click':
            number1 = float(input('First number '))
            addition = input('Addition ')
            number2 = float(input('The second number '))
            if addition == '+':
                print(number1+number2)
            elif addition == '-':
                print(number1-number2)
            elif addition == '/':
                print(number1/number2)
            elif addition == '*':
                print(number1*number2)
            elif addition == '%':
                print(number1%number2)
            else:
                print('Emptiness')
        elif calculator != None:
            print('Missed')
        else:
            print('Hold more')


    def shutdown_mobile(self):

        shutdown = str(input('Turn off the phone by pressing (off) '))

        if self.off == shutdown:
            print('Extinguished')
        elif self.off != None:
            print('Not that')
        else:
            print('Stronger push')
