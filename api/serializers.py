from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import UserRegister,OwnerRegister,ControlledAreaStaff

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

class OwnerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerRegister
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class ControlledAreaStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlledAreaStaff
        fields = '__all__'


