from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.CharField(max_length=255)
    clinic = models.BooleanField(default=False)
    email = models.EmailField(blank=True)
