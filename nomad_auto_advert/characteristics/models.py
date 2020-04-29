from django.db import models


class TransmissionType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarBodyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EngineType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
