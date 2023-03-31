from django.urls import path
from .views import is_subscribed

urlpatterns = [
    path("is_subscribed/", is_subscribed, name="is_subscribed"),
]