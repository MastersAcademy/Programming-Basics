#!/usr/bin/env python3
from classes5 import Human

class Child(Human):
    def __init__(self, eye_colour, hair_colour, weight, height):
        Human.__init__( self, eye_colour, hair_colour, weight, height )
    def _weight(self):
        print ("This information is private!")
    def _height(self):
        print ("This information is private!")

print (Child.weight())
print (Child.height())
print (Child.cooking())
