from django.db import models
from users.models import Users as User

choices_mode = [('A', 'Mode A'), ('B', 'Mode B')]
class FiatPayment(models.Model):
    amount_fiat = models.DecimalField(max_digits=10, decimal_places=2)
    amount_usdt = models.DecimalField(max_digits=10, decimal_places=2)
    fiat_code = models.CharField(max_length=3)
    hash_trx = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    processed_date = models.DateTimeField(auto_now_add=True)

class Trade(models.Model):
    fiat_payment = models.OneToOneField(FiatPayment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    processed = models.BooleanField(default=False)

class BlockchainPayment(models.Model):
    trade = models.OneToOneField(Trade, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    processed = models.BooleanField(default=False)



