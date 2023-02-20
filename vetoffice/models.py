from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)


class Patient(models.Model):
    breed = models.CharField(max_length=200)
    pet_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
