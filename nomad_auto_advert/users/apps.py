from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "nomad_auto_advert.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import nomad_auto_advert.users.signals  # noqa F401
        except ImportError:
            pass
