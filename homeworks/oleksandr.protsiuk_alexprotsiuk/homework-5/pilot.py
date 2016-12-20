class Pilot:  # this class is processing info from "Getter" method of plain classes.
    def __init__(self, status):
        self.status = status
        if status is 'full':
            print('=======\nHi! I am a Pilot.\nWe have a full tank of fuel, so we can fly right now.')
        elif status is 'half':
            print('=======\nHi! I am a Pilot.\nWe have some fuel in tank, so we can fly, but not far from')
        else:
            print('=======\nHi! I am a Pilot.\nWe have no fuel in tank, so we can`t fly.')
