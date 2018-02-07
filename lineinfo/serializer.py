from rest_framework import serializers
from .models import Busline, Bus

class BuslineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Busline
        fields = ('line_id','line_name','direction','bus_stop_id','line_index',
                    'bus_stop_name', 'latitude','longitude')

class BusSerializer(serializers.ModelSerializer):
        class Meta:
            model = Bus
            fields = ('bus_id','brand','model','license_plate','year')