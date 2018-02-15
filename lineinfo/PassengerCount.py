from django.db import models
from django.core.cache import cache
from .models import Busline, Bus

import random
    
#all values are random based. This will allow us to fill our data/examples

def perform_meas():
    current = cache.get("current_passengers")
    if current>4:
        out = random.randint(0,current-3)
    on = random.randint(0,3)
    current = on - out

    if cache.get('line_accumulator') == cache.get('number_of_stops'):
        out = current
        current = 0
        on = 0
    
    update_cache(on, current, current)

    return(on, out, current)

def update_cache(psg_on, psg_out, psg_current):
    cache.set("on_passengers", psg_on,None)
    cache.set("out_passengers", psg_out , None)
    cache.set("current_passengers", psg_current ,None)
