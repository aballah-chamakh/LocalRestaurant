from djanfo.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import FoodViewSet

router = routers.DefaultRouter()
router.register('food',FoodViewSet)


urlpattern = [
path('',include(router.urls)),
]
