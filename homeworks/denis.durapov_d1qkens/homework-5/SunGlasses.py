from Glasses import Glasses


class SunGlasses(Glasses):
    def __init__(self, model, frame, lens, shape, light_transmission, color):
        super().__init__(frame, lens, shape)
        self.model = model
        self.light_transmission = light_transmission
        self.color = color

    def __str__(self):
        return "Sunglasses Model: %s\n Frame: %s\n Lens: %s\n Shape: %s\n Light: %i\n Color: %s"\
               % (self.model, self.frame, self.lens, self.shape, self.light_transmission, self.color)
