from transactions.models import FiatPayment, BlockchainPayment
from coins.convert import convert_fiat_to_usdt
from api.exchange import transfer_between_wallet, get_balance
from api.serializers import hashSerializar
from transactions.serializers import FiatPaymentResponseSerializer
from datetime import datetime
from transactions.domain.fees import calc_fees

def create_fiat_payment_process(amount, user, coin_code, destiny):
  convert = convert_fiat_to_usdt(coin_code=coin_code, amount_fiat=amount)
  wallet = user.wallets

  newFiatPayment = FiatPayment(
    amount_fiat=amount,
    fiat_code=coin_code,
    user=user,
  )

  if(convert is None):
    raise ValueError('error convert_to_usdt') 
  
  amount_fee = calc_fees(newFiatPayment, user, convert['amount_usdt'] )
  balance = get_balance(wallet.address)

  if(float(convert['amount_usdt']) > float(balance['balance'])):
    raise ValueError('insufficient balance') 
  
  transfer = transfer_between_wallet(wallet_origin=wallet.address,wallet_destiny=destiny,amount= float(amount_fee))
  
  if(transfer is None):
    raise ValueError('error transfer_between_wallet') 

  newFiatPayment.hash_trx=transfer['hash']
  newFiatPayment.amount_usdt=convert['amount_usdt']
  newFiatPayment.amount_usdt_fee=amount_fee
  newFiatPayment.save()

  return transfer

def confirm_fiat_payment_process(hash, user):
  try:
    current_fiat = FiatPayment.objects.get(user=user, hash_trx=hash)
    if(not current_fiat.processed ):
      current_fiat.processed = True
      current_fiat.processed_date = datetime.now()
      current_fiat.save()
    serializer = FiatPaymentResponseSerializer(current_fiat)
    return serializer.data
  except FiatPayment.DoesNotExist:
    raise ValueError('payment dont exist') 
  

def create_blockchain_payment_process(amount, user, coin, destiny):
  wallet = user.wallets
  balance = get_balance(wallet.address)

  newBlockChain = BlockchainPayment(
    amount = amount,
    coin = coin,
    user = user,
    processed = False,
  )

  if(float(amount) > float(balance['balance'])  ):
    raise ValueError('insufficient balance') 
  
  amount_fee = calc_fees(newBlockChain, user, amount )
  transfer = transfer_between_wallet(wallet_origin=wallet.address,wallet_destiny=destiny,amount= float(amount_fee))
  
  if(transfer is None):
    raise ValueError('error transfer_between_wallet') 

  newBlockChain.processed = True
  newBlockChain.hash_trx = transfer['hash']
  newBlockChain.processed_date = datetime.now()
  newBlockChain.amount_fee = amount_fee
  newBlockChain.save()

  return transfer


