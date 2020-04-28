from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        commands = [
            'load_car_types',
            'load_car_marks',
            'load_car_models',
            'load_car_generation',
            'load_car_serie',
            'load_car_modifications',
            'load_car_equipments',
            # 'load_car_options',
            'load_colors',
        ]

        for c in commands:
            self.stdout.write(f'Starting command - {c}')
            call_command(c)

        self.stdout.write('Done!!!')
