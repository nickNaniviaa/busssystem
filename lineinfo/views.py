from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Busline, Bus
from .serializer import BuslineSerializer, BusSerializer

from django.core.cache import cache

from sensors.models import GlobalPostioningSystem, PassengerCount

import itertools

gps = GlobalPostioningSystem()
passenger_counter = PassengerCount()


class BusLineList(APIView):
    def get(self, request):
        queryset_all = Busline.objects.all()
        queryset_first_three = queryset_all.filter(line_id = cache.get('num_linha'),
                                     direction = cache.get('direction'),
                                     line_index__gte = cache.get('line_accumulator')).order_by('id')[:3]
        
        queryset_last = queryset_all.order_by("-bus_stop_id").filter(line_id = cache.get('num_linha'),
                                     direction = cache.get('direction'),
                                     line_index__gte = cache.get('line_accumulator'))[:1]
        
        if cache.get('number_of_stops') == None:
            cache.set('number_of_stops',queryset_last.values_list('bus_stop_id').get()[0])

        queryset = itertools.chain(queryset_first_three, queryset_last)
        serializer = BuslineSerializer(queryset, many=True)

        return Response(serializer.data)


class BusList(APIView):
    def get(self, request):
        queryset = Bus.objects.all()
        serializer = BusSerializer(queryset, many=True)
        print(gps.get_coordinates())
        print(cache.get('number_of_stops'))
        return Response(serializer.data)