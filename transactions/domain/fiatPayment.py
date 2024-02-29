from transactions.models import FiatPayment
from coins.convert import convert_fiat_to_usdt
from api.exchange import transfer_to, get_balance
from rest_framework import status

def create_payment_process(amount, user, coin_code):
  convert = convert_fiat_to_usdt(coin_code=coin_code, amount_fiat=amount)
  if(convert is None):
    raise ValueError('error convert_to_usdt') 

  wallet = user.wallets
  balance = get_balance(wallet.address)
  if(float(convert['amount_usdt']) > float(balance['balance'])  ):
    raise ValueError('insufficient balance') 
  
  transfer = transfer_to(wallet.address)
  if(transfer is None):
    raise ValueError('error transfer_between_wallet') 

  newFiatPayment = FiatPayment(
    amount_fiat=amount,
    amount_usdt=convert['amount_usdt'],
    fiat_code=coin_code,
    user=user,
    hash_trx=transfer['hash'],
  )
  newFiatPayment.save()

  return transfer
