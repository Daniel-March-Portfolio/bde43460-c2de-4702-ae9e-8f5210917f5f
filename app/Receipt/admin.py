from django.contrib import admin

from Receipt.models import Receipt


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("apartment", "total_payment", "month", "year",)
    ordering = ("apartment", "-year", "-month", "uuid",)
    readonly_fields = ("uuid",)

    @staticmethod
    def total_payment(obj: Receipt):
        return obj.total_payment / 100


admin.site.register(Receipt, ReceiptAdmin)
