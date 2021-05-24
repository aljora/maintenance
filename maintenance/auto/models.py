from datetime import date
from django.db import models
from django_measurement.models import MeasurementField
from measurement.measures import Distance, Volume

# Create your models here.


KILOMETRE = 'km'
MILE = 'mi'
DISTANCE_UNIT_CHOICES = [
    (KILOMETRE, 'Kilometre'),
    (MILE, 'Mile')
]

LITRE = 'l'
VOLUME_UNIT_CHOICES = [
    (LITRE, 'Litre')
]


class Service(models.Model):
    date = models.DateField(default=date.today, null=True, blank=True)
    odometer = MeasurementField(
        measurement=Distance,
        null=True,
        blank=True,
        unit_choices=DISTANCE_UNIT_CHOICES
    )
    description = models.TextField()


class FuelService(Service):
    volume = MeasurementField(
        measurement=Volume,
        null=True,
        blank=True,
        unit_choices=VOLUME_UNIT_CHOICES
    )
    car = models.ForeignKey(
        'Car',
        on_delete=models.CASCADE,
        related_name='fuellings'
    )


class PartService(Service):
    activity = models.ForeignKey(
        'Activity',
        on_delete=models.CASCADE,
        related_name='services'
    )


class Activity(models.Model):
    duration = models.DurationField(null=True, blank=True)
    distance = MeasurementField(
        measurement=Distance,
        null=True,
        blank=True,
        unit_choices=DISTANCE_UNIT_CHOICES
    )
    part = models.OneToOneField(
        'Part',
        on_delete=models.CASCADE
    )


class Inspection(Activity):

    def __str__(self):
        return (
            f'Inspect {self.part} '
            f'every {self.duration} '
            f'or {self.distance}'
        )


class Replacement(Activity):

    def __str__(self):
        return (
            f'Replace {self.part} '
            f'every {self.duration} '
            f'or {self.distance}'
        )


class PartType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Part(models.Model):
    parttype = models.ForeignKey(
        'PartType',
        on_delete=models.CASCADE
    )
    car = models.ForeignKey(
        'Car',
        on_delete=models.CASCADE,
        related_name='parts'
    )

    def __str__(self):
        return f'{self.car} {self.parttype}'


class Make(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=255)
    make = models.ForeignKey(
        'Make',
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['name', 'make'],
            name='makemodel'
        )]

    def __str__(self):
        return f'{self.make} {self.name}'


class Car(models.Model):
    year = models.PositiveSmallIntegerField()
    model = models.ForeignKey(
        'CarModel',
        on_delete=models.CASCADE
    )
    vin = models.CharField(
        max_length=17,
        blank=True,
        verbose_name='Vehicle Identification Number',
    )
    distance_unit = models.CharField(
        max_length=2,
        choices=DISTANCE_UNIT_CHOICES,
        default=KILOMETRE
    )

    def __str__(self):
        return f'{self.year} {self.model}'
