from addition import Home

class my_home(Home):
    def __init__(self, wall, roof, doors, windows, create_new_room):
        self.create_new_room = create_new_room

    def create_room(self):
        return "create new room!"


