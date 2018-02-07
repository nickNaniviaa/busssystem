from django.db import models

# Create your models here.


class Busline(models.Model):
    line_id = models.IntegerField()
    line_name = models.CharField(max_length=20)
    direction = models.BooleanField()
    bus_stop_id = models.IntegerField()
    line_index = models.IntegerField()
    bus_stop_name = models.CharField(max_length=17)
    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    longitude = models.DecimalField(max_digits=13, decimal_places=10)


class Bus(models.Model):
    bus_id = models.IntegerField()
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    license_plate = models.CharField(max_length=8)
    year = models.IntegerField()