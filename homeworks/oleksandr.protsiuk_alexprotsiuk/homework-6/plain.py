import random  # import random module


class Plain:  # main class
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __status(self):  # private method of Plain class
        var = ('full', 'half', 'empty')
        tank = random.choice(var)
        return (tank)

    @property
    def status(self):  # "Getter" method
        return self.__status()
