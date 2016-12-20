#!/usr/bin/env python3
print ("The object from the third hometask is the Human (Homo sapiens)")
class Human:
    def __init__(self, eye_colour, hair_colour, weight, height):
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour
        self.weight = weight
        self.height = height

    def colour(self):
        return "%s %s" % (self.eye_colour, self.hair_colour)

    def eye_colour(self):
        if self.eye_colour == 'blue':
            print ('Or, you are blue-eyed person!')
        elif self.eye_colour == 'brown':
            print ('Or, you are brown-eyed person!')
        else:
            print ('You are beautiful with your strange eyes!')

girl = Human ('blue', 'dark', 55, 165)
boy = Human ('brown', 'black', 75, 180)
print (girl.eye_colour)
print (boy.eye_colour)
print (girl.hair_colour)
print (girl.height)
print (girl.weight + boy.height)
print (boy.height)
print (girl.colour())
print (boy.colour())




