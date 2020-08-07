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
