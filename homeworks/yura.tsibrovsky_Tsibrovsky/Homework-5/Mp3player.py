from Soundplaysystem import Soundplaysystem



class Mp3player(Soundplaysystem):
    def __init__(self, name, input_source, power_type, can_play_mp3files):
        Soundplaysystem.__init__(self, name, input_source, power_type, can_play_mp3files, 'buttons')
        self.can_play_mp3files = can_play_mp3files if can_play_mp3files else 'true'




sonywalkman = Mp3player('Sony Walkman', '2 W', 'AAA batteries', 'CD')
ipod = Mp3player('Apple Ipod', '2 W', 'inner rechargable batteries', 'flash memory')
print(sonywalkman)
print(ipod)


