class Car(object):
  
    def __init__(self, *args):
        if len(args) == 0:
            self.name = 'General'
            self.model = 'GM'
        if len(args) >= 1:
            self.name = args[0]
        if len(args) >= 2:
            self.model = args[1]
        if self.name in ( 'Porshe', 'Koenigsegg'):
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if len(args) >= 3:
            self.vehicle_type = args[2]
        else:
            self.vehicle_type = 'saloon'
        if self.vehicle_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
        self.speed = 0
    def is_saloon(self):    
        return self.vehicle_type == 'saloon'
    def drive(self, speed):
        if self.vehicle_type == 'trailer':
            self.speed =  77
        else:
            self.speed = 1000 
        return self