from django.conf import settings

default_exclude_fields = ['password']

USER_EXCLUDE_FIELDS = getattr(settings, 'DNA_USER_EXCLUDE_FIELDS', default_exclude_fields)
