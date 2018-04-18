from django.core.cache import cache

from collections import deque
from pygame import mixer

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATION_DIR = os.path.join(BASE_DIR, 'audio_estacoes')

mixer.init()

def add_next_station_queue(station_id):
    current_queue = cache.get('station_queue')
    current_queue.append('proxima_parada.mp3')
    current_queue.append(f'estacao_{station_id}.mp3')

    cache.set('station_queue', current_queue, None)


def add_current_station_queue(station_id):
    current_queue = cache.get('station_queue')
    current_queue.append(f'estacao_{station_id}.mp3')

    cache.set('station_queue', current_queue, None)

def play_next():
    current_queue = cache.get('station_queue')
    if mixer.music.get_pos() == -1 and current_queue:
        next_song = current_queue.popleft()
        
        mixer.music.load(STATION_DIR+f'\{next_song}')
        mixer.music.play(0)

        cache.set('station_queue', current_queue, None)

