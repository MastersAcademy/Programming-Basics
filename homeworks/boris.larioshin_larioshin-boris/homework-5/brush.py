class Brush(object):
    def __init__(self, title, bristles_type, platform_material):
        self.title = title
        self.bristles_types = bristles_type
        self.platform_material = platform_material

    def __str__(self):
        return "Торгівельна марка: %s, тип щєтини: %s, матеріал платформи: %s" % (self.title, self.bristles_types,
                                                                                  self.platform_material)
