
from django.db import models


class AvailabilityQuerySet(models.QuerySet):

    def default(self):
        return self.filter(is_default=True).first()
