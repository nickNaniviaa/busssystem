from django.core.cache import cache

from .gpsreader import read_gps

class Gps(): # pylint: disable=too-few-public-methods
    def __init__(self):
        self.__latitude, self.__longitude = self.get_coordinates()

    def get_coordinates(self):
        self.__latitude, self.__longitude = read_gps()
        return (self.__latitude ,self.__longitude)

# def has_arrived():
#     lat, lon = get_updated_coordinates()
#     queryset_all = Busline.objects.all()
#     queryset_filter = queryset_all.filter(line_id = cache.get('num_linha'),
#                                             direction = cache.get('direction'),
#                                             line_index = cache.get('line_accumulator')+1)

#     latitude = queryset_filter.values('latitude')[0]['latitude']
#     longitude = queryset_filter.values('longitude')[0]['longitude']
    
#     arrived = vincenty((lat,lon),(latitude,longitude)).meters<10

#     if arrived:
#         cache.set('arrival_flag',arrived,None)

#         if cache.get('arrival_time') is None:
#             cache.set('arrival_time',datetime.datetime.now(),None)

#         #if door open, perform passenger measurement
#         # if get_door_status():
#         #     perform_meas()
    
#     #compare if the status was toogled
#     if not arrived and cache.get('arrival_flag'):
#         update_system()
