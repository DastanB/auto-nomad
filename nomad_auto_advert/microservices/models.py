from django.conf import settings
from django.utils import timezone
from requests import Request, Session
from django.db import models


class Service(models.Model):
    CAPS = 'caps'

    name = models.CharField(
        unique=True,
        editable=False,
        max_length=100,
        help_text="Name of the service."
    )

    host = models.URLField(
        unique=True,
        editable=False,
        help_text="Host of the service. Ex. auth.example.com"
    )

    url = models.URLField(
        editable=True,
        help_text="URL of the proxy to the service, Ex. traefik IP address"
    )

    objects = models.Manager()

    class Meta:
        ordering = ['name', 'host']

    def __str__(self):
        return '{name} ({host})'.format(name=self.name, host=self.host)

    def __unicode__(self):
        return '{name} ({host})'.format(name=self.name, host=self.host)

    def remote_call(self, method, api='', headers=None, cookies=None, data=None,
                    request_kw=None, session_kw=None, timeout=None):
        if request_kw is None:
            request_kw = {}

        if session_kw is None:
            session_kw = {}

        if headers is None:
            headers = {}

        session = Session()

        url = self.url
        host = self.host if self.host[-1] != '/' else self.host[:-1]

        headers.update({
            'Host': host,
            'x-api-key': settings.COMMON_API_KEY,
        })

        api_endpoint = api if api[0] != '/' else api[1:]

        url = '{url}/{api_endpoint}'.format(url=url, api_endpoint=api_endpoint)
        request = Request(method=method.upper(), url=url, data=data, **request_kw)
        prepared_request = session.prepare_request(request)

        prepared_request.headers.update(headers)

        if data is not None:
            prepared_request.data = data

        if cookies is not None:
            session.cookies.update(cookies)

        response = session.send(request=prepared_request, **session_kw)

        return response


class BaseAPIKeyManager(models.Manager):

    def is_valid(self, key: str) -> bool:
        queryset = self.get_queryset()

        try:
            api_key = queryset.get(key=key)  # type: AbstractAPIKey
        except self.model.DoesNotExist:
            return False

        if not api_key.is_valid(key):
            return False

        if api_key.has_expired:
            return False

        return True


class APIKeyManager(BaseAPIKeyManager):
    pass


class AbstractAPIKey(models.Model):
    objects = APIKeyManager()

    name = models.CharField(max_length=50, blank=False, default=None,
                            help_text=(
                                "A free-form name for the API key. "
                                "Need not be unique. "
                                "50 characters max."
                            ),
    )
    key = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    revoked = models.BooleanField(blank=True, default=False,
                                  help_text=(
                                      "If the API key is revoked, clients cannot use it anymore. "
                                      "(This cannot be undone.)"
                                      ),
    )
    expiry_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Expires",
        help_text="Once API key expires, clients cannot use it anymore.",
    )

    class Meta:
        abstract = True
        ordering = ("-created",)
        verbose_name = "API key"
        verbose_name_plural = "API keys"

    def _has_expired(self) -> bool:
        if self.expiry_date is None:
            return False
        return self.expiry_date < timezone.now()

    _has_expired.short_description = "Has expired"
    _has_expired.boolean = True
    has_expired = property(_has_expired)

    def is_valid(self, key: str) -> bool:
        return key == self.key

    def __str__(self) -> str:
        return f"{self.name}: {self.key}"


class APIKey(AbstractAPIKey):
    pass
