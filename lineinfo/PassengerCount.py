from django.db import models
from django.core.cache import cache
from .models import Busline, Bus

import random
    
#all values are random based. This will allow us to fill our data/examples
cache.set("measurement_performed",False,None)

def perform_meas():
    if not cache.get('measurement_performed'):
        current = cache.get("current_passengers")
        if current>4:
            out = random.randint(0,current-3)
        on = random.randint(0,3)
        current =current + on - out

        # check if it is not the first time the measurement was requested to be performed
        
        #out = out + cache.get('out_passengers')
        #on = on + cache.get('on_passengers')

        update_cache(on, current, current)
        return(on, out, current)

def update_cache(psg_on, psg_out, psg_current):
    cache.set("on_passengers", psg_on,None)
    cache.set("out_passengers", psg_out , None)
    cache.set("current_passengers", psg_current ,None)
