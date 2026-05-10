from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.CharField(max_length=255)
    clinic = models.BooleanField(default=False, null=True)
    email = models.EmailField(blank=True)


class Animal(models.Model):
    class Type(models.TextChoices):
        DOG = "dog", "dog"
        CAT = "cat", "cat"
        BIRD = "bird", "bird"

    animal_name = models.CharField()
    age = models.IntegerField()
    image = models.CharField()
    type = models.CharField(choices=Type.choices, default=Type.CAT)
    clinic = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False, related_name="clinic_animals"
    )
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, related_name="owned_pets"
    )


class Products(models.Model):
    product_name = models.CharField()
    description = models.CharField()
    image = models.CharField()
    price = models.IntegerField()
    clinic = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False, related_name="clinic_products"
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, related_name="ordered_items"
    )


class Appointment(models.Model):
    class Reason(models.TextChoices):
        R1 = "Shower", "Shower"
        R2 = "Nail Care", "Nail Care"
        R3 = "Router Check up", "Router Check up"

    date = models.DateField()
    time = models.TimeField()
    reason = models.CharField(choices=Reason.choices, default=Reason.R1)
    clinic = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False, related_name="clinic"
    )
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, related_name="owner"
    )
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, null=True, related_name="animal"
    )
