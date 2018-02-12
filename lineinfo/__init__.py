lineinfo = 'lineinfo.apps.line_info_config'

from django.core.cache import cache
from .cachesetup import readparams

params = readparams()

cache.set('driver_id',params[0], None)
cache.set('driver_name',params[1], None)
cache.set('num_linha',params[2], None)
cache.set('direction',params[3], None)
cache.set('start_time',params[4], None)
cache.set('line_accumulator', 0, None)