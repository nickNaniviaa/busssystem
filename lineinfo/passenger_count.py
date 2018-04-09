from django.db import models
from django.core.cache import cache
from .models import Busline, Bus

import random
    


def perform_meas():
    current = cache.get("current_passengers")
    out = 0
    if current>4:
        out = random.randint(0,current-3)
    on = random.randint(0,3)
    current = current + on - out

    update_cache(current)
    return on, out, current

def update_cache(psg_current):
    cache.set("current_passengers", psg_current ,None)

