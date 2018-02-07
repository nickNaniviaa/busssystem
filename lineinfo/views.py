from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Busline, Bus
from .serializer import BuslineSerializer, BusSerializer

from django.core.cache import cache


class BusLineList(APIView):
    def get(self, request):
        print("Valor da Cache:{}".format(+cache.get('numlinha')))
        queryset = Busline.objects.all()
        serializer = BuslineSerializer(queryset, many=True)

        return Response(serializer.data)


class BusList(APIView):
    def get(self, request):
        queryset = Bus.objects.all()
        serializer = BusSerializer(queryset, many=True)

        return Response(serializer.data)
