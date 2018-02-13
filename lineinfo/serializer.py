from rest_framework import serializers
from .models import Busline, Bus
from django.core.cache import cache

class BuslineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Busline
        fields = ('line_id','line_name','direction','bus_stop_id','line_index',
                    'bus_stop_name')

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
    