from django.db import models
from users.models import Users as User
from users.models import UserFeeConfiguration
from coins.models import CryptoCoin


class FeesHistory(models.Model):
    payment_fee = models.DecimalField(max_digits=10, decimal_places=2)
    trade_fee = models.DecimalField(max_digits=10, decimal_places=2)
    blockchain_fee = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    paid=models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING )
    created_at = models.DateTimeField(auto_now_add=True)

class FiatPayment(models.Model):
    amount_fiat = models.DecimalField(max_digits=10, decimal_places=2)
    amount_usdt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_usdt_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fiat_code = models.CharField(max_length=3)
    hash_trx = models.CharField(max_length=70, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    processed_date = models.DateTimeField(null=True)
    fees = models.ForeignKey(FeesHistory, on_delete=models.DO_NOTHING )

class Trade(models.Model):
    fiat_payment = models.OneToOneField(FiatPayment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    processed = models.BooleanField(default=False)

class BlockchainPayment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    coin = models.ForeignKey(CryptoCoin, on_delete=models.PROTECT)
    hash_trx = models.CharField(max_length=70, unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    processed_date = models.DateTimeField(null=True)
    fees = models.ForeignKey(FeesHistory, on_delete=models.DO_NOTHING )

