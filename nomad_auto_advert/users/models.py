from django.db import models


class User(object):
    def __init__(self, data):
        for k, v in data.items():
            setattr(self, k, v)
        self.data = data
        self.is_authenticated = True

    def __str__(self):
        return str(self.data)


class Profile(models.Model):
    """
    {'id': 1,
    'phone': '+77083495035',
    'email': '',
    'first_name': 'Yerlan',
    'last_name': 'nauryzbayev',
    'patronymic': 'Nurzhanuly',
    'city': None}
    """

    INDIVIDUAL, ENTITY = range(2)
    USER_TYPE_CHOICES = (
        (INDIVIDUAL, "Физическое лицо"),
        (ENTITY, "Юридическое лицо"),
    )

    user_ext = models.PositiveIntegerField(unique=True)
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=INDIVIDUAL)

    is_superuser = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

    points = models.IntegerField(default=0)

    @property
    def is_staff(self):
        return self.is_superuser or self.is_moderator

    def __str__(self):
        return f"{self.id} : {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        unique_together = ('user_ext', 'phone')


class ContactPhone(models.Model):
    profile = models.ForeignKey(
        to='users.Profile',
        related_name='contact_phones',
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} {self.phone}"
