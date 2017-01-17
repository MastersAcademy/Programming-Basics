class Television(object):
    def __init__(self, audio_format, video_format, signal_type, default_volume):
        self.audio_format = audio_format
        self.video_format = video_format
        self.signal_type = signal_type
        self.default_volume = default_volume


class Smart(Television):
    def __init__(self, audio_format, video_format, signal_type, default_volume, internet_connection, usb_connection):
        Television.__init__(self, audio_format, video_format, signal_type, default_volume)
        self.internet_connection = internet_connection if True else False
        self.usb_connection = usb_connection if True else False
