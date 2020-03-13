def get_client_ip(django_request_object):
    try:
        x_forwarded_for = django_request_object.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = django_request_object.META.get('REMOTE_ADDR')
    except KeyError:
        ip = '0.0.0.0'
    return ip
