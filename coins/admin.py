from django.contrib import admin
from coins.models import Country,CryptoCoin,FiatCoin
# Register your models here.

class GeneralList(admin.ModelAdmin):
    list_display = ("code", "name")

admin.site.register(Country, GeneralList)
admin.site.register(CryptoCoin, GeneralList)
admin.site.register(FiatCoin, GeneralList)
