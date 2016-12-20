from Basic_class import Computer


class Notebook(Computer):
    def __init__(self, name, model, ram, cpu, wireless_connection, touchpad, webcam):
        super().__init__(name, model, ram, cpu)
        self.wireless_connection = wireless_connection
        self.touchpad = touchpad
        self.__webcam = webcam

    def __integrated_wireless_connection(self):
        return self.wireless_connection

    def integrated_mouse(self):
        return self.touchpad