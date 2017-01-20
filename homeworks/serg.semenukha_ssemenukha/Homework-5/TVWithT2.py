from TV import BaseTV


class TVWithT2(BaseTV):
    def __init__(self, resolution, size):
        super().__init__(resolution, size)
        self.sources.append("t2")

    def __str__(self):
        return "I'm TV with T2 having %s resolution and %d inches display size" % (self.resolution, self.size)
