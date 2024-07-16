from django.contrib import admin

from Progress.models import Progress


class ProgressAdmin(admin.ModelAdmin):
    ordering = ("uuid",)
    readonly_fields = ("uuid", "percentage",)


admin.site.register(Progress, ProgressAdmin)
