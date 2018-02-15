from django.db import models
from django.core.cache import cache
from .models import Busline, Bus


def seila():
    cache.set("chablau",12345)
    queryset_all = Busline.objects.all()
    print(queryset_all)
    return("o_i_sei_la")


def get_coordinates():
    latitude = 1
    longitude = 2 
    return (latitude,longitude)

def check_within_range(bus_stop_id, line_index):
    if cache.get('number_of_stops') != line_index:
        print(bus_stop_id)            
    else:
        print('Ultimo bus - Calcul')
    return("Oi")

def check_time_lastbustop():
    return("Calculando")

def setCache():
    pass