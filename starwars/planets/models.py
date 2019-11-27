import uuid

from django.db import models


class Planet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    diameter = models.CharField(max_length=255, blank=True, null=True)
    rotation_period = models.CharField(max_length=255, blank=True, null=True)
    orbital_period = models.CharField(max_length=255, blank=True, null=True)
    gravity = models.CharField(max_length=255, blank=True, null=True)
    population = models.CharField(max_length=255, blank=True, null=True)
    climate = models.CharField(max_length=255)
    terrain = models.CharField(max_length=255)
    surface_water = models.CharField(max_length=255, blank=True, null=True)
    films = models.ManyToManyField('Film', blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Film(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    episode_id = models.IntegerField(null=True, blank=True)
    opening_crawl = models.CharField(max_length=255, null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    producer = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
