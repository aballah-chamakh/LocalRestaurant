from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_queryset(self):
        search = self.requets.GET.get('search')
        qs = self.Model.objects.filter(name=search)
        return qs 
