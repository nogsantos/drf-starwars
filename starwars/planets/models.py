import uuid
from django.db import models


class Planet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    weather = models.CharField(max_length=255)
    solo = models.CharField(max_length=255)
    swapi_apearece = models.IntegerField(default=0)
