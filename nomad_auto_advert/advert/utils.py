from nomad_auto_advert.cars.models import Option, MultipleOption
from nomad_auto_advert.cars.constants import OVERVIEW_SINGLE_FIELDS, ANTI_THEFT_SINGLE_FIELDS, SALON_SINGLE_FIELDS, \
    OTHER_SINGLE_FIELDS, MULTIMEDIA_SINGLE_FIELDS, EXTERIOR_ELEMENTS_SINGLE_FIELDS, COMFORT_SINGLE_FIELDS, \
    SAFETY_SINGLE_FIELDS, OVERVIEW_CHOICE_FIELDS, ANTI_THEFT_CHOICE_FIELDS, SALON_CHOICE_FIELDS, OTHER_CHOICE_FIELDS, \
    MULTIMEDIA_CHOICE_FIELDS, EXTERIOR_ELEMENTS_CHOICE_FIELDS, COMFORT_CHOICE_FIELDS, SAFETY_CHOICE_FIELDS, \
    OVERVIEW_MULTIPLE_FIELDS, ANTI_THEFT_MULTIPLE_FIELDS, SALON_MULTIPLE_FIELDS, OTHER_MULTIPLE_FIELDS, \
    MULTIMEDIA_MULTIPLE_FIELDS, EXTERIOR_ELEMENTS_MULTIPLE_FIELDS, COMFORT_MULTIPLE_FIELDS, SAFETY_MULTIPLE_FIELDS


def make_car_custom_options_json(options):

    result = {
        'Обзор': [],
        'Защита от угона': [],
        'Салон': [],
        'Прочее': [],
        'Элементы экстерьера': [],
        'Мультимедиа': [],
        'Комфорт': [],
        'Безопасность': []
    }

    fields = Option._meta.get_fields()

    for field in fields:

        field_name = str(field).split('.')[2]

        if getattr(options, field_name):

            if field.get_internal_type() == 'BooleanField':

                if OVERVIEW_SINGLE_FIELDS.get(field_name):
                    result['Обзор'].append({field_name: OVERVIEW_SINGLE_FIELDS[field_name]})
                if ANTI_THEFT_SINGLE_FIELDS.get(field_name):
                    result['Защита от угона'].append({field_name: ANTI_THEFT_SINGLE_FIELDS[field_name]})
                if SALON_SINGLE_FIELDS.get(field_name):
                    result['Салон'].append({field_name: SALON_SINGLE_FIELDS[field_name]})
                if OTHER_SINGLE_FIELDS.get(field_name):
                    result['Прочее'].append({field_name: OTHER_SINGLE_FIELDS[field_name]})
                if MULTIMEDIA_SINGLE_FIELDS.get(field_name):
                    result['Мультимедиа'].append({field_name: MULTIMEDIA_SINGLE_FIELDS[field_name]})
                if EXTERIOR_ELEMENTS_SINGLE_FIELDS.get(field_name):
                    result['Элементы экстерьера'].append({field_name: EXTERIOR_ELEMENTS_SINGLE_FIELDS[field_name]})
                if COMFORT_SINGLE_FIELDS.get(field_name):
                    result['Комфорт'].append({field_name: COMFORT_SINGLE_FIELDS[field_name]})
                if SAFETY_SINGLE_FIELDS.get(field_name):
                    result['Безопасность'].append({field_name: SAFETY_SINGLE_FIELDS[field_name]})

            if field.get_internal_type() == 'PositiveSmallIntegerField':

                value = getattr(options, f'get_{field_name}_display')

                if OVERVIEW_CHOICE_FIELDS.get(field_name):
                    result['Обзор'].append({field_name: value()})
                if ANTI_THEFT_CHOICE_FIELDS.get(field_name):
                    result['Защита от угона'].append({field_name: value()})
                if SALON_CHOICE_FIELDS.get(field_name):
                    result['Салон'].append({field_name: value()})
                if OTHER_CHOICE_FIELDS.get(field_name):
                    result['Прочее'].append({field_name: value()})
                if MULTIMEDIA_CHOICE_FIELDS.get(field_name):
                    result['Мультимедиа'].append({field_name: value()})
                if EXTERIOR_ELEMENTS_CHOICE_FIELDS.get(field_name):
                    result['Элементы экстерьера'].append({field_name: value()})
                if COMFORT_CHOICE_FIELDS.get(field_name):
                    result['Комфорт'].append({field_name: value()})
                if SAFETY_CHOICE_FIELDS.get(field_name):
                    result['Безопасность'].append({field_name: value()})

            if field.get_internal_type() == 'ManyToManyField':

                m2m_options = getattr(options, field_name)

                if m2m_options.count() > 0:

                    if OVERVIEW_MULTIPLE_FIELDS.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Обзор'].append({field_name: m2m_options.all()[i].name})
                    if ANTI_THEFT_MULTIPLE_FIELDS.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Защита от угона'].append({field_name: m2m_options.all()[i].name})
                    if SALON_MULTIPLE_FIELDS.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Салон'].append({field_name: m2m_options.all()[i].name})
                    if OTHER_MULTIPLE_FIELDS.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Прочее'].append({field_name: m2m_options.all()[i].name})
                    if MULTIMEDIA_MULTIPLE_FIELDS.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Мультимедиа'].append({field_name: m2m_options.all()[i].name})
                    if EXTERIOR_ELEMENTS_MULTIPLE_FIELDS.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Элементы экстерьера'].append({field_name: m2m_options.all()[i].name})
                    if COMFORT_MULTIPLE_FIELDS.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Комфорт'].append({field_name: m2m_options.all()[i].name})
                    if SAFETY_MULTIPLE_FIELDS.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Безопасность'].append({field_name: m2m_options.all()[i].name})

    return result
