from django.core.management import BaseCommand
from nomad_auto_advert.cars.management.commands.utils.csv_abstract_chainer import AbstractChainer
from nomad_auto_advert.cars.models import CarType, CarMark, CarModel, CarGeneration, CarSerie, CarModification, \
    CarOption, CarOptionValue, CarEquipment, CarCharacteristic, CarCharacteristicValue


class Command(BaseCommand):
    def chain_car_mark(self):
        mark_type_chainer = AbstractChainer(chain_model=CarMark, chain_with_model=CarType, chain_field='car_type_id',
                                            chain_with_field='car_type_ext', chain_by_field='ext')
        mark_type_chainer.chain()

    def chain_car_model(self):
        model_mark_chainer = AbstractChainer(chain_model=CarModel, chain_with_model=CarMark, chain_field='car_mark_id',
                                             chain_with_field='car_mark_ext', chain_by_field='ext')
        model_mark_chainer.chain()

    def chain_car_generation(self):
        generation_model_chainer = AbstractChainer(chain_model=CarGeneration, chain_with_model=CarModel,
                                                   chain_field='car_model_id', chain_with_field='car_model_ext',
                                                   chain_by_field='ext')
        generation_model_chainer.chain()

    def chain_car_serie(self):
        serie_generation_chainer = AbstractChainer(chain_model=CarSerie, chain_with_model=CarGeneration,
                                                   chain_field='car_generation_id',
                                                   chain_with_field='car_generation_ext', chain_by_field='ext')
        serie_generation_chainer.chain()

        serie_model_chainer = AbstractChainer(chain_model=CarSerie, chain_with_model=CarModel,
                                              chain_field='car_model_id', chain_with_field='car_model_ext',
                                              chain_by_field='ext')
        serie_model_chainer.chain()

    def chain_car_modification(self):
        modification_serie_chainer = AbstractChainer(chain_model=CarModification, chain_with_model=CarSerie,
                                                     chain_field='car_serie_id', chain_with_field='car_serie_ext',
                                                     chain_by_field='ext')
        modification_serie_chainer.chain()

    def chain_car_option(self):
        parent_chainer = AbstractChainer(chain_model=CarOption, chain_with_model=CarOption,
                                         chain_field='parent_id', chain_with_field='parent_ext',
                                         chain_by_field='ext')
        parent_chainer.chain()

    def chain_car_option_value(self):
        values_with_option_chainer = AbstractChainer(chain_model=CarOptionValue, chain_with_model=CarOption,
                                                     chain_field='car_option_id', chain_with_field='car_option_ext',
                                                     chain_by_field='ext')
        values_with_option_chainer.chain()

        values_with_equipment_chainer = AbstractChainer(chain_model=CarOptionValue, chain_with_model=CarEquipment,
                                                        chain_field='car_equipment_id',
                                                        chain_with_field='car_equipment_ext', chain_by_field='ext')
        values_with_equipment_chainer.chain()

    def chain_car_equipment(self):
        equipment_modification_chainer = AbstractChainer(chain_model=CarEquipment, chain_with_model=CarModification,
                                                         chain_field='car_modification_id',
                                                         chain_with_field='car_modification_ext', chain_by_field='ext')
        equipment_modification_chainer.chain()

    def chain_car_characteristic(self):
        parent_chainer = AbstractChainer(chain_model=CarCharacteristic, chain_with_model=CarCharacteristic,
                                         chain_field='parent_id', chain_with_field='parent_ext',
                                         chain_by_field='ext')
        parent_chainer.chain()

    def chain_car_characteristic_value(self):
        values_with_characteristic = AbstractChainer(chain_model=CarCharacteristicValue,
                                                     chain_with_model=CarCharacteristic,
                                                     chain_field='car_characteristic_id',
                                                     chain_with_field='car_characteristic_ext', chain_by_field='ext')
        values_with_characteristic.chain()

        values_with_modification = AbstractChainer(chain_model=CarCharacteristicValue,
                                                   chain_with_model=CarModification, chain_field='car_modification_id',
                                                   chain_with_field='car_modification_ext', chain_by_field='ext')
        values_with_modification.chain()

    '''
    AbstractChainer(chain_model=, chain_with_model=, chain_field='', chain_with_field='', chain_by_field='ext')
    '''

    def handle(self, *args, **options):
        self.chain_car_mark()
        self.chain_car_model()
        self.chain_car_generation()
        self.chain_car_serie()
        self.chain_car_modification()
        self.chain_car_option()
        self.chain_car_option_value()
        self.chain_car_equipment()
        self.chain_car_characteristic()
        self.chain_car_characteristic_value()

