from django.contrib import admin

from Tariff.models import WaterTariff, AreaTariff


class WaterTariffAdmin(admin.ModelAdmin):
    list_display = ("title", "monthly_price",)
    ordering = ("title", "uuid",)
    readonly_fields = ("uuid",)

    @staticmethod
    def monthly_price(obj: WaterTariff):
        return obj.price / 100


class AreaTariffAdmin(admin.ModelAdmin):
    list_display = ("title", "monthly_price",)
    ordering = ("title", "uuid",)
    readonly_fields = ("uuid",)

    @staticmethod
    def monthly_price(obj: AreaTariff):
        return obj.price / 100


admin.site.register(WaterTariff, WaterTariffAdmin)
admin.site.register(AreaTariff, AreaTariffAdmin)
