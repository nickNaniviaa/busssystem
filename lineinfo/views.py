from django.shortcuts import render
from django.core.cache import cache

import itertools

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Busline, Bus
from .serializer import BuslineSerializer, BusSerializer

from sensors.models import GlobalPostioningSystem as gps
from sensors.models import PassengerCount as ps_count



class BusLineList(APIView):
     
    def get(self, request):
        #always query get_coordinates
        gps.get_coordinates()

        queryset_all = Busline.objects.all()
        
        #query for the last
        queryset_last = queryset_all.order_by("-bus_stop_id").filter(line_id = cache.get('num_linha'),
                                     direction = cache.get('direction'),
                                     line_index__gte = cache.get('line_accumulator'))[:1]
        
        #set number of stops
        if cache.get('number_of_stops') == 0:
            cache.set('number_of_stops',queryset_last.values_list('bus_stop_id').get()[0], None)
        
        #set querylimits by current stop & total number of stops
        if cache.get('line_accumulator') + 2 > cache.get('number_of_stops'):
            adjusted_index_stop = cache.get('number_of_stops') - cache.get('line_accumulator')
        else:
            adjusted_index_stop = 3

        #query for the first 3 bus stops
        queryset_first_three = queryset_all.filter(line_id = cache.get('num_linha'),
                                direction = cache.get('direction'),
                                line_index__gte = cache.get('line_accumulator')).order_by('id')[:adjusted_index_stop]
                                
        queryset = itertools.chain(queryset_first_three, queryset_last)
        serializer = BuslineSerializer(queryset, many=True)

        return Response(serializer.data)


class BusList(APIView):
    def get(self, request):
        queryset = Bus.objects.filter(id=1)
        serializer = BusSerializer(queryset, many=True)
        gps.get_coordinates()
        return Response(serializer.data)