from django.db import models


'''
Models to make advert search filter
'''


class CarBodyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"
