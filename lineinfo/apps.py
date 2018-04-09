from django.apps import AppConfig
from django.core.cache import cache
from .cachesetup import readparams
class Line_Config(AppConfig):
    name = "lineinfo"
    def ready(self):
        from .models import Busline
        params = readparams()

        cache.set('driver_id',int(params[0]), None)
        cache.set('driver_name',params[1], None)
        cache.set('num_linha',int(params[2]), None)
        cache.set('direction',int(params[3]), None)
        cache.set('start_time',params[4], None)
        cache.set('line_accumulator', 0, None)

        cache.set('current_passengers', 0, None)
        cache.set("on_passengers", 0, None)
        cache.set("out_passengers", 0, None)

        cache.set('average_stop_time', 10, None)
        cache.set('update_time', True, None)
        cache.set('arrival_flag', False, None)
        cache.set('end', False, None)


        queryset_filter = Busline.objects.filter(line_id = params[2],
                                                direction = params[3])

        last_bus_stop = queryset_filter.order_by('line_index').reverse()[0]
        last_line_index = last_bus_stop.line_index
        last_stop_id = last_bus_stop.bus_stop_id

        cache.set("number_of_stops", last_line_index, None)
        cache.set("last_stop_id", last_stop_id, None)
        
        print("Setting Cache Done!")
