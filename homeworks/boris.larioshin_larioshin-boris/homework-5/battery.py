class Battery(object):
    def __init__(self, title, type='AA', power='1,5V'):
        self.title = title
        self.type = type
        self.power = power

    def battery_info(self):
        return print('Батарейка: ' + self.title + ' типу: ' + self.type + ' та потужністю: ' + self.power)