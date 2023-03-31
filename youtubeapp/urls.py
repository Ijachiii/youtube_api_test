from django.urls import path
from .views import is_subscribed_to_channel

urlpatterns = [
    path("", is_subscribed_to_channel, name="home"),
]