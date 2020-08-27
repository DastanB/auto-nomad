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

                temp = dict(OVERVIEW_SINGLE_FIELDS)
                if temp.get(field_name):
                    result['Обзор'].append({field_name: temp[field_name]})
                temp = dict(ANTI_THEFT_SINGLE_FIELDS)
                if temp.get(field_name):
                    result['Защита от угона'].append({field_name: temp[field_name]})
                temp = dict(SALON_SINGLE_FIELDS)
                if temp.get(field_name):
                    result['Салон'].append({field_name: temp[field_name]})
                temp = dict(OTHER_SINGLE_FIELDS)
                if temp.get(field_name):
                    result['Прочее'].append({field_name: temp[field_name]})
                temp = dict(MULTIMEDIA_SINGLE_FIELDS)
                if temp.get(field_name):
                    result['Мультимедиа'].append({field_name: temp[field_name]})
                temp = dict(EXTERIOR_ELEMENTS_SINGLE_FIELDS)
                if temp.get(field_name):
                    result['Элементы экстерьера'].append({field_name: temp[field_name]})
                temp = dict(COMFORT_SINGLE_FIELDS)
                if temp.get(field_name):
                    result['Комфорт'].append({field_name: temp[field_name]})
                temp = dict(SAFETY_SINGLE_FIELDS)
                if temp.get(field_name):
                    result['Безопасность'].append({field_name: temp[field_name]})

            if field.get_internal_type() == 'PositiveSmallIntegerField':

                value = getattr(options, f'get_{field_name}_display')

                temp = dict(OVERVIEW_CHOICE_FIELDS)
                if temp.get(field_name):
                    result['Обзор'].append({field_name: value()})
                temp = dict(ANTI_THEFT_CHOICE_FIELDS)
                if temp.get(field_name):
                    result['Защита от угона'].append({field_name: value()})
                temp = dict(SALON_CHOICE_FIELDS)
                if temp.get(field_name):
                    result['Салон'].append({field_name: value()})
                temp = dict(OTHER_CHOICE_FIELDS)
                if temp.get(field_name):
                    result['Прочее'].append({field_name: value()})
                temp = dict(MULTIMEDIA_CHOICE_FIELDS)
                if temp.get(field_name):
                    result['Мультимедиа'].append({field_name: value()})
                temp = dict(EXTERIOR_ELEMENTS_CHOICE_FIELDS)
                if temp.get(field_name):
                    result['Элементы экстерьера'].append({field_name: value()})
                temp = dict(COMFORT_CHOICE_FIELDS)
                if temp.get(field_name):
                    result['Комфорт'].append({field_name: value()})
                temp = dict(SAFETY_CHOICE_FIELDS)
                if temp.get(field_name):
                    result['Безопасность'].append({field_name: value()})

            if field.get_internal_type() == 'ManyToManyField':

                m2m_options = getattr(options, field_name)

                if m2m_options.count() > 0:

                    temp = dict(OVERVIEW_MULTIPLE_FIELDS)
                    if temp.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Обзор'].append({field_name: m2m_options.all()[i].name})
                    temp = dict(ANTI_THEFT_MULTIPLE_FIELDS)
                    if temp.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Защита от угона'].append({field_name: m2m_options.all()[i].name})
                    temp = dict(SALON_MULTIPLE_FIELDS)
                    if temp.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Салон'].append({field_name: m2m_options.all()[i].name})
                    temp = dict(OTHER_MULTIPLE_FIELDS)
                    if temp.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Прочее'].append({field_name: m2m_options.all()[i].name})
                    temp = dict(MULTIMEDIA_MULTIPLE_FIELDS)
                    if temp.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Мультимедиа'].append({field_name: m2m_options.all()[i].name})
                    temp = dict(EXTERIOR_ELEMENTS_MULTIPLE_FIELDS)
                    if temp.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Элементы экстерьера'].append({field_name: m2m_options.all()[i].name})
                    temp = dict(COMFORT_MULTIPLE_FIELDS)
                    if temp.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Комфорт'].append({field_name: m2m_options.all()[i].name})
                    temp = dict(SAFETY_MULTIPLE_FIELDS)
                    if temp.get(field_name):
                        for i in range(m2m_options.count()):
                            result['Безопасность'].append({field_name: m2m_options.all()[i].name})

    return result
