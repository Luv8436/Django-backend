from django.contrib import admin

# Register your models here.
from .models import Device , Temperature , Humidity

admin.site.register(Device)
admin.site.register(Temperature)
admin.site.register(Humidity)