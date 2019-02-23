from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image.url')
    class Meta :
        model = Food
        fields = ('name','image','decrition','price')
