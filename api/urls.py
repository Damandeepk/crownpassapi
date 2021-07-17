from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet,UserRegisterViewSet,OwnerRegisterViewSet,ControlledAreaStaffViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('userregister', UserRegisterViewSet)
router.register('ownerregister', OwnerRegisterViewSet)
router.register('controlareastaff', ControlledAreaStaffViewSet)



urlpatterns = [
    path('', include(router.urls)),
]