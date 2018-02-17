from django.db import models
from django.core.cache import cache
from .models import Busline, Bus

from .gpsreader import readGps
import googlemaps
import datetime

gmaps = googlemaps.Client(key='AIzaSyAGmmSFGnaJGgxm8qz1NP68IdKLMy8P2yU')
average_stop_time = cache.get('average_stop_time')


def get_updated_coordinates():
    latitude, longitude = readGps()
    set_cache(latitude,longitude)
    return (latitude,longitude)
def set_cache(latitude, longitude):
    cache.set('latitude', latitude,None)
    cache.set('longitude', longitude, None)

def has_arrived():
    pass


def calculate_duration_next_stop(stop_id,line_idx):
    next_bus_stop = cache.get('line_accumulator')+1


    #check which will be starting point: either current position OR a bus stop
    if line_idx == next_bus_stop:
        latitude , longitude = get_updated_coordinates() 
    else:
        queryset_all = Busline.objects.all()
        queryset_filter = queryset_all.filter(line_id = cache.get('num_linha'),
                            direction = cache.get('direction'),
                            line_index = line_idx-1)

        latitude = queryset_filter.values('latitude')[0]['latitude']
        longitude = queryset_filter.values('longitude')[0]['longitude']

    #set origin
    origin = str(latitude)+','+str(longitude)

    #query next bus stop info
    query_next = Busline.objects.get(id = stop_id)
    latitude_next = query_next.latitude
    longitude_next = query_next.longitude
    destination = str(latitude_next)+','+str(longitude_next)

    time_now = datetime.datetime.now()
    
    if line_idx == next_bus_stop:
        departure_time = 'now'
        previous_path=0
    else:
        previous_path = cache.get('timestop_seconds'+str(line_idx-1))
        time_delta = datetime.timedelta(seconds=previous_path)
        departure_time = time_now+time_delta
    #Calculate Distance
    distance = gmaps.distance_matrix(origin,destination,departure_time = departure_time)
    #sums the previous_path (if any) in addition to the duration - in seconds - provided by the 
    value = distance["rows"][0]["elements"][0]["duration_in_traffic"]["value"]+previous_path
    
    time_arrival = time_now+datetime.timedelta(seconds = value)

    cache.set("timestop_time"+str(line_idx),value+average_stop_time,value+60)

    #set a cache accordingly to the line_index value and sets it to expire at the planned time+60 seconds (it will be eventually refreshed for the next stations)
    cache.set("timestop_seconds"+str(line_idx),value+average_stop_time,value+60)


    return(time_arrival)
