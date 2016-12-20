#!/usr/bin/env python3
from classes5 import Human

class Woman(Human):
    def __init__(self, eye_colour, hair_colour, weight, height, cooking, kneeting, shopping):
        Human.__init__( self, eye_colour, hair_colour, weight, height)
        self.cooking = cooking
        self.kneeting = kneeting
        self.shopping = shopping

    def cooking(self):
        return "I'll cook your favourite meal!!!"

    def kneeting(self):
        return "I'll make a beautiful scarf for you!"

    def shopping(self):
        return "Ok, give me some money!"
