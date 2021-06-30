from django.urls import path
from django.conf.urls import url
from .views import (home,)

app_name = 'portfolio'

urlpatterns = [
    path('', home, name='home'),
]