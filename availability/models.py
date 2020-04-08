
from django.db import models
from django.utils.translation import ugettext_lazy as _

from availability.managers import AvailabilityManager


class Availability(models.Model):

    name = models.CharField(_('Name'), max_length=255)

    is_default = models.BooleanField(_('Is default'), default=False)

    color = models.CharField(_('Color'), max_length=100, blank=True)

    code = models.CharField(_('Code'), max_length=255, unique=True)

    objects = AvailabilityManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Availability')
        verbose_name_plural = _('Availability')


class AvailabilityField(models.ForeignKey):

    def __init__(
            self,
            to=Availability,
            verbose_name=_("Availability"),
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            *args,
            **kwargs):
        super().__init__(
            to=to,
            verbose_name=verbose_name,
            on_delete=on_delete,
            null=null,
            blank=blank,
            *args,
            **kwargs)
