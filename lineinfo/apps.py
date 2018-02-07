from django.apps import AppConfig
from django.core.cache import cache

class line_info_config(AppConfig):
    name = 'lineinfo'
    print("hi")
    def ready(self):
        cache.set('numlinha',12)
        print (cache.get('numlinha'))
