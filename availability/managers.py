
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from availability.querysets import AvailabilityQuerySet


class AvailabilityManager(models.Manager):

    def get_queryset(self):
        return AvailabilityQuerySet(self.model, using=self._db)

    def with_code(self, code):
        try:
            return self.get_queryset().get(code=code)
        except ObjectDoesNotExist:
            pass

        return None

    def default(self):
        try:
            return self.get_queryset().default()
        except Exception:
            pass

        return None
