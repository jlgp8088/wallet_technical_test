from coins.models import FiatCoin
from django.core.exceptions import ObjectDoesNotExist
from api.convert import convert_to_usdt


def convert_fiat_to_usdt(coin_code, amount_fiat):
  try:
      coin = FiatCoin.objects.get(code=coin_code)
      response = convert_to_usdt(amountfiat=amount_fiat, codecoin=coin.code)
      return response
  except ObjectDoesNotExist:
    raise ValueError('Invalid Coin') 
  except Exception as e:
    raise ValueError(str(e))