from django.db import models
from datetime import datetime 

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    uid = models.IntegerField(unique=True,primary_key=True,null=False)

class Temperature(models.Model):
    uid = models.ForeignKey(Device, on_delete=models.CASCADE)
    temperature = models.IntegerField(null=False)
    time = models.DateTimeField(null=False)

class Humidity(models.Model):
    uid = models.ForeignKey(Device, on_delete=models.CASCADE)
    humidity = models.IntegerField(null=False)
    time = models.DateTimeField(null=False)
