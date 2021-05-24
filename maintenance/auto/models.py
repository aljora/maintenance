from datetime import date
from django.contrib.gis.measure import Distance
from django.db import models

# Create your models here.


class Service(models.Model):
    date = models.DateField(default=date.today)
    odometer = Distance()
    description = models.TextField()


class PartService(Service):
    activity = models.ForeignKey(
        'Activity',
        on_delete=models.CASCADE,
        related_name='services'
    )


class FuelService(Service):
    volume = models.PositiveSmallIntegerField()
    car = models.ForeignKey(
        'Car',
        on_delete=models.CASCADE,
        related_name='fuellings'
    )


class Activity(models.Model):
    duration = models.DurationField()
    distance = Distance()


class PartType(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Part(models.Model):
    parttype = models.ForeignKey(
        'PartType',
        on_delete=models.CASCADE
    )
    inspection = models.OneToOneField(
        'Activity',
        on_delete=models.SET_NULL
    )
    replacement = models.OneToOneField(
        'Activity',
        on_delete=models.SET_NULL
    )
    car = models.ForeignKey(
        'Car',
        on_delete=models.CASCADE,
        related_name='parts'
    )


class Make(models.Model):
    name = models.CharField(max_length=255, unique=True)


class CarModel(models.Model):
    name = models.CharField(max_length=255)
    make = models.ForeignKey(
        'Make',
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = models.UniqueConstraint(
            fields=['name', 'make'],
            name='makemodel'
        )


class Car(models.Model):
    year = models.PositiveSmallIntegerField()
    model = models.ForeignKey(
        'CarModel',
        on_delete=models.CASCADE
    )
    vin = models.CharField(max_length=17)
    KILOMETRE = 'km'
    MILE = 'mi'
    DISTANCE_UNIT_CHOICES = [
        (KILOMETRE, 'Kilometre'),
        (MILE, 'Mile')
    ]
    distance_unit = models.CharField(
        max_length=2,
        choices=DISTANCE_UNIT_CHOICES,
        default=KILOMETRE
    )
