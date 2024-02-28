from django.db import models

class Country(models.Model):
    code=models.CharField(max_length=2, null=False)
    name=models.CharField(max_length=30)

class FiatCoin(models.Model):
    code=models.CharField(max_length=3, null=False, unique=True)
    name=models.CharField(max_length=30)
    country=models.ForeignKey(Country, on_delete=models.CASCADE)

class CryptoCoin(models.Model):
    code=models.CharField(max_length=4, null=False, unique=True)
    name=models.CharField(max_length=30)
    