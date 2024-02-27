from django.db import models
from django.contrib.auth.models import User as DjangoUser


# Create your models here.

class Users(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField(unique=True)
  user_login=models.OneToOneField(DjangoUser, on_delete=models.CASCADE)


