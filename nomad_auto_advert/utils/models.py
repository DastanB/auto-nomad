from django.db import models


class ReverseOrderManager(models.Manager):
    pass


class NameModelMixin(object):
    @property
    def self_name(self):
        return f'{self._meta.app_label}.{self.__class__.__name__}.{self.id}'
