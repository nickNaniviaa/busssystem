from django.db import models
from django.core.cache import cache
# Create your models here.
import random

class GlobalPostioningSystem(object): 
    latitude = 1
    longitude = 2

    @classmethod
    def get_coordinates(inst):
        print(inst.latitude)
        return (inst.latitude,inst.longitude)

    @classmethod
    def check_within_range(inst, bus_stop_id, line_index):
        if cache.get('number_of_stops') != line_index:
            print(bus_stop_id)            
        else:
            print('Ultimo bus - Calcul')

        return("Oi")

    @classmethod
    def check_time_lastbustop():
        return("Calculando")

    @classmethod
    def setCache():
        pass

class PassengerCount(object):
    def __init__(self):
        self.on = 0
        self.out = 0
        self.current = 0
    
#all values are random based. This will allow us to fill our data

    def perform_meas(self):
        if self.current>4:
            self.out = random.randint(0,self.current-3)
        self.on = random.randint(0,3)
        self.current = self.on - self.out

        if cache.get('line_accumulator') == cache.get('number_of_stops'):
            self.out = self.current
            self.current = 0
            self.on = 0
        
        self.update_cache()

        return(self.on, self.out, self.current)

    def update_cache(self):
        pass