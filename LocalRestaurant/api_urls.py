from django.urls import path
from django.conf.urls import include
from food import urls as food_urls

urlspatterns = [
path('',include(food_urls))


]
