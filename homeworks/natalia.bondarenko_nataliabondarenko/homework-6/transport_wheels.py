import collections
import random

from wheel import Wheel


class TransportWheels(Wheel):

    
    material = 'metal'
    components = 'wheel rim, hub, disk/spokes, automobile tire'
    types = ['Car wheel, specificity - disk',
           'Bicycle wheel, specificity - spokes',
           'Truck wheel, specificity - larger diameter']
        
    def __init__(self):
        Wheel.__init__(self, 'TransportWheels')
        self.base_method = 'rotate around the axis in the vertical plane'
        # Creation of the dictionary to write object data
        #to a file in json and XML formats:
        self.key_value = collections.OrderedDict(
            zip(('classes', 'form', 'base_method',
                 'material', 'components','types'),
                ('TransportWheels(Wheel)', self.form, self.base_method,
                 self.material, self.components, random.choice(self.types))
                )
            )
        
    def set_up(self):
        return 'Base settings: material - %s, components - %s.%s'%(self.material, self.components, self.types)

    
        
        



        
        
