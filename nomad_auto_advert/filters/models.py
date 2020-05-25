from django.db import models


'''
Models to make advert search filter
'''


class CarBodyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"


class EngineVolumeType(models.Model):
    amount = models.FloatField()

    def __str__(self):
        return f"{self.id}: {self.amount}"


class CarTransmissionType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"


class CarDriveType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"


class CarEngineType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"
