from rest_framework import exceptions, status
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from nomad_auto_advert.microservices.models import Service
from nomad_auto_advert.users.models import Profile


class CapsTokenAuthentication(BaseAuthentication):
    keyword = 'Token'
    model = None

    @property
    def caps(self):
        return Service.objects.get(name='caps')

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
            # TODO: in latest version of microservices, this condition returns None, instead of raising an error
            # return None

        elif len(auth) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        response = self.caps.remote_call('get', '/api/microservices/profile/',
                                         headers={'Authorization': 'Token {key}'.format(key=key)})
        if not status.is_success(response.status_code):
            print("☜(˚▽˚)☞", response.text)
            raise exceptions.AuthenticationFailed(response.json())

        response_data = response.json()
        print("☜(˚▽˚)☞", response_data)
        id = response_data.get('id')
        if not id:
            message = "Invalid token"
            raise exceptions.AuthenticationFailed(message)

        data = {
            'user_ext': id,
            'phone': response_data.get('phone'),
            'email': response_data.get('email'),
            'first_name': response_data.get('first_name'),
            'last_name': response_data.get('last_name'),
            'patronymic': response_data.get('patronymic'),
            'city': str(response_data.get('city').get('id')) if response_data.get('city') else ''
        }

        if Profile.objects.filter(user_ext=id).exists():
            profile = Profile.objects.get(user_ext=id)
            not_synced_fields = [x for x in data.keys() if data[x] != getattr(profile, x)]
            if len(not_synced_fields):
                print(f'not_synced_fields: {not_synced_fields}')
                for f in not_synced_fields:
                    setattr(profile, f, data[f])
                profile.save()
        else:
            profile = Profile.objects.create(**data)
        setattr(profile, 'is_authenticated', True)

        return profile, key

    def authenticate_header(self, request):
        return self.keyword


# TODO: Yerlan said that this snippet is required in order to serve swagger
class CapsPlainTokenAuthentication(CapsTokenAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth:
            return None
        try:
            token = auth[0].decode()
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)
