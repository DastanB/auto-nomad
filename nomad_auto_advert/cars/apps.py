from django.apps import AppConfig


class CarsAppConfig(AppConfig):

    name = "nomad_auto_advert.cars"
    verbose_name = "Cars"

    def ready(self):
        try:
            import nomad_auto_advert.cars.signals  # noqa F401
        except ImportError:
            pass
