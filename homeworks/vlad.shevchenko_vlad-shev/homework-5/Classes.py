class TV(object):
    def __init__(self, audio_format, video_format, signal_type, default_volume):
        self.audio_format = audio_format
        self.video_format = video_format
        self.signal_type = signal_type
        self.default_volume = default_volume

    def rise_default_volume(self):
        self.default_volume = int(self.default_volume) + 10
        return self.default_volume

    def lower_default_volume(self):
        self.default_volume = int(self.default_volume) - 10
        return self.default_volume


class SmartTV(TV):
    def __init__(self,audio_format, video_format, signal_type, default_volume, internet_connection, usb_connection):
        TV.__init__(self, audio_format, video_format, signal_type, default_volume)
        self.internet_connection = internet_connection if True else False
        self.usb_connection = usb_connection if True else False

    def check_internet(self):
        if self.internet_connection:
            return True
        else:
            return False

    def check_usb(self):
        if self.usb_connection:
            return 'USB On'
