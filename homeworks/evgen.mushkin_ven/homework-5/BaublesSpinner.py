from SpoonBait import SpoonBait


class BaublesSpinner(SpoonBait):

    def __init__(self, color, catch, proportions, rotation):
        super(BaublesSpinner, self).__init__(color, catch, proportions)
        self.rotation = rotation

    def __str__(self):
        return "color: %s, catch: %s, proportions: %s, rotation: %s" % (self.color, self.catch, self.proportions, self.rotation)
