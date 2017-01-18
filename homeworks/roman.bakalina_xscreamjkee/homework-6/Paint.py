#!/usr/bin/env python3

from Vehicle import Vehicle


class Paint(Vehicle):

    def __init__(self, model, color, newcolor):
        Vehicle.__init__(self, model, color)
        self.newcolor = newcolor
    
    def change_color(self):
        return "On car\'%s\'color changed\'%s\'to\'%s\'" % (self.model, self.color, self.newcolor)
 
