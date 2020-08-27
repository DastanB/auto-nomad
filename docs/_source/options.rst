=======
Options
=======

All options are taken from auto.ru_

- ``/api/cars/custom-options/readable/``
    **[GET]**

    | Use to get options in readable format
    |

- ``/api/cars/multiple-options/``
    **[GET]**

    | Use to get multiple options which you will use while creating *cars options*
    |

- ``/api/cars/custom-options/``
    **[POST]**

    | Use to create *cars options*
    | If it's *single field*, then give **boolean** value [true/false]
    | If it's *choice field*, then give ont **int** value [id]
    | If it's *multiple field*, then give **array** of *multiple options*
    |

- ``/api/cars/custom-options/{car_pk}/``
    **[GET]**

    | Use to get options in readable format of a specific car
    | ``{car_pk}`` = ID of a car
    |

.. _auto.ru : https://auto.ru
