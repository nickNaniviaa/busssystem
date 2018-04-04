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
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    license_plate = models.CharField(max_length=8)
    year = models.IntegerField()


class UpdBusFeed(models.Model):
    bus_id = models.IntegerField()
    driver_id = models.IntegerField()
    line_id = models.IntegerField()
    bus_stop_id = models.IntegerField()
    passengers_in = models.IntegerField()
    passengers_out = models.IntegerField()
    passengers_total = models.IntegerField()
    expected_arrival = models.DateField()
    arrival_time = models.DateField()
    departure_time = models.DateField()
