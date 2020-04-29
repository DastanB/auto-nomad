from django.apps import AppConfig


class CharacteristicsAppConfig(AppConfig):

    name = "nomad_auto_advert.characteristics"
    verbose_name = "Characteristics"

    def ready(self):
        try:
            import nomad_auto_advert.characteristics.signals  # noqa F401
        except ImportError:
            pass
