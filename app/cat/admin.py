from django.contrib import admin # noqa

# Register your models here.
"""
Django admin customization.
"""

from django.utils.translation import gettext_lazy as _

from cat import models


class CatBreedsAdmin(admin.ModelAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['name', 'origin']
    fieldsets = (
        (None, {'fields': ('name', 'description')}),
        (_('Personal Info'), {'fields': ('origin',)}),
        (_('Important dates'), {'fields': ('date_joined',)}),
    )
    readonly_fields = ['date_joined']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name',
                'origin',
                'temperament',
                'description',
                'date_joined',
                'date_modified',
            ),
        }),
    )


admin.site.register(models.CatBreeds, CatBreedsAdmin)
