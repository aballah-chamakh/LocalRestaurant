from redt_framework import serializers
from .models import User,Profile

class UserSerialier(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only=True,required=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True,required=True)
    class Meta :
        fields = ('email','username','password','password2')
    def valid(self,data):
        email = self.data.get('email')
        qs = User.objects.filter(email=email)

        if qs :
            raise serializers.ValidationError('this email already exist')
        pw1 = self.data.get('password')
        pw2 = slef.data.get('passwoerd2')
        if pw1 != pw2 :
            raise serializers.ValidationError('passwords should match')

    def create(self,validated_data):
        email = self.validated_data.get('email')
        username = self.validated_data('username')
        password = self.validated_data('password')
        user_obj = User.objects.create(email=email,username=username)
        user_obj.set_password(password)
        user_obj.save()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta :
        
