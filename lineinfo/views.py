from django.core.cache import cache

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Busline, Bus
from .serializer import BuslineSerializer, BusSerializer

from .helper import has_arrived

class BusLineList(APIView):
     
    def get(self, request):
        #query all objects to filter
        queryset_all = Busline.objects.all()

        #query for the first 3 bus stops
        queryset_filtered = queryset_all.filter(line_id = cache.get('num_linha'),
                                direction = cache.get('direction'),
                                line_index__gt = cache.get('line_accumulator'))
                                
        queryset = queryset_filtered
        serializer = BuslineSerializer(queryset, many=True)

        return Response(serializer.data)


class BusList(APIView):
    def get(self, request):
        queryset = Bus.objects.filter(id=1)
        has_arrived()
        serializer = BusSerializer(queryset, many=True)
        return Response(serializer.data)