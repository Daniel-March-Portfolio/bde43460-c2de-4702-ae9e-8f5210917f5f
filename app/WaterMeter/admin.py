from django.contrib import admin

from WaterMeter.models import WaterMeter, WaterMeterHistory


class WaterMeterAdmin(admin.ModelAdmin):
    list_display = ("apartment", "uuid",)
    ordering = ("uuid",)
    readonly_fields = ("uuid",)


class WaterMeterHistoryAdmin(admin.ModelAdmin):
    list_display = ("meter_apartment", "meter_id", "month", "year", "value",)
    ordering = ("meter_id", "-year", "-month", "uuid",)
    readonly_fields = ("uuid",)

    @staticmethod
    def meter_apartment(obj: WaterMeterHistory):
        return obj.meter.apartment


admin.site.register(WaterMeter, WaterMeterAdmin)
admin.site.register(WaterMeterHistory, WaterMeterHistoryAdmin)
