class Car(object):
    def __init__(self, count_wheels, engine, body):
        self.count_wheels = count_wheels
        self.engine = engine
        self.body = body
        self.oil_level = 0
        self.engine_status = False


    def __set_oil_level(self):
        self.oil_level = 3
        return self.oil_level
         
    def start_engine(self):
        if self.oil_level == 0:
            self.engine_status = False
            print('Not enought oil')
            return self.engine_status
        else:
            self.oil_level -= 1
            print('Engine started!! Your oil level %i' %(self.oil_level))
            self.engine_status = True
            return self.engine_status

    def stop_engine(self):
        self.engine_status = False
        print('Engine stopped')
        return self.engine_status

    def drive(self):
        if self.engine_status == True:
            return 'drive with speed 70 km'
        else:
            return 'start engine before'
