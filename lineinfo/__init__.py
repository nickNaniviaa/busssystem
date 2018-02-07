lineinfo = 'lineinfo.apps.line_info_config'

from django.core.cache import cache
from cachesetup import readparams

param = read_params()
cache.set('numlinha',12, None)