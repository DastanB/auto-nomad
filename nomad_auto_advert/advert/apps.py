from django.apps import AppConfig


class AdvertConfig(AppConfig):

    name = 'nomad_auto_advert.advert'
    verbose_name = 'Advert'

    def ready(self):
        try:
            import nomad_auto_advert.users.signals  # noqa F401
        except ImportError:
            pass
