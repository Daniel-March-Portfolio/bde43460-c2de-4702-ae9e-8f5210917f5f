from django.contrib import admin

from Apartment.models import Apartment


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("building", "number",)
    ordering = ("building", "number", "uuid",)
    readonly_fields = ("uuid",)


admin.site.register(Apartment, ApartmentAdmin)
