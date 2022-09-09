import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=125, null=False, blank=False)
    last_name = models.CharField(max_length=125, null=False, blank=False)
    email = models.EmailField(max_length=125, unique=True, null=False, blank=False)

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]