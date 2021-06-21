from django.urls import path
from django.conf.urls import url
from .views import (home, get_location, location_detail)

app_name = 'checkcashingchicago'

urlpatterns = [
    path('', home, name='home'),
    path('get_courses', get_location, name='get_location'),
    path('location_detail/<slug:slug>/', location_detail, name='location_detail'),
]
