class Glasses:
    def __init__(self, frame, lens, shape):
        self.frame = frame
        self.lens = lens
        self.shape = shape

    def __str__(self):
        return "Glasses Frame: %s\n Lens: %s\n Shape: %s" % (self.frame, self.lens, self.shape)
