from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer,UserRegisterSerializer,OwnerRegisterSerializer,ControlledAreaStaffSerializer
from .models import UserRegister,OwnerRegister,ControlledAreaStaff


class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = UserRegister.objects.all()
    serializer_class = UserRegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OwnerRegisterViewSet(viewsets.ModelViewSet):
    queryset = OwnerRegister.objects.all()
    serializer_class = OwnerRegisterSerializer

class ControlledAreaStaffViewSet(viewsets.ModelViewSet):
    queryset = ControlledAreaStaff.objects.all()
    serializer_class = ControlledAreaStaffSerializer



