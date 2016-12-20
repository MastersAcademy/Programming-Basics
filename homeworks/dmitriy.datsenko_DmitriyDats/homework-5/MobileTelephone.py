class MobilePhone():


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