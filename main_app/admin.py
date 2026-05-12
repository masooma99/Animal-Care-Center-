from django.contrib import admin
from .models import CustomUser, Products, Order, Appointment, Animal

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Appointment)
admin.site.register(Animal)
