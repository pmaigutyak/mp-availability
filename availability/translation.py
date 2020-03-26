
from modeltranslation.translator import translator

from availability.models import Availability


translator.register(Availability, fields=['name'])
