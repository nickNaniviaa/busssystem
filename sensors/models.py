from django.db import models

# Create your models here.


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
        self.onto = 0
        self.out = 0
        self.current = 0
    
    def perform_meas(self):
        return(self.onto, self.out, self.current)