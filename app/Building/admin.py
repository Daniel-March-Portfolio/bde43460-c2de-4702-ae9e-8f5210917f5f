from django.contrib import admin

from Building.models import Building


class BuildingAdmin(admin.ModelAdmin):
    list_display = ("address",)
    ordering = ("address", "uuid", "uuid",)
    readonly_fields = ("uuid",)


admin.site.register(Building, BuildingAdmin)
