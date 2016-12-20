from SpoonBait import SpoonBait


class OscillatingBait (SpoonBait):
    def __init__(self, color, catch, proportions, oscillating):
        super(OscillatingBait, self).__init__(color, catch, proportions)
        self.oscillating = oscillating

    def __str__(self):
        return "color: %s, catch: %s, proportions: %s,  oscillating: %s" % (self.color, self.catch, self.proportions,
                                                                            self.oscillating)
