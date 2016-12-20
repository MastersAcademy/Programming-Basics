class Computer:

    def __init__(self, name, model, ram, cpu):
        self.name = name
        self.model = model
        self.ram = ram
        self.cpu = cpu

    def system_settings(self):
        return str(self.name) + ' ' + self.model + ' ' + self.ram + ' ' + self.cpu
