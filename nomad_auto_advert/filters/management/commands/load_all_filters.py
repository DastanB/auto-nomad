from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        commands = (
            "load_car_body_type",
            "load_car_drive_type",
            "load_car_engine_type",
            "load_car_transmission_type",
            "load_engine_volume"
        )

        for c in commands:
            self.stdout.write(f'Starting command - {c}')
            call_command(c)

        self.stdout.write('Done!!!')
