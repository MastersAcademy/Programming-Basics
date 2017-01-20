from addition import Home

class MyHome(Home):
    def __init__(self, wall, roof, doors, windows,rooms, create_new_room):
        Home.__init__(self, wall, roof, doors, windows, rooms, "my_home")
        self.addRooms()

    def addRooms(self):
        self.rooms +=1
        print("create new room!")

    def balcony(self):
        self.terrace = True






