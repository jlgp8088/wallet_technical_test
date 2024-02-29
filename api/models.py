from django.db import models

# Create your models here.
choices_states = (('I','Initialized'),('P','Process'),('F','Fail'),('S','Success'),)

class LogTransactions(models.Model):
  hash_trx =models.CharField(max_length=100)
  wallet_origin =models.CharField(max_length=100)
  wallet_destiny =models.CharField(max_length=100)
  value=models.DecimalField(max_digits=10, decimal_places=2)
  state=models.CharField(max_length=1, choices= choices_states)