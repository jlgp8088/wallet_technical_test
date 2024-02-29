from api.serializers import hashSerializar, walletBalanceSerializar
from api.models import LogTransactions
import random
import string
import secrets
import environ
env = environ.Env()
environ.Env.read_env()

def transfer_between_wallet(wallet_origin, wallet_destiny, amount):
  logTrx = LogTransactions.objects.create(
    wallet_origin=wallet_origin,
    wallet_destiny=wallet_destiny,
    value=amount,
    state='I'
  )
  try:
    hash_aleatorio = secrets.token_hex(32)
    hash_formateado = '0x' + hash_aleatorio
    data={'hash': hash_formateado}
    hashSerializer = hashSerializar(data=data)
    if(hashSerializer.is_valid()):
      logTrx.state='S'
      logTrx.hash_trx=hashSerializer.data['hash']
      logTrx.save()
      return hashSerializer.data
  except Exception as e:
    logTrx.state='F'
    logTrx.save()
    raise ValueError('error transfer_between_wallet:'+str(e)) 
  

def transfer_to(wallet_origin, amount):
  wallet_destiny = env('PRINCIPAL_ADDRESS')
  return transfer_between_wallet (wallet_origin, wallet_destiny, amount)


def transfer_from(wallet_destiny, amount):
  wallet_origin = env('PRINCIPAL_ADDRESS')
  return transfer_between_wallet (wallet_origin, wallet_destiny, amount)

def create_wallet():
  longitud = 40
  caracteres_hex = string.hexdigits[:-6] 
  hash_aleatorio = '0x' + ''.join(random.choices(caracteres_hex, k=longitud - 2))
  
  return hash_aleatorio

def get_balance(address):
  data = {
    'balance': 10000
  }
  balanceSerializer = walletBalanceSerializar(data=data)

  if(balanceSerializer.is_valid()):
    return balanceSerializer.data
  else:
    raise ValueError('error transfer_between_wallet:'+str(balanceSerializer.errors)) 
