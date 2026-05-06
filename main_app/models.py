from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()  # (min=17)
    image = models.CharField()
    clinic = models.BooleanField()
    email = models.EmailField()
    password = models.CharField()  # (min_length=8)

    def __str__(self):
        return self.name
