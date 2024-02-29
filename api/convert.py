from api.serializers import FiatUsdtSerializar
from decimal import Decimal,  ROUND_HALF_UP

def convert_to_usdt (amountfiat, codecoin):
  # Logic to get value from api
  coin_convert = {
    'EUR': 0.9,
    'USD': 1
  }

  factor = coin_convert.get(codecoin, None)
  # End api process

  amountfiat =Decimal(amountfiat)
  factor =Decimal(factor)
  amount_usdt = (amountfiat / factor).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
  
  data = {
    'amount_fiat': amountfiat,
    'amount_usdt': amount_usdt,
    'fiat_code': codecoin,
  }

  serializeResponse = FiatUsdtSerializar(data=data)
  
  if(serializeResponse.is_valid()):
    return serializeResponse.data
  else:
    return None