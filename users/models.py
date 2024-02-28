from django.db import models
from django.contrib.auth.models import User as DjangoUser
from transactions.models import UserFeeConfiguration


# Create your models here.

class Users(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField(unique=True)
  user_login=models.OneToOneField(DjangoUser, on_delete=models.CASCADE)


class Wallets(models.Model):
  address=models.CharField(max_length=100)
  user=models.OneToOneField(Users, on_delete=models.CASCADE)


