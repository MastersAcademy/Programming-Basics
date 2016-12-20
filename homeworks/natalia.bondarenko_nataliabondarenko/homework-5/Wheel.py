class Wheel(object):
    
    form = 'round shape'
    
    def __init__(self,name):
        self.name = name
        self.base_method = 'rotate around the axis'

    def __str__(self):
       return "%s is %s and %s" % (self.name,self.form,self.base_method) 
        
