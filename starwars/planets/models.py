import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class Planet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    climate = models.CharField(max_length=255)
    terrain = models.CharField(max_length=255)
    films = JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
