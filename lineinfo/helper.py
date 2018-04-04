from django.db import models
from django.core.cache import cache
from .models import Busline, Bus
import googlemaps
import datetime, schedule, time
from geopy.distance import vincenty
from .gps_sensor import Gps


#gmaps and AUTH Key
gmaps = googlemaps.Client(key='AIzaSyAGmmSFGnaJGgxm8qz1NP68IdKLMy8P2yU')
#average stop time 
average_stop_time = cache.get('average_stop_time')
#gps object
gps = Gps()



def calculate_duration_next_stop(stop_id,line_id):
    if cache.get("update_time"):
        #get latitude/longitude from both origin and destiation
        latitude_origin, longitude_origin = starting_position(line_id)
        latitude_destination, longitude_destination = next_station(stop_id)
        #get previous path duration and departure time (in hours - accordingly)
        previous_path, departure_time = starting_time(line_id)
        #define origin and destination
        origin = format_query(latitude_origin, longitude_origin)
        destination = format_query(latitude_destination, longitude_destination)
        
        value = gmaps_distance_query(origin, destination, departure_time, previous_path)
        #set a cache accordingly to the line_index value and sets it to expire at the planned time+60 seconds (it will be eventually refreshed for the next stations)

        #calculates considering time_now the planned arrival (in hours)
        time_arrival = datetime.datetime.now() + datetime.timedelta(seconds = value)
        set_cache_parameters(value, time_arrival, line_id, stop_id)        

    else:
        time_arrival = cache.get("timestop_hour"+str(line_id))
   
    return(time_arrival)


def starting_position(line_id):
    if next_stop(line_id):
        latitude, longitude = Gps().get_coordinates()
    else:
        queryset_all = Busline.objects.all()
        queryset_filter = queryset_all.filter(line_id = cache.get('num_linha'),
                                              direction = cache.get('direction'),
                                              line_index = line_id-1)

        latitude = queryset_filter.values('latitude')[0]['latitude']
        longitude = queryset_filter.values('longitude')[0]['longitude']

    return latitude, longitude

def starting_time(line_id):
    if next_stop(line_id):
        departure_time = 'now'
        previous_path = 0
    else:
        previous_path = cache.get('timestop_seconds'+str(line_id-1))

        current_time = datetime.datetime.now()
        time_delta = datetime.timedelta(seconds=previous_path)
        departure_time = current_time + time_delta

    return previous_path, departure_time

def next_station(stop_id):
    query_next = Busline.objects.get(direction = cache.get('direction'), bus_stop_id = stop_id)
    latitude = query_next.latitude
    longitude = query_next.longitude

    return latitude, longitude

def format_query(latitude, longitude):
    return str(latitude) + ',' + str(longitude)

def next_stop(line_id):
    return line_id == cache.get('line_accumulator')+1

def gmaps_distance_query(origin, destination, departure_time, previous_path):
    distance = gmaps.distance_matrix(origin,destination,departure_time = departure_time)
    value = distance["rows"][0]["elements"][0]["duration_in_traffic"]["value"] + previous_path
    return value

def set_cache_parameters(value_in_seconds, time_in_hours, line_id, stop_id):
    cache.set("timestop_seconds"+str(line_id), value= value_in_seconds + average_stop_time, timeout= None)
    cache.set("timestop_hour"+str(line_id), value= time_in_hours, timeout= None)


    if is_last_stop(stop_id):
        cache.set("update_time", False, None)

def is_last_stop(stop_id):
    return cache.get("last_stop_id") == stop_id

def has_arrived():
    pass
