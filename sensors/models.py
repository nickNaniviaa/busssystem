from django.db import models
from django.core.cache import cache
# Create your models here.
import random

class GlobalPostioningSystem(object):
    def __init__(self, params=''):
        self.params = params
        self.latitude = 1
        self.longitude = 2
    
    def get_coordinates(self):
        return (self.latitude,self.longitude)
    
    def check_within_range(self, latitude, longitude):
        return("Oi")
    
    def check_time_lastbustop(self):
        return("Calculando")

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
        
        update_cache()

        return(self.on, self.out, self.current)

    def update_cache(self):
        pass