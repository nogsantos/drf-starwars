# Generated by Django 2.2.6 on 2019-11-27 00:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('episode_id', models.IntegerField(blank=True, null=True)),
                ('opening_crawl', models.CharField(blank=True, max_length=255, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('producer', models.CharField(blank=True, max_length=255, null=True)),
                ('release_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('diameter', models.CharField(blank=True, max_length=255, null=True)),
                ('rotation_period', models.CharField(blank=True, max_length=255, null=True)),
                ('orbital_period', models.CharField(blank=True, max_length=255, null=True)),
                ('gravity', models.CharField(blank=True, max_length=255, null=True)),
                ('population', models.CharField(blank=True, max_length=255, null=True)),
                ('climate', models.CharField(max_length=255)),
                ('terrain', models.CharField(max_length=255)),
                ('surface_water', models.CharField(blank=True, max_length=255, null=True)),
                ('films', models.ManyToManyField(blank=True, to='planets.Film')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
