import os
from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarMark


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Car mark logo set started!')

        path = 'files/logo'
        images = os.listdir(path)
        counter = 0

        for file_name in images:
            image_path = os.path.join(path, file_name)

            if "_" in file_name and file_name[0].isdigit():
                self.stdout.write(file_name)

                mark_ext = file_name.split('_')[0]
                car_mark = CarMark.objects.get(ext=mark_ext)

                with open(image_path, 'rb') as target:
                    car_mark.logo.save(
                        file_name,
                        target
                    )

                counter += 1
            else:
                self.stdout.write(f'Error. File name: {file_name}')

        self.stdout.write(f'Done! Loaded: {counter} logos')
