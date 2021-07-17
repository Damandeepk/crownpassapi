from django.contrib import admin
from .models import UserRegister,OwnerRegister,ControlledAreaStaff

# Register your models here.

admin.site.register(UserRegister)
admin.site.register(OwnerRegister)
admin.site.register(ControlledAreaStaff)