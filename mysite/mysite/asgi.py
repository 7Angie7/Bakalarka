# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import semaphore.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
export DJANGO_SETTINGS_MODULE=mysites.settings

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            semaphore.routing.websocket_urlpatterns
        )
    ),
})
