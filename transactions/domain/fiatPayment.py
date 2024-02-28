from transactions.models import FiatPayment
from coins.convert import convert_fiat_to_usdt
from api.exchange import transfer_to
from rest_framework import status

def create_payment_process(amount, user, coin_code):
  convert = convert_fiat_to_usdt(coin_code=coin_code, amount_fiat=amount)
  if(convert is None):
    raise ValueError('error convert_to_usdt') 
   
  transfer = transfer_to('0xBA80d3B7D5CA2786345CfCB4F21dccAfc893526B')

  if(transfer is None):
    raise ValueError('error transfer_between_wallet') 

  if(convert is not None):
    newFiatPayment = FiatPayment(
      amount_fiat=amount,
      amount_usdt=convert['amount_usdt'],
      fiat_code=coin_code,
      user=user,
      hash_trx=transfer['hash'],
    )
    newFiatPayment.save()
  else:
    return convert