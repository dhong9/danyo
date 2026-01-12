from django.db import models

# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length=50)
    iata = models.CharField(max_length=4)
    icao = models.CharField(max_length=4)