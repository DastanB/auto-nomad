XENON_BIXENON, LASER, LED = range(1, 4)
HEADLIGHTS_TYPES = (
    (XENON_BIXENON, 'Ксеноновые/Биксеноновые'),
    (LASER, 'Лазерные'),
    (LED, 'Светодиодные')
)

SIGNALING, FEEDBACK_SIGNALING = 1, 2
SIGNALING_TYPES = (
    (SIGNALING, 'Сигнализация'),
    (FEEDBACK_SIGNALING, 'Сигнализация с обратной связью')
)

SEAT_COUNT_2, SEAT_COUNT_4, SEAT_COUNT_5, SEAT_COUNT_6, SEAT_COUNT_7, SEAT_COUNT_8, SEAT_COUNT_9 = range(1, 8)
SEAT_COUNT_TYPES = (
    (SEAT_COUNT_2, 'Количество мест: 2'),
    (SEAT_COUNT_4, 'Количество мест: 4'),
    (SEAT_COUNT_5, 'Количество мест: 5'),
    (SEAT_COUNT_6, 'Количество мест: 6'),
    (SEAT_COUNT_7, 'Количество мест: 7'),
    (SEAT_COUNT_8, 'Количество мест: 8'),
    (SEAT_COUNT_9, 'Количество мест: 9'),
)

CLOTH, VELOUR, COMBINED, IMITATION_LEATHER, ALCANTARA, LEATHER = range(1, 7)
INTERIOR_MATERIAL_TYPES = (
    (CLOTH, 'Ткань'),
    (VELOUR, 'Велюр'),
    (COMBINED, 'Комбинированный'),
    (IMITATION_LEATHER, 'Искусственная кожа'),
    (ALCANTARA, 'Алькантара'),
    (LEATHER, 'Кожа'),
)

LIGHT, DARK = 1, 2
INTERIOR_COLOR_TYPES = (
    (LIGHT, 'Светлый'),
    (DARK, 'Тёмный'),
)

DRIVER_SEATS, FRONT_SEATS = 1, 2
SEAT_TYPES = (
    (DRIVER_SEATS, 'Сиденья водителя'),
    (FRONT_SEATS, 'Передних сидений'),
)

FULL_SIZE, DOKATKA = 1, 2
SPARE_WHEEL_TYPES = (
    (FULL_SIZE, 'Полноразмерное'),
    (DOKATKA, 'Докатка'),
)

STEEL_WHEELS, LIGHT_ALLOY = 1, 2
DISC_TYPES = (
    (STEEL_WHEELS, 'Стальные диски'),
    (LIGHT_ALLOY, 'Легкосплавные'),
)

WHEEL_12, WHEEL_13, WHEEL_14, WHEEL_15, WHEEL_16, WHEEL_17, WHEEL_18, WHEEL_19, WHEEL_20, WHEEL_21, WHEEL_22, \
    WHEEL_23, WHEEL_24, WHEEL_25, WHEEL_26, WHEEL_27, WHEEL_28 = range(1, 18)
DISC_SIZE_TYPES = (
    (WHEEL_12, 'Диски 12"'),
    (WHEEL_13, 'Диски 13"'),
    (WHEEL_14, 'Диски 14"'),
    (WHEEL_15, 'Диски 15"'),
    (WHEEL_16, 'Диски 16"'),
    (WHEEL_17, 'Диски 17"'),
    (WHEEL_18, 'Диски 18"'),
    (WHEEL_19, 'Диски 19"'),
    (WHEEL_20, 'Диски 20"'),
    (WHEEL_21, 'Диски 21"'),
    (WHEEL_22, 'Диски 22"'),
    (WHEEL_23, 'Диски 23"'),
    (WHEEL_24, 'Диски 24"'),
    (WHEEL_25, 'Диски 25"'),
    (WHEEL_26, 'Диски 26"'),
    (WHEEL_27, 'Диски 27"'),
    (WHEEL_28, 'Диски 28"'),
)

AUDIO_PREPARATION, AUDIO_SYSTEM, HI_FI, TV = range(1, 5)
AUDIO_SYSTEM_TYPES = (
    (AUDIO_PREPARATION, 'Аудиоподготовка'),
    (AUDIO_SYSTEM, 'Аудиосистема'),
    (HI_FI, 'Аудиосистема Hi-Fi'),
    (TV, 'Аудиосистема с TV'),
)

CONDITIONER, CLIMATE_CONTROL_1, CLIMATE_CONTROL_2, CLIMATE_CONTROL_MULTI_ZONE = range(1, 5)
CONDITIONER_TYPES = (
    (CONDITIONER, 'Кондиционер'),
    (CLIMATE_CONTROL_1, 'Климат-контроль 1-зонный'),
    (CLIMATE_CONTROL_2, 'Климат-контроль 2-зонный'),
    (CLIMATE_CONTROL_MULTI_ZONE, 'Климат-контроль многозонный'),
)

POWER_STEERING, ACTIVE_POWER_STEERING = 1, 2
POWER_STEERING_TYPES = (
    (POWER_STEERING, 'Усилитель руля'),
    (ACTIVE_POWER_STEERING, 'Активный усилитель руля'),
)

CRUISE_CONTROL, ADAPTIVE_CRUISE_CONTROL = 1, 2
CRUISE_CONTROL_TYPES = (
    (CRUISE_CONTROL, 'Круиз-контроль'),
    (ADAPTIVE_CRUISE_CONTROL, 'Адаптивный круиз-контроль'),
)

FRONT_CAMERA, BACK_CAMERA, CAMERA_360 = 1, 2, 3
CAMERA_TYPES = (
    (FRONT_CAMERA, 'Передняя'),
    (BACK_CAMERA, 'Задняя'),
    (CAMERA_360, '360°'),
)

OVERVIEW_SINGLE_FIELDS = (
    ('daytime_running_lights', 'Дневные ходовые огни'),
    ('fog_lights', 'Противотуманные фары'),
    ('automatic_headlight_range_control', 'Автоматический корректор фар'),
    ('headlight_washer', 'Омыватель фар'),
    ('adaptive_lighting_system', 'Система адаптивного освещения'),
    ('high_beam_control_system', 'Система управления дальним светом'),
    ('rain_sensor', 'Датчик дождя'),
    ('light_sensor', 'Датчик света')
)
OVERVIEW_CHOICE_FIELDS = (
    ('headlights', {
        'name_ru': 'Фары',
        'fields': HEADLIGHTS_TYPES
    }),
)
OVERVIEW_MULTIPLE_FIELDS = (
    ['electric_heating', {
        'name_ru': 'Электрообогрев',
        'fields': None
    }],
)

ANTI_THEFT_SINGLE_FIELDS = (
    ('central_locking', 'Центральный замок'),
    ('immobilizer', 'Иммобилайзер'),
    ('interior_penetration_sensor', 'Датчик проникновения в салон (датчик объема)'),
)
ANTI_THEFT_CHOICE_FIELDS = (
    ('signaling', {
        'name_ru': 'Сигнализация',
        'fields': SIGNALING_TYPES
    }),
)
ANTI_THEFT_MULTIPLE_FIELDS = []

SALON_SINGLE_FIELDS = (
    ('front_sport_seats', 'Спортивные передние сиденья'),
    ('seat_with_massage', 'Сиденья с массажем'),
    ('heated_steering_wheel', 'Обогрев рулевого колеса'),
    ('leather_steering_wheel', 'Отделка кожей рулевого колеса'),
    ('gear_lever_leather_trim', 'Отделка кожей рычага КПП'),
    ('luke', 'Люк'),
    ('panoramic_roof', 'Панорамная крыша / лобовое стекло'),
    ('ceiling_trim_in_black_fabric', 'Отделка потолка чёрной тканью'),
    ('front_center_armrest', 'Передний центральный подлокотник'),
    ('third_rear_headrest', 'Третий задний подголовник'),
    ('third_row_of_seats', 'Третий ряд сидений'),
    ('folding_rear_seats', 'Складывающееся заднее сиденье'),
    ('passenger_backrest_folding_function', 'Функция складывания спинки сиденья пассажира'),
    ('folding_table_on_the_backs_of_the_front_seats', 'Складной столик на спинках передних сидений'),
    ('tinted_glass', 'Тонированные стекла'),
    ('sun_blinds_in_rear_doors', 'Солнцезащитные шторки в задних дверях'),
    ('rear_window_sun_blind', 'Солнцезащитная шторка на заднем стекле'),
    ('interior_lighting', 'Декоративная подсветка салона'),
    ('decorative_pedals', 'Декоративные накладки на педали'),
    ('door_sills', 'Накладки на пороги'),
)
SALON_CHOICE_FIELDS = (
    ('seat_count', {
        'name_ru': 'Количество мест',
        'fields': SEAT_COUNT_TYPES
    }),
    ('interior_material', {
        'name_ru': 'Материал салона',
        'fields': INTERIOR_MATERIAL_TYPES
    }),
    ('interior_color', {
        'name_ru': 'Цвет салона',
        'fields': INTERIOR_COLOR_TYPES
    }),
    ('seat_height_adjustment', {
        'name_ru': 'Регулировка сидений по высоте',
        'fields': SEAT_TYPES
    }),
    ('seat_position_memory', {
        'name_ru': 'Память положения сидений',
        'fields': SEAT_TYPES
    })
)
SALON_MULTIPLE_FIELDS = (
    ['seat_electric_adjustment', {
        'name_ru': 'Электрорегулировка сидений',
        'fields': None
    }],
    ['heated_seat', {
        'name_ru': 'Подогрев сидений',
        'fields': None
    }],
    ['seat_ventilation', {
        'name_ru': 'Вентиляция сидений',
        'fields': None
    }]
)

OTHER_SINGLE_FIELDS = (
    ('towbar', 'Фаркоп'),
    ('crankcase_protection', 'Защита картера'),
)
OTHER_CHOICE_FIELDS = (
    ('spare_wheel', {
        'name_ru': 'Запасное колесо',
        'fields': SPARE_WHEEL_TYPES
    }),
)
OTHER_MULTIPLE_FIELDS = (
    ['suspension', {
        'name_ru': 'Подвеска',
        'fields': None
    }],
)

EXTERIOR_ELEMENTS_SINGLE_FIELDS = (
    ('airbrushing', 'Аэрография'),
    ('decorative_moldings', 'Декоративные молдинги'),
    ('roof_rails', 'Рейлинги на крыше'),
)
EXTERIOR_ELEMENTS_CHOICE_FIELDS = (
    ('disc_type', {
        'name_ru': 'Тип дисков',
        'fields': DISC_TYPES
    }),
    ('disc_size', {
        'name_ru': 'Размер дисков',
        'fields': DISC_SIZE_TYPES
    })
)
EXTERIOR_ELEMENTS_MULTIPLE_FIELDS = []

MULTIMEDIA_SINGLE_FIELDS = (
    ('aux', 'AUX'),
    ('bluetooth', 'Bluetooth'),
    ('usb', 'USB'),
    ('rear_seat_multimedia_system', 'Мультимедиа система для задних пассажиров'),
    ('navigation_system', 'Навигационная система'),
    ('voice_control', 'Голосовое управление'),
    ('android_auto', 'Android Auto'),
    ('car_play', 'CarPlay'),
    ('yandex_auto', 'Яндекс.Авто'),
    ('wireless_charge_for_phone', 'Беспроводная зарядка для смартфона'),
    ('socket_12v', 'Розетка 12V'),
    ('socket_220v', 'Розетка 220V'),
)
MULTIMEDIA_CHOICE_FIELDS = (
    ('audio_system', {
        'name_ru': 'Аудиосистема',
        'fields': AUDIO_SYSTEM_TYPES
    }),
)
MULTIMEDIA_MULTIPLE_FIELDS = []

COMFORT_SINGLE_FIELDS = (
    ("ob_board_computer", "Бортовой компьютер"),
    ("electronic_dashboard", "Электронная приборная панель"),
    ("head_up_display", "Проекционный дисплей"),
    ("keyless_access_system", "Система доступа без ключа"),
    ("start_engine_by_button", "Запуск двигателя с кнопки"),
    ("start_stop_system", "Система «старт-стоп»"),
    ("remote_engine_start", "Дистанционный запуск двигателя"),
    ("programmable_pre_heater", "Программируемый предпусковой отопитель"),
    ("electric_boot_lid", "Электропривод крышки багажника"),
    ("open_truck_without_hands", "Открытие багажника без помощи рук"),
    ("power_mirrors", "Электропривод зеркал"),
    ("electric_folding_mirrors", "Электроскладывание зеркал"),
    ("multifunctional_steering_wheel", "Мультифункциональное рулевое колесо"),
    ("paddle_shifters", "Подрулевые лепестки переключения передач"),
    ("cooled_glove_box", "Охлаждаемый перчаточный ящик"),
    ("adjustable_pedal_assembly", "Регулируемый педальный узел"),
    ("door_closer", "Доводчик дверей"),
    ("cigarette_lighter_and_ashtray", "Прикуриватель и пепельница"),
)
COMFORT_CHOICE_FIELDS = (
    ('conditioner', {
        'name_ru': 'Кондиционер',
        'fields': CONDITIONER_TYPES
    }),
    ('power_steering', {
        'name_ru': 'Усилитель руля',
        'fields': POWER_STEERING_TYPES
    }),
    ('cruise_control', {
        'name_ru': 'Круиз-контроль',
        'fields': CRUISE_CONTROL_TYPES
    }),
    ('camera', {
        'name_ru': 'Камера',
        'fields': CAMERA_TYPES
    })
)
COMFORT_MULTIPLE_FIELDS = (
    ['power_window', {
        'name_ru': 'Электростеклоподъёмники',
        'fields': None
    }],
    ['steering_wheel_adjustment', {
        'name_ru': 'Регулировка руля',
        'fields': None
    }],
    ['parking_assistance_system', {
        'name_ru': 'Система помощи при парковке',
        'fields': None
    }]
)

SAFETY_SINGLE_FIELDS = (
    ("abs", "Антиблокировочная система (ABS)"),
    ("esp", "Система стабилизации (ESP)"),
    ("tire_pressure_sensor", "Датчик давления в шинах"),
    ("rear_door_block", "Блокировка замков задних дверей"),
    ("era_glonass", "ЭРА-ГЛОНАСС"),
    ("armored_body", "Бронированный кузов"),
)
SAFETY_CHOICE_FIELDS = []
SAFETY_MULTIPLE_FIELDS = (
    ['airbag', {
        'name_ru': 'Подушки безопасности',
        'fields': None
    }],
    ['isofix_fastening_system', {
        'name_ru': 'Система крепления Isofix',
        'fields': None
    }],
    ['support_system', {
        'name_ru': 'Вспомогательные системы',
        'fields': None
    }]
)
