
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AvailabilityAppConfig(AppConfig):

    name = 'availability'
    verbose_name = _('Availability')


default_app_config = 'availability.AvailabilityAppConfig'
