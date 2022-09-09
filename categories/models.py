import uuid

from django.db import models


class Categories(models.Model):
    id   = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=125, unique=True)

