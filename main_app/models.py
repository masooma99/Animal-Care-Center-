from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.CharField(max_length=255)
    clinic = models.BooleanField(default=False)
    email = models.EmailField(blank=True)


class Animal(models.Model):
    Name = models.CharField()
    age = models.IntegerField()
    image = models.CharField()
    clinic = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False, related_name="clinic_animals"
    )
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, related_name="owned_pets"
    )
