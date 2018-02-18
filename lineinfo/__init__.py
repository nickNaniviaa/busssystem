lineinfo = 'lineinfo.apps.line_info_config'

from django.core.cache import cache
from .cachesetup import readparams

params = readparams()

cache.set('driver_id',int(params[0]), None)
cache.set('driver_name',params[1], None)
cache.set('num_linha',int(params[2]), None)
cache.set('direction',int(params[3]), None)
cache.set('start_time',params[4], None)
cache.set('line_accumulator', 1, None)

cache.set('current_passengers', 0, None)
cache.set("on_passengers", 0,None)
cache.set("out_passengers", 0 , None)

cache.set('average_stop_time',10,None)
cache.set('update_time',True,None)
cache.set('arrival_flag',False, None)