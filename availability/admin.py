
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from modeltranslation.admin import TranslationAdmin
from modeltranslation.utils import get_translation_fields

from availability.models import Availability


@admin.register(Availability)
class AvailabilityAdmin(TranslationAdmin):

    search_fields = get_translation_fields('name')

    list_display = ['name_tag', 'code', 'color']

    fieldsets = (
        (None, {
            'fields': (
                tuple(get_translation_fields('name')),
                ('is_default', 'code', 'color', ),
            )
        }),
    )

    def save_model(self, request, obj, form, change):

        if obj.is_default:
            Availability.objects.all().update(is_default=False)

        super().save_model(request, obj, form, change)

    def name_tag(self, obj):

        name = obj.name

        if obj.is_default:
            name += ' ({})'.format(_('Default'))

        return name

    name_tag.short_description = _('Name')
