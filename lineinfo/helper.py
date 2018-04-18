from django.db import models
from django.core.cache import cache
from .models import Busline, Bus, UpdBusFeed
import googlemaps
import datetime, schedule, time
from geopy.distance import great_circle
from .gps_sensor import Gps
from .passenger_count import perform_meas
from .helper_song import play_next, add_current_station_queue, add_next_station_queue

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
    distance = gmaps.distance_matrix(origin,destination,departure_time=departure_time)
    value = distance["rows"][0]["elements"][0]["duration_in_traffic"]["value"] + previous_path
    return value

def set_cache_parameters(value_in_seconds, time_in_hours, line_id, stop_id):
    cache.set("timestop_seconds"+str(line_id), value=value_in_seconds + average_stop_time, timeout=None)
    cache.set("timestop_hour"+str(line_id), value=time_in_hours, timeout=None)

    if is_last_stop(stop_id):
        cache.set("update_time", False, None)

def is_last_stop(stop_id):
    return cache.get("last_stop_id") == stop_id

def next_stop_position():
    next_stop_index = cache.get('line_accumulator')+1    
    queryset_all = Busline.objects.all()
    queryset_filter = queryset_all.filter(line_id = cache.get('num_linha'),
                                            direction = cache.get('direction'),
                                            line_index = next_stop_index )
    

    latitude = queryset_filter.values('latitude')[0]['latitude']
    longitude = queryset_filter.values('longitude')[0]['longitude']

    return latitude, longitude


def next_stop_id():
    next_stop_index = cache.get('line_accumulator')+1    
    queryset_all = Busline.objects.all()
    queryset_filter = queryset_all.filter(line_id = cache.get('num_linha'),
                                            direction = cache.get('direction'),
                                            line_index = next_stop_index )
    

    stop_id = queryset_filter.values('bus_stop_id')[0]['bus_stop_id']
    cache.set("next_stop_id", stop_id, None)

    return stop_id

def calculate_distance_to_next_stop():
    latitude, longitude = gps.get_coordinates()
    stop_latitude, stop_longitude = next_stop_position()
    distance = great_circle((latitude, longitude), (stop_latitude, stop_longitude)).meters

    return distance

def has_arrived():
    if not cache.get('end'): 
        distance = calculate_distance_to_next_stop()
        print(f'A distância é: {distance}')

        status = cache.get('arrival_flag')

        next_bus_stop_id = next_stop_id()

        if distance < 20 and not status:
            print("Chegou na Estação")
            cache.set('arrival_flag', True, None)
            arrival_time = datetime.datetime.now()
            cache.set('arrival_time', arrival_time, None)
            
            add_current_station_queue(next_bus_stop_id)

            if last_stop():
                finish_bus_route(arrival_time)

        elif distance > 20 and status:
            print("Saiu da Estação")
            cache.set('arrival_flag', False, None)
            departure_time = datetime.datetime.now()
            update_bus_route(departure_time)
            cache.set('update_time', True, None)

            #play proxima estação
            next_bus_stop_id = next_stop_id()
            add_next_station_queue(next_bus_stop_id)

        play_next()

def last_stop():
    return cache.get('next_stop_id') == cache.get('last_stop_id')

def update_bus_route(departure_time):
    bus_stop = cache.get('next_stop_id')
    cache.incr('line_accumulator', 1)
    print("Bus {} Bus Stop - with inc:".format(bus_stop, cache.get('line_accumulator')))
    
    passengers_in, passengers_out, current_passengers = perform_meas()

    arrival_time = cache.get('arrival_time')
    departure_time = departure_time

    save_new_entry(bus_stop, passengers_in, passengers_out, current_passengers,
                   arrival_time, departure_time )

def finish_bus_route(arrival_time):
    print("Last Bus Stop")
    bus_stop = cache.get('last_stop_id')
    
    cache.set('end', True, None)
    cache.incr('line_accumulator', 1)

    passengers_out = cache.get('current_passengers')
    passengers_in = 0
    current_passengers = 0
    cache.set('current_passengers', 0, None)
    
    arrival_time = arrival_time
    departure_time = arrival_time
    
    save_new_entry(bus_stop, passengers_in, passengers_out, current_passengers,
                   arrival_time, departure_time )


    

def get_bus_parameters():
    line_accumulator = cache.get('line_accumulator')
    bus_id = 1 #Yes, Hardcoded
    driver_id = cache.get('driver_id')
    num_linha = cache.get('num_linha')
    expected_arrival = cache.get('timestop_hour'+str(line_accumulator), datetime.datetime.now())
    cache.set('timestop_hour'+str(line_accumulator), None) #Clear Cache

    return bus_id, driver_id, num_linha, expected_arrival

def save_new_entry(stop_id, passengers_in,
                   passengers_out, current_passengers,
                   arrival_time, departure_time):
    bus_id, driver_id, num_linha, expected_arrival = get_bus_parameters()

    new_entry = UpdBusFeed(bus_id = bus_id,
                           driver_id = driver_id,
                           line_id = num_linha,
                           bus_stop_id = stop_id,
                           passengers_in = passengers_in,
                           passengers_out = passengers_out,
                           passengers_total = current_passengers,
                           expected_arrival = expected_arrival,
                           arrival_time = arrival_time,
                           departure_time = departure_time)
    new_entry.save()
