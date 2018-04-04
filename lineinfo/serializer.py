from rest_framework import serializers
from django.core.cache import cache

from .helper import calculate_duration_next_stop
from .gps_sensor import Gps
from .models import Busline, Bus


class BuslineSerializer(serializers.ModelSerializer):
    real_time_arrival = serializers.SerializerMethodField()
    seconds_arrival = serializers.SerializerMethodField()
    class Meta:
        model = Busline
        fields = ('line_id','line_name','direction','bus_stop_id','line_index',
                    'bus_stop_name','real_time_arrival','seconds_arrival')

    def get_real_time_arrival(self,obj):
        arrival_time = calculate_duration_next_stop(obj.bus_stop_id,obj.line_index)
        formatted_arrival_time = str(arrival_time.hour)+'h:'+str(arrival_time.minute)+'m'
        return(formatted_arrival_time)

    def get_seconds_arrival(self,obj):
        value_in_seconds = cache.get('timestop_seconds'+str(obj.line_index))
        return(value_in_seconds-cache.get('average_stop_time'))



class BusSerializer(serializers.ModelSerializer):
    line_info = serializers.SerializerMethodField()
    gps_position = serializers.SerializerMethodField()
    direction = serializers.SerializerMethodField()
    accumulator = serializers.SerializerMethodField()
    passengers = serializers.SerializerMethodField()

    
    class Meta:
        model = Bus
        exclude = ['brand', 'model', 'license_plate', 'year']

    def get_line_info(self, obj):
        return(cache.get('num_linha'))

    def get_direction(self, obj):
        return(cache.get('direction'))
    
    def get_accumulator(self, obj):
        return(cache.get('line_accumulator'))

    def get_gps_position(self,obj):
        return(Gps().get_coordinates())
    
    def get_passengers(self,obj):
        return(cache.get('current_passengers'))

    