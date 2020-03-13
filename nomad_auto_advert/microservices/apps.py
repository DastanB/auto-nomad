from django.apps import AppConfig

services = None


class MicroservicesConfig(AppConfig):
    name = 'nomad_auto_advert.microservices'

    def ready(self):
        try:
            from nomad_auto_advert.microservices.models import Service
            global services
            services = Service.objects.all()
        except Exception as exception:
            pass
