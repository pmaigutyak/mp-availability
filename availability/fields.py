
from django.forms import ModelChoiceField
from django.utils.translation import ugettext_lazy as _

from availability.models import Availability


class AvailabilityField(ModelChoiceField):

    def __init__(self, **kwargs):

        label = kwargs.pop('label', _('Availability'))

        kwargs.pop('initial', '')
        kwargs.pop('queryset', '')

        super().__init__(
            label=label,
            initial=Availability.objects.default(),
            queryset=Availability.objects.all(),
            **kwargs)
