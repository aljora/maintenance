from datetime import date, timedelta
from django.db import models
from django_measurement.models import MeasurementField
from django.urls import reverse
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

DAYSPERMONTH = 31


class Service(models.Model):
    date = models.DateField(default=date.today, null=True, blank=True)
    odometer = MeasurementField(
        measurement=Distance,
        null=True,
        blank=True,
        unit_choices=DISTANCE_UNIT_CHOICES
    )
    description = models.TextField(blank=True)

    # class Meta:
        # abstract = True

    def get_absolute_url(self):
        return reverse('auto:index')


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

    def __str__(self):
        return (
            f'{self.date} @ {self.odometer}: '
            f'{self.volume} for {self.car}'
        )


class InspectService(Service):
    activity = models.ForeignKey(
        'Inspection',
        on_delete=models.CASCADE,
        related_name='services'
    )

    def __str__(self):
        return (
            f'{self.date} @ {self.odometer}: '
            f'{self.activity}'
        )


class ReplaceService(Service):
    activity = models.ForeignKey(
        'Replacement',
        on_delete=models.CASCADE,
        related_name='services'
    )

    def __str__(self):
        return (
            f'{self.date} @ {self.odometer}: '
            f'{self.activity}'
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

    @property
    def months(self):
        return self.duration.days / DAYSPERMONTH

    @months.setter
    def months(self, value):
        self.duration = timedelta(days=value*DAYSPERMONTH)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse('auto:index')


class Inspection(Activity):

    def __str__(self):
        return (
            f'Inspect {self.part} '
            f'every {self.months:g} months '
            f'or {self.distance.km:g} {KILOMETRE}'
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
        return f'{self.parttype}'

    def get_absolute_url(self):
        return reverse('auto:part-detail', kwargs={'pk': self.pk})


class Make(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


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

    class Meta:
        ordering = ['make']


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

    def get_absolute_url(self):
        return reverse('auto:car-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['model', 'year']
