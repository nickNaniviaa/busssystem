from rest_framework import serializers
from .models import Busline, Bus
from django.core.cache import cache

from sensors.models import GlobalPostioningSystem as gps

class BuslineSerializer(serializers.ModelSerializer):
    real_time_arrival = serializers.SerializerMethodField()
    class Meta:
        model = Busline
        fields = ('line_id','line_name','direction','bus_stop_id','line_index',
                    'bus_stop_name','real_time_arrival')

    def get_real_time_arrival(self,obj):
        gps.check_within_range(obj.bus_stop_id, obj.line_index)
        return(1)



class BusSerializer(serializers.ModelSerializer):
    line_info = serializers.SerializerMethodField()
    gps_position = serializers.SerializerMethodField()
    direction = serializers.SerializerMethodField()
    accumulator = serializers.SerializerMethodField()

    
    class Meta:
        model = Bus
        exclude = ['brand','model','license_plate','year']

    def get_line_info(self, obj):
        return(cache.get('num_linha'))

    def get_direction(self, obj):
        return(cache.get('direction'))
    
    def get_accumulator(self, obj):
        return(cache.get('line_accumulator'))

    def get_gps_position(self,obj):
        return(cache.get('latitude'),cache.get('longitude'))
    