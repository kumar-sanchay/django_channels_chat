from django.urls import re_path
from .consumers import Consumer


websocket_consumer = [
    re_path(r'^chat/(?P<room_name>\w+)/', Consumer),
]