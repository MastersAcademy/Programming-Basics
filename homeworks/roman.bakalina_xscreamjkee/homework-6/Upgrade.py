#!/usr/bin/env python3

from Vehicle import Vehicle


class UpgradeCar(Vehicle):
    
    def __init__(self, model ,color):
        Vehicle.__init__(self, model ,color)
        
    def upgrade_motor(self):
        return 'The motor in the \'%s\' modernized' % self.model

    def upgrade_body(self):
        return 'The body in the \'%s\' modernized' % self.model