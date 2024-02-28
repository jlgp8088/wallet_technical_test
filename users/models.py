from django.db import models
from django.contrib.auth.models import User as DjangoUser


# Create your models here.

class UserFeeConfiguration(models.Model):
    mode = models.CharField(max_length=1)
    payment_fee_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    trade_fee_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    instant_payment= models.BooleanField()

class Users(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField(unique=True)
  user_login=models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
  fee_mode=models.ForeignKey(UserFeeConfiguration, on_delete=models.DO_NOTHING )

class Wallets(models.Model):
  address=models.CharField(max_length=100)
  user=models.OneToOneField(Users, on_delete=models.CASCADE)


