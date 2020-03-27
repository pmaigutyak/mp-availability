
from django.db import models

from availability.querysets import AvailabilityQuerySet


class AvailabilityManager(models.Manager):

    def get_queryset(self):
        return AvailabilityQuerySet(self.model, using=self._db)

    def default(self):
        try:
            return self.get_queryset().default()
        except Exception:
            pass

        return None
