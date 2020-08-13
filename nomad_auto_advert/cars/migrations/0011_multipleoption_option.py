# Generated by Django 2.2.5 on 2020-08-06 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_carcolor_ext'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('separator_id', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headlights', models.PositiveSmallIntegerField(choices=[(1, 'Ксеноновые/Биксеноновые'), (2, 'Лазерные'), (3, 'Светодиодные')], null=True, verbose_name='Фары')),
                ('daytime_running_lights', models.BooleanField(default=False, verbose_name='Дневные ходовые огни')),
                ('fog_lights', models.BooleanField(default=False, verbose_name='Противотуманные фары')),
                ('automatic_headlight_range_control', models.BooleanField(default=False, verbose_name='Автоматический корректор фар')),
                ('headlight_washer', models.BooleanField(default=False, verbose_name='Омыватель фар')),
                ('adaptive_lighting_system', models.BooleanField(default=False, verbose_name='Система адаптивного освещения')),
                ('high_beam_control_system', models.BooleanField(default=False, verbose_name='Система управления дальним светом')),
                ('rain_sensor', models.BooleanField(default=False, verbose_name='Датчик дождя')),
                ('light_sensor', models.BooleanField(default=False, verbose_name='Датчик света')),
                ('signaling', models.PositiveSmallIntegerField(choices=[(1, 'Сигнализация'), (2, 'Сигнализация с обратной связью')], null=True, verbose_name='Сигнализация')),
                ('central_locking', models.BooleanField(default=False, verbose_name='Центральный замок')),
                ('immobilizer', models.BooleanField(default=False, verbose_name='Иммобилайзер')),
                ('interior_penetration_sensor', models.BooleanField(default=False, verbose_name='Датчик проникновения в салон (датчик объема)')),
                ('seat_count', models.PositiveSmallIntegerField(choices=[(1, 'Количество мест: 2'), (2, 'Количество мест: 4'), (3, 'Количество мест: 5'), (4, 'Количество мест: 6'), (5, 'Количество мест: 7'), (6, 'Количество мест: 8'), (7, 'Количество мест: 9')], null=True, verbose_name='Количество мест')),
                ('interior_material', models.PositiveSmallIntegerField(choices=[(1, 'Ткань'), (2, 'Велюр'), (3, 'Комбинированный'), (4, 'Искусственная кожа'), (5, 'Алькантара'), (6, 'Кожа')], null=True, verbose_name='Материал салона')),
                ('interior_color', models.PositiveSmallIntegerField(choices=[(1, 'Светлый'), (2, 'Тёмный')], null=True, verbose_name='Цвет салона')),
                ('seat_height_adjustment', models.PositiveSmallIntegerField(choices=[(1, 'Сиденья водителя'), (2, 'Передних сидений')], null=True, verbose_name='Регулировка сидений по высоте')),
                ('seat_position_memory', models.PositiveSmallIntegerField(choices=[(1, 'Сиденья водителя'), (2, 'Передних сидений')], null=True, verbose_name='Память положения сидений')),
                ('front_sport_seats', models.BooleanField(default=False, verbose_name='Спортивные передние сиденья')),
                ('seat_with_massage', models.BooleanField(default=False, verbose_name='Сиденья с массажем')),
                ('heated_steering_wheel', models.BooleanField(default=False, verbose_name='Обогрев рулевого колеса')),
                ('leather_steering_wheel', models.BooleanField(default=False, verbose_name='Отделка кожей рулевого колеса')),
                ('gear_lever_leather_trim', models.BooleanField(default=False, verbose_name='Отделка кожей рычага КПП')),
                ('luke', models.BooleanField(default=False, verbose_name='Люк')),
                ('panoramic_roof', models.BooleanField(default=False, verbose_name='Панорамная крыша / лобовое стекло')),
                ('ceiling_trim_in_black_fabric', models.BooleanField(default=False, verbose_name='Отделка потолка чёрной тканью')),
                ('front_center_armrest', models.BooleanField(default=False, verbose_name='Передний центральный подлокотник')),
                ('third_rear_headrest', models.BooleanField(default=False, verbose_name='Третий задний подголовник')),
                ('third_row_of_seats', models.BooleanField(default=False, verbose_name='Третий ряд сидений')),
                ('folding_rear_seats', models.BooleanField(default=False, verbose_name='Складывающееся заднее сиденье')),
                ('passenger_backrest_folding_function', models.BooleanField(default=False, verbose_name='Функция складывания спинки сиденья пассажира')),
                ('folding_table_on_the_backs_of_the_front_seats', models.BooleanField(default=False, verbose_name='Складной столик на спинках передних сидений')),
                ('tinted_glass', models.BooleanField(default=False, verbose_name='Тонированные стекла')),
                ('sun_blinds_in_rear_doors', models.BooleanField(default=False, verbose_name='Солнцезащитные шторки в задних дверях')),
                ('rear_window_sun_blind', models.BooleanField(default=False, verbose_name='Солнцезащитная шторка на заднем стекле')),
                ('interior_lighting', models.BooleanField(default=False, verbose_name='Декоративная подсветка салона')),
                ('decorative_pedals', models.BooleanField(default=False, verbose_name='Декоративные накладки на педали')),
                ('door_sills', models.BooleanField(default=False, verbose_name='Накладки на пороги')),
                ('spare_wheel', models.PositiveSmallIntegerField(choices=[(1, 'Полноразмерное'), (2, 'Докатка')], null=True, verbose_name='Запасное колесо')),
                ('towbar', models.BooleanField(default=False, verbose_name='Фаркоп')),
                ('crankcase_protection', models.BooleanField(default=False, verbose_name='Защита картера')),
                ('disc_type', models.PositiveSmallIntegerField(choices=[(1, 'Стальные диски'), (2, 'Легкосплавные')], null=True, verbose_name='Тип дисков')),
                ('disc_size', models.PositiveSmallIntegerField(choices=[(1, 'Диски 12"'), (2, 'Диски 13"'), (3, 'Диски 14"'), (4, 'Диски 15"'), (5, 'Диски 16"'), (6, 'Диски 17"'), (7, 'Диски 18"'), (8, 'Диски 19"'), (9, 'Диски 20"'), (10, 'Диски 21"'), (11, 'Диски 22"'), (12, 'Диски 23"'), (13, 'Диски 24"'), (14, 'Диски 25"'), (15, 'Диски 26"'), (16, 'Диски 27"'), (17, 'Диски 28"')], null=True, verbose_name='Размер дисков')),
                ('airbrushing', models.BooleanField(default=False, verbose_name='Аэрография')),
                ('decorative_moldings', models.BooleanField(default=False, verbose_name='Декоративные молдинги')),
                ('roof_rails', models.BooleanField(default=False, verbose_name='Рейлинги на крыше')),
                ('audio_system', models.PositiveSmallIntegerField(choices=[(1, 'Аудиоподготовка'), (2, 'Аудиосистема'), (3, 'Аудиосистема Hi-Fi'), (4, 'Аудиосистема с TV')], null=True, verbose_name='Аудиосистема')),
                ('aux', models.BooleanField(default=False, verbose_name='AUX')),
                ('bluetooth', models.BooleanField(default=False, verbose_name='Bluetooth')),
                ('usb', models.BooleanField(default=False, verbose_name='USB')),
                ('rear_seat_multimedia_system', models.BooleanField(default=False, verbose_name='Мультимедиа система для задних пассажиров')),
                ('navigation_system', models.BooleanField(default=False, verbose_name='Навигационная система')),
                ('voice_control', models.BooleanField(default=False, verbose_name='Голосовое управление')),
                ('android_auto', models.BooleanField(default=False, verbose_name='Android Auto')),
                ('car_play', models.BooleanField(default=False, verbose_name='CarPlay')),
                ('yandex_auto', models.BooleanField(default=False, verbose_name='Яндекс.Авто')),
                ('wireless_charge_for_phone', models.BooleanField(default=False, verbose_name='Беспроводная зарядка для смартфона')),
                ('socket_12v', models.BooleanField(default=False, verbose_name='Розетка 12V')),
                ('socket_220v', models.BooleanField(default=False, verbose_name='Розетка 220V')),
                ('conditioner', models.PositiveSmallIntegerField(choices=[(1, 'Кондиционер'), (2, 'Климат-контроль 1-зонный'), (3, 'Климат-контроль 2-зонный'), (4, 'Климат-контроль многозонный')], null=True, verbose_name='Кондиционер')),
                ('power_steering', models.PositiveSmallIntegerField(choices=[(1, 'Усилитель руля'), (2, 'Активный усилитель руля')], null=True, verbose_name='Усилитель руля')),
                ('cruise_control', models.PositiveSmallIntegerField(choices=[(1, 'Круиз-контроль'), (2, 'Адаптивный круиз-контроль')], null=True, verbose_name='Круиз-контроль')),
                ('camera', models.PositiveSmallIntegerField(choices=[(1, 'Передняя'), (2, 'Задняя'), (3, '360°')], null=True, verbose_name='Камера')),
                ('ob_board_computer', models.BooleanField(default=False, verbose_name='Бортовой компьютер')),
                ('electronic_dashboard', models.BooleanField(default=False, verbose_name='Электронная приборная панель')),
                ('head_up_display', models.BooleanField(default=False, verbose_name='Проекционный дисплей')),
                ('keyless_access_system', models.BooleanField(default=False, verbose_name='Система доступа без ключа')),
                ('start_engine_by_button', models.BooleanField(default=False, verbose_name='Запуск двигателя с кнопки')),
                ('start_stop_system', models.BooleanField(default=False, verbose_name='Система «старт-стоп»')),
                ('remote_engine_start', models.BooleanField(default=False, verbose_name='Дистанционный запуск двигателя')),
                ('programmable_pre_heater', models.BooleanField(default=False, verbose_name='Программируемый предпусковой отопитель')),
                ('electric_boot_lid', models.BooleanField(default=False, verbose_name='Электропривод крышки багажника')),
                ('open_truck_without_hands', models.BooleanField(default=False, verbose_name='Открытие багажника без помощи рук')),
                ('power_mirrors', models.BooleanField(default=False, verbose_name='Электропривод зеркал')),
                ('electric_folding_mirrors', models.BooleanField(default=False, verbose_name='Электроскладывание зеркал')),
                ('multifunctional_steering_wheel', models.BooleanField(default=False, verbose_name='Мультифункциональное рулевое колесо')),
                ('paddle_shifters', models.BooleanField(default=False, verbose_name='Подрулевые лепестки переключения передач')),
                ('cooled_glove_box', models.BooleanField(default=False, verbose_name='Охлаждаемый перчаточный ящик')),
                ('adjustable_pedal_assembly', models.BooleanField(default=False, verbose_name='Регулируемый педальный узел')),
                ('door_closer', models.BooleanField(default=False, verbose_name='Доводчик дверей')),
                ('cigarette_lighter_and_ashtray', models.BooleanField(default=False, verbose_name='Прикуриватель и пепельница')),
                ('abs', models.BooleanField(default=False, verbose_name='Антиблокировочная система (ABS)')),
                ('esp', models.BooleanField(default=False, verbose_name='Система стабилизации (ESP)')),
                ('tire_pressure_sensor', models.BooleanField(default=False, verbose_name='Датчик давления в шинах')),
                ('rear_door_block', models.BooleanField(default=False, verbose_name='Блокировка замков задних дверей')),
                ('era_glonass', models.BooleanField(default=False, verbose_name='ЭРА-ГЛОНАСС')),
                ('armored_body', models.BooleanField(default=False, verbose_name='Бронированный кузов')),
                ('airbag', models.ManyToManyField(null=True, related_name='airbags', to='cars.MultipleOption')),
                ('electric_heating', models.ManyToManyField(null=True, related_name='electric_heating', to='cars.MultipleOption')),
                ('heated_seat', models.ManyToManyField(null=True, related_name='heated_seats', to='cars.MultipleOption')),
                ('isofix_fastening_system', models.ManyToManyField(null=True, related_name='isofix_fastening_systems', to='cars.MultipleOption')),
                ('parking_assistance_system', models.ManyToManyField(null=True, related_name='parking_assistance_systems', to='cars.MultipleOption')),
                ('power_window', models.ManyToManyField(null=True, related_name='power_windows', to='cars.MultipleOption')),
                ('seat_electric_adjustment', models.ManyToManyField(null=True, related_name='seat_electric_adjustments', to='cars.MultipleOption')),
                ('seat_ventilation', models.ManyToManyField(null=True, related_name='seats_ventilation', to='cars.MultipleOption')),
                ('steering_wheel_adjustment', models.ManyToManyField(null=True, related_name='steering_wheel_adjustments', to='cars.MultipleOption')),
                ('support_system', models.ManyToManyField(null=True, related_name='support_systems', to='cars.MultipleOption')),
                ('suspension', models.ManyToManyField(null=True, related_name='suspensions', to='cars.MultipleOption')),
            ],
        ),
    ]