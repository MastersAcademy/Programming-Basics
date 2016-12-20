class SpoonBait:

    def __init__(self, color, catch, proportions):
        self.color = color
        self.catch = catch
        self.proportions = proportions

    def __str__(self):
        return "color: %s, catch: %s, proportions: %s" % (self.color, self.catch, self.proportions)

    def __get_color(self):
        return self.color

    def check_color(self):
        return self.__get_color()
