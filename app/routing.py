from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/clock/',consumers.clock.as_asgi()),
    re_path(r'ws/echo/',consumers.AsyncEchoConsumer.as_asgi()),
    re_path(r'ws/echo2/',consumers.AsyncEchoConsumer.as_asgi()),
    re_path(r'ws/echo3/',consumers.AsyncEchoConsumer.as_asgi()),
]