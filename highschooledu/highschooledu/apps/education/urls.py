from django.urls import path
from .views import (home)

app_name = 'education'

urlpatterns = [
    path('', home, name='home'),
]
