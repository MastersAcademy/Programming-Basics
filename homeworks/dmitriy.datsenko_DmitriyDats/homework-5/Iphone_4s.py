class Iphone_4s():


    def __init__(self, model, version, screen, width, height, the_weight, camera):
        self.model = model
        self.version = version
        self.screen = screen
        self.width = width
        self.height = height
        self.the_weight = the_weight
        self.camera = camera


    def __str__(self):
        return 'model: %s, version: %s, screen: %s, width: %s, height: %s, the weight: %s, camera: %s' % (self.model, self.version, self.screen, self.width, self.height, self.the_weight, self.camera)

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


#mobile = Iphone_4s(model='Iphone 4S', version='5', screen='3.5', width='58.6 mm', height='115.2 mm', the_weight='140 grams', camera='8 px')
#mobile.inclusion_mobile()
#mobile.menu_button()
#mobile.icons()
#mobile.shutdown_mobile()