from django.apps import AppConfig


class FiltersAppConfig(AppConfig):

    name = "nomad_auto_advert.filters"
    verbose_name = "Filters"

    def ready(self):
        try:
            import nomad_auto_advert.filters.signals  # noqa F401
        except ImportError:
            pass
