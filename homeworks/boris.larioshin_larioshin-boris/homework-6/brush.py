class Brush(object):
    """""
    base class describes a brush
    """""
    def __init__(self, title, bristles_type, platform_material):
        self.title = title
        self.bristles_type = bristles_type
        self.platform_material = platform_material

    def __str__(self):
        return "Trade mark:%s, bristles: %s, material: %s" % (self.title, self.bristles_type, self.platform_material)
