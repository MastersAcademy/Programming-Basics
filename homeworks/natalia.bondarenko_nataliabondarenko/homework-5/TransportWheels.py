import random
from Wheel import Wheel

class TransportWheels(Wheel):
    
    material = 'metal'
    components = 'wheel rim, hub, disk/spokes, automobile tire'
    types = ['Сar wheel, specificity - disk',
           'Bicycle wheel, specificity - spokes',
           'Truck wheel, specificity - larger diameter']
        
    def __init__(self):
        Wheel.__init__(self, 'TransportWheels')
        self.base_method = 'rotate around the axis in the vertical plane'
        
    def set_up(self):

        return 'Base settings: material - %s, components - %s.%s'%(self.material,self.components,random.choice(self.types))
    
