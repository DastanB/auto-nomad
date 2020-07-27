from django.apps import AppConfig


class GeoAppConfig(AppConfig):
    name = 'nomad_auto_advert.geo'
    verbose_name = 'Geo'

    def ready(self):
        try:
            import nomad_auto_advert.geo.signals  # noqa F401
        except ImportError:
            pass
