from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Busline, Bus
from .serializer import BuslineSerializer, BusSerializer

from django.core.cache import cache

from sensors.models import GlobalPostioningSystem, PassengerCount

gps = GlobalPostioningSystem()
passenger_counter = PassengerCount()


class BusLineList(APIView):
    def get(self, request):
        queryset = Busline.objects.all()
        print(gps.get_coordinates())
        queryset = queryset.filter(line_id = cache.get('num_linha'),
                                     direction = cache.get('direction'),
                                     line_index__gte = cache.get('line_accumulator') )

        serializer = BuslineSerializer(queryset, many=True)

        return Response(serializer.data)


class BusList(APIView):
    def get(self, request):
        queryset = Bus.objects.all()
        serializer = BusSerializer(queryset, many=True)
        print(gps.get_coordinates())
        return Response(serializer.data)
