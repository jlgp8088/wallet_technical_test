from django.contrib import admin
from users.models import UserFeeConfiguration
# Register your models here.

class GeneralList(admin.ModelAdmin):
    list_display = (
        "mode",
        "payment_fee_percentage",
        "trade_fee_percentage",
        "instant_payment",
    )

admin.site.register(UserFeeConfiguration, GeneralList)
