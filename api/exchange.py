import hashlib
from api.serializers import trxCryptoSerializar

def transfer_between_wallet(wallet_origin, wallet_destiny):
  try:
    datos_transaccion = f"{wallet_origin}-{wallet_destiny}"
    hash_falso = hashlib.sha256(datos_transaccion.encode()).hexdigest()
    data={'hash': hash_falso}
    hashSerializer = trxCryptoSerializar(data=data)
    if(hashSerializer.is_valid()):
      return hashSerializer.data
  except Exception as e:
    raise ValueError('error transfer_between_wallet:'+str(e)) 
  

def transfer_to(wallet_origin):
  wallet_destiny = 'wallet principal'
  return transfer_between_wallet (wallet_origin, wallet_destiny)


def transfer_from(wallet_destiny):
  wallet_origin = 'wallet principal'
  return transfer_between_wallet (wallet_origin, wallet_destiny)