# Generated by Django 3.2.3 on 2021-08-17 19:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_measurement.models
import measurement.measures.distance
import measurement.measures.volume


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('vin', models.CharField(blank=True, max_length=17, verbose_name='Vehicle Identification Number')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('distance_unit', models.CharField(choices=[('km', 'Kilometre'), ('mi', 'Mile')], default='km', max_length=2)),
            ],
            options={
                'ordering': ['model', 'year', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='auto.car')),
            ],
            options={
                'ordering': ['parttype'],
            },
        ),
        migrations.CreateModel(
            name='PartType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('odometer', django_measurement.models.MeasurementField(blank=True, measurement=measurement.measures.distance.Distance, null=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Replacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField(blank=True, null=True)),
                ('distance', django_measurement.models.MeasurementField(blank=True, measurement=measurement.measures.distance.Distance, null=True)),
                ('part', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auto.part')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='part',
            name='parttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.parttype'),
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField(blank=True, null=True)),
                ('distance', django_measurement.models.MeasurementField(blank=True, measurement=measurement.measures.distance.Distance, null=True)),
                ('part', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auto.part')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.make')),
            ],
            options={
                'ordering': ['make'],
            },
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.carmodel'),
        ),
        migrations.CreateModel(
            name='ReplaceService',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auto.service')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='auto.replacement')),
            ],
            bases=('auto.service',),
        ),
        migrations.CreateModel(
            name='InspectService',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auto.service')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='auto.inspection')),
            ],
            bases=('auto.service',),
        ),
        migrations.CreateModel(
            name='FuelService',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auto.service')),
                ('volume', django_measurement.models.MeasurementField(blank=True, measurement=measurement.measures.volume.Volume, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuellings', to='auto.car')),
            ],
            bases=('auto.service',),
        ),
    ]
