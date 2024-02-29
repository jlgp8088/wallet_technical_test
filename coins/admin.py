from django.contrib import admin
from coins.models import Country,CryptoCoin,FiatCoin
# Register your models here.

admin.site.register(Country)
admin.site.register(CryptoCoin)
admin.site.register(FiatCoin)
