from django.urls import path

from .views import *

urlpatterns = [
    path("", hp_controller, name="hp"),
    path("more", learn_more_controller, name="more"),
]
