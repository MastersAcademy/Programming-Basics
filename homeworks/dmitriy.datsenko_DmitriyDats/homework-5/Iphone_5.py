from Iphone_4s import Iphone_4s


class Iphone_5(Iphone_4s):


    def __init__(self, model, version, screen, width, height, the_weight, camera):
        Iphone_4s.__init__(self, model, version, screen, width, height, the_weight, camera)
        self.model = model
        self.version = version
        self.screen = screen
        self.width = width
        self.height = height
        self.the_weight = the_weight
        self.camera = camera

#mobile2 = Iphone_5(model='Iphone 5', version='5', screen='4', width='58.6 mm', height='123.8 mm', the_weight='112 grams', camera='8 px')
#print(mobile2.screen)