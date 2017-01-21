class BaseTV:
    def __init__(self, resolution, size):
        self.resolution = resolution
        self.size = size
        self.sources = ["hdmi", "dvi", "vga", "rf"]

    def scan(self):
        for source in self.sources:
            print("Scanning %s: no signal" % (source))

    def __str__(self):
        return "I'm basic TV having %s resolution and %d inches display size" % (self.resolution, self.size)
