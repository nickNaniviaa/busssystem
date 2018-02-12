from rest_framework import serializers
from .models import Busline, Bus

class BuslineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Busline
        fields = ('line_id','line_name','direction','bus_stop_id','line_index',
                    'bus_stop_name')

class BusSerializer(serializers.ModelSerializer):
    line_info = serializers.SerializerMethodField()
    class Meta:
        model = Bus
        fields = '__all__'

    
    def get_line_info(self, obj):
        return("Xa")
    