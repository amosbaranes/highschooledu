from django.urls import path
from .views import (home, get_courses)

app_name = 'education'

urlpatterns = [
    path('', home, name='home'),
    path('get_courses', get_courses, name='get_courses'),
]
